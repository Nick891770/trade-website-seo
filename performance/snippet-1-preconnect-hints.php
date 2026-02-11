/**
 * Snippet Name: Laws Electrical — Preconnect Hints
 * Description: Tells the browser to start connecting to third-party domains
 *              earlier, reducing latency for Google Fonts, Analytics, etc.
 * Where to add: Code Snippets plugin > Add New > "Run snippet everywhere"
 */

function laws_preconnect_hints() {
    echo '<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>' . "\n";
    echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
    echo '<link rel="preconnect" href="https://www.googletagmanager.com">' . "\n";
    echo '<link rel="dns-prefetch" href="https://www.google-analytics.com">' . "\n";
}
add_action( 'wp_head', 'laws_preconnect_hints', 1 );
