/*
 * Copyright 2018 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

var _currentHash = "";

(function ($) {
    'use strict';

    // Headers' anchor link that shows on hover
    $(function () {
        // append anchor links to headings in markdown.
        var article = document.getElementsByTagName('main')[0];
        if (!article) {
            return;
        }
        var headings = article.querySelectorAll('h1, h2, h3, h4, h5, h6');
        headings.forEach(function (heading) {
            if (heading.id) {
                var a = document.createElement('a');
                // set visibility: hidden, not display: none to avoid layout change
                a.style.visibility = 'hidden';
                // [a11y] hide this from screen readers, etc..
                a.setAttribute('aria-hidden', 'true');
                a.setAttribute( 'class', 'anchor' );
                // material insert_link icon in svg format
                a.innerHTML = ' <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="24" height="24" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"/><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg>';
                a.href = '#' + heading.id;
                heading.insertAdjacentElement('beforeend', a);
                heading.addEventListener('mouseenter', function () {
                    a.style.visibility = 'initial';
                });
                heading.addEventListener('mouseleave', function () {
                    a.style.visibility = 'hidden';
                });
            }
        });
    });

}(jQuery));

function getLocationWithoutHash() {
    return window.location.toString().replace(window.location.hash.toString(), '').toString();
}

function outlineAnchorInToC(currentHash) {
    if(currentHash == '') {
        $('#TableOfContents').find('a:first').addClass('active');
    }
    else {
        $('#TableOfContents').find('a').each(function() {
            $(this).removeClass('active');
            if($(this).attr('href') == currentHash) {
                $(this).addClass('active');
            }
        });
    }
}

function calculateAnchorDistances() {
    var dict = new Object();
    $('.anchor').each(function () {
        var hash = $(this).attr('href');
        var distance = $(this).offset().top;
        dict[hash] = distance;
    });

    return dict;
}

function processAnchor(anchorDistances) {
    var top = window.pageYOffset;
    for(var hash in anchorDistances) {
        var distance = top - anchorDistances[hash] + 95;
        if (distance < 30 && distance > -30 && _currentHash != hash) {
            _currentHash = hash;

            outlineAnchorInToC(_currentHash);
            break;
        }
    };
}

$(function () {
    
    outlineAnchorInToC(window.location.hash);
    var allowOutlineAnchor = true;

    var anchorDistances = calculateAnchorDistances();
    $(document).scroll(function () {
        if(allowOutlineAnchor) {
            processAnchor(anchorDistances);
        }
    });
    $('#TableOfContents').find('a').click(function () {
        allowOutlineAnchor = false;
        var hash = $(this).attr('href');
        var test = $('.anchor[href="'+ hash.toString() +'"]');
        $([document.documentElement, document.body]).animate({
            scrollTop: test.offset().top - 95
        }, 1000, function () {
            allowOutlineAnchor = true;
            outlineAnchorInToC(window.location.hash);
        });
    });
});