---
title: Festlegen des starken Verschlüsselungstyps mit JavaScript via C++
linktitle: Festlegen des starken Verschlüsselungstyps
type: docs
weight: 60
url: /de/javascript-cpp/setting-strong-encryption-type/
description: Lernen Sie, wie man starke Verschlüsselungstypen für Excel Dateien mit Aspose.Cells for JavaScript via C++ festlegt.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) ermöglicht es Ihnen, Arbeitsmappen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter bereitgestellt werden. Ein kryptografischer Dienstanbieter (oder CSP) ist eine Reihe von kryptografischen Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist "Office 97/2000 Compatible". Dies ist ein CSP mit einigen öffentlich bekannten Sicherheitsproblemen. Arbeitsmappen, die mit der "schwachen Verschlüsselung (XOR)" oder dem Verschlüsselungstyp "Office 97/2000 Compatible" gesichert sind, können leicht geknackt werden.

Um dieses Problem zu überwinden, verwenden Sie eine der starken Verschlüsselungstypen, die von Microsoft Excel bereitgestellt werden. Sie können den Verschlüsselungstyp auf den stärksten verfügbaren CSP ändern. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich, zum Beispiel 'Microsoft Strong Cryptographic Provider'.

Sie können auch Excel-Dateien mit starkem Verschlüsselungstyp mithilfe der Aspose.Cells-API verschlüsseln und mit einem Passwort schützen.

{{% /alert %}}  
## **Verschlüsselung mit Microsoft Excel anwenden**  
Um die Dateiverschlüsselung in Microsoft Excel (zum Beispiel 2007) zu implementieren:

1. Wählen Sie im **Extras**-Menü die Option **Optionen** aus.  
1. Wählen Sie den Tab **Sicherheit** aus.  
1. Geben Sie einen Wert für das Feld **Kennwort zum Öffnen** ein.  
1. Klicken Sie auf **Erweitert**.  
1. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.  

## **Verschlüsselung mit Aspose.Cells anwenden**  
Die unten stehenden Codebeispiele wenden eine starke Verschlüsselung auf eine Datei an und setzen ein Passwort.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```
