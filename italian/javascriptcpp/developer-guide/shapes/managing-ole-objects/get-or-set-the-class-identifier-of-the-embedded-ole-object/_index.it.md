---
title: Ottieni o imposta l identificatore della classe dell oggetto OLE embedded con JavaScript tramite C++
linktitle: Ottieni o Imposta l Identificatore di Classe dell Oggetto OLE Incorporato
type: docs
weight: 200
url: /it/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Impara come ottenere o impostare l identificatore di classe degli oggetti OLE embedded in JavaScript usando Aspose.Cells tramite C++.
---

## **Possibili Scenari di Utilizzo**  
Aspose.Cells fornisce la proprietà [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) che puoi usare per ottenere o impostare l'identificatore di classe di un oggetto OLE embedded. Gli identificatori di classe degli oggetti OLE sono effettivamente GUID, cioè Identificatori Unici Globali. Un GUID ha sempre una lunghezza di 16 byte; pertanto, gli identificatori di classe sono anche di 16 byte. Si trovano spesso all’interno del Registro di Windows e forniscono informazioni all'applicazione host su come aprire gli oggetti OLE incorporati contenenti varie risorse incorporate all’interno dell’applicazione client.

## **Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato**  
Lo screenshot seguente mostra l'identificatore di classe dell'oggetto OLE, cioè il GUID, che è stato letto dal [file Excel di esempio](5115190.xls) contenente l'oggetto PowerPoint OLE incorporato.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Codice di Esempio**  
Vedi il seguente esempio di codice eseguito con il [file Excel di esempio](5115190.xls) e il suo output sulla console, che stampa l'identificatore di classe dell'oggetto OLE, ovvero il GUID. Il GUID stampato è esattamente lo stesso mostrato nello screenshot.

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
### **Output della console**  
Questo è il output sulla console del codice di esempio sopra quando eseguito con il [file Excel di esempio](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
