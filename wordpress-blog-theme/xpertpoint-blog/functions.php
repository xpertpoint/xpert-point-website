<?php
add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('xpertpoint-blog-style', get_stylesheet_uri(), array(), wp_get_theme()->get('Version'));
});

add_action('rss2_item', function () {
    if (has_post_thumbnail()) {
        $image = wp_get_attachment_image_src(get_post_thumbnail_id(), 'large');
        if ($image) {
            printf('<enclosure url="%s" length="0" type="image/jpeg" />' . "\n", esc_url($image[0]));
        }
    }
});
