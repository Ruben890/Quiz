const modal_btn = [...document.getElementsByClassName("modal-bottom")];
const modal_body = document.getElementById("model-body-confirm");
const btn_start = document.getElementById("btn_start");
const url = window.location.href;

modal_btn.forEach((modal_btn) =>
  modal_btn.addEventListener("click", () => {
    const pk = modal_btn.getAttribute("pk");
    const title = modal_btn.getAttribute("title");
    const time = modal_btn.getAttribute("time");
    const descriction = modal_btn.getAttribute("descriction");

    /**  elemnetos html*/

    document.getElementById(
      "exampleModalLabel"
    ).innerHTML = `<h3>${title}</h3>`;
    modal_body.innerHTML = `
    <p><b>Time:</b>${time}min</p>
    </hr>
    <p>${descriction}</p>
    `;

    /* start button */
    btn_start.addEventListener("click", () => {
      window.location.href = url + pk;
    });
  })
);
