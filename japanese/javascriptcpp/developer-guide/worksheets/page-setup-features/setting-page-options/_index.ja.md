---
title: JavaScriptを使用したページオプション設定（C++経由）
linktitle: ページオプションの設定
type: docs
weight: 10
url: /ja/javascript-cpp/setting-page-options/
description: この記事では、JavaScriptを使用してExcelワークシートのページオプションをプログラム的に設定するサンプルコードを提供します。ページの向き、スケーリング係数、ページ合わせの設定、用紙サイズ、印刷品質、最初のページ番号を設定します。
keywords: Excelのページ向き設定（C++経由JavaScript）、スケーリングファクター設定（C++経由JavaScript）、用紙サイズ設定（C++経由JavaScript）
---

{{% alert color="primary" %}}  
時々、印刷を制御するためにワークシートのページ設定設定を構成する必要があります。これらのページ設定設定にはさまざまなオプションが用意されています。  
{{% /alert %}}  

## **ページオプションの設定**  

Aspose.Cells では、ページセットアップオプションが完全にサポートされています。この記事では、Aspose.Cells を使用してページオプションを設定する方法を説明し、設定のためのコードサンプルを示します:  

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) を提供します。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) クラスによって表されます。  

[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは、ワークシートのページ設定オプションを設定するために使われる[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)プロパティを提供します。実際、この [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) プロパティは、印刷されたワークシートのページレイアウト設定に使用される [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスのオブジェクトです。[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスはページ設定オプションを設定するさまざまなプロパティを提供します。これらの一部については以下で説明します。  

### **ページの向き**  

ページの向きは [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスの[**orientation**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#orientation--)プロパティを使って縦か横に設定できます。[**orientation**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#orientation--)プロパティは、以下にリストされている[**PageOrientationType**](https://reference.aspose.com/cells/javascript-cpp/pageorientationtype)列挙型の事前定義された値のいずれかを受け入れます。  

|**ページの向きの種類**|**説明**|  
| :- | :- |  
|Landscape| 横向きの向き|  
|Portrait| 縦向きの向き|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Orientation</title>
    </head>
    <body>
        <h1>Set Page Orientation Example</h1>
        <p>You may optionally select an existing Excel file to modify. If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PageOrientationType } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // No file selected - will operate on a new workbook
                document.getElementById('result').innerHTML = '<p>No file selected. A new workbook will be created and modified.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>File selected. The workbook will be loaded and modified.</p>';
            }

            // Load workbook from selected file if provided, otherwise create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Setting the orientation to Portrait (property assignment per getter/setter conversion)
            worksheet.pageSetup.orientation = PageOrientationType.Portrait;

            // Save the Workbook as Excel97To2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PageOrientation_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Orientation set to Portrait. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **拡大/縮小率**  

スケーリング係数を調整して、ワークシートのサイズを縮小または拡大することが可能です、そのためには[**zoom**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#zoom--)プロパティを使用します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scaling Factor Example</title>
    </head>
    <body>
        <h1>Scaling Factor Example</h1>
        <p>Select an existing Excel file to modify or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Scaling Factor to 100</button>
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

            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook
                workbook = new Workbook();
            }

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the scaling factor to 100
            worksheet.pageSetup.zoom = 100;

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ScalingFactor_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scaling factor set to 100. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **ページに合わせるオプション**  

ワークシートの内容を特定のページ数に収めるには、[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスの[**fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--)と[**fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)プロパティを使用します。これらのプロパティはワークシートのスケーリングにも使用されます。  

{{% alert color="primary" %}}  
[**fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--)/[**fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)または[**zoom**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#zoom--)プロパティのいずれかを選択できますが、両方同時には使えません。  
{{% /alert %}}  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Fit To Pages Example</h1>
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

            if (!fileInput.files.length) {
                // No file selected: create a new workbook
                const workbook = new Workbook();

                // Accessing the first worksheet in the Excel file
                const worksheet = workbook.worksheets.get(0);

                // Setting the number of pages to which the length of the worksheet will be spanned
                worksheet.pageSetup.fitToPagesTall = 1;

                // Setting the number of pages to which the width of the worksheet will be spanned
                worksheet.pageSetup.fitToPagesWide = 1;

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Excel97To2003);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'FitToPagesOptions_out.xls';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
                return;
            }

            // If a file is selected, load it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the number of pages to which the length of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesTall = 1;

            // Setting the number of pages to which the width of the worksheet will be spanned
            worksheet.pageSetup.fitToPagesWide = 1;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FitToPagesOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **用紙サイズ**  

印刷されるワークシートの用紙サイズを[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスの[**paperSize**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperSize--)プロパティを使って設定します。[**paperSize**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#paperSize--)プロパティは以下にリストされた[**PaperSizeType**](https://reference.aspose.com/cells/javascript-cpp/papersizetype)列挙型の事前定義された値のいずれかを受け入れます。  

|**用紙サイズの種類**|**説明**|  
| :- | :- |  
|PaperLetter|Letter (8-1/2 in. x 11 in.)|  
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|  
|PaperTabloid|Tabloid (11 in. x 17 in.)|  
|PaperLedger|Ledger (17 in. x 11 in.)|  
|PaperLegal|Legal (8-1/2 in. x 14 in.)|  
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|  
|PaperExecutive|Executive (7-1/4 in. x 10-1/2 in.)|  
|PaperA3|A3 (297 mm x 420 mm)|  
|PaperA4|A4 (210 mm x 297 mm)|  
|PaperA4Small|A4 Small (210 mm x 297 mm)|  
|PaperA5|A5 (148 mm x 210 mm)|  
|PaperB4|JIS B4 (257 mm x 364 mm)|  
|PaperB5|JIS B5 (182 mm x 257 mm)|  
|PaperFolio|Folio (8-1/2 in. x 13 in.)|  
|PaperQuarto|Quarto (215 mm x 275 mm)|  
|Paper10x14|10 in. x 14 in.|  
|Paper11x17|11 in. x 17 in.|  
|PaperNote|Note (8-1/2 in. x 11 in.)|  
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|  
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|  
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|  
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|  
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|  
|PaperCSheet|C size sheet|  
|PaperDSheet|D size sheet|  
|PaperESheet|E size sheet|  
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|  
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|  
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|  
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|  
|PaperEnvelopeC6 |Envelope C6 (114 mm x 162 mm)|  
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|  
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|  
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|  
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|  
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|  
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|  
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|  
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|  
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|  
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|  
|PaperISOB4|B4 (ISO) 250 x 353 mm|  
|PaperJapanesePostcard|Japanese Postcard (100mm x 148mm)|  
|Paper9x11|9 in. x 11 in.|  
|Paper10x11|10 in. x 11 in.|  
|Paper15x11|15 in. x 11 in.|  
|PaperEnvelopeInvite|Envelope Invite(220mm x 220mm)|  
|PaperLetterExtra|US Letter Extra 9 \275 x 12 in|  
|PaperLegalExtra|US Legal Extra 9 \275 x 15 in|  
|PaperTabloidExtra|US Tabloid Extra 11.69 x 18 in|  
|PaperA4Extra|A4 Extra 9.27 x 12.69 in|  
|PaperLetterTransverse|Letter Transverse 8 \275 x 11 in|  
|PaperA4Transverse|A4 Transverse 210 x 297 mm|  
|PaperLetterExtraTransverse|Letter Extra Transverse 9\275 x 12 in|  
|PaperSuperA|SuperA/SuperA/A4 227 x 356 mm|  
|PaperSuperB|SuperB/SuperB/A3 305 x 487 mm|  
|PaperLetterPlus|US Letter Plus 8.5 x 12.69 in|  
|PaperA4Plus|A4 Plus 210 x 330 mm|  
|PaperA5Transverse|A5 Transverse 148 x 210 mm|  
|PaperJISB5Transverse|B5 (JIS) Transverse 182 x 257 mm|  
|PaperA3Extra|A3 Extra 322 x 445 mm|  
|PaperA5Extra|A5 Extra 174 x 235 mm|  
|PaperISOB5Extra|B5 (ISO) Extra 201 x 276 mm|  
|PaperA2|A2 420 x 594 mm|  
|PaperA3Transverse|A3 Transverse 297 x 420 mm|  
|PaperA3ExtraTransverse|A3 Extra Transverse 322 x 445 mm|  
|PaperJapaneseDoublePostcard|Japanese Double Postcard 200 x 148 mm|  
|PaperA6|A6 105 x 148 mm|  
|PaperJapaneseEnvelopeKaku2|Japanese Envelope Kaku #2|  
|PaperJapaneseEnvelopeKaku3|Japanese Envelope Kaku #3|  
|PaperJapaneseEnvelopeChou3|Japanese Envelope Chou #3|  
|PaperJapaneseEnvelopeChou4|Japanese Envelope Chou #4|  
|PaperLetterRotated|11in x 8.5in|  
|PaperA3Rotated|420mm x 297mm|  
|PaperA4Rotated|297mm x 210mm|  
|PaperA5Rotated|210mm x 148mm|  
|PaperJISB4Rotated|B4 (JIS) Rotated 364 x 257 mm|  
|PaperJISB5Rotated|B5 (JIS) Rotated 257 x 182 mm|  
|PaperJapanesePostcardRotated|Japanese Postcard Rotated 148 x 100 mm|  
|PaperJapaneseDoublePostcardRotated|Double Japanese Postcard Rotated 148 x 200 mm|  
|PaperA6Rotated|A6 Rotated 148 x 105 mm|  
|PaperJapaneseEnvelopeKaku2Rotated|Japanese Envelope Kaku #2 Rotated|  
|PaperJapaneseEnvelopeKaku3Rotated|Japanese Envelope Kaku #3 Rotated|  
|PaperJapaneseEnvelopeChou3Rotated|Japanese Envelope Chou #3 Rotated|  
|PaperJapaneseEnvelopeChou4Rotated|Japanese Envelope Chou #4 Rotated|  
|PaperJISB6|B6 (JIS) 128 x 182 mm|  
|PaperJISB6Rotated|B6 (JIS) Rotated 182 x 128 mm|  
|Paper12x11|12 x 11 in|  
|PaperJapaneseEnvelopeYou4|Japanese Envelope You #4|  
|PaperJapaneseEnvelopeYou4Rotated|Japanese Envelope You #4 Rotated|  
|PaperPRC16K|PRC 16K 146 x 215 mm|  
|PaperPRC32K|PRC 32K 97 x 151 mm|  
|PaperPRCBig32K|PRC 32K(Big) 97 x 151 mm|  
|PaperPRCEnvelope1|PRC Envelope #1 102 x 165 mm|  
|PaperPRCEnvelope2|PRC Envelope #2 102 x 176 mm|  
|PaperPRCEnvelope3|PRC Envelope #3 125 x 176 mm|  
|PaperPRCEnvelope4|PRC Envelope #4 110 x 208 mm|  
|PaperPRCEnvelope5|PRC Envelope #5 110 x 220 mm|  
|PaperPRCEnvelope6|PRC Envelope #6 120 x 230 mm|  
|PaperPRCEnvelope7|PRC Envelope #7 160 x 230 mm|  
|PaperPRCEnvelope8|PRC Envelope #8 120 x 309 mm|  
|PaperPRCEnvelope9|PRC Envelope #9 229 x 324 mm|  
|PaperPRCEnvelope10|PRC Envelope #10 324 x 458 mm|  
|PaperPRC16KRotated|PRC 16K Rotated|  
|PaperPRC32KRotated|PRC 32K Rotated|  
|PaperPRCBig32KRotated|PRC 32K(Big) Rotated|  
|PaperPRCEnvelope1Rotated|PRC Envelope #1 Rotated 165 x 102 mm|  
|PaperPRCEnvelope2Rotated|PRC Envelope #2 Rotated 176 x 102 mm|  
|PaperPRCEnvelope3Rotated|PRC Envelope #3 Rotated 176 x 125 mm|  
|PaperPRCEnvelope4Rotated|PRC Envelope #4 Rotated 208 x 110 mm|  
|PaperPRCEnvelope5Rotated|PRC Envelope #5 Rotated 220 x 110 mm|  
|PaperPRCEnvelope6Rotated|PRC Envelope #6 Rotated 230 x 120 mm|  
|PaperPRCEnvelope7Rotated|PRC Envelope #7 Rotated 230 x 160 mm|  
|PaperPRCEnvelope8Rotated|PRC Envelope #8 Rotated 309 x 120 mm|  
|PaperPRCEnvelope9Rotated|PRC Envelope #9 Rotated 324 x 229 mm|  
|PaperPRCEnvelope10Rotated|PRC Envelope #10 Rotated 458 x 324 mm|  
|PaperB3|usual B3(13.9 x 19.7 in)|  
|PaperBusinessCard|Business Card(90mm x 55 mm)|  
|PaperThermal|Thermal(3 x 11 in)|  
|Custom|Represents the custom paper size.|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Manage Paper Size Example</h1>
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

            if (!fileInput.files.length) {
                // proceed with a new blank workbook if no file selected
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the paper size to A4
            worksheet.pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;

            // Save the Workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ManagePaperSize_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Paper size set to A4. Click the download link to save the file.</p>';
        });
    </script>
</html>
```  

### **印刷品質**  

[**printQuality**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printQuality--)プロパティを使用して、印刷されるワークシートの印刷品質を設定します。印刷品質の単位はポイント毎インチ（DPI）です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Quality Example</title>
    </head>
    <body>
        <h1>Set Print Quality Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            // Setting the print quality of the worksheet to 180 dpi
            worksheet.pageSetup.printQuality = 180;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintQuality_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print quality set to 180 dpi. Click the download link to save the file.</p>';
        });
    </script>
</html>
```  

### **最初のページ番号**  

ワークシートページのページ番号付けを[**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)クラスの[**firstPageNumber**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#firstPageNumber--)プロパティを使って開始します。[**firstPageNumber**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#firstPageNumber--)プロパティは最初のワークシートページ番号を設定し、次のページは昇順で番号付けされます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set First Page Number Example</h1>
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
            // Creating a new Workbook object (blank workbook)
            const workbook = new Workbook();

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the first page number of the worksheet pages
            worksheet.pageSetup.firstPageNumber = 2;

            // Saving the Workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetFirstPageNumber_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">First page number set to 2. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
