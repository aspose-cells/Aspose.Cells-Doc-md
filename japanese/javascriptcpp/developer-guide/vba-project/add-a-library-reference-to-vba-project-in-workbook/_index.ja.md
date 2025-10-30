---
title: JavaScriptを使用したC++でのワークブック内のVBAプロジェクトにライブラリ参照を追加
linktitle: ワークブックのVBAプロジェクトにライブラリの参照を追加
type: docs
weight: 80
url: /ja/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/
---

{{% alert color="primary" %}}

時折、コードを通じてVBAプロジェクトにライブラリ参照を追加または登録する必要があります。Aspose.Cellsの[**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)メソッドを使用して行うことができます。

{{% /alert %}}

## **Microsoft ExcelのVBAプロジェクトにライブラリ参照を追加する**

Microsoft Excelでは、**ツール > 参照設定...**をクリックしてVBAプロジェクトにライブラリ参照を追加できます。

## **Aspose.Cells for JavaScriptを使用してワークブックのVBAプロジェクトにライブラリ参照を追加**

以下のサンプルコードは、[**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/javascript-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)メソッドを使用してワークブックのVBAプロジェクトに2つのライブラリ参照を追加または登録します。

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
