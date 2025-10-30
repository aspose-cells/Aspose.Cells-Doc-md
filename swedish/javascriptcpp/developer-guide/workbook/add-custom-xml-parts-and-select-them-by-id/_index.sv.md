```markdown
---
title: Lägg till anpassade XML delar och välj dem efter ID med JavaScript via C++
linktitle: Lägg till anpassade XML delar och välj dem efter ID
type: docs
weight: 70
url: /sv/javascript-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Lär dig hur du lägger till anpassade XML delar till Excel dokument och väljer dem efter ID med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Anpassade XML-delar är den XML-data som lagras inuti Microsoft Excel-dokument och används av de applikationer som hanterar dem. Det finns för närvarande inget direkt sätt att lägga till dem via Microsoft Excels användargränssnitt. Däremot kan du lägga till dem programmässigt på olika sätt, t.ex., med VSTO, Aspose.Cells, etc. Använd [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)-samlingen om du vill lägga till anpassad XML-del med Aspose.Cells API. Du kan också ställa in dess ID med [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--)-egenskapen. På samma sätt, om du vill välja en anpassad XML-del efter ID, kan du använda [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)-samlingen.  

## **Lägg till anpassade XML-delar och välj dem efter ID**  

Följande exempelkod lägger först till fyra anpassade XML-delar med hjälp av [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)-samlingen. Sedan ställer den in deras ID:n med [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--)-egenskapen. Slutligen hittar eller väljer den en av de tillagda anpassade XML-delarna med [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--)-samlingen. Se även konsolutdata för koden nedan för referens.  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add and Select Custom XML Parts Example</title>
    </head>
    <body>
        <h1>Add and Select Custom XML Parts Example</h1>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Some data in the form of byte array.
            // Please use correct XML and Schema instead.
            const btsData = new Uint8Array([1, 2, 3]);
            const btsSchema = new Uint8Array([1, 2, 3]);

            // Create four custom xml parts.
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);

            // Assign ids to custom xml parts.
            wb.customXmlParts.get(0).id = "Fruit";
            wb.customXmlParts.get(1).id = "Color";
            wb.customXmlParts.get(2).id = "Sport";
            wb.customXmlParts.get(3).id = "Shape";

            // Specify search custom xml part id.
            let srchID = "Fruit";
            srchID = "Color";
            srchID = "Sport";

            // Search custom xml part by the search id.
            const cxp = wb.customXmlParts.selectByID(srchID);

            // Print the found or not found message on console and UI.
            if (cxp.isNull()) {
                console.log(`Not Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: red;">Not Found: CustomXmlPart ID ${srchID}</p>`;
            } else {
                console.log(`Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: green;">Found: CustomXmlPart ID ${srchID}</p>`;
            }

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
        });
    </script>
</html>
```  

## **Konsoloutput**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
 ```
