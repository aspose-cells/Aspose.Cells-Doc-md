---
title: C++を使用したJavaScriptによる画像管理
linktitle: 画像の管理
type: docs
weight: 10
url: /ja/javascript-cpp/managing-pictures/
description: C++を使用したAspose.Cells for JavaScriptでスプレッドシートに画像を追加し位置を調整する方法を学びます。
---

Aspose.Cellsを使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の位置を実行時に制御することができます。これについては後のセクションで詳しく説明します。

この資料では、画像の追加方法や特定のセルの内容を示す画像の挿入方法について解説します。

## **画像の追加**

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:  
[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)オブジェクトのコレクションの[**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)メソッドの[**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-)を呼び出すだけです。[**Add**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-string-)メソッドは以下のパラメータを取ります：

- **左上の行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an optional Excel file to update (or leave empty to create a new workbook), and select an image file to insert as a picture.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Load existing workbook if provided, otherwise create a new one
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read image file bytes
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file (Excel 97-2003 .xls format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **写真の位置合わせ**

Aspose.Cellsを使用して写真の位置合わせを制御する方法には2つの方法があります:

- 比例位置合わせ：行の高さと幅に比例した位置を定義します。
- 絶対位置指定：画像を挿入するページ上の正確な位置を定義します。例：セルの縁から左に40ピクセル、下に20ピクセル。

### **比例位置合わせ**

開発者は、[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)オブジェクトの[**upperDeltaX**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaX--)と[**upperDeltaY**](https://reference.aspose.com/cells/javascript-cpp/shape/#upperDeltaY--)のプロパティを使用して、行の高さと列の幅に比例した画像の位置を設定できます。[**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)コレクションから画像のインデックスを渡すことで、[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)オブジェクトを取得できます。この例では、F6セルに画像を配置しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Picture to New Workbook</h1>
        <p>Select an image to insert into a new Excel workbook. The picture will be placed at cell F6 (row 5, column 5).</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert:</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Create Workbook and Add Picture</button>
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
            const imageInput = document.getElementById('imageInput');
            if (!imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as bytes
            const imageFile = imageInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Positioning the picture proportional to row height and column width (property assignments)
            picture.upperDeltaX = 200;
            picture.upperDeltaY = 200;

            // Saving the Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and picture added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **絶対位置づけ**

開発者は、[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)オブジェクトの[**left**](https://reference.aspose.com/cells/javascript-cpp/shape/#left--)と[**top**](https://reference.aspose.com/cells/javascript-cpp/shape/#top--)のプロパティを使用して、画像を絶対位置に配置することも可能です。この例では、セルF6に画像を配置し、左から60ピクセル、上から10ピクセルの位置にあります。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture</title>
    </head>
    <body>
        <h1>Add Picture to Workbook Example</h1>
        <p>Select an image file to insert into a new Excel workbook:</p>
        <input type="file" id="fileInput" accept="image/*" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file.</p>';
                return;
            }

            // Read image file as bytes
            const imageFile = fileInput.files[0];
            const arrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(arrayBuffer);

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a picture at the location of a cell whose row and column indices are 5 in the worksheet ("F6")
            const pictureIndex = worksheet.pictures.add(5, 5, imageBytes);

            // Accessing the newly added picture
            const picture = worksheet.pictures.get(pictureIndex);

            // Absolute positioning of the picture in unit of pixels
            picture.left = 60;
            picture.top = 10;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **セル参照に基づいて画像を挿入**

Aspose.Cellsを使用すると、ワークシートのセルの内容を画像形状で表示できます。画像は、データを表示したいセルにリンクされています。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、自動的にグラフィックオブジェクトに変更が反映されます。

[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection)コレクションの[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)オブジェクトの[**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-)メソッドを呼び出して、ワークシートに画像を追加します。セル範囲は、[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)オブジェクトの[**formula**](https://reference.aspose.com/cells/javascript-cpp/picture/#formula--)属性を使用して指定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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
            // This example creates a new workbook, modifies cells and pictures, and saves it.
            const workbook = new Workbook();

            // Get the first worksheet's cells collection
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Add string values to the cells
            cells.get("A1").value = "A1";
            cells.get("C10").value = "C10";

            // Get pictures collection and add a blank picture to the D1 cell
            const picts = worksheet.pictures;
            const picIndex = picts.add(0, 3, 10, 6, null);
            const pic = picts.get(picIndex);

            // Specify the formula that refers to the source range of cells
            pic.formula = "A1:C10";

            // Update the shapes selected value in the worksheet
            worksheet.shapes.updateSelectedValue();

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [セルのテキストと条件付きアイコンセットの追加](/cells/ja/javascript-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Webアドレスからリンクされた画像の挿入](/cells/ja/javascript-cpp/insert-a-linked-picture-from-web-address/)
- [セル参照に基づく画像の挿入](/cells/ja/javascript-cpp/insert-a-picture-based-on-cell-reference/)
- [Web画像のURLをExcelワークシートに読み込む](/cells/ja/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
