---
title: 複雑な基準を満たすレコードを表示するためにMicrosoft Excelの高度なフィルタを適用する方法
type: docs
weight: 280
url: /ja/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: 複雑な条件を満たすレコードを表示するためにMicrosoft Excelの詳細設定フィルタを適用する方法について、C++ APIを使用したAspose.Cells for JavaScriptを用いて学びます。
keywords: C++を介して高度なフィルタを適用、設定、追加、作成する方法と、範囲に高度なフィルタを追加する方法について学びます。
---

## **可能な使用シナリオ**  

Microsoft Excelでは、複合条件を満たすレコードを表示するためにワークシートデータに *高度なフィルター* を適用できます。Excelの *データ > 詳細設定* コマンドを使ってこのフィルターを適用することができます（スクリーンショット参照）。  

![todo:image_alt_text](1.png)  

C++を使用したAspose.Cells for JavaScriptは、[**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-)メソッドを使用して高度なフィルタを適用することも可能です。Microsoft Excelと同様に、次のパラメータを受け入れます。  

**isFilter**  

リストをその場でフィルタ処理するかどうかを示します。  

**listRange**  

リストの範囲。  

**criteriaRange**  

基準の範囲。  

**copyTo**  

データをコピーする範囲。  

**uniqueRecordOnly**  

唯一の行を表示またはコピーします。  

## **複雑な基準を満たすレコードを表示するMicrosoft Excelの高度なフィルタの適用**  

次のサンプルコードは、[サンプルExcelファイル](48496692.xlsx)に高度なフィルターを適用し、[出力Excelファイル](48496691.xlsx)を生成します。スクリーンショットは両方のファイルを比較表示しています。スクリーンショット内のデータは、複雑な条件に従ってフィルタリングされています。  

![todo:image_alt_text](2.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
