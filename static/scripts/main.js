const main = document.getElementById("main")
const sentinel = document.querySelector('#sentinel');
var modal = document.getElementById("myModal");

var btn = document.getElementById("myBtn");

var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
  modal.style.display = "block";
}
span.onclick = function () {
  modal.style.display = "none";
}
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function showModel(){

}

function loadItems(){
  $.ajax({
    type: "GET",
    url: "/load",
    contentType: "application/json; charset=utf-8",
    success: function(data){
      main.innerHTML+='<div class="card"><div class="img"><img src="'+data+'" class="paw"></div></div><br>'
    }
  });
  $.ajax({
    type: "GET",
    url: "/load",
    contentType: "application/json; charset=utf-8",
    success: function(data){
      main.innerHTML+='<div class="card"><div class="img"><img src="'+data+'" class="paw"></div></div><br>'
    }
  });
}

const intersectionObserver = new IntersectionObserver(entries => {
  loadItems();
});
intersectionObserver.observe(sentinel);