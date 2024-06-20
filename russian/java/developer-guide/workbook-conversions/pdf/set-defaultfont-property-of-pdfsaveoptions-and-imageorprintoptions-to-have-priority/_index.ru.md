---
title: Установите свойство DefaultFont объектов PdfSaveOptions и ImageOrPrintOptions в приоритетном порядке
type: docs
weight: 30
url: /ru/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Возможные сценарии использования**

При установке свойства **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) можно ожидать, что при сохранении в формат PDF или изображения будет установлен этот **DefaultFont** для всего текста в рабочей книге, используя отсутствующий (не установленный) шрифт.

Когда сохраняется в формат PDF или изображения, Aspose.Cells сначала пытается установить шрифт по умолчанию рабочей книги (т.е. [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)). Если шрифт по умолчанию рабочей книги все еще не может правильно показывать/воспроизводить текст, то Aspose.Cells попытается воспроизвести с использованием шрифта, указанного в атрибуте **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Чтобы соответствовать вашему ожиданию, у нас есть логическое свойство с именем "**CheckWorkbookDefaultFont**" в [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions). Вы можете установить его в значение false, чтобы отключить попытку установки шрифта по умолчанию рабочей книги, или позволить установке **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) иметь приоритет.

## **Установите свойство DefaultFont объектов PdfSaveOptions/ImageOrPrintOptions**

Следующий образец кода открывает файл Excel. В ячейке A1 (на первом листе) установлен текст "Christmas Time Font text". Название шрифта - "Christmas Time Personal Use", который не установлен на машине. Мы устанавливаем атрибут **DefaultFont** объектов [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) на "Times New Roman". Мы также устанавливаем логическое свойство **CheckWorkbookDefaultFont** в "**false**", чтобы гарантировать, что текст ячейки A1 будет отображаться шрифтом "Times New Roman" и не будет использоваться шрифт по умолчанию рабочей книги (в данном случае - "Calibri"). Код рендерит первый лист в форматах PNG и TIFF. Затем рендерит в формат PDF.

{{% alert color="primary" %}}

Значение по умолчанию атрибута ***CheckWorkbookDefaultFont*** - **true**.

{{% /alert %}}

Это скриншот файла [шаблона](49446914.xlsx), используемого в примере кода.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Это выходное изображение PNG после установки свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) в "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Смотрите выходное изображение [TIFF](out1_imageTIFF.tiff) после установки свойства [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) в "Times New Roman".

Смотрите выходной [PDF](out1_pdf.pdf) файл после установки свойства [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) в "Times New Roman".

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
