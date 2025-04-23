---
title: Преобразование листа в изображение — удаление пустого пространства вокруг данных с помощью Node.js через C++
linktitle: Преобразование электронной таблицы в изображение  удалите пустое пространство вокруг данных
type: docs
weight: 40
url: /ru/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Узнайте, как преобразовать лист Microsoft Excel в изображение и убрать пустое пространство вокруг данных с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Иногда вам может потребоваться представить изображения электронных таблиц в приложениях или веб-страницах. Например, вам может потребоваться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или в другой документ. По сути, вы хотите отобразить электронную таблицу в качестве изображения, чтобы ее можно было вставить в другие приложения. Aspose.Cells позволяет преобразовывать электронные таблицы Microsoft Excel в изображения.

{{% /alert %}}

## **Удалите пустое пространство вокруг данных**

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) API преобразует электронную таблицу в файл изображения с любыми указанными атрибутами, например, формат изображения, пагинированные листы и т.д. Поддерживается несколько форматов изображений, включая BMP, GIF, JPG, TIFF и EMF.

Когда вы используете функцию преобразования листа в изображение, выходное изображение по умолчанию имеет пустое пространство, то есть рамку вокруг нее. Вы можете удалить это, установив верхние, нижние, левые и правые поля макета страницы для исходного листа электронной таблицы на 0 и задав соответствующие [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) атрибуты.

Следующий фрагмент кода удаляет пустое пространство вокруг данных на выходном изображении.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
