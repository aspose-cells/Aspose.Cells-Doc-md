---
title: JavaScriptをC++経由でExcelファイルに画像や図形を挿入する  
linktitle: シェイプ  
type: docs  
weight: 140  
url: /ja/javascript-cpp/insert-shapes/  
description: C++のAspose.Cells for JavaScriptを使用して、Excelファイル内の画像、OLEオブジェクト、図形を管理します。  
---  

{{% alert color="primary" %}}  
必要に応じてワークシートにシェイプを挿入する必要がある場合があります。同じシェイプを異なる位置に挿入したり、バッチで複数のシェイプを挿入したりすることもあります。  
心配しないでください！[Aspose.Cells](https://products.aspose.com/cells/)はこれらの操作をすべてサポートしています。  
{{% /alert %}}  

Excelのシェイプは主に次のタイプに分類されます：  
- **写真**  
- **OLEオブジェクト**  
- **直線**  
- **四角形**  
- **基本図形**  
- **ブロック矢印**  
- **数式図形**  
- **フローチャート**  
- **星とバナー**  
- **吹き出し**  

このガイドドキュメントでは、各タイプから1つまたは2つのシェイプを選び、サンプルを作成します。これらの例を通じて、[Aspose.Cells](https://products.aspose.com/cells/)を使用して指定されたシェイプをワークシートに挿入する方法を学びます。  

## **JavaScriptを使用したExcelワークシートへの画像の追加**  

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:  
[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)オブジェクトのコレクションの[**Pictures**](https://reference.aspose.com/cells/javascript-cpp/picturecollection)メソッドの[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)を呼び出すだけです。[**PictureCollection.add(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/javascript-cpp/picturecollection/#add-number-number-number-number-uint8array-)メソッドは以下のパラメータを取ります：  

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
        <p>
            Optional: select an existing Excel file to modify, or leave empty to create a new workbook.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image to insert into the worksheet (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert.</p>';
                return;
            }

            // If an Excel file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const arrayBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Add a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Read the selected image file as Uint8Array
            const imageFile = imageInput.files[0];
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const imageBytes = new Uint8Array(imageArrayBuffer);

            // Adding a picture at the location of a cell whose row and column indices are 5 (F6)
            worksheet.pictures.add(5, 5, imageBytes);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **JavaScriptを使用したExcelワークシートへのOLEオブジェクトの挿入**  

Aspose.Cellsは、ワークシートへのOLEオブジェクトの追加、抽出、および操作をサポートします。そのため、コレクションリストに新しいOLEオブジェクトを追加するために使用される[**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection)クラスと、OLEオブジェクトを表す[**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject)クラスがあります。重要なメンバーは次の通りです：  

- `[**OleObject.imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--)`プロパティは、イメージ（アイコン）のデータをバイト配列型で指定します。この画像は、ワークシート内のOLEオブジェクトを表示するために使われます。  
- `[**OleObject.objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--)`プロパティは、オブジェクトのデータをバイト配列の形式で指定します。このデータは、ダブルクリックによって関連付けられたプログラムで表示されます。  

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert OLE Object Example</h1>
        <p>
            Select an image to display as the OLE object's icon and an Excel file to embed as the OLE object.
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <input type="file" id="excelInput" accept=".xls,.xlsx" />
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
            const imageInput = document.getElementById('imageInput');
            const excelInput = document.getElementById('excelInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE icon.</p>';
                return;
            }
            if (!excelInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file to embed.</p>';
                return;
            }

            const imageFile = imageInput.files[0];
            const excelFile = excelInput.files[0];

            // Read files as ArrayBuffers
            const imageArrayBuffer = await imageFile.arrayBuffer();
            const excelArrayBuffer = await excelFile.arrayBuffer();

            // Convert to Uint8Array for Aspose.Cells
            const imageData = new Uint8Array(imageArrayBuffer);
            const objectData = new Uint8Array(excelArrayBuffer);

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            sheet.oleObjects.add(14, 3, 200, 220, imageData);

            // Set embedded ole object data.
            sheet.oleObjects.get(0).objectData = objectData;

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object embedded successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **JavaScriptを使用してExcelワークシートに線を挿入**  

ラインの形状は**lines**カテゴリに属します。  

*  

- 線を挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- それから、『最近使ったシェイプ』または『ライン』からラインを選択します。  

![](line.png)  

***Aspose.Cells を使用***  

ワークシートに線を挿入するために以下の方法を使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
このメソッドは、[LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape)オブジェクトを返します。  
{{% /alert %}}  

以下の例では、ワークシートにラインを挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Line Example</h1>
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
            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Create workbook from uploaded file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Access first worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Add the line to the worksheet
                sheet.shapes.addLine(2, 0, 2, 0, 100, 300);

                // Save workbook to XLSX format and create download link
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'sample.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Line added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](line2.png)  

## **JavaScriptを使用してExcelワークシートに線矢印を挿入**  

矢印ラインの形状は**Lines**カテゴリに属しており、ラインの特殊なケースです。  

*  

- 矢印を挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- それから、『最近使ったシェイプ』または『ライン』から矢印ラインを選択します。  

![](line_arrow1.png)  

***Aspose.Cells を使用***  

ワークシートに直線矢印を挿入するために以下の方法を使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addLine(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLine-number-number-number-number-number-number-)  
このメソッドは、[LineShape](https://reference.aspose.com/cells/javascript-cpp/lineshape)オブジェクトを返します。  
{{% /alert %}}  

以下の例では、ワークシートに矢印ラインを挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Line Arrow Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains shapes
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the line arrow to the worksheet
            let s = sheet.shapes.addLine(2, 0, 2, 0, 100, 300); // method 1
            // let s = sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Line, 2, 0, 2, 0, 100, 300); // method 2
            // let s = sheet.shapes.addShape(AsposeCells.MsoDrawingType.Line, 2, 0, 2, 0, 100, 300); // method 3

            // add a arrow at the line begin
            s.line.beginArrowheadStyle = AsposeCells.MsoArrowheadStyle.Arrow; // arrow type
            s.line.beginArrowheadWidth = AsposeCells.MsoArrowheadWidth.Wide; // arrow width
            s.line.beginArrowheadLength = AsposeCells.MsoArrowheadLength.Short; // arrow length

            // add a arrow at the line end
            s.line.endArrowheadStyle = AsposeCells.MsoArrowheadStyle.ArrowOpen; // arrow type
            s.line.endArrowheadWidth = AsposeCells.MsoArrowheadWidth.Narrow; // arrow width
            s.line.endArrowheadLength = AsposeCells.MsoArrowheadLength.Long; // arrow length

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.with_arrow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File with Arrow';

            document.getElementById('result').innerHTML = '<p style="color: green;">Arrow added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](line_arrow2.png)  

## **JavaScriptを使用してExcelワークシートに矩形を挿入**  

四角形の形状は**Rectangles**カテゴリに属します。  

*  

- 長方形を挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- それから、『最近使ったシェイプ』または『四角形』から選択します。  

![](rectangle.png)  

***Aspose.Cells を使用***  

ワークシートに長方形を挿入するには、次のメソッドを使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addRectangle(number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addRectangle-number-number-number-number-number-number-)  
このメソッドは、[RectangleShape](https://reference.aspose.com/cells/javascript-cpp/rectangleshape)オブジェクトを返します。  
{{% /alert %}}  

以下の例では、ワークシートに四角形を挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Rectangle</title>
    </head>
    <body>
        <h1>Add Rectangle to Worksheet</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the rectangle to the worksheet
            sheet.shapes.addRectangle(2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rectangle added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](rectangle2.png)  

## **JavaScriptを使用してExcelワークシートに立方体を挿入**  

キューブの形状は**基本図形**カテゴリに属します。  

*  

- キューブを挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**基本図形**からキューブを選択します  

![](cube.png)  

***Aspose.Cells を使用***  

ワークシートにキューブを挿入するには、次のメソッドを使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは、[Shape](https://reference.aspose.com/cells/javascript-cpp/shape)オブジェクトを返します。  
{{% /alert %}}  

例は、ワークシートにキューブを挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Cube</title>
    </head>
    <body>
        <h1>Add Cube to Worksheet</h1>
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
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the cube to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.Cube, 2, 0, 2, 0, 100, 300);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            result.innerHTML = '<p style="color: green;">Cube added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](cube2.png)  

## **JavaScriptを使用してExcelワークシートにコールアウトクアッド矢印を挿入**  

コールアウトクアッドアローの形状は**ブロック矢印**カテゴリに属します。  

*  

- コールアウト四角矢印を挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**ブロック矢印**からコールアウトクアッドアローを選びます  

![](callout_quad_arrow.png)  

***Aspose.Cells を使用***  

ワークシートにコールアウト四角矢印を挿入するには、次のメソッドを使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) オブジェクトを返します。  
{{% /alert %}}  

例は、ワークシートにコールアウトクアッドアローを挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Callout Quad Arrow</title>
    </head>
    <body>
        <h1>Add Callout Quad Arrow Shape</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            sheet.shapes.addAutoShape(AutoShapeType.QuadArrowCallout, 2, 0, 2, 0, 100, 100);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](callout_quad_arrow2.png)  

## **JavaScriptを使用してExcelワークシートに乗算記号を挿入する**  

掛け算記号の形状は**式図形**カテゴリに属します。  

*  

- 乗算記号を挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**式図形**から掛け算記号を選択します  

![](multiplication_sign.png)  

***Aspose.Cells を使用***  

次の方法を使用してワークシートに乗算記号を挿入できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) オブジェクトを返します。  
{{% /alert %}}  

例は、ワークシートに掛け算記号を挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Multiply Sign</title>
    </head>
    <body>
        <h1>Add Multiplication Sign to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multiplication sign to the worksheet
            sheet.shapes.addAutoShape(AsposeCells.AutoShapeType.MathMultiply, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Multiplication sign added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](multiplication_sign2.png)  

## **JavaScriptを使用してExcelワークシートにマルチドキュメントを挿入する**  

多ドキュメントの形状は**フローチャート**カテゴリに属します。  

*  

- 多重ドキュメントを挿入するセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、多ドキュメントを**フローチャート**から選択します  

![](multidocument.png)  

***Aspose.Cells を使用***  

次の方法を使用してワークシートに多重ドキュメントを挿入できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) オブジェクトを返します。  
{{% /alert %}}  

例は、多ドキュメントをワークシートに挿入する方法を示しています。  

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
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Create workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the multidocument to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.FlowChartMultidocument, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](multidocument2.png)  

## **JavaScriptを使ってExcelワークシートに五角形の星を挿入する**  

五芒星の形状は**星とバナー**カテゴリに属しています。  

*  

- 五角星を挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**星とバナー**から五芒星を選択します  

![](star_5_points.png)  

***Aspose.Cells を使用***  

この方法は [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) オブジェクトを返します。  
{{% /alert %}}  

次の例は、ワークシートに五芒星を挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Star Shape</title>
    </head>
    <body>
        <h1>Add Five-Pointed Star to Worksheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Add the Five-pointed star to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.Star5, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Star shape added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](star_5_points2.png)  

## **JavaScriptを使用してExcelワークシートに思考バブルのクラウドを挿入する**  

思考バブル雲の形状は**コールアウト**カテゴリに属しています。  

*  

- 思考バブルクラウドを挿入したいセルを選択します  
- [挿入] メニューをクリックし、[図形] をクリックします。  
- その後、**コールアウト**から思考バブル雲を選択します  

![](thought_bubble_cloud.png)  

***Aspose.Cells を使用***  

ワークシートに思考バブルクラウドを挿入するために次の方法を使用できます。  

{{% alert color="primary" %}}  
[**ShapeCollection.addAutoShape(AutoShapeType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addAutoShape-autoshapetype-number-number-number-number-number-number-)  
このメソッドは [Shape](https://reference.aspose.com/cells/javascript-cpp/shape) オブジェクトを返します。  
{{% /alert %}}  

次の例は、ワークシートに思考バブル雲を挿入する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Cloud Callout Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AutoShapeType } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the thought bubble cloud to the worksheet
            sheet.shapes.addAutoShape(AutoShapeType.CloudCallout, 2, 0, 2, 0, 100, 100);

            // Save and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cloud callout added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードを実行すると、次の結果が得られます。  

![](thought_bubble_cloud2.png)  

## **高度なトピック**  
- [図形の調整値を変更](/cells/ja/javascript-cpp/change-adjustment-values-of-the-shape/)  
- [ワークシート間で図形をコピーする](/cells/ja/javascript-cpp/copy-shapes-between-worksheets/)  
- [非プリミティブ形状のデータ](/cells/ja/javascript-cpp/data-in-non-primitive-shape/)  
- [ワークシート内の形状の絶対位置を検索する](/cells/ja/javascript-cpp/finding-absolute-position-of-shape-inside-the-worksheet/)  
- [形状から接続ポイントを取得する](/cells/ja/javascript-cpp/get-connection-points-from-shape/)  
- [コントロールの管理](/cells/ja/javascript-cpp/managing-controls/)  
- [ワークシートにアイコンを追加する](/cells/ja/javascript-cpp/insert-svg-to-excel/)  
- [OLE オブジェクトの管理](/cells/ja/javascript-cpp/managing-ole-objects/)  
- [画像の管理](/cells/ja/javascript-cpp/managing-pictures/)  
- [Smart Art の管理](/cells/ja/javascript-cpp/managing-smartart/)  
- [テキストボックスの管理](/cells/ja/javascript-cpp/managing-textbox-of-excel/)  
- [Aspose.Cells にワードアートウォーターマークを追加](/cells/ja/javascript-cpp/add-wordart-watermark-to-worksheet/)  
- [リンクされた図形の値を更新する](/cells/ja/javascript-cpp/refresh-values-of-linked-shapes/)  
- [ワークシート内でShape FrontまたはBackを送信する](/cells/ja/javascript-cpp/send-shape-front-or-back-inside-the-worksheet/)  
- [形状オプションを管理する](/cells/ja/javascript-cpp/managing-shape-options/)  
- [形状テキストオプションの管理](/cells/ja/javascript-cpp/managing-shape-text-options/)  
- [Web拡張 - Office アドイン](/cells/ja/javascript-cpp/web-extensions-office-add-ins/)
