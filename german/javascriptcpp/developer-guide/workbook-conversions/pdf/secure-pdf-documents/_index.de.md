---
title: Geschützte PDF Dokumente mit JavaScript via C++ sichern
linktitle: Sichere PDF Dokumente
type: docs
weight: 120
url: /de/javascript-cpp/secure-pdf-documents/
description: Lernen Sie, wie Sie PDF Dokumente durch Verwendung von Besitzer und Benutzerpasswörtern sichern und Berechtigungen für PDF Dateien mit Aspose.Cells for JavaScript via C++ festlegen.
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/) für die Arbeit mit Sicherheit. Sie können Besitzer- und Benutzerkennwörter beim Speichern in PDF festlegen. Das Besitzer- oder Benutzerkennwort ist erforderlich, um das verschlüsselte PDF-Dokument zu öffnen.

- Das Benutzerschlüssel kann null oder eine leere Zeichenkette sein; in diesem Fall wird kein Passwort vom Benutzer beim Öffnen des PDF-Dokuments verlangt.
- Das Öffnen des PDF-Dokuments mit dem richtigen Besitzerkennwort gewährt vollen Zugriff (ohne Zugriffsrestriktionen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der unten stehende Beispielcode beschreibt, wie PDFs mit Aspose.Cells gesichert werden können.

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

Wenn die Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) kurz vor dem Rendern in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die richtigen Werte im PDF dargestellt.

{{% /alert %}}
