/* consent.js — Basic Consent Mode v2 controller for alusat.com.
 * Loaded with `defer`; the synchronous default-denied state is already set by an
 * inline script in head.html BEFORE this file executes, so no analytics event
 * can fire before the applicable consent state is established.
 *
 * Behavior (approved design — reload-on-accept, no manual page_view replay):
 *  - New visitor (no stored choice): banner is shown. No consent update is sent,
 *    so GA4 stays denied and emits no measurement requests.
 *  - Accept: persist 'granted', send consent update granted, then reload the page.
 *    After reload the inline default reads 'granted' and the existing gtag('config')
 *    emits exactly ONE normal page_view. No reload loop (stored value is now set).
 *  - Reject: persist 'denied', send consent update denied, hide banner. No reload.
 *  - Withdraw (reopen -> reject while previously granted): persist 'denied', send
 *    consent update denied. Already-transmitted page_view(s) cannot be retracted;
 *    only future navigation is denied.
 *  - Reopen: footer button re-shows the banner so the choice can be changed.
 */
(function () {
  'use strict';

  var KEY = 'alusat_consent';
  var STATES = ['granted', 'denied'];

  var banner = document.getElementById('consent-banner');
  var acceptBtn = document.getElementById('consent-accept');
  var rejectBtn = document.getElementById('consent-reject');
  var reopenBtn = document.getElementById('consent-reopen');

  function pushConsent(state) {
    if (STATES.indexOf(state) === -1) return;
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', {
        'ad_storage': state,
        'ad_user_data': state,
        'ad_personalization': state,
        'analytics_storage': state
      });
    }
  }

  function getStored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }

  function setStored(value) {
    try { localStorage.setItem(KEY, value); } catch (e) { /* storage blocked */ }
  }

  function showBanner() { if (banner) banner.removeAttribute('hidden'); }
  function hideBanner() { if (banner) banner.setAttribute('hidden', ''); }

  function accept() {
    setStored('granted');
    pushConsent('granted');
    window.location.reload();
  }

  function reject() {
    setStored('denied');
    pushConsent('denied');
    hideBanner();
  }

  function reopen() {
    showBanner();
  }

  var stored = getStored();

  if (!stored) {
    showBanner();
  } else {
    hideBanner();
    pushConsent(stored); /* idempotent; reinforces inline default */
  }

  if (acceptBtn) acceptBtn.addEventListener('click', accept);
  if (rejectBtn) rejectBtn.addEventListener('click', reject);
  if (reopenBtn) reopenBtn.addEventListener('click', reopen);
})();
