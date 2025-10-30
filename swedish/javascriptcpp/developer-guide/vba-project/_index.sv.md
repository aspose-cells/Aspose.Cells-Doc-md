---
title: Hantera VBA koder i Excel makroaktiverad arbetsbok
linktitle: Makroprojekt
type: docs
weight: 200
url: /sv/javascript-cpp/manage-vba-project/
description: Lägg till VBA modul och ändra VBA eller makro med Aspose.Cells for JavaScript via C++.
---

## **Lägg till en VBA-modul i JavaScript via C++**
{{% alert color="primary" %}}

Aspose.Cells låter dig lägga till en ny VBA-modul och makrokod med Aspose.Cells for JavaScript via C++. Vänligen använd [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-)-metoden för att lägga till den nya VBA-modulen i arbetsboken

{{% /alert %}}

Följande exempel skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar resultatet i XLSM-format. När du öppnar XLSM-filen i Microsoft Excel och klickar på **Utvecklare > Visual Basic**-menyn, kommer du att se en modul med namnet "TestModule" och därinne följer makrokoden.

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

## **Ändra VBA eller Makro i JavaScript via C++**

{{% alert color="primary" %}} 

Du kan modifiera VBA- eller Makrokod med Aspose.Cells for JavaScript via C++. Aspose.Cells har lagt till följande modul och klasser för att läsa och ändra VBA-projektet i Excel-filen.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar hur du ändrar VBA eller makrokoden inne i käll-Excel-filen med hjälp av Aspose.Cells.

{{% /alert %}} 

Följande exempel laddar den käll-Excel filen som har VBA- eller makrokod inuti den.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Efter att Aspose.Cells provkoden har körts kommer VBA- eller makrokoden att modifieras på detta sätt

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Du kan ladda ner den [källa Excel-filen](5112508.xlsm) och den [utdata Excel-filen](5112511.xlsm) från de angivna länkarna.

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

## **Fortsatta ämnen**
- [Lägg till en biblioteksreferens till VBA-projektet i arbetsboken](/cells/sv/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Tilldela makro till formulärkontroll](/cells/sv/javascript-cpp/assign-macro-to-form-control/)
- [Kontrollera om den digitala signaturen av VBA-koden är giltig](/cells/sv/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Kontrollera om VBA-koden är signerad](/cells/sv/javascript-cpp/check-if-vba-code-is-signed/)
- [Kontrollera om VBA-projektet i en arbetsbok är signerat](/cells/sv/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken](/cells/sv/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signera digitalt ett VBA-kodprojekt med certifikat](/cells/sv/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportera VBA-certifikat till fil eller ström](/cells/sv/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrera VBA-projekt vid inläsning av en arbetsbok](/cells/sv/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Lösenordsskydda VBA-projektet för Excel-arbetsbok](/cells/sv/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
