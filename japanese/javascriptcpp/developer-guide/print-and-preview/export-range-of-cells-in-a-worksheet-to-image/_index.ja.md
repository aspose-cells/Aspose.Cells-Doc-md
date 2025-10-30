---
title: JavaScriptをC++経由で使用して、ワークシートの範囲を画像にエクスポートします。
linktitle: ワークシート内のセルの範囲をイメージにエクスポート
type: docs
weight: 60
url: /ja/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/
---

## **可能な使用シナリオ**  

Aspose.Cells for JavaScriptをC++経由で使用して、ワークシートやチャートを希望の幅と高さの画像にエクスポートできます。これには{0}メソッドを使用し、エクスポートされる画像の幅と高さをピクセル単位で指定します。  

## **ワークシートのセルの範囲をイメージにエクスポート**  

範囲の画像を取得するには、印刷エリアを希望の範囲に設定し、余白をすべて0にします。また、[**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#onePagePerSheet--)を**true**に設定します。以下のコードはD8:G16の範囲の画像を取得します。以下はコードで使用されている[サンプルExcelファイル](47153160.xlsx)のスクリーンショットです。任意のExcelファイルで試すことができます。  

## **サンプルExcelファイルのスクリーンショットとそのエクスポートされたイメージ**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

コードを実行すると、範囲D8:G16のイメージが作成されます。  

**![todo:image_alt_text](Output-Image.png)**  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export Range To Image</title>
    </head>
    <body>
        <h1>Export Range Of Cells In Worksheet To Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender } = AsposeCells;

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

            // Create workbook from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Set the print area with your desired range
            worksheet.pageSetup.printArea = "D8:G16";

            // Set all margins as 0
            worksheet.pageSetup.leftMargin = 0;
            worksheet.pageSetup.rightMargin = 0;
            worksheet.pageSetup.topMargin = 0;
            worksheet.pageSetup.bottomMargin = 0;

            // Set OnePagePerSheet option as true and image options
            const options = new ImageOrPrintOptions();
            options.onePagePerSheet = true;
            options.imageType = ImageType.Jpeg;
            options.horizontalResolution = 200;
            options.verticalResolution = 200;

            // Take the image of your worksheet
            const sr = new SheetRender(worksheet, options);
            const outputData = sr.toImage(0);

            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportRangeOfCellsInWorksheetToImage.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image exported successfully! Click the download link to download the image.</p>';
        });
    </script>
</html>
```
