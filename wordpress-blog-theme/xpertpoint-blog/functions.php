<?php
add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('xpertpoint-blog-style', get_stylesheet_uri(), array(), wp_get_theme()->get('Version'));
});
