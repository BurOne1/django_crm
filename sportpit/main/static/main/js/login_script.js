const container = document.querySelector(".container"),
      pwFields = document.querySelectorAll(".password"),
      singUp = document.querySelector(".singup-link"),
      login = document.querySelector(".login-link");

      singUp.addEventListener("click", ()=>{
          container.classList.add("active");
      });
      login.addEventListener("click", ()=>{
          container.classList.remove("active");
      });
