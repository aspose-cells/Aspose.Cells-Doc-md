---
title: Excelマクロ対応ワークブックのVBAコード管理
linktitle: マクロプロジェクト
type: docs
weight: 200
url: /ja/javascript-cpp/manage-vba-project/
description: C++を使用してAspose.Cells for JavaScript経由でVBAモジュールを追加し、VBAまたはマクロを修正します。
---

## **JavaScriptを使用してC++経由でVBAモジュールを追加します。**
{{% alert color="primary" %}}

Aspose.Cellsを使用すると、C++経由でAspose.Cells for JavaScriptを使って新しいVBAモジュールとマクロコードを追加できます。ワークブック内に新しいVBAモジュールを追加するには、[**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-)メソッドを使用してください。

{{% /alert %}}

以下のサンプルコードは、新しいワークブックを作成し、新しいVBAモジュールとマクロコードを追加して、XLSM形式で保存します。出力されたXLSMファイルをMicrosoft Excelで開き、「開発」>「Visual Basic」をクリックすると、「TestModule」と名前付けられたモジュールと、その中のマクロコードが表示されます。

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

## **JavaScriptを使用してC++経由でVBAまたはマクロを修正します。**

{{% alert color="primary" %}} 

C++経由でAspose.Cells for JavaScriptを使用してVBAまたはマクロコードを修正できます。Aspose.Cellsは、ExcelファイルのVBAプロジェクトを読み取り修正するための以下のモジュールとクラスを追加しました。

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

この記事では、Aspose.Cellsを使用してソースExcelファイル内のVBAまたはマクロコードを変更する方法を説明します。

{{% /alert %}} 

以下のサンプルコードは、内包されているVBAまたはマクロコードを持つソースExcelファイルを読み込みます。

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Aspose.Cellsのサンプルコードの実行後、VBAまたはマクロコードは次のように変更されます。

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

提供されたリンクから [ソースExcelファイル](5112508.xlsm) と [出力Excelファイル](5112511.xlsm) をダウンロードできます。

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

## **高度なトピック**
- [ワークブック内のVBAプロジェクトにライブラリ参照を追加する](/cells/ja/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [フォームコントロールにマクロを割り当てる](/cells/ja/javascript-cpp/assign-macro-to-form-control/)
- [VBAコードのデジタル署名が有効かどうかをチェックする](/cells/ja/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [VBAコードが署名されているかを確認する](/cells/ja/javascript-cpp/check-if-vba-code-is-signed/)
- [WorkbookのVBAプロジェクトが署名されているかを確認する](/cells/ja/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [VBAプロジェクトが保護されており、閲覧用にロックされているかを確認する](/cells/ja/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー](/cells/ja/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [証明書でVBAコードプロジェクトにデジタル署名する](/cells/ja/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA証明書をファイルまたはストリームにエクスポートする](/cells/ja/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [ワークブックの読み込み時にVBAプロジェクトをフィルタリングする](/cells/ja/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [VBAプロジェクトが保護されているかを調べる](/cells/ja/javascript-cpp/find-out-if-vba-project-is-protected/)
- [ExcelワークブックのVBAプロジェクトをパスワードで保護する](/cells/ja/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
