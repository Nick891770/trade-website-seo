/**
 * Snippet Name: Laws Electrical — Defer Non-Critical JS
 * Description: Adds defer attribute to all frontend JavaScript except jQuery,
 *              so scripts load without blocking page rendering.
 * Where to add: Code Snippets plugin > Add New > "Only run in the front end"
 *
 * IMPORTANT: After activating, test the site thoroughly. If anything breaks
 * (dropdowns, sliders, forms), add the broken script's handle to the
 * $no_defer array below.
 */

function laws_defer_scripts( $tag, $handle, $src ) {
    // Don't defer in admin area
    if ( is_admin() ) {
        return $tag;
    }

    // Scripts that must NOT be deferred (add handles here if things break)
    $no_defer = array(
        'jquery-core',
        'jquery-migrate',
        'jquery',
    );

    if ( in_array( $handle, $no_defer, true ) ) {
        return $tag;
    }

    // Skip if already has defer or async
    if ( strpos( $tag, ' defer' ) !== false || strpos( $tag, ' async' ) !== false ) {
        return $tag;
    }

    return str_replace( ' src=', ' defer src=', $tag );
}
add_filter( 'script_loader_tag', 'laws_defer_scripts', 10, 3 );
