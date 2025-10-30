---
title: Kombinera flera arbetsböcker till en enda arbetsbok med JavaScript via C++
linktitle: Arbetsboksfusion
type: docs
weight: 66
url: /sv/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Lär dig hur du kombinerar flera arbetsböcker till en enda arbetsbok med hjälp av Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Ibland behöver du kombinera arbetsböcker med olika innehåll som bilder, diagram och data till en enda arbetsbok. Aspose.Cells for JavaScript via C++ stöder denna funktion. Den här artikeln visar hur man skapar en konsolapplikation och kombinerar arbetsböcker med några enkla kodrader med Aspose.Cells.

{{% /alert %}}

## **Kombinera arbetsböcker med bilder och diagram**

Exempelkoden kombinerar två arbetsböcker till en enda arbetsbok med hjälp av Aspose.Cells for JavaScript via C++. Koden laddar källarboksfilerna, använder metoden [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) för att kombinera dem och sparar utdataarbetsboken.

### **Källarbetsböcker**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Resultatarbetsböcker**

- [combined.xlsx](5473095.xlsx)

### **Skärmbilder**

Här är skärmbilder på käll- och resultatarbetsböcker.

{{% alert color="primary" %}}

Du kan använda vilka källarbetsböcker som helst. Dessa bilder är bara för illustration.

{{% /alert %}}

**Den första arbetsbokens arbetsblad - staplad** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Andra arbetsbladet i arbetsboken - linje** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Första arbetsbladet i bildarbetsboken - bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Alla tre arbetsblad i den kombinerade arbetsboken - staplad, linje, bild** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Kombinera flera arbetsblad till ett enda arbetsblad](/cells/sv/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Sammanfoga filer](/cells/sv/javascript-cpp/merge-files/)
