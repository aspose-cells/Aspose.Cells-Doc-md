---
title: Manage VBA codes of Excel Macro-Enabled workbook
linktitle: Macro Project
type: docs
weight: 200
url: /javascript-cpp/manage-vba-project/
description: Add VBA Module and Modify VBA or Macro with Aspose.Cells for JavaScript via C++.
---

## **Add a VBA Module in JavaScript via C++**
{{% alert color="primary" %}}

Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells for JavaScript via C++. Please use the [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) method to add the new VBA Module inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.

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

## **Modify VBA or Macro in JavaScript via C++**

{{% alert color="primary" %}} 

You can modify VBA or Macro Code using Aspose.Cells for JavaScript via C++. Aspose.Cells has added the following modules and classes to read and modify the VBA project in the Excel file.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells.

{{% /alert %}} 

The following sample code loads the source Excel file which has the following VBA or Macro code inside it

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

After the execution of Aspose.Cells sample code, the VBA or Macro code will be modified like this

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

You can download the [source Excel file](5112508.xlsm) and the [output Excel file](5112511.xlsm) from the given links.

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
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
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

## **Advanced topics**
- [Add a library reference to VBA project in workbook](/cells/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assign Macro to Form Control](/cells/javascript-cpp/assign-macro-to-form-control/)
- [Check if Digital Signature of VBA Code is Valid](/cells/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Check if VBA Code is Signed](/cells/javascript-cpp/check-if-vba-code-is-signed/)
- [Check if VBA project in a Workbook is Signed](/cells/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Check if VBA Project is Protected and Locked for Viewing](/cells/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook](/cells/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitally Sign a VBA Code Project with Certificate](/cells/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Export VBA Certificate to File or Stream](/cells/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Filter VBA Project while loading a workbook](/cells/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Find out if VBA Project is Protected](/cells/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Password Protect the VBA Project of Excel Workbook](/cells/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)