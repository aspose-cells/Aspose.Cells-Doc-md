---  
title: Check if VBA project in a Workbook is Signed with JavaScript via C++  
linktitle: Check if VBA project in a Workbook is Signed  
type: docs  
weight: 70  
url: /javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/  
description: Learn how to check if a VBA project in a workbook is signed using Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}

You can check if your VBA project is signed or not using Microsoft Excel via **Tools > Digital Signatures...** menu command. Similarly, you can check it programmatically using Aspose.Cells [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) property.

{{% /alert %}}

## **Check if VBA Project in a Workbook is Signed in JavaScript**

The following code loads the workbook and checks if its VBA project is signed using [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) property. The property will return **true** if the project is signed, otherwise it will return **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```