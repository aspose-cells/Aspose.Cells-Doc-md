---
title: C++経由のJavaScriptによるフォント設定
linktitle: フォント設定
description: Aspose.Cells はスプレッドシートファイルを操作するためのJavaScriptライブラリです。これにより、セルのフォント設定を行うことができ、ユーザーはセルのフォントスタイルやプロパティをカスタマイズできます。この記事では、Aspose.Cellsライブラリを使用してセルのフォント設定を行う方法を紹介します。
keywords: Aspose.Cells、Cells、フォント設定、スタイル、プロパティ、JavaScriptをC++経由
type: docs
weight: 30
url: /ja/javascript-cpp/cells-font-settings/
---

{{% alert color="primary" %}}  
テキストの見た目はフォント設定を変更することでコントロールできます。フォント設定にはフォントの名前、スタイル、サイズ、色、その他の効果が含まれる場合があります。Microsoft Excelと同様に、Aspose.Cellsもセルのフォント設定をサポートしています。  
{{% /alert %}}  

## **フォント設定の構成**  

Aspose.Cellsは、Microsoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)クラスは、Excelファイル内の各ワークシートへアクセスできる[**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)クラスは[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--)コレクションを提供し、その中の各アイテムは[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスのオブジェクトを表します。  

Aspose.Cellsは、セルの書式設定スタイルを取得および設定に使用される[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)クラスの[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--)および[**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)メソッドを提供します。[**Style**](https://reference.aspose.com/cells/javascript-cpp/style)クラスはフォント設定を構成するためのプロパティを提供します。  

### **フォント名の設定**  

 開発者は、[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) オブジェクトの [**name**](https://reference.aspose.com/cells/javascript-cpp/font/#name-string-) メソッドを使用して、任意のフォントをセル内のテキストに適用できます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font name to "Times New Roman"
            style.font.name = "Times New Roman";

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **太字にフォントスタイルを設定する**  

開発者は、[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)オブジェクトの[**isBold**](https://reference.aspose.com/cells/javascript-cpp/font/#isBold-boolean-)メソッドを**true**に設定して、テキストを太字にできます。   

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font weight to bold
            style.font.isBold = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and A1 updated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **フォントサイズの設定**  

[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)オブジェクトの[**size**](https://reference.aspose.com/cells/javascript-cpp/font/#size-number-)メソッドを使用してフォントサイズを設定します。  

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
            const resultDiv = document.getElementById('result');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.count;
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font size to 14
            style.font.size = 14;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **フォントの色の設定**  

 [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) オブジェクトの [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-) メソッドを使ってフォントの色を設定します。JavaScriptの一部であるColor列挙から任意の色を選び、それを [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-) メソッドに割り当ててください。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Set Cell Style Example</h1>
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
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font color to blue
            style.font.color = AsposeCells.Color.Blue;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **フォントの下線タイプの設定**  

[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)オブジェクトの[**underline**](https://reference.aspose.com/cells/javascript-cpp/font/#underline-fontunderlinetype-)メソッドを使用してテキストに下線を引きます。Aspose.Cellsは、[**FontUnderlineType**](https://reference.aspose.com/cells/javascript-cpp/fontunderlinetype)列挙体にさまざまな事前定義されたフォント下線タイプを提供します。  

|**フォントの下線の種類**|**説明**|  
| :- | :- |  
|Accounting|単一のアカウンティング下線  
|Double|ダブル下線  
|DoubleAccounting|ダブルアカウンティング下線  
|None|下線なし  
|Single|単一の下線  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontUnderlineType } = AsposeCells;

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font to be underlined
            style.font.underline = FontUnderlineType.Single;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready to download.</p>';
        });
    </script>
</html>
```


### **取り消し線の効果の設定**  

[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)オブジェクトの[**isStrikeout**](https://reference.aspose.com/cells/javascript-cpp/font/#isStrikeout-boolean-)メソッドを**true**に設定して取消線を適用します。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the strike out effect on the font
            style.font.isStrikeout = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **下付き文字の効果の設定**  

[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)オブジェクトの[**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-)メソッドを**true**に設定して下付き文字を適用します。  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Add Worksheet</h1>
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
            const resultDiv = document.getElementById('result');

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet and get its index
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access the "A1" cell
            const cell = worksheet.cells.get("A1");

            // Set value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtain the style of the cell
            const style = cell.style;

            // Set strikeout on the font
            style.font.isStrikeout = true;

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **フォントの上付き文字効果の設定**  

開発者は、[**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--)オブジェクトの[**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-)メソッドを**true**に設定して上付き文字の効果を適用できます。  

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting superscript effect
            style.font.isSuperscript = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


## **高度なトピック**  
- [フォントに上付き文字および下付き文字効果を適用する](/cells/ja/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [スプレッドシートまたはブックで使用されているフォントのリストを取得する](/cells/ja/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
