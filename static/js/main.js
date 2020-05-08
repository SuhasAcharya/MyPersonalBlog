alert('If you are a Smartphone User,Please put your Smartphone is Landscape Mode! ')

const parallax1 = document.getElementById("p1");
window.addEventListener("scroll",function () {
let offset = window.pageYOffset;
parallax1.style.backgroundPositionY = offset * 0.7 + "px";
})



const parallax2 = document.getElementById("p3");
window.addEventListener("scroll",function () {
let offset = window.pageYOffset;
parallax2.style.backgroundPositionY = offset * 0.99 + "px";
})

