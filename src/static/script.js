// Home
if (document.querySelector("#homeForm")) {

    // highlight current page in nav bar
    document.querySelector("#homeNav").classList.toggle("active");
    
    // display forms
    let selectedApp = document.querySelector("#appSelect");
    let selectedTarget = document.querySelector("#targetSelect");

    let urlForm = document.querySelector("#urlForm");
    let urlInput = document.querySelector("#urlForm input");

    let fileForm = document.querySelector("#fileForm");
    let fileInput = document.querySelector("#fileForm input");

    let qrForm = document.querySelector("#qrForm");
    let qrInput = document.querySelector("#qrForm input");
    
    fileForm.style.display = "none";
    // qrForm.style.display = "none";

    selectedApp.addEventListener("change", function() {
        if (selectedApp.value == "URL Shortener") {
            qrForm.style.display = "none";

        } else if (selectedApp.value == "QR Code Generator") {
            qrForm.style.display = "block";
        }
    })

    selectedTarget.addEventListener("change", function() {
        if (selectedTarget.value == "Website") {
            urlForm.style.display = "block";
            fileForm.style.display = "none";
            urlInput.required = true;
            fileInput.required = false;

        } else if (selectedTarget.value == "File") {
            urlForm.style.display = "none";
            fileForm.style.display = "block";
            urlInput.required = false;
            fileInput.required = true;
        }
    })


    // QR code responds
    
    qrConfig = document.querySelector(".fa-qrcode");
    qrColor = document.querySelector("#qrColor");
    qrBackColor = document.querySelector("#qrBackColor");

    qrColor.addEventListener("input", function() {
        qrConfig.style.color = qrColor.value;
        console.log(qrColor.value);
    })

    qrBackColor.addEventListener("input", function() {
        qrConfig.style.backgroundColor = qrBackColor.value;
        console.log(qrBackColor.value);
    })
    
} // End of Home


// Auth
if (document.querySelector(".authForm")) { // add onchange

    let signBtn = document.querySelector(".signBtn");
    let regBtn = document.querySelector(".regBtn");

    let signForm = document.querySelector(".signForm");
    let regForm = document.querySelector(".regForm");
    console.log(signForm);
    console.log(regForm);

    regForm.style.display = "none";

    signBtn.addEventListener("click", function() {
        signBtn.classList.remove("btn-secondary");
        signBtn.classList.add("btn-primary");
        regBtn.classList.remove("btn-primary");
        regBtn.classList.add("btn-secondary");
        signForm.style.display = "block";
        regForm.style.display = "none";
    })

    regBtn.addEventListener("click", function() {
        regBtn.classList.remove("btn-secondary");
        regBtn.classList.add("btn-primary");
        signBtn.classList.remove("btn-primary");
        signBtn.classList.add("btn-secondary");
        regForm.style.display = "block";
        signForm.style.display = "none";
    })

} // End of Auth