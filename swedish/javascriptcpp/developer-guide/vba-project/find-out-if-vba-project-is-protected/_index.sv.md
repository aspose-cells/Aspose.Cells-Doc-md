---
title: Ta reda på om VBA projekt är skyddat med JavaScript via C++
linktitle: Ta reda på om VBA projektet är skyddat
type: docs
weight: 20
url: /sv/javascript-cpp/find-out-if-vba-project-is-protected/
---

## **Ta reda på om VBA-projekt är skyddat i JavaScript**

Du kan avgöra om VBA (Visual Basic Applications) projektet för din Excel-fil är skyddat eller inte med Aspose.Cells med [**VbaProject.isProtected()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isProtected--)-egenskapen.

## **Exempelkod**

Följande exempel skapar en arbetsbok och kontrollerar om dess VBA-projekt är skyddat eller inte. Sedan skyddar den VBA-projektet och kontrollerar igen. Se dess konsolutdata för referens. Innan skyddet returnerar [**VbaProject.isProtected()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isProtected--) **false**, men efter skyddet returnerar det **true**.

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

            // Find out if VBA Project is Protected using isProtected method.
            const beforeProtected = vbaProj.isProtected();
            console.log("IsProtected - Before Protecting VBA Project: " + beforeProtected);

            // Protect the VBA project.
            vbaProj.protect(true, "11");

            // Find out if VBA Project is Protected using isProtected method.
            const afterProtected = vbaProj.isProtected();
            console.log("IsProtected - After Protecting VBA Project: " + afterProtected);

            // Save the modified workbook as XLSM to preserve VBA project
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

## **Konsoloutput**

Detta är konsoloutputen av den ovanstående exempelkoden som referens.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
