---  
title: Node.jsとC++を使用したOLEオブジェクトの管理  
linktitle: OLE オブジェクトを管理する  
type: docs  
weight: 50  
url: /ja/nodejs-cpp/managing-ole-objects/  
description: Aspose.Cells for Node.js via C++でOLEオブジェクトの管理方法を学びます。ワークシート内でOLEオブジェクトの追加、抽出、操作を行います。  
---  

## **紹介**  

OLE（Object Linking and Embedding）は、複合ドキュメント技術のフレームワークです。簡単に言えば、複合ドキュメントは、テキスト、カレンダー、アニメーション、音声、動画、3D、ニュースの更新、コントロールなどの視覚的および情報的オブジェクトを含むことができるディスプレイデスクトップのようなものです。各デスクトップオブジェクトは、ユーザーと対話できる独立したプログラムエンティティであり、また他のオブジェクトと通信することも可能です。  

OLEは多くの異なるプログラムによってサポートされており、あるプログラムで作成した内容を別のプログラムで利用できるようにするために使われます。例えば、Microsoft WordのドキュメントをMicrosoft Excelに挿入できます。挿入可能な内容の種類を見るには、「挿入」メニューの「オブジェクト」をクリックします。インストールされていてOLEオブジェクトをサポートしているプログラムだけが、「オブジェクトの種類」ボックスに表示されます。  

### **ワークシートにOLEオブジェクトを挿入する**  

Aspose.Cells for Node.js via C++は、ワークシート内でOLEオブジェクトの追加、抽出、操作をサポートします。そのため、Aspose.Cellsには、コレクションに新しいOLEオブジェクトを追加するために使用される`[**OleObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/oleobjectcollection)`クラスと、OLEオブジェクトを表す別のクラス`[**OleObject**](https://reference.aspose.com/cells/nodejs-cpp/oleobject)`があります。重要なメンバーは以下の通りです：  

- `[**getImageData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getImageData--)`プロパティは、イメージ（アイコン）のデータをバイト配列型で指定します。この画像は、ワークシート内のOLEオブジェクトを表示するために使われます。  
- `[**getObjectData()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getObjectData--)`プロパティは、オブジェクトのデータをバイト配列の形式で指定します。このデータは、ダブルクリックによって関連付けられたプログラムで表示されます。  

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define a string variable to store the image path.
const imageUrl = path.join(dataDir, "logo.jpg");

// Get the picture into the streams.
const imageData = fs.readFileSync(imageUrl);

// Get an excel file path in a variable.
const filePath = path.join(dataDir, "book1.xls");

// Get the file into the streams.
const objectData = fs.readFileSync(filePath);

// Add an Ole object into the worksheet with the image
// Shown in MS Excel.
sheet.getOleObjects().add(14, 3, 200, 220, imageData);

// Set embedded ole object data.
sheet.getOleObjects().get(0).setObjectData(objectData);

// Save the excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **ワークブックからOLEオブジェクトを抽出**  

以下の例では、ワークブックからOLEオブジェクトを抽出する方法を示します。この例では既存のXLSファイルから異なるOLEオブジェクトを取得し、OLEオブジェクトのファイル形式に基づいて異なるファイル（DOC、XLS、PPT、PDFなど）を保存します。  

コードを実行した後、対応するOLEオブジェクト形式の異なるファイルを保存できます。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);

// Specify the output filename.
let fileName = path.join(dataDir, `ole_${i}.`);

// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Xlsx:
fileName += "xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "jpg";
break;
default:
//........
break;
}

// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = new Uint8Array(ole.getObjectData());
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, `Excel_File${i}.out.xlsx`));
}

// Create the files based on the oleobject format types.
else {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
```  

### **埋め込まれたMOLファイルの抽出**  

Aspose.Cells for Node.js via C++は、MOL（分子構造データファイル：原子と結合に関する情報を含む）などの一般的でない種類のオブジェクトの抽出もサポートしています。以下のコードスニペットは、埋め込みられたMOLファイルを抽出し、[サンプルExcelファイル](94896196.xlsx)を使用してディスクに保存する例です。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "EmbeddedMolSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
let index = 1;

const worksheets = workbook.getWorksheets();
const sheetCount = worksheets.getCount();
for (let i = 0; i < sheetCount; i++) {
const sheet = worksheets.get(i);
const oles = sheet.getOleObjects();
const oleCount = oles.getCount();
for (let j = 0; j < oleCount; j++) {
const ole = oles.get(j);
const fileName = path.join(outputDir, `OleObject${index}.mol`);
const fileStream = fs.createWriteStream(fileName);
fileStream.write(Buffer.from(ole.getObjectData()));
fileStream.end();
index++;
}
}
```  

## **高度なトピック**  
- [リンクされたオブジェクトの表示ラベルへのアクセスと変更](/cells/ja/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Aspose.Cellsを使用してMicrosoft ExcelでOLEオブジェクトを自動的に更新する](/cells/ja/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [ワークブックからOLEオブジェクトを抽出](/cells/ja/nodejs-cpp/extract-ole-objects-from-workbook/)  
- [埋め込まれたOLEオブジェクトのクラス識別子を取得または設定する](/cells/ja/nodejs-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Ole ObjectとしてWAVファイルを挿入する](/cells/ja/nodejs-cpp/inserting-a-wav-file-as-an-ole-object/)  


