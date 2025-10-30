---
title: Hämta eller ställ in klassidentifieraren för det inbäddade OLE objektet med JavaScript via C++
linktitle: Hämta eller ange klassidentifieraren för det inbäddade OLE objektet
type: docs
weight: 200
url: /sv/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Lär dig hur du hämtar eller ställer in klassidentifieraren för inbäddade OLE objekt i JavaScript med Aspose.Cells via C++.
---

## **Möjliga användningsscenario**  
Aspose.Cells tillhandahåller egenskapen [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) som du kan använda för att hämta eller ställa in klassidentifieraren för ett inbäddat OLE-objekt. OLE-objektets klassidentifierare är faktiskt GUIDs, dvs. Globally Unique Identifiers. GUID är alltid 16 byte lång; därför är klassidentifierare också 16 byte långa. De finns ofta i Windows-registret och ger information till värdapplikationen om hur man öppnar inbäddade OLE-objekt som innehåller olika inbäddade resurser i klientapplikationen.

## **Hämta eller ange klassidentifieraren för det inbäddade OLE-objektet**  
Följande skärmbild visar klassidentifikatorn för OLE-objektet, dvs. GUID, som har lästs från [exempel-Excelfilen](5115190.xls) som innehåller det inbäddade PowerPoint OLE-objektet.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Exempelkod**  
Se följande exempel på kod som körs med [exempel-Excelfilen](5115190.xls) och dess konsolutmatning, vilken visar klassidentifieraren för OLE-objektet dvs. GUID. Den utskrivna GUID är exakt densamma som visas i skärmbilden.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **Konsoloutput**  
Detta är konsolutmatningen av ovanstående exempel på kod när det körs med [exempel-Excelfilen](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
