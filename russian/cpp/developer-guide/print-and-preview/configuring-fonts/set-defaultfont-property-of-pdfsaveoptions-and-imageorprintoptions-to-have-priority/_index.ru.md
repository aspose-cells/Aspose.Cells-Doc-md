---
title: Установить свойство DefaultFont для PdfSaveOptions и ImageOrPrintOptions с приоритетом для C++
linktitle: Установите свойство DefaultFont объектов PdfSaveOptions и ImageOrPrintOptions в приоритетном порядке
type: docs
weight: 30
url: /ru/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Узнайте, как расставлять приоритеты настроек шрифтов при сохранении документов с помощью Aspose.Cells в C++.
---

## **Возможные сценарии использования**

При установке свойства **DefaultFont** объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), возможно, вы ожидаете, что сохранение в PDF или изображение установит этот DefaultFont для всего текста в книге, у которого отсутствует (не установлен) шрифт.

В целом, при сохранении в PDF или изображение, Aspose.Cells сначала пытается установить шрифт по умолчанию рабочей книги (т.е. Workbook.DefaultStyle.Font). Если шрифт по умолчанию книги все еще не отображает/не рендерит текст правильно, тогда Aspose.Cells попытается отобразить с помощью шрифта, указанного против атрибута DefaultFont в [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

Чтобы соответствовать вашим ожиданиям, в [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) есть логическое свойство «**CheckWorkbookDefaultFont**». Вы можете установить его в **false**, чтобы отключить попытки использовать шрифт по умолчанию рабочей книги или чтобы приоритет получил настройка **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

## **Установите свойство DefaultFont объектов PdfSaveOptions/ImageOrPrintOptions**

 Следующий пример кода открывает файл Excel. Ячейка A1 (в первом листе) содержит текст "Christmas Time Font text". Название шрифта — "Christmas Time Personal Use", который не установлен на машине. Мы устанавливаем атрибут **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) в "Times New Roman". Также устанавливаем свойство **CheckWorkbookDefaultFont** в значение **"false"**, что гарантирует отображение текста ячейки A1 с шрифтом "Times New Roman" и не использует шрифт по умолчанию рабочей книги (в данном случае — "Calibri"). Код рендерит первый рабочий лист в форматы изображений PNG и TIFF, а затем в PDF.

{{% alert color="primary" %}}

 Значение по умолчанию для атрибута **CheckWorkbookDefaultFont** равно **true**.

{{% /alert %}}

Это скриншот [шаблонного файла](49446913.xlsx), используемого в примере кода.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

 Это изображение PNG после установки свойства [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) в "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 См. изображение [TIFF](48496672.tiff) после установки свойства [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) в "Times New Roman".

Посмотрите результат [PDF](48496673.pdf), установив свойство [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) в «Times New Roman».

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
