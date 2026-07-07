<?php
// Handles all forms (newsletter + booking) from bike_page.html and coffee_page.html.
// Sends the submission to the business inbox and an auto-reply to the customer,
// using this cPanel account's own mail sending — no third-party service involved.

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
    exit;
}

function sanitize_header_value($value) {
    return trim(preg_replace('/[\r\n]+/', ' ', (string) $value));
}

$businessEmail = 'hello@xpertpoint.ro';
$fromDomain = 'xpertpoint.ro';

$subject = sanitize_header_value($_POST['subject'] ?? 'Mesaj nou de pe site');
$customerEmail = filter_var($_POST['email'] ?? '', FILTER_VALIDATE_EMAIL);

// Surface the chosen package in the subject line so it's visible from the inbox list, not just after opening the email.
$serviceType = sanitize_header_value($_POST['service_type'] ?? '');
if ($serviceType !== '') {
    $subject .= ' — ' . $serviceType;
}

// Build the business notification body from every submitted field (skip internal-only ones).
$skipFields = ['subject'];
$body = "Mesaj nou de pe xpertpoint.ro\n\n";
foreach ($_POST as $key => $value) {
    if (in_array($key, $skipFields, true)) continue;
    if (!is_string($value)) continue;
    $label = ucfirst(str_replace('_', ' ', $key));
    $body .= $label . ': ' . trim($value) . "\n";
}

$headers = "From: Xpert Point <no-reply@$fromDomain>\r\n";
if ($customerEmail) {
    $headers .= 'Reply-To: ' . sanitize_header_value($customerEmail) . "\r\n";
}

$sent = mail($businessEmail, $subject, $body, $headers);

if ($sent && $customerEmail) {
    $autoReplySubject = 'Am primit mesajul tău — Xpert Point';
    $autoReplyBody = "Bună,\n\nAm primit cererea ta și revenim cât mai curând cu un răspuns.\n\nEchipa Xpert Point";
    $autoReplyHeaders = "From: Xpert Point <$businessEmail>\r\n";
    mail($customerEmail, $autoReplySubject, $autoReplyBody, $autoReplyHeaders);
}

echo json_encode(['success' => (bool) $sent]);
