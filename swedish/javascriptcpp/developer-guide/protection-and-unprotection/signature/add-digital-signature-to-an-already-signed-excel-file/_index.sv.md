---
title: Lägg till digital signatur i en redan signerad Excel fil med JavaScript via C++
linktitle: Lägg till digital signatur i en redan signerad Excelfil
type: docs
weight: 20
url: /sv/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Denna artikel beskriver hur man lägger till en digital signatur i en redan signerad Excel fil med JavaScript och Aspose.Cells for JavaScript via C++.
keywords: Lägg till digital signatur i en redan signerad Excel fil, Hur man lägger till en digital signatur i ett redan signerad Excel dokument med JavaScript via C++.
---

## **Möjliga användningsscenario**

Aspose.Cells for JavaScript via C++ tillhandahåller metoden [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) som du kan använda för att lägga till en digital signatur i en redan signerad Excel-fil.

{{% alert color="primary" %}}

Vänligen observera att när du lägger till en digital signatur i ett redan signerad Excel-dokument, fungerar det bäst om den ursprungliga filen är genererad av Aspose.Cells. Men om den ursprungliga filen är genererad av andra motorer (t.ex. Microsoft Excel) kan Aspose.Cells inte behålla filen oförändrad efter att den laddats och sparats om, vilket gör den ursprungliga signaturen ogiltig.

{{% /alert %}}

## **Hur man lägger till en digital signatur till en redan signerad Excel-fil**

 Följande exempel visar hur man använder [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)-metoden för att lägga till en digital signatur i en redan signerad Excel-fil. Kontrollera [exempel-Excel-filen](50528280.xlsx) som används i denna kod. Denna fil är redan digitalt signerad. Kontrollera [utdata Excel-filen](50528281.xlsx) som genereras av koden. Vi har använt demosertifikatet [AsposeDemo.pfx](50528279.pfx) i denna kod, som har ett lösenord **aspose**. Skärmbilden visar effekten av kodexemplet på exemplexcel-filen efter körning.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Digital Signature Example</title>
    </head>
    <body>
        <h1>Add Digital Signature to Workbook</h1>
        <p>Select an Excel file and a PFX certificate, enter the certificate password, then click "Add Digital Signature".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <br/><br/>
        <input type="file" id="certInput" accept=".pfx" />
        <br/><br/>
        <label for="certPassword">Certificate Password:</label>
        <input type="password" id="certPassword" value="aspose" />
        <br/><br/>
        <button id="runExample">Add Digital Signature</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, DigitalSignature, DigitalSignatureCollection, SaveFormat, Utils } = AsposeCells;

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
            const certInput = document.getElementById('certInput');
            const passwordInput = document.getElementById('certPassword');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!certInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            // Read files as ArrayBuffer
            const excelFile = fileInput.files[0];
            const certFile = certInput.files[0];
            const certPassword = passwordInput.value;

            const excelArrayBuffer = await excelFile.arrayBuffer();
            const certArrayBuffer = await certFile.arrayBuffer();

            // Instantiate Workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(excelArrayBuffer));

            // Create the digital signature collection
            const dsCollection = new DigitalSignatureCollection();

            // Create new digital signature and add it in digital signature collection
            // Using certificate bytes (Uint8Array), password, comment and signing date
            const signature = new DigitalSignature(new Uint8Array(certArrayBuffer), certPassword, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
            dsCollection.add(signature);

            // Add digital signature collection inside the workbook
            workbook.addDigitalSignature(dsCollection);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDigitallySignedByCells.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Digitally Signed Excel File';

            // Dispose the workbook
            workbook.dispose();

            resultDiv.innerHTML = '<p style="color: green;">Digital signature added successfully! Click the download link to get the signed file.</p>';
        });
    </script>
</html>
```
