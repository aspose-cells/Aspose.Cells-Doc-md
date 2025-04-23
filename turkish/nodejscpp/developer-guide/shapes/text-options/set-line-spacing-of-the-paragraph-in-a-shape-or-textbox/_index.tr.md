---  
title: C++ kullanarak Node.js ile Şekilde veya Metin Kutusunda Paragraf Satır Aralığını Ayarla  
linktitle: Bir Şekil veya Metin Kutusundaki Paragrafın Satır Boşluğunu Ayarlama  
type: docs  
weight: 290  
url: /tr/nodejs-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/  
description: Aspose.Cells for Node.js via C++ kullanarak şekiller veya metin kutularında paragraf satır aralığını nasıl ayarlayacağınızı öğrenin.  
---  

{{% alert color="primary" %}}  

[**TextParagraph**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/) sınıfının [**TextParagraph.getLineSpace()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getLineSpace--), [**TextParagraph.getSpaceBefore()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceBefore--) ve [**TextParagraph.getSpaceAfter()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceAfter--) özelliklerini kullanarak paragrafın satır aralığını, öncesi ve sonrası boşluklarını ayarlayabilirsiniz.  

{{% /alert %}}  

Aşağıdaki örnek kod, belirtilen özelliklerin kullanımını açıklar.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add text box inside the sheet
ws.getShapes().addTextBox(2, 0, 2, 0, 100, 200);

// Access first shape which is a text box and set its text
const shape = ws.getShapes().get(0);
shape.setText("Sign up for your free phone number.\nCall and text online for free.");

// Access the first paragraph
const p = shape.getTextBody().getTextParagraphs().get(1);

// Set the line space
p.setLineSpaceSizeType(AsposeCells.LineSpaceSizeType.Points);
p.setLineSpace(20);

// Set the space after
p.setSpaceAfterSizeType(AsposeCells.LineSpaceSizeType.Points);
p.setSpaceAfter(10);

// Set the space before
p.setSpaceBeforeSizeType(AsposeCells.LineSpaceSizeType.Points);
p.setSpaceBefore(10);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

