---
title: JavaScriptを使用したヘッダーとフッターの設定（C++経由）
linktitle: ヘッダーとフッターの設定
type: docs
weight: 30
url: /ja/javascript-cpp/setting-headers-and-footers/
description: この記事では、Aspose.Cells for JavaScriptを使用してExcelのワークシートのヘッダーとフッターに画像をプログラム的に挿入する方法について説明します。 
keywords: Excelのヘッダーとフッターに画像を挿入し、JavaScriptを使用してC++でスクリプトコマンドを設定
---

{{% alert color="primary" %}}

ヘッダーとフッターはそれぞれ上部の余白の下に表示されるテキスト行です。ワークシートにもヘッダーやフッターを追加することができます。ヘッダーやフッターには、ページ番号、著者名、トピック名、または日付と時刻などの有用な情報を表示することができます。ヘッダーとフッターはページ設定の設定を使用して管理されます。

{{% /alert %}}

## **ヘッダーとフッタの設定**

Aspose.Cells for JavaScriptをC++で使用すると、実行時にワークシートにヘッダーとフッターを追加できますが、印刷のためには事前にデザインされたファイルで手動で設定することを推奨します。Microsoft ExcelをGUIツールとして使用し、ヘッダーとフッターを設定して労力と開発時間を節約できます。Aspose.Cellsはファイルをインポートし、設定を保存できます。

ヘッダーやフッターをランタイムで追加するために、Aspose.Cells は特別な API 呼び出しとスクリプトコマンドを提供しています。

### **スクリプトコマンド**

スクリプトコマンドは、ヘッダーやフッターのフォーマットを設定する特別なコマンドです。

|**スクリプトコマンド**|**説明**|
| :- | :- |
|&P|現在のページ番号
|&G|画像
|&N|ページの総数
|&D|現在の日付
|&T|現在の時刻
|&A|ワークシート名
|&F|パスを除いたファイル名
|&&Text|は &Text を表示します。例： &&WO は &WO と表示されます|
|&"\<FontName>"|フォント名を表します。例: &"Arial"
|&"\<FontName>, \<FontStyle>"|スタイル付きのフォント名を表します。例: &"Arial,Bold"
|&\<FontSize>|フォントサイズを表します。例：「&14abc」。ただし、このコマンドの後にヘッダーに印刷されるプレーンな数字が続く場合、その数字はフォントサイズとスペースで区切る必要があります。例：「&14 123」。|

### **ヘッダーやフッタの設定**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスは、ワークシートにヘッダーとフッターを追加するための[**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-)と[**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-)の2つのメソッドを提供します。これらのメソッドは2つのパラメータだけを受け取ります：

- **Section** – ヘッダーやフッターを配置するセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **Script** – ヘッダーやフッターのために使用するスクリプト。このスクリプトにはヘッダーやフッターをフォーマットするためのスクリプトコマンドが含まれます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **ヘッダーやフッターに画像を挿入**

[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスには、ヘッダーとフッターに画像を追加するための[**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-)と[**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-)の追加メソッドがあります。これらのメソッドは次のパラメータを受け取ります：

- **Section** – 画像が配置されるヘッダーやフッターセクション。左、中央、右の3つのセクションがあり、それぞれ0、1、2で表されます。
- **バイト配列** – グラフィカルデータ（バイナリデータはバイト配列のバッファに書き込む必要があります）。

以下のコードを実行し、ファイルを開いた後、ワークシートのヘッダーを確認してください。

1. **ファイル** メニューから **ページ設定** を選択します。ダイアログが表示されます。
1. **ヘッダー/フッター** タブを選択します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
