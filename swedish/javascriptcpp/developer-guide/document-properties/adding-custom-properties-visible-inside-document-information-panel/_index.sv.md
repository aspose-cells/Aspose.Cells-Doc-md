---
title: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen med JavaScript via C++
linktitle: Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen
type: docs
weight: 300
url: /sv/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Lär dig hur du lägger till anpassade egenskaper till en arbetsboksobjekt med Aspose.Cells for JavaScript via C++. Dessa egenskaper kan ses i dokumentinformationspanelen.
---

## **Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen**

Aspose.Cells for JavaScript via C++ kan användas för att lägga till anpassade egenskaper i arbetsboksobjektet som är synliga i dokumentinformationspanelen. Du kan öppna dokumentinformationspanelen i Microsoft Excel med kommandona Arkiv > Info > Egenskaper > Visa dokumentpanel.

Använd [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-)-metoden för att lägga till en anpassad egenskap som syns i Dokumentinformation-panelen.

Följande exempel kod lägger till två anpassade egenskaper. Den första egenskapen saknar typ och den andra är av typen DateTime. När du öppnar den genererade Excel-filen kommer du att se dessa två egenskaper i Dokumentinformation-panelen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Relaterad artikel**

{{% alert color="primary" %}}

- [Använd anpassade XML-delsar i Aspose.Cells](/cells/sv/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
