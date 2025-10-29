---  
title: Установка межстрочного интервала параграфа в фигуре или поле с помощью Node.js через C++  
linktitle: Установить интервал между строками абзаца в фигуре или текстовом поле  
type: docs  
weight: 290  
url: /ru/nodejs-cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/  
description: Узнайте, как установить межстрочный интервал в параграфах фигур или полей, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Вы можете установить межстрочный интервал параграфа, его отступ перед и после с помощью свойств [**TextParagraph.getLineSpace()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getLineSpace--), [**TextParagraph.getSpaceBefore()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceBefore--) и [**TextParagraph.getSpaceAfter()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getSpaceAfter--) класса [**TextParagraph**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/).  

{{% /alert %}}  

Приведенный нижеследующий образец кода объясняет использование упомянутых свойств.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
