---
title: Verwalten von VBA Codes in einer Excel Makro aktivierten Arbeitsmappe
linktitle: Makro Projekt
type: docs
weight: 200
url: /de/javascript-cpp/manage-vba-project/
description: Fügen Sie ein VBA Modul hinzu und ändern Sie VBA oder Makros mit Aspose.Cells for JavaScript über C++.
---

## **Fügen Sie ein VBA-Modul in JavaScript über C++ hinzu**
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein neues VBA-Modul und Makro-Code mit Aspose.Cells for JavaScript über C++ hinzuzufügen. Bitte verwenden Sie die [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-)-Methode, um das neue VBA-Modul innerhalb der Arbeitsmappe hinzuzufügen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, fügt ein neues VBA-Modul und Makro-Code hinzu und speichert die Ausgabe im XLSM-Format. Sobald Sie die XLSM-Ausgabedatei in Microsoft Excel öffnen und die Befehle **Entwickler > Visual Basic** klicken, sehen Sie ein Modul mit dem Namen "TestModule" und darin den folgenden Makro-Code.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ändern Sie VBA oder Makro in JavaScript über C++**

{{% alert color="primary" %}} 

Sie können VBA- oder Makro-Code mit Aspose.Cells for JavaScript über C++ ändern. Aspose.Cells hat die folgenden Module und Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu ändern.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makrocode in der Quell-Excel-Datei mithilfe von Aspose.Cells ändern können.

{{% /alert %}} 

Der folgende Beispielcode lädt die Quelldatei mit Excel, die den VBA- oder Makro-Code enthält

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Nach der Ausführung des Beispielcodes von Aspose.Cells wird der VBA- oder Makrocode wie folgt modifiziert sein

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Sie können die [Quell-Excel-Datei](5112508.xlsm) und die [Ausgabe-Excel-Datei](5112511.xlsm) über die angegebenen Links herunterladen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Erweiterte Themen**
- [Fügen Sie einen Bibliotheksverweis zum VBA-Projekt im Arbeitsblatt hinzu](/cells/de/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Makro einem Formularsteuerelement zuweisen](/cells/de/javascript-cpp/assign-macro-to-form-control/)
- [Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist](/cells/de/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Überprüfen Sie, ob der VBA-Code signiert ist](/cells/de/javascript-cpp/check-if-vba-code-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist](/cells/de/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt geschützt und zum Anzeigen gesperrt ist](/cells/de/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei](/cells/de/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitales Signieren eines VBA-Codeprojekts mit Zertifikat](/cells/de/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportieren Sie das VBA-Zertifikat in eine Datei oder einen Stream](/cells/de/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtern eines VBA-Projekts beim Laden einer Arbeitsmappe](/cells/de/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Herausfinden, ob das VBA-Projekt geschützt ist](/cells/de/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Passwortschutz des VBA-Projekts der Excel-Arbeitsmappe](/cells/de/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
