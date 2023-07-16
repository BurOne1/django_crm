const body = document.querySelector("body"),
      sideBar = body.querySelector(".sideBar"),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box");

      toggle.addEventListener("click", () =>{
         sideBar.classList.toggle("close");
      });

      searchBtn.addEventListener("click", () =>{
         sideBar.classList.remove("close");
      });