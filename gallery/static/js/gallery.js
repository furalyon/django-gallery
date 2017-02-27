// helper functions

var trim = function(str)
{
    return str.trim ? str.trim() : str.replace(/^\s+|\s+$/g,'');
};

var hasClass = function(el, cn)
{
    return (' ' + el.className + ' ').indexOf(' ' + cn + ' ') !== -1;
};

var addClass = function(el, cn)
{
    if (!hasClass(el, cn)) {
        el.className = (el.className === '') ? cn : el.className + ' ' + cn;
    }
};

var removeClass = function(el, cn)
{
    el.className = trim((' ' + el.className + ' ').replace(' ' + cn + ' ', ' '));
};




var links = document.querySelectorAll('.gallery__link'),
    // caption_element = document.querySelector('#room-viewer__caption'),

image_viewer_show_image = function(link) {
    var thumbnail = link.children[0],

    image = document.createElement('img'),
    overlay = document.createElement('span'),
    gallerymodal = document.createElement('div'),
    body = document.querySelector('body');

    image.src = thumbnail.getAttribute('src'),
    image.alt = thumbnail.getAttribute('alt');
    image.id = 'gallery__img'
    addClass(gallerymodal, 'gallerymodal');
    addClass(image, 'img');
    addClass(overlay, 'gallerymodal__overlay');
    gallerymodal.appendChild(image);
    body.appendChild(gallerymodal);
    body.appendChild(overlay);
    setTimeout(function() {
        addClass(body, 'gallerymodalIsOpen');
    }, 50);
    image_viewer_bind_closing();
},

image_viewer_close_image = function() {
    removeClass(document.querySelector('body'),('gallerymodalIsOpen'));
    //delay for animation to finish
    setTimeout(function() {
        document.getElementById('gallery__img').remove();
        document.querySelector('.gallerymodal__overlay').remove();
        document.querySelector('.gallerymodal').remove();
    }, 600);
},


image_viewer_bind_closing = function() {
    window.addEventListener('keyup',function (e) {
        if (e.keyCode == 27) {
            image_viewer_close_image();
        }
    });
    document.querySelector('.gallerymodal__overlay').addEventListener('click',function (e) {
            image_viewer_close_image();
    });
},

image_viewer_bind_click_function = function(e) {
    e.preventDefault();
    image_viewer_show_image(this);
},

image_viewer_bind_links = function() {
    for (var i=0;i<links.length;i++) {
        links[i].addEventListener('click', image_viewer_bind_click_function)
    }
},

image_viewer_rebind_links = function() {
    links = document.querySelectorAll('.gallery__link');
    for (var i=0;i<links.length;i++) {
        // links[i].removeEventListener('click', image_viewer_bind_click_function);
        links[i].addEventListener('click', image_viewer_bind_click_function);
    }
};

(function(window, document, undefined) {
    image_viewer_bind_links();
})(window, window.document);