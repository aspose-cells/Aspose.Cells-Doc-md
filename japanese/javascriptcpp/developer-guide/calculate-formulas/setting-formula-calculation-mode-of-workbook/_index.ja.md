---
title: Workbookの数式計算モードをJavaScriptを介したC++で設定する方法
linktitle: ワークブックの式の計算モードを設定する
description: この記事では、C++を介してAspose.Cells for JavaScriptを使用し、Microsoft Excelのワークブックの数式計算モードを設定する方法を紹介します。既存のExcelファイルを読み込むか、新規作成し、Aspose.Cellsの提供するプロパティを使用して計算モードを設定し、結果を取得します。最後に、変更したExcelファイルを保存します。
keywords: Aspose.Cells、Excel、ワークブック、数式計算モード設定、JavaScript経由のC++
type: docs
weight: 110
url: /ja/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excelでは、フォーミュラ計算モード、つまりフォーミュラの計算方法を設定できます。3つの可能な値があります。  

- 自動 - 何かが変更されるたびに再計算し、ワークブックが開かれるたびに再計算します。  
- データテーブル以外自動 - 何かが変更されるたびに再計算しますが、データテーブルを除外します。  
- マニュアル - ユーザーがF9またはCTRL+ALT+F9を押すか、ワークブックが保存されたときにのみ再計算します。  
{{% /alert %}}  

Microsoft Excelでの式計算モードを設定するには:  

1. **式**、次に**計算オプション**を選択します。  
1つのオプションを選択します。  

Aspose.Cells for JavaScriptはC++を使用して[**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--)モードプロパティを使った**数式計算モード**の設定も可能です。以下の値のいずれかを持つ[**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype)列挙型に割り当てることができます：  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
