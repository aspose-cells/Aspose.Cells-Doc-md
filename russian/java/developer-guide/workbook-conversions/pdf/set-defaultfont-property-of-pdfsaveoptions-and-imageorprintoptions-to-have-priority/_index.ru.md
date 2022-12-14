---
title: Установите свойство DefaultFont PdfSaveOptions и ImageOrPrintOptions, чтобы иметь приоритет
type: docs
weight: 30
url: /ru/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Возможные сценарии использования**

 При установке**Шрифт по умолчанию** свойство[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) а также[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) вы можете ожидать, что сохранение в PDF или изображение установит**Шрифт по умолчанию** ко всему тексту в книге, в котором отсутствует (не установлен) шрифт.

 Как правило, при сохранении в PDF или изображение Aspose.Cells сначала пытается установить шрифт Workbook по умолчанию (т. е.[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). Если шрифт рабочей книги по умолчанию по-прежнему не может правильно отображать/отображать текст, тогда Aspose.Cells попытается отобразить шрифт, указанный против**Шрифт по умолчанию** атрибут в[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Чтобы оправдать ваши ожидания, у нас есть логическое свойство с именем "**CheckWorkbookDefaultFont** " в[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . Вы можете установить для него значение false, чтобы отключить использование шрифта книги по умолчанию, или разрешить**Шрифт по умолчанию** установка в[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) иметь приоритет.

## **Установите свойство DefaultFont для PdfSaveOptions/ImageOrPrintOptions**

Следующий пример кода открывает файл Excel. В ячейке A1 (на первом листе) установлен текст «Текст шрифта Christmas Time». Название шрифта «Christmas Time Personal Use» не установлено на машине. Мы устанавливаем**Шрифт по умолчанию**атрибут[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)в «Таймс Нью Роман». Мы также устанавливаем**CheckWorkbookDefaultFont**логическое свойство "**ЛОЖЬ**", что гарантирует, что текст ячейки A1 отображается с использованием шрифта "Times New Roman" и не должен использовать шрифт книги по умолчанию (в данном случае "Calibri"). Код отображает первый рабочий лист в форматах изображений PNG и TIFF. Наконец, он преобразуется в формат файла PDF.

{{% alert color="primary" %}}

 Значение по умолчанию***CheckWorkbookDefaultFont*** атрибут**истинный**.

{{% /alert %}}

Это скриншот из[файл шаблона](49446914.xlsx)используется в примере кода.

![дело:изображение_альтернативный_текст](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Это выходное изображение PNG после установки[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)собственность "Таймс Нью Роман".

![дело:изображение_альтернативный_текст](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Посмотреть результат[ТИФФ](out1_imageTIFF.tiff)изображение после установки[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)собственность "Таймс Нью Роман".

Посмотреть результат[PDF](out1_pdf.pdf)файл после установки[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)собственность "Таймс Нью Роман".

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
