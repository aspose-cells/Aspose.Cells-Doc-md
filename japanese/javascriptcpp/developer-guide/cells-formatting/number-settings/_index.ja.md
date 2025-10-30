---
title: 数字の設定
linktitle: 数字の設定
description: Aspose.Cellsは、多くの異なるセル番号設定をサポートするスプレッドシートファイル操作用のJavaScriptライブラリです。この記事では、Aspose.Cellsライブラリを使用してセルの数字設定を管理し、数字のフォーマットを調整する方法を紹介します。
keywords: Aspose.Cells、JavaScriptライブラリ、電子スプレッドシート、セル番号設定、フォーマット、管理、数字と日付の形式
type: docs
weight: 10
url: /ja/javascript-cpp/cells-number-settings/
---

## **数字と日付の表示形式を設定する方法**  

Microsoft Excelの非常に優れた特徴の一つは、数値と日付の表示形式を設定できることです。数値データは、十進法、通貨、パーセンテージ、分数、簿記値など、さまざまな値を表すために使用できます。これら全ての数値は、その値が表す情報の種類に応じて異なるフォーマットで表示されます。同様に、日付や時間も多くの表示形式があります。  
Aspose.Cellsはこの機能をサポートし、開発者が数値や日付の表示形式を設定できるようにします。  

### **Microsoft Excelで表示形式を設定する方法**  

Microsoft Excelで表示形式を設定するには：  

1. 任意のセルを右クリックします。  
2. **セルの書式設定**を選択します。ダイアログが表示され、あらゆる種類の値の表示フォーマットを設定できます。  

ダイアログの左側には、**標準**、**数値**、**通貨**、**会計**、**日付**、**時刻**、**パーセンテージ**など多くのカテゴリがあります。Aspose.Cellsはこれらすべての表示フォーマットをサポートしています。  

Aspose.Cellsは、Excelファイルを表すモジュール[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)モジュールには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションがあります。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)モジュールによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)モジュールは[**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供し、その中の各アイテムは[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトを示します。  

Aspose.Cellsは、[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)プロパティを[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)モジュールに提供します。このプロパティは、セルのフォーマット取得と設定に使用されます。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)モジュールには、数字と日付の表示形式を扱うための便利なプロパティがいくつかあります。  

### **組み込みの数値形式の使用方法**  

Aspose.Cellsは、数字と日付の表示形式を設定するための組み込みの数値フォーマットを提供しています。これらの組み込み数値フォーマットは、[**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-)プロパティを使用して適用できます。すべての組み込み数値フォーマットには固有の数値が割り当てられています。開発者は、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-)プロパティに任意の数値を割り当てて、表示形式を適用できます。この方法は高速です。Aspose.Cellsがサポートする組み込みの数値フォーマットは以下の通りです。  

|**値**|**タイプ**|**フォーマット文字列**|  
| :- | :- | :- |  
|0|General|General|  
|1|Decimal|0|  
|2|Decimal|0.00|  
|3|Decimal|#,##0|  
|4|Decimal|#,##0.00|  
|5|Currency|$#,##0;$-#,##0|  
|6|Currency|$#,##0;[Red]$-#,##0|  
|7|Currency|$#,##0.00;$-#,##0.00|  
|8|Currency|$#,##0.00;[Red]$-#,##0.00|  
|9|Percentage|0%|  
|10|Percentage|0.00%|  
|11|Scientific|0.00E+00|  
|12|Fraction|# ?/?|  
|13|Fraction|# */*|  
|14|Date|m/d/yyyy|  
|15|Date|d-mmm-yy|  
|16|Date|d-mmm|  
|17|Date|mmm-yy|  
|18|Time|h:mm AM/PM|  
|19|Time|h:mm:ss AM/PM|  
|20|Time|h:mm|  
|21|Time|h:mm:ss|  
|22|Time|m/d/yy h:mm|  
|37|Currency|#,##0;-#,##0|  
|38|Currency|#,##0;[Red]-#,##0|  
|39|Currency|#,##0.00;-#,##0.00|  
|40|Currency|#,##0.00;[Red]-#,##0.00|  
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|  
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|  
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|  
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|  
|45|Time|mm:ss|  
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = new Date();

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 20;

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 2546;

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  


### **カスタム数値形式の使用方法**  

表示形式を設定するためのカスタムフォーマット文字列を定義するには、[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)オブジェクトの[**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)プロパティを使用します。この方法はプリセットのフォーマットを使うよりも遅いですが、より柔軟です。  

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
            const fileInput = document.getElementById('fileInput');

            // Instantiate or open workbook depending on whether a file is provided
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding the current system date to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.putValue(new Date());

            // Getting the Style of the A1 Cell
            let style = cellA1.style;

            // Setting the display format to number 15 to show date as "d-mmm-yy"
            style.number = 15;

            // Applying the style to the A1 cell
            cellA1.style = style;

            // Adding a numeric value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.putValue(20);

            // Getting the Style of the A2 Cell
            style = cellA2.style;

            // Setting the display format to number 9 to show value as percentage
            style.number = 9;

            // Applying the style to the A2 cell
            cellA2.style = style;

            // Adding a numeric value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.putValue(2546);

            // Getting the Style of the A3 Cell
            style = cellA3.style;

            // Setting the display format to number 6 to show value as currency
            style.number = 6;

            // Applying the style to the A3 cell
            cellA3.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


{{% alert color="primary" %}}  

[**custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-)プロパティを使って数値形式を設定すると、以前に[**number**](https://reference.aspose.com/cells/javascript-cpp/style/#number-number-)プロパティを使用して設定された形式が上書きされ、その逆も同様です。  

{{% /alert %}}  

## **高度なトピック**  
- [Style.Customプロパティを設定する際のカスタム数値形式を確認する](/cells/ja/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [サポートされている数値形式のリスト](/cells/ja/javascript-cpp/list-of-supported-number-formats/)  
- [カスタム日付形式パターン g および ge mm dd の表現](/cells/ja/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [ブックでのカスタム数値小数点およびグループの区切りの指定](/cells/ja/javascript-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [DBNumカスタムパターンの書式設定の指定](/cells/ja/javascript-cpp/specifying-dbnum-custom-pattern-formatting/)
