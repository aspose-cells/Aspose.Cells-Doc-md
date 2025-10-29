---  
title: Установка полей комментария или фигуры внутри листа с помощью Node.js через C++  
linktitle: Установить поля комментария или формы внутри таблицы  
type: docs  
weight: 1500  
url: /ru/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Узнайте, как устанавливать поля комментариев или фигур внутри листа Excel с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells позволяет вам устанавливать поля любой фигуры или комментария с помощью свойства [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/). Это свойство возвращает объект класса [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment), который имеет различные свойства, например, [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--) и др., которые можно использовать для установки верхних, левых, нижних и правых полей.  

## **Задать поля комментария или формы внутри рабочего листа**  

Пожалуйста, ознакомьтесь со следующим образцом кода. Он загружает [образец Excel файла](61767851.xlsx), содержащий две формы. Код получает доступ к формам поочередно и устанавливает их верхние, левые, нижние и правые поля. Пожалуйста, ознакомьтесь с [файлом вывода Excel](61767852.xlsx), сгенерированным кодом, и снимком экрана, показывающим эффект кода на файл вывода Excel.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
