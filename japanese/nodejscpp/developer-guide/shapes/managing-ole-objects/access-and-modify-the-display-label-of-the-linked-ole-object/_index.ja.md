---
title: Node.js経由でC++を使用してリンクされたOleオブジェクトの表示ラベルにアクセスして変更する
linktitle: リンクされたオブジェクトの表示ラベルへのアクセスと変更
type: docs
weight: 100
url: /ja/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Aspose.Cells for Node.js via C++を使用してリンクされたOleオブジェクトの表示ラベルにアクセスして変更する方法を学びます。 
---

## **可能な使用シナリオ**

Microsoft Excelでは、以下のスクリーンショットのようにOleオブジェクトの表示ラベルを変更できます。また、Aspose.Cells APIの[**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--)プロパティを使用してOleオブジェクトの表示ラベルにアクセスまたは変更することも可能です。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **リンクされたオブジェクトの表示ラベルへのアクセスと変更**

次のサンプルコードをご覧ください。このコードはOleオブジェクトを含む[sample Excelファイル](64716810.xlsx)をロードします。コードはOleオブジェクトにアクセスし、そのラベルを「Sample APIs」から「Aspose APIs」に変更します。以下に示すコンソール出力は、サンプルコードがサンプルExcelファイルに与える効果を示しています。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **コンソール出力**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
