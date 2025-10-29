---
title: Установить свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions с приоритетом в Node.js через C++
linktitle: Установите свойство DefaultFont объектов PdfSaveOptions и ImageOrPrintOptions в приоритетном порядке
type: docs
weight: 30
url: /ru/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Узнайте, как установить свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions с помощью Aspose.Cells for Node.js via C++. Обеспечьте правильное отображение шрифтов при их отсутствии.
---

## **Возможные сценарии использования**

При установке свойства **DefaultFont** объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), возможно, вы ожидаете, что сохранение в PDF или изображение установит этот DefaultFont для всего текста в книге, у которого отсутствует (не установлен) шрифт.

 Обычно при сохранении в PDF или изображение Aspose.Cells for Node.js via C++ сначала пытается установить шрифт по умолчанию рабочей книги (т.е. `Workbook.DefaultStyle.Font`). Если шрифт по умолчанию рабочей книги все еще не может отображать или рендерить текст должным образом, тогда Aspose.Cells попытается выполнить рендеринг с шрифтом, указанным против атрибута DefaultFont в [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

Чтобы соответствовать вашим ожиданиям, у нас есть логическое свойство с именем "**CheckWorkbookDefaultFont**" в [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Вы можете установить его в **false**, чтобы отключить попытку использования шрифта по умолчанию книги или предоставить приоритет настройке **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

## **Установите свойство DefaultFont объектов PdfSaveOptions/ImageOrPrintOptions**

 Следующий пример кода открывает файл Excel. Ячейка A1 (в первом листе) содержит текст "Christmas Time Font text". Название шрифта — "Christmas Time Personal Use", который не установлен на машине. Мы устанавливаем атрибут **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) в "Times New Roman". Также устанавливаем свойство **CheckWorkbookDefaultFont** в значение **"false"**, что гарантирует отображение текста ячейки A1 с шрифтом "Times New Roman" и не использует шрифт по умолчанию рабочей книги (в данном случае — "Calibri"). Код рендерит первый рабочий лист в форматы изображений PNG и TIFF, а затем в PDF.

{{% alert color="primary" %}}

 Значение по умолчанию для атрибута **CheckWorkbookDefaultFont** равно **true**.

{{% /alert %}}

Это скриншот [шаблонного файла](49446913.xlsx), используемого в примере кода.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

 Это изображение PNG после установки свойства [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) в "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 См. изображение [TIFF](48496672.tiff) после установки свойства [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) в "Times New Roman".

 См. файл [PDF](48496673.pdf) после установки свойства [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) в "Times New Roman".

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
