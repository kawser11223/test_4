// Select on pressing COPY
var els_copy = document.querySelectorAll("[data-copy]");
for (var i = 0; i < els_copy.length; i++) {
  var el = els_copy[i];
  el.addEventListener("submit", function(e) {
    e.preventDefault();
    var text = e.target.querySelector('input[type="text"]').select();
    document.execCommand("copy");
  });
}

// Select all text when pressing inside text field
var els_selectAll = document.querySelectorAll("[data-click-select-all]");
for (var i = 0; i < els_selectAll.length; i++) {
  var el = els_selectAll[i];
  el.addEventListener("click", function(e) {
    e.target.select();
  });
}
