```markdown
---
title: Zusätzliche XML Teile hinzufügen und per ID mit JavaScript via C++ auswählen
linktitle: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen
type: docs
weight: 70
url: /de/javascript-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Erfahren Sie, wie Sie benutzerdefinierte XML Teile zu Excel Dokumenten hinzufügen und sie per ID mit Aspose.Cells for JavaScript via C++ auswählen.
---

## **Mögliche Verwendungsszenarien**  

Benutzerdefinierte XML-Teile sind die XML-Daten, die innerhalb der Microsoft Excel-Dokumente gespeichert sind und von den Anwendungen, die damit arbeiten, verwendet werden. Derzeit gibt es keinen direkten Weg, sie mit der Microsoft Excel UI hinzuzufügen. Sie können sie jedoch programmatisch auf verschiedene Weisen hinzufügen, z.B. mit VSTO, Aspose.Cells usw. Verwenden Sie die [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) Sammlung, wenn Sie ein benutzerdefiniertes XML-Teil mit der Aspose.Cells API hinzufügen möchten. Sie können auch seine ID mit der [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--) Eigenschaft setzen. Ebenso, wenn Sie ein benutzerdefiniertes XML-Teil per ID auswählen möchten, können Sie die [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) Sammlung verwenden.  

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**  

Der folgende Beispielcode fügt zuerst vier benutzerdefinierte XML-Teile mit der [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) Sammlung hinzu. Dann setzt er deren IDs mit der [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--) Eigenschaft. Schließlich findet oder wählt er eines der hinzugefügten benutzerdefinierten XML-Teile mit der [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) Sammlung aus. Bitte beachten Sie auch die Konsolenausgabe des unten gegebenen Codes zu Referenz.  

## **Beispielcode**  

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

## **Konsolenausgabe**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
 ```
