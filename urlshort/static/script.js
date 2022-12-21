if (document.querySelector("#homeForm")) {
    
    // display forms
    var selectedApp = document.querySelector("#appSelect");
    var selectedTarget = document.querySelector("#targetSelect");

    var urlForm = document.querySelector("#urlForm");
    var urlInput = document.querySelector("#urlForm input");

    var fileForm = document.querySelector("#fileForm");
    var fileInput = document.querySelector("#fileForm input");

    var qrForm = document.querySelector("#qrForm");
    var qrInput = document.querySelector("#qrForm input");
    
    fileForm.style.display = "none";
    // qrForm.style.display = "none";

    selectedApp.addEventListener("change", function() {
        if (selectedApp.value == "urlApp") {
            qrForm.style.display = "none";

        } else if (selectedApp.value == "qrApp") {
            qrForm.style.display = "block";
        }
    })

    selectedTarget.addEventListener("change", function() {

        // if (selectedApp.value == "urlApp") {

            if (selectedTarget.value == "webTarget") {
                urlForm.style.display = "block";
                fileForm.style.display = "none";
                urlInput.required = true;
                fileInput.required = false;

            } else if (selectedTarget.value == "fileTarget") {
                urlForm.style.display = "none";
                fileForm.style.display = "block";
                urlInput.required = false;
                fileInput.required = true;
                
            }
        // }

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
    
}