---
title: Importera XML till Excel arbetsbok med JavaScript via C++
linktitle: XML mappar
type: docs
weight: 210
url: /sv/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importera data från XML filer till Excel med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att importera XML-kartan inuti arbetsboken med hjälp av [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-)-metoden. Du kan importera XML-karta med Microsoft Excel med följande steg:

- Välj **Utvecklare**-fliken
- Klicka på **Importera** i XML-avsnittet och följ de nödvändiga stegen.

Du måste tillhandahålla dina XML-data för att slutföra importen. Här är ett [prov-XML-data](5115037.txt) som du kan använda för testning.

{{% /alert %}}

## **Importera XML-karta med Microsoft Excel**

Följande skärmbild visar hur man importerar XML-karta med Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importera XML-karta med Aspose.Cells for JavaScript via C++**

Följande kodexempel visar hur man använder [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Det genererar den [utdataexcel-filen](5115036.xlsx) som visas i den här skärmbilden.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Avancerade ämnen**
- [Lägg till XML-karta inuti arbetsboken med XmlMapCollection.add() metod](/cells/sv/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportera XML-data som är länkad till XML-karta inuti arbetsboken](/cells/sv/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Hitta rotresursnamnet på XML-kartan](/cells/sv/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Länka celler till XML-kartelement](/cells/sv/javascript-cpp/link-cells-to-xml-map-elements/)
