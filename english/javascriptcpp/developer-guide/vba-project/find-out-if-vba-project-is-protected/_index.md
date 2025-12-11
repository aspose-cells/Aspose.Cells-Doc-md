---
title: Find out if VBA Project is Protected with JavaScript via C++
linktitle: Find out if VBA Project is Protected
type: docs
weight: 20
url: /javascript-cpp/find-out-if-vba-project-is-protected/
---

## **Find out if a VBA Project is Protected in JavaScript**

You can determine whether the VBA (Visual Basic for Applications) project of your Excel file is protected using Aspose.Cells via the **VbaProject.isProtected()** property.

## **Sample Code**

The following sample code creates a workbook, checks if its VBA project is protected, then protects the VBA project and checks again. Refer to the console output for the results. Before protection, **VbaProject.isProtected()** returns **false**, and after protection it returns **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Protect VBA Project Example</title>
    </head>
    <body>
        <h1>Protect VBA Project Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access the VBA project of the workbook.
            const vbaProj = workbook.vbaProject;

            // Find out whether the VBA project is protected using the isProtected method.
            const beforeProtected = vbaProj.isProtected();
            console.log("IsProtected - Before Protecting VBA Project: " + beforeProtected);

            // Protect the VBA project.
            vbaProj.protect(true, "11");

            // Find out whether the VBA project is protected using the isProtected method.
            const afterProtected = vbaProj.isProtected();
            console.log("IsProtected - After Protecting VBA Project: " + afterProtected);

            // Save the modified workbook as XLSM to preserve the VBA project.
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'vba_protected.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>IsProtected before: ${beforeProtected}</p>
                <p>IsProtected after: ${afterProtected}</p>
            `;
        });
    </script>
</html>
```

## **Console Output**

This is the console output of the above sample code for reference.

{{< highlight javascript >}}
IsProtected - Before Protecting VBA Project: False
IsProtected - After Protecting VBA Project: True
{{< /highlight >}}