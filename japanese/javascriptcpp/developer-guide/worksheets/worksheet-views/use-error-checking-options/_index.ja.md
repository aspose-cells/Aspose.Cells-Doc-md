---
title: エラーチェックオプションをJavaScriptを介してC++で使用します
linktitle: エラーチェックオプションを使用する
type: docs
weight: 140
url: /ja/javascript-cpp/use-error-checking-options/
description: Aspose.Cells for JavaScriptを使って、Excelワークシートでエラーチェックオプションをプログラム的に使用する方法を学びます。
keywords: Excelで数値をテキストとして保存するJavaScript/C++エラー検出オプション
---

{{% alert color="primary" %}}  
Microsoft Excelでは、ユーザーはエラーチェックのオプションやルールを定義することができます。ユーザーが数式を作成する際にエラーチェックが表示されることがよくあり、セルの右上隅に小さな三角形が表示されます。Excelは、一般的な問題を修正するための情報を提供します。  
{{% /alert %}}  

## **エラーの種類**  

ゼロ除算など、結果を返せない数式を含むエラーは直ちに対処が必要であり、セルにエラー値が表示されます。緑の三角にマウスを合わせると感嘆符が表示され、それをクリックするとオプションのリストが開きます。  

このエラーはオプションで解決または無視できます。無視した場合、そのエラーは次回のエラー検査で表示されません。  

Aspose.Cellsはエラー検査機能を提供します。[**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption)クラスは、数字をテキストとして保存するエラーや数式計算エラー、検証エラーなど、さまざまなタイプのエラー検査を管理します。[**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype)列挙体を使用して、望ましいエラー検査を設定します。  

## **テキストとして保存された数値**  

時折、数値はセル内でテキストとしてフォーマットされ保存されることがあります。これは計算に問題を引き起こしたり、混乱する並び順を生むことがあります。テキストとしてフォーマットされた数値は、セル内で右寄せではなく左寄せになります。セル内で数学的演算を行うはずの式が値を返さない場合は、式が参照しているセルの配置を確認し、これらのいくつかまたはすべてのセルがテキストとして保存された数値である可能性があります。  

テキストとして保存された数値を実際の数値に素早く変換するために、エラーチェックオプションを使用できます。Microsoft Excel 2003では:  

1. **ツール** メニューで **オプション** をクリックします。  
1. エラーチェックタブを選択します。  
   **テキストとして保存された数値** オプションがデフォルトでチェックされています。  
1. 無効にします。  

次のサンプルコードは、Aspose.CellsのAPIを使用してXLSファイルのワークシートにおいてテキストとして保存された数値のエラーチェックオプションを無効にする方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
