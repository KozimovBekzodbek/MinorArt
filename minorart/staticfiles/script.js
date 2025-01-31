const openerMenu = document.querySelector('.opener-menu');
const closerMenu = document.querySelector('.closer-menu');
const menu = document.querySelector('#navbar .menu');
const navs = document.querySelectorAll('#navbar .menu ul li')


// navbar
openerMenu.addEventListener('click', () => {
    menu.classList.add('open');
});
closerMenu.addEventListener('click', () => {
    menu.classList.remove('open');
})


menu.addEventListener('click', (e) => {
    if (e.target.classList.contains('menu')) {
        menu.classList.remove('open');
    }
})

navs.forEach((nav) => {
    nav.addEventListener('click', () => {
        menu.classList.remove('open');
    })
})




// // change theme
// const modeIcon = document.querySelector('#navbar .mode i:last-child'); // mode icon
// let root = document.querySelector(":root") // root

// // LocalStorage'da 'status' mavjudligini tekshirish va boshlang'ich qiymat o'rnatish
// if (localStorage.getItem("status") === null) {
//     localStorage.setItem("status", "true"); // Boshlang'ich qiymatni o'rnatish faqat bir marta
// }



// // Temani localStorage'dagi 'status' qiymatiga qarab qo'llash
// function applyTheme() {
//     const status = localStorage.getItem("status");

//     if (status === "true") {
//         // Night Mode (true holati)
//         modeIcon.classList.remove("lni-sun");
//         modeIcon.classList.add("lni-night");

//         root.style.setProperty("--color-body", "rgb(20, 44, 44)");
//         root.style.setProperty("--color-text", "#E0E0E0");


//     } else {
//         // Light Mode (false holati)
//         modeIcon.classList.remove("lni-night");
//         modeIcon.classList.add("lni-sun");

//         root.style.setProperty("--color-body", "#ffffff");
//         root.style.setProperty("--color-text", "#2a2a2a");


//     }
// }

// // Temani almashtirish
// function toggleTheme() {
//     const status = localStorage.getItem("status");
//     // Statusni o'zgartirish va localStorage'ga saqlash
//     localStorage.setItem("status", status === "true" ? "false" : "true");

//     // Yangilangan holatni qo'llash
//     applyTheme();
// }

// // Dastlabki tema holatini qo'llash
// applyTheme();

// // Event listener qo'shish
// modeIcon.addEventListener("click", toggleTheme);

















// swiper
let headerswiper = new Swiper(".headerswiper", {
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});



// swiper products
var swiperProducts = new Swiper(".swiperProducts", {
    slidesPerView: 1.1,
    spaceBetween: 20,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
    breakpoints: {
        480: {
            slidesPerView: 1.9,
            spaceBetween: 20,
        },
        576: {
            slidesPerView: 1.6,
        },
        768: {
            slidesPerView: 2.1,
        },
        992: {
            slidesPerView: 2.3,
        },
        1200: {
            slidesPerView: 3.5,
        },
        1400: {
            slidesPerView: 4.1,
        },
    },
});


// swiper news
var swiperNews = new Swiper(".swiperNews", {
    slidesPerView: 1.1,
    spaceBetween: 20,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
    breakpoints: {
        480: {
            slidesPerView: 1.9,
            spaceBetween: 20,
        },
        576: {
            slidesPerView: 1.6,
        },
        768: {
            slidesPerView: 2.1,
        },
        992: {
            slidesPerView: 2.3,
        },
        1200: {
            slidesPerView: 3.5,
        },
        1400: {
            slidesPerView: 4.1,
        },
    },
});








// detail swiper
var swiperProducts = new Swiper(".detailSwiper", {
    slidesPerView: 3.2,
    spaceBetween: 20,

    loop: true,
    // breakpoints: {
    //     480: {
    //         slidesPerView: 1.9,
    //         spaceBetween: 20,
    //     },
    //     576: {
    //         slidesPerView: 1.6,
    //     },
    //     768: {
    //         slidesPerView: 2.1,
    //     },
    //     992: {
    //         slidesPerView: 2.3,
    //     },
    //     1200: {
    //         slidesPerView: 3.5,
    //     },
    //     1400: {
    //         slidesPerView: 4.1,
    //     },
    // },
});


// detail clickable swiper
const images = document.querySelector('#detail-page-content .left-side .bottom');
if (images) {

    images.addEventListener('click', (e) => {
        if (e.target.tagName === "IMG") {
            let mainImageAfter = document.querySelector("#detail-page-content .left-side .top")
            mainImageAfter.classList.add("show")

            let mainImage = document.querySelector("#detail-page-content .left-side .top img")


            mainImage.src = e.target.src


            setInterval(() => {
                mainImageAfter.classList.remove("show")
            }, 500);
        }
    })

}