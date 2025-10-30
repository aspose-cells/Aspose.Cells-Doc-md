---
title: ピボットテーブルとソースデータ
type: docs
weight: 30
url: /ja/javascript-cpp/pivot-table-and-source-data/
---

## **Pivot Tableのソースデータ**

デザイン時にはわからない異なるデータソース（たとえばデータベースなど）からデータを取るピボットテーブルを作成したいときがあります。この記事では、ピボットテーブルのデータソースを動的に変更するアプローチについて説明します。

### **ピボットテーブルのデータソースを変更する**

1. 新しいデザイナーテンプレートを作成します。
   1. 以下のスクリーンショットに示すように、新しいデザイナーテンプレートファイルを作成します。
   1. その後、**DataSource**という名前の範囲を定義します。この範囲はこれらのセルの範囲を参照します。

      **デザイナーテンプレートの作成と名前付き範囲の定義、DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. この名前付き範囲に基づいてPivot Tableを作成します。
   1. Microsoft Excelで**データ**、**ピボットテーブル**、**ピボットテーブルおよびピボットチャートレポート**を選択します。
   1. 最初のステップで作成した名前付き範囲に基づいてピボットテーブルを作成します。

      **DataSourceに基づいてピボットテーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. 対応するフィールドをピボットテーブルの行と列にドラッグし、スクリーンショットに示されているような結果のピボットテーブルを作成します。

   **対応するフィールドに基づいてピボットテーブルを作成する** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


設計したピボットテーブルが以下に示されています。
   1. **データオプション**の設定で**開くときに更新**をチェックします。

      **ピボットテーブルオプションの設定** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


これで、このファイルをデザイナーテンプレートファイルとして保存できます。

1. 新しいデータを埋め込んでピボットテーブルのソースデータを変更します。
   1. デザイナーテンプレートが作成されたら、次のコードを使用してピボットテーブルのソースデータを変更します。

以下のコード例を実行すると、ピボットテーブルのソースデータが変更されます。

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

            // Instantiating a Workbook object using uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Populating new data to the worksheet cells
            worksheet.cells.get("A9").value = "Golf";
            worksheet.cells.get("B9").value = "Qtr4";
            worksheet.cells.get("C9").value = 7000;

            // Changing named range "DataSource"
            const range = worksheet.cells.createRange(0, 0, 9, 3);
            range.name = "DataSource";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
