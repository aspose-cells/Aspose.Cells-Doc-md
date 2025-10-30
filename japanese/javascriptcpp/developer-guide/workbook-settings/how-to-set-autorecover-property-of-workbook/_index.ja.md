---
title: JavaScriptを使用してワークブックのAutoRecoverプロパティを設定する方法（C++経由）
linktitle: ワークブックのAutoRecoverプロパティを設定する方法
type: docs
weight: 220
url: /ja/javascript-cpp/how-to-set-autorecover-property-of-workbook/
description: C++経由のAspose.Cells for JavaScriptを使ってワークブックのAutoRecoverプロパティを設定する方法を学びます。
---

{{% alert color="primary" %}}  
Aspose.Cellsを使用して、ワークブックの自動回復プロパティを設定できます。このプロパティのデフォルト値は**true**です。これを**false**に設定すると、Microsoft ExcelはそのExcelファイルの自動回復（自動保存）を無効にします。  

Aspose.Cellsは、このオプションを有効または無効にするための[**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--)プロパティを提供しています。  
{{% /alert %}}  

以下のコードは、ワークブックの[**Workbook.autoRecover**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#autoRecover--)プロパティの使用方法を説明します。最初にこのプロパティのデフォルト値（**true**）を読み取り、その後**false**に設定してワークブックを保存します。次に再度ワークブックを読み取り、その時点でのこのプロパティの値（**false**）を確認します。  

## ワークブックのAutoRecoverプロパティを設定するJavaScriptコード  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - AutoRecover</title>
    </head>
    <body>
        <h1>AutoRecover Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            // Create workbook object
            const workbook = new Workbook();

            // Read AutoRecover property
            const autoRecoverBefore = workbook.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover before: ${autoRecoverBefore}</p>`;

            // Set AutoRecover property to false
            workbook.settings.autoRecover = false;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download output_out.xlsx';

            // Read the saved workbook again from the saved data
            const workbook2 = new Workbook(new Uint8Array(outputData));

            // Read AutoRecover property
            const autoRecoverAfter = workbook2.settings.autoRecover;
            resultDiv.innerHTML += `<p>AutoRecover after reload: ${autoRecoverAfter}</p>`;
        });
    </script>
</html>
```  

## **出力**  



{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}
