---
title: Add a library reference to VBA project in workbook with JavaScript via C++
linktitle: Add a library reference to VBA project in workbook
type: docs
weight: 80
url: /javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/
---

{{% alert color="primary" %}}

Sometimes, you need to add or register the library reference to the VBA project through code. You can do it using Aspose.Cells **VbaProjectReferenceCollection.addRegisteredReference(string, string)** method.

{{% /alert %}}

## **Add a library reference to the VBA project in Microsoft Excel**

In Microsoft Excel, you can add a library reference to the VBA project by clicking **Tools > References...** manually.

## **Add a library reference to the VBA project in a workbook using Aspose.Cells for JavaScript via C++**

The following sample code adds or registers two library references to the VBA project of the workbook using **VbaProjectReferenceCollection.addRegisteredReference(string, string)** method.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add VBA References Example</h1>
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
            // Creating a new Workbook
            const workbook = new Workbook();

            // Accessing the VBA project (converted from getVbaProject())
            const vbaProj = workbook.vbaProject;

            // Accessing References collection (converted from getReferences())
            vbaProj.references.addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
            vbaProj.references.addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

            // Saving the workbook as XLSM and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated XLSM File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA references added and file generated. Click the download link to save the file.</p>';
        });
    </script>
</html>
```