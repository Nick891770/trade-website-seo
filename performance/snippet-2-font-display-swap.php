/**
 * Snippet Name: Laws Electrical — Font Display Swap
 * Description: Forces font-display: swap on custom fonts so text is visible
 *              immediately while fonts load (fixes render-blocking text).
 * Where to add: Code Snippets plugin > Add New > "Run snippet everywhere"
 *
 * NOTE: Before adding this snippet, check Elementor > Custom Fonts first.
 *       If there's a font-display dropdown there, set it to "swap" instead
 *       of using this code snippet.
 */

function laws_font_display_swap( $css ) {
    if ( strpos( $css, '@font-face' ) !== false ) {
        // Replace any existing font-display value with swap
        $css = preg_replace(
            '/font-display\s*:\s*[a-z]+/',
            'font-display: swap',
            $css
        );
        // If no font-display was set at all, add it after each @font-face {
        if ( strpos( $css, 'font-display' ) === false ) {
            $css = str_replace(
                '@font-face {',
                '@font-face { font-display: swap;',
                $css
            );
        }
    }
    return $css;
}
add_filter( 'wp_get_custom_css', 'laws_font_display_swap' );

// Also handle Elementor's inline font CSS
function laws_elementor_font_display( $html ) {
    if ( strpos( $html, '@font-face' ) !== false && strpos( $html, 'font-display' ) === false ) {
        $html = str_replace( '@font-face {', '@font-face { font-display: swap;', $html );
    }
    return $html;
}
add_filter( 'elementor/frontend/the_content', 'laws_elementor_font_display' );
