---
title: JavaScriptを利用したC++でのワークシートの保護解除
linktitle: ワークシートの保護解除
type: docs
weight: 20
url: /ja/javascript-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

開発者が保護されたワークシートから保護を解除してファイルに変更を加える必要がある場合は？ Aspose.Cells を使用して簡単に行うことができます。

{{% /alert %}}

## **ワークシートの保護を解除する**

### **Microsoft Excel の使用**

ワークシートから保護を解除するには：

**ツール**メニューから**保護**を選択し、その後**シートの保護解除**を選びます。ワークシートがパスワード保護されていなければ、保護は解除されます。パスワード保護されている場合は、ダイアログでパスワードの入力を求められます。パスワードを入力すれば、シートの保護が解除されます。

### **Aspose.Cells を使用して単純に保護されたワークシートの保護解除**

ワークシートは、[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスの[**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--)メソッドを呼び出すことで保護解除できます。パスワードなしの単純な保護されたシートは、パスワードで保護されていないシートです。このようなシートは、パラメータを渡さずに[**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--)メソッドを呼び出すことで解除可能です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet without a password
            worksheet.unprotect();

            // Saving the Workbook in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Aspose.Cells を使用してパスワードで保護されたワークシートの保護解除**

パスワード保護されたワークシートは、パスワードで保護されたシートです。そのようなシートは、パスワードを引数に取るオーバーロードされた[**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--)メソッドを呼び出すことで解除できます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet with a password (empty password in original code)
            worksheet.unprotect("");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
