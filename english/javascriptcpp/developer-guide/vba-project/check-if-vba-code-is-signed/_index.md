---
title: Check if VBA Code is Signed with JavaScript via C++
linktitle: Check if VBA Code is Signed
type: docs
weight: 100
url: /javascript-cpp/check-if-vba-code-is-signed/
description: Learn how to check if the VBA code project is signed using Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells allows the user to check if the VBA code project is signed or not. Please use the [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) property to check if the VBA code project is signed or not.

{{% /alert %}}

The following code explains how to check if the VBA code is signed or not using the [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) property. You can use any of your excel files to test this code. For testing purposes, you can use [this excel file used in the code](5115032.xlsm).

## **Check if VBA Code is Signed in JavaScript**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## Console Output

Below is the console output of the above code using the [sample excel file](5115032.xlsm) provided by the link.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}