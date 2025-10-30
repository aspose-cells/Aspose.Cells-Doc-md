---
title: Skydda PDF dokument med JavaScript via C++
linktitle: Säkra PDF dokument
type: docs
weight: 120
url: /sv/javascript-cpp/secure-pdf-documents/
description: Lär dig att säkra PDF dokument genom att använda ägar och användarlösenord, samt ställa in behörigheter för PDF filer med hjälp av Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells tillhandahåller [**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ange ägar- och användarlösenord vid sparning till PDF. Ägarlösenord eller användarlösenord krävs för att öppna den krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller en tom sträng; i så fall krävs inget lösenord av användaren när PDF-dokumentet öppnas.
- Att öppna PDF-dokumentet med rätt ägarlösenord ger full tillgång (utan några tillgångsrestriktioner angivna) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Exempelkoden nedan beskriver hur du säkrar PDF:er med Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Secure PDF Example</title>
    </head>
    <body>
        <h1>Secure PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PDF save options and security options
            const saveOption = new PdfSaveOptions();
            saveOption.securityOptions = new PdfSecurityOptions();

            // Set security options (converted from getters/setters to properties)
            saveOption.securityOptions.userPassword = "user";
            saveOption.securityOptions.ownerPassword = "owner";
            saveOption.securityOptions.extractContentPermission = false;
            saveOption.securityOptions.printPermission = false;

            // Save the workbook to PDF with security options
            const outputData = workbook.save(SaveFormat.Pdf, saveOption);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'securepdf_test.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Secure PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the secured PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) precis innan det renderas till PDF. Detta ser till att formelberoende värden omberäknas och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
