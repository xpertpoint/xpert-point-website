<?php
add_action('wp_enqueue_scripts', function () {
    // style.min.css e generat de tools/build.py din style.css (minificat + fonturile găzduite pe www.xpertpoint.ro).
    wp_enqueue_style('xpertpoint-blog-style', get_stylesheet_directory_uri() . '/style.min.css', array(), wp_get_theme()->get('Version'));
    // Dashicons sunt necesare doar în bara de administrare.
    if (!is_user_logged_in()) {
        wp_dequeue_style('dashicons');
        wp_deregister_style('dashicons');
    }
}, 100);

add_action('rss2_item', function () {
    if (has_post_thumbnail()) {
        $image = wp_get_attachment_image_src(get_post_thumbnail_id(), 'large');
        if ($image) {
            printf('<enclosure url="%s" length="0" type="image/jpeg" />' . "\n", esc_url($image[0]));
        }
    }
});
