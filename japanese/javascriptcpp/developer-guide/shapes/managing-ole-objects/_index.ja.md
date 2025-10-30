---
title: C++を使用したJavaScriptによるOLEオブジェクトの管理
linktitle: OLE オブジェクトを管理する
type: docs
weight: 50
url: /ja/javascript-cpp/managing-ole-objects/
description: C++を使用したAspose.Cells for JavaScriptでOLEオブジェクトを管理する方法を学びます。ワークシート内でOLEオブジェクトを追加、抽出、操作します。
---

## **紹介**  

OLE（Object Linking and Embedding）は、複合ドキュメント技術のフレームワークです。簡単に言えば、複合ドキュメントは、テキスト、カレンダー、アニメーション、音声、動画、3D、ニュースの更新、コントロールなどの視覚的および情報的オブジェクトを含むことができるディスプレイデスクトップのようなものです。各デスクトップオブジェクトは、ユーザーと対話できる独立したプログラムエンティティであり、また他のオブジェクトと通信することも可能です。  

OLEは多くの異なるプログラムによってサポートされており、あるプログラムで作成した内容を別のプログラムで利用できるようにするために使われます。例えば、Microsoft WordのドキュメントをMicrosoft Excelに挿入できます。挿入可能な内容の種類を見るには、「挿入」メニューの「オブジェクト」をクリックします。インストールされていてOLEオブジェクトをサポートしているプログラムだけが、「オブジェクトの種類」ボックスに表示されます。  

### **ワークシートにOLEオブジェクトを挿入する**  

C++を使用したAspose.Cells for JavaScriptは、ワークシート内でOLEオブジェクトの追加、抽出、操作をサポートしています。このため、Aspose.Cellsにはコレクションに新しいOLEオブジェクトを追加するための[**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection)クラスがあります。もう一つのクラス[**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject)はOLEオブジェクトを表します。重要なメンバーは次の通りです：  

- `[**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--)`プロパティは、イメージ（アイコン）のデータをバイト配列型で指定します。この画像は、ワークシート内のOLEオブジェクトを表示するために使われます。  
- `[**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--)`プロパティは、オブジェクトのデータをバイト配列の形式で指定します。このデータは、ダブルクリックによって関連付けられたプログラムで表示されます。  

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object Example</h1>
        <p>
            Select an image to display for the OLE object (e.g., logo.jpg) and a file to embed into the OLE object (e.g., book1.xls).
        </p>
        <label>Image (for OLE display): <input type="file" id="imageInput" accept="image/*" /></label>
        <br/>
        <label>Object to embed (e.g., .xls): <input type="file" id="objectInput" accept=".xls,.xlsx,.doc,.docx,.pdf" /></label>
        <br/>
        <button id="runExample">Add OLE Object and Save</button>
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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE display.</p>';
                return;
            }
            if (!objectInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a file to embed into the OLE object.</p>';
                return;
            }

            // Read files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageBuffer = await imageFile.arrayBuffer();
            const objectBuffer = await objectFile.arrayBuffer();

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            // Position: row 14, column 3, width 200, height 220 (same as JavaScript example)
            sheet.oleObjects.add(14, 3, 200, 220, new Uint8Array(imageBuffer));

            // Set embedded ole object data (converted setter to property assignment)
            sheet.oleObjects.get(0).objectData = new Uint8Array(objectBuffer);

            // Save the excel file (Excel97To2003 format to match .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **ワークブックからOLEオブジェクトを抽出**  

以下の例では、ワークブックからOLEオブジェクトを抽出する方法を示します。この例では既存のXLSファイルから異なるOLEオブジェクトを取得し、OLEオブジェクトのファイル形式に基づいて異なるファイル（DOC、XLS、PPT、PDFなど）を保存します。  

コードを実行した後、対応するOLEオブジェクト形式の異なるファイルを保存できます。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract OLE Objects</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Extract OLE Objects</button>
        <div id="downloadContainer"></div>
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
            const downloadContainer = document.getElementById('downloadContainer');
            const result = document.getElementById('result');
            downloadContainer.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the OleObject Collection in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const oles = worksheet.oleObjects;

            // Loop through all the oleobjects and extract each object.
            for (let i = 0; i < oles.count; i++) {
                const ole = oles.get(i);

                // Specify the output filename.
                let ext = 'jpg';

                // Specify each file format based on the oleobject format type.
                switch (ole.fileFormatType) {
                    case AsposeCells.FileFormatType.Doc:
                        ext = "doc";
                        break;
                    case AsposeCells.FileFormatType.Xlsx:
                        ext = "xlsx";
                        break;
                    case AsposeCells.FileFormatType.Ppt:
                        ext = "ppt";
                        break;
                    case AsposeCells.FileFormatType.Pdf:
                        ext = "pdf";
                        break;
                    case AsposeCells.FileFormatType.Unknown:
                        ext = "jpg";
                        break;
                    default:
                        ext = "bin";
                        break;
                }

                const fileName = `ole_${i}.${ext}`;

                // Save the oleobject as a new excel file if the object type is xlsx.
                if (ole.fileFormatType === AsposeCells.FileFormatType.Xlsx) {
                    const ms = new Uint8Array(ole.objectData);
                    const oleBook = new Workbook(ms);
                    oleBook.settings.isHidden = false;
                    const outputData = oleBook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = `Excel_File${i}.out.xlsx`;
                    link.textContent = `Download Excel_File${i}.out.xlsx`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                } else {
                    // Create the files based on the oleobject format types.
                    const data = ole.objectData;
                    const blob = new Blob([data]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                }
            }

            result.innerHTML = '<p style="color: green;">OLE object extraction completed. Use the links above to download the files.</p>';
        });
    </script>
</html>
```  

### **埋め込まれたMOLファイルの抽出**  

C++を使用したAspose.Cells for JavaScriptは、MOL（原子と結合に関する情報を含む分子データファイル）などの珍しいタイプのオブジェクトの抽出もサポートしています。以下のコードスニペットは、埋め込みMOLファイルを抽出し、この[サンプルExcelファイル](94896196.xlsx)を使用してディスクに保存する方法を示しています。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects Example</title>
    </head>
    <body>
        <h1>Extract OLE Objects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            let index = 1;

            const worksheets = workbook.worksheets;
            const sheetCount = worksheets.count;
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            for (let i = 0; i < sheetCount; i++) {
                const sheet = worksheets.get(i);
                const oles = sheet.oleObjects;
                const oleCount = oles.count;
                for (let j = 0; j < oleCount; j++) {
                    const ole = oles.get(j);
                    const data = ole.objectData;
                    const blob = new Blob([data], { type: 'application/octet-stream' });
                    const url = URL.createObjectURL(blob);
                    const fileName = `OleObject${index}.mol`;
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    resultDiv.appendChild(link);
                    index++;
                }
            }

            if (!resultDiv.hasChildNodes()) {
                resultDiv.innerHTML = '<p>No OLE objects found in the workbook.</p>';
            } else {
                const info = document.createElement('p');
                info.style.color = 'green';
                info.textContent = 'OLE objects extracted. Click the links to download the extracted .mol files.';
                resultDiv.insertBefore(info, resultDiv.firstChild);
            }
        });
    </script>
</html>
```  

## **高度なトピック**  
- [リンクされたオブジェクトの表示ラベルへのアクセスと変更](/cells/ja/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する](/cells/ja/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [ワークブックからOLEオブジェクトを抽出](/cells/ja/javascript-cpp/extract-ole-objects-from-workbook/)  
- [埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する](/cells/ja/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Ole ObjectとしてWAVファイルを挿入する](/cells/ja/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
