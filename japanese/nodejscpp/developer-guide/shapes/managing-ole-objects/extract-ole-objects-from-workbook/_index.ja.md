---  
title: Node.js経由でC++を使用してWorkbookからOLEオブジェクトを抽出する  
linktitle: ワークブックからOLEオブジェクトを抽出  
type: docs  
weight: 110  
url: /ja/nodejs-cpp/extract-ole-objects-from-workbook/  
---  

{{% alert color="primary" %}}  
時々、WorkbookからOLEオブジェクトを抽出する必要があります。Aspose.CellsはこれらのOLEオブジェクトの抽出と保存をサポートしています。

この記事では、Node.jsのコンソールアプリケーションをC++経由で作成し、いくつかの簡単なコード行でWorkbookから異なるOLEオブジェクトを抽出する方法を示します。  
{{% /alert %}}  

## **ワークブックからOLEオブジェクトを抽出**  

### **テンプレートワークブックの作成**  

1. Microsoft Excelでワークブックを作成します。  
1. 最初のシートにOLEオブジェクトとしてMicrosoft Wordドキュメント、Excelワークブック、およびPDFドキュメントを追加します。  

|**OLEオブジェクトを含むテンプレートドキュメント（OleFile.xls）**|  
| :- |  
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|  

次に、OLEオブジェクトを抽出し、それぞれのファイルタイプでハードディスクに保存します。  

### **Aspose.Cellsをダウンロードしてインストールする**  

1. [Aspose.Cells for Node.js via C++をダウンロード](https://downloads.aspose.com/cells/nodejs-cpp)。  
1. 開発コンピュータにインストールします。  

すべてのAsposeのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークを注入するだけです。  

### **プロジェクトを作成する**  

**Node.js**を開始し、新しいコンソールアプリケーションを作成します。この例ではNode.jsのコンソールアプリケーションを示しますが、任意のJavaScript互換環境でも使用できます。  

1. 依存関係を追加  
   1. Aspose.Cellsコンポーネントへの参照をプロジェクトに追加します。例として、`require`関数を使用してパッケージを含めます：  
   ```javascript  
   const { Cells } = require("aspose.cells");  
   ```

### **OLE オブジェクトの抽出**  

以下のコードは、OLEオブジェクト（DOC、XLS、PDFファイル）を検索し抽出し、ディスクに保存します。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "oleFile.xlsx"));

// Get the OleObject Collection in the first worksheet.
const oles = workbook.getWorksheets().get(0).getOleObjects();

// Loop through all the oleobjects and extract each object in the worksheet.
for (let i = 0; i < oles.getCount(); i++) {
const ole = oles.get(i);
// Specify the output filename.
let fileName = path.join(dataDir, "outOle" + i + ".");
// Specify each file format based on the oleobject format type.
switch (ole.getFileFormatType()) {
case AsposeCells.FileFormatType.Doc:
fileName += "doc";
break;
case AsposeCells.FileFormatType.Excel97To2003:
fileName += "Xlsx";
break;
case AsposeCells.FileFormatType.Ppt:
fileName += "Ppt";
break;
case AsposeCells.FileFormatType.Pdf:
fileName += "Pdf";
break;
case AsposeCells.FileFormatType.Unknown:
fileName += "Jpg";
break;
default:
//........
break;
}
// Save the oleobject as a new excel file if the object type is xls.
if (ole.getFileFormatType() === AsposeCells.FileFormatType.Xlsx) {
const ms = Buffer.from(ole.getObjectData());
if (ole.getObjectData() != null) {
const oleBook = new AsposeCells.Workbook(ms);
oleBook.getSettings().setIsHidden(false);
oleBook.save(path.join(dataDir, "outOle" + i + ".out.xlsx"));
}
} else {
if (ole.getObjectData() != null) {
fs.writeFileSync(fileName, ole.getObjectData());
}
}
}
```  

