---
title: Använd anpassade XML delar i Aspose.Cells med JavaScript via C++
linktitle: Använd anpassade XML delar i Aspose.Cells
type: docs
weight: 390
url: /sv/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: Lär dig att använda anpassade XML delar i Aspose.Cells for JavaScript via C++. Integrera extern XML data sömlöst i Excel filer.
---

## Användning av anpassade XML-delar i Aspose.Cells

Anpassade XML-delar är XML-data som lagras av olika applikationer som SharePoint etc. inuti Excel-filen. Denna data används av olika applikationer som behöver den. Microsoft Excel använder inte denna data så det finns ingen GUI för att lägga till den. Du kan visa denna data genom att byta ut extensionen på **.xlsx** till **.zip** och sedan öppna den med **WinZip**. Du kan också öppna ZIP-filen med vilken tredjeparts Windows zip-utility som helst, såsom WinRAR eller WinZip. Data finns i mappen **customXml**.

Du kan lägga till anpassade XML-delar med Aspose.Cells for JavaScript via C++ genom [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) -metoden.

Följande exempel använder [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) metoden och lägger till **Book Catalog XML** med namnet **BookStore**. Bilden nedan visar resultatet av denna kod. Som du kan se är Book Catalog XML tillagt i BookStore-noden, som är namnet på denna egenskap.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## JavaScript-kod för att använda anpassade XML-delar

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## Relaterad artikel

- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
