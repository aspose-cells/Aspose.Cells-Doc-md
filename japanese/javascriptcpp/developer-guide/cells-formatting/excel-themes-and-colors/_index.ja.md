---
title: Excelのテーマと色
linktitle: Excelのテーマと色  
type: docs  
weight: 100  
url: /ja/javascript-cpp/excel-themes-and-colors/  
description: Aspose.Cells for JavaScriptをC++経由で使用した場合のカスタムカラースキームの使い方を学ぶ  
keywords: JavaScriptでカラースキームを作成・適用、プログラム的にカスタムカラーシステムを作成、JavaScriptでカスタムカラースキームを適用する方法、Excelでカラースキームを使用する方法  
---

## **Excelでのカラースキームの適用と作成方法**  
ドキュメントテーマを使用すると、Excelドキュメントの色、フォント、グラフィックの書式効果を簡単に調整し、迅速に更新できます。  
テーマは、名前付きスタイル、グラフィック効果、他のオブジェクトを使用してブックの外観を統一します。例えば、Accent1スタイルはOfficeテーマとApexテーマで異なって見えます。多くの場合、ドキュメントテーマを適用し、その後必要に応じて修正します。  

### **Excelでのカラースキームの適用方法**  
1. Excelを開き、「ページレイアウト」タブに移動します。  
1. 「テーマ」セクションの「カラー」ボタンをクリックします。  
<br>  
<img src="color.png" width=70% />  
1. 要件に合ったカラーパレットを選択するか、スキームにマウスを重ねてライブプレビューを表示します。  

### **Excelでのカスタムカラースキームの作成方法**  
ドキュメントに新鮮で独自の外観を与えるために独自のカラーセットを作成するか、組織のブランド規準に準拠します。  

1. Excelを開き、「ページレイアウト」タブに移動します。  
1. 「テーマ」セクションの「カラー」ボタンをクリックします。  
1. 「カスタムカラーのカスタマイズ...」ボタンをクリックします。  
<br>  
<img src="color2.png" width=70% />  

1. 「新しいテーマの色の作成」ダイアログボックスで、各要素の色を選択できます。  
<br>  
<img src="color3.png" width=70% />  
1. 必要な色をすべて選択した後、「名前」フィールドにカスタムカラースキームの名前を入力します。  

1. 「保存」ボタンをクリックしてカスタムカラースキームを保存します。カスタムカラースキームは今後の使用のために「カラー」ドロップダウンメニューで利用可能になります。  

## **Aspose.Cellsでのカラースキームの作成と適用方法**  
Aspose.Cellsにはテーマと色をカスタマイズする機能が提供されています。  

### **Aspose.Cellsでのカスタムカラーテーマの作成方法**  
テーマカラーをファイル内で使用する場合、各セルを個別に変更する必要はなく、テーマの色だけを変更すればよいです。  

使用例では、希望の色でカスタムテーマを適用する方法が示されています。Microsoft Excel 2007 で手動で作成されたサンプルテンプレートファイルを使用します。  

以下の例では、テンプレートXLSXファイルを読み込み、異なるテーマカラータイプの色を定義し、カスタム色を適用してExcelファイルを保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **Aspose.Cells でテーマカラーを適用する方法**  
以下の例では、セルの前景色とフォント色をデフォルトのテーマ（ワークブック）のカラータイプに基づいて適用し、Excelファイルをディスクに保存します。  


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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Aspose.Cells でテーマカラーを取得および設定する方法**  
テーマカラーを実装するいくつかのメソッドとプロパティが以下に示されています。  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): 前景色の設定に使用します。  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): 背景色の設定に使用します。  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): フォント色の設定に使用します。  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): テーマ色を取得するために使用します。  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): テーマ色を設定するために使用します。  

使用例では、テーマカラーを取得および設定する方法が示されています。  

以下の例では、テンプレートXLSXファイルを使用し、異なるテーマカラータイプの色を取得、色を変更し、Microsoft Excelファイルを保存します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **高度なトピック**  
- [Excelファイルからテーマデータを抽出](/cells/ja/javascript-cpp/extract-theme-data-from-excel-file/)
