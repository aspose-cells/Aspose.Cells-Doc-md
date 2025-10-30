---
title: Passwort von verschlüsselten Dateien mit JavaScript via C++ überprüfen
linktitle: Passwort von verschlüsselten Dateien verifizieren
type: docs
weight: 10
url: /de/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/
description: Überprüfen Sie das Passwort von verschlüsselten Excel (xlsx, xlsb, xls, xlsm) und Open Office (ODS) Dateien mit Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  
Wenn Excel- (xlsx, xlsb, xls, xlsm) und Open Office- (ODS) Dateien mit einem Passwort gesperrt sind, unterstützt Aspose eine einfache Passwortüberprüfung, ohne spezifische Daten der Dateien zu analysieren.  
{{% /alert %}}  

## **Das Passwort der verschlüsselten Datei verifizieren**  

 Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells for JavaScript via C++ die Methode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-). Diese Methode akzeptiert zwei Parameter, den Datei-Stream und das zu überprüfende Passwort.  
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Verify Excel Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatUtil, Utils } = AsposeCells;

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
            const bytes = new Uint8Array(arrayBuffer);

            const isPasswordValid = FileFormatUtil.verifyPassword(bytes, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```
