---
title: Рендеринг листа в графический контекст с помощью Node.js и C++
linktitle: Отобразить Рабочий лист на графический контекст
type: docs
weight: 300
url: /ru/nodejs-cpp/render-worksheet-to-graphic-context/
description: Узнайте, как рендерить рабочий лист в графический контекст с помощью Aspose.Cells for Node.js via C++. Это включает рендеринг в файлы изображений, на экраны и в принтеры.
---

{{% alert color="primary" %}}

Aspose.Cells теперь может рендерить рабочие листы в графический контекст. Графический контекст может быть чем угодно, например, изображением, экраном или принтером. Пожалуйста, используйте один из следующих двух методов для рендеринга рабочего листа в графический контекст.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Следующий код демонстрирует, как использовать Aspose.Cells для рендеринга рабочего листа в графический контекст. После выполнения кода он распечатает весь рабочий лист и заполнит оставшееся пустое пространство синим цветом в графическом контексте и сохранит изображение как файл **OutputImage_out_.png**. Вы можете использовать любой исходный файл Excel для тестирования этого кода. Также ознакомьтесь с комментариями внутри кода для лучшего понимания.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
{{< app/cells/assistant language="nodejs-cpp" >}}
