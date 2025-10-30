---
title: Aspose.Cells for JavaScriptをC++で使用してパスワードの修正を確認する
linktitle: 修正パスワードの確認
type: docs
weight: 2400
url: /ja/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: Aspose.Cells for JavaScriptをC++で使用して、修正用のパスワードが一致するかどうかを確認する方法を学びます。
---

{{% alert color="primary" %}}  
プログラムmatically、与えられたパスワードが**修正用パスワード**と一致するかどうかを確認する必要がある場合があります。Aspose.Cellsは`WorkbookSettings.writeProtection.validatePassword()`メソッドを提供しており、これを使用してパスワードの正確性を確認できます。  
{{% /alert %}}  

## **Microsoft Excelで変更するためのパスワードをチェックする**  

Microsoft Excelで作成するワークブックに**開くためのパスワード**および**変更するためのパスワード**を割り当てることができます。これらのパスワードを指定するためのMicrosoft Excelが提供するインターフェースを示すスクリーンショットをご覧ください。  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **C++を使用したAspose.Cells for JavaScriptでのパスワードの変更確認**  

以下のサンプルコードは、[ソースExcel](5112232.xlsx)ファイルを読み込みます。このファイルには、開くためのパスワードが1234、修正用パスワードが5678と設定されています。最初に、567が正しい修正パスワードかどうかを確認し、間違っていればfalseを返します。次に、5678が正しい修正パスワードかどうかをチェックし、正しければtrueを返します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Write Protection Passwords</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Specify password to open inside the load options
            const opts = new LoadOptions();
            opts.password = "1234";

            // Open the source Excel file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Check if 567 is Password to modify
            let ret = workbook.settings.writeProtection.validatePassword("567");
            let outputHtml = `<p>Is 567 correct Password to modify: ${ret}</p>`;

            // Check if 5678 is Password to modify
            ret = workbook.settings.writeProtection.validatePassword("5678");
            outputHtml += `<p>Is 5678 correct Password to modify: ${ret}</p>`;

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```  

### **コンソール出力**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
