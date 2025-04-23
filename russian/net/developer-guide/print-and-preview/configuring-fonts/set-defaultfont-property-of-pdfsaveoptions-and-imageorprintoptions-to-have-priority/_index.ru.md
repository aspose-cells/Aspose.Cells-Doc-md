---
title: Установите свойство DefaultFont объектов PdfSaveOptions и ImageOrPrintOptions в приоритетном порядке
type: docs
weight: 30
url: /ru/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Возможные сценарии использования**

При установке свойства **DefaultFont** объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), возможно, вы ожидаете, что сохранение в PDF или изображение установит этот DefaultFont для всего текста в книге, у которого отсутствует (не установлен) шрифт.

Как правило, при сохранении в PDF или изображение, Aspose.Cells сначала попытается установить шрифт по умолчанию книги (т. е. Workbook.DefaultStyle.Font). Если шрифт по умолчанию книги все равно не может правильно отображать/воспроизводить текст, то Aspose.Cells попытается воспроизвести с шрифтом, указанным против атрибута DefaultFont в [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

Чтобы соответствовать вашим ожиданиям, у нас есть логическое свойство с именем "**CheckWorkbookDefaultFont**" в [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions). Вы можете установить его в **false**, чтобы отключить попытку использования шрифта по умолчанию книги или предоставить приоритет настройке **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions).

## **Установите свойство DefaultFont объектов PdfSaveOptions/ImageOrPrintOptions**

Приведенный ниже примерный код открывает файл Excel. Ячейка A1 (на первом листе) имеет текст "Christmas Time Font text". Название шрифта "Christmas Time Personal Use" отсутствует на компьютере. Мы устанавливаем атрибут ***DefaultFont*** объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) на "Times New Roman". Мы также устанавливаем логическое свойство **CheckWorkbookDefaultFont** в **"false"**, что гарантирует, что текст ячейки A1 воспроизводится шрифтом "Times New Roman" и не использует шрифт по умолчанию книги (в этом случае - "Calibri"). Код воспроизводит первый лист в форматах PNG и TIFF. Наконец, он воспроизводится в формате PDF.

{{% alert color="primary" %}}

Значение по умолчанию атрибута ***CheckWorkbookDefaultFont*** - **true**.

{{% /alert %}}

Это скриншот [шаблонного файла](49446913.xlsx), используемого в примере кода.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Это выходное изображение PNG после установки свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) в "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

См. выходной файл [TIFF](48496672.tiff) изображения после установки свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) на "Times New Roman".

См. выходной [PDF](48496673.pdf) файл после установки свойства [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) на "Times New Roman".

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
{{< app/cells/assistant language="csharp" >}}
