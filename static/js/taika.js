// Sidebar toggle for mobile + tiny counters
document.addEventListener("click", function (e) {
  const t = e.target.closest("[data-tk-toggle=sidebar]");
  if (t) {
    document.querySelector(".tk-sidebar")?.classList.toggle("show");
  }
});

// Animated key figures / stat counters
document.querySelectorAll("[data-count]").forEach(function (el) {
  const target = parseFloat(el.getAttribute("data-count"));
  const suffix = el.getAttribute("data-suffix") || "";
  let cur = 0;
  const step = Math.max(1, Math.ceil(target / 40));
  const tick = () => {
    cur += step;
    if (cur >= target) { el.textContent = target.toLocaleString() + suffix; }
    else { el.textContent = cur.toLocaleString() + suffix; requestAnimationFrame(tick); }
  };
  tick();
});
