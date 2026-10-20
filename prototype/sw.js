// Pass-through service worker: lets the prototype install as a full-screen app.
// No caching, so every launch loads the latest pushed version.
self.addEventListener("install", function () { self.skipWaiting(); });
self.addEventListener("activate", function (e) { e.waitUntil(self.clients.claim()); });
self.addEventListener("fetch", function () {});
