---
title: Установите свойство DefaultFont объектов PdfSaveOptions и ImageOrPrintOptions в приоритетном порядке
type: docs
weight: 30
url: /ru/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Возможные сценарии использования**

При установке свойства **DefaultFont** объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), возможно, вы ожидаете, что сохранение в PDF или изображение установит этот DefaultFont для всего текста в книге, у которого отсутствует (не установлен) шрифт.

Общее правило: при сохранении в PDF или изображение Aspose.Cells для Python via .NET вначале пытается установить шрифт по умолчанию для рабочей книги (т.е. Workbook.DefaultStyle.Font). Если шрифт по умолчанию неправильно отображается или рендерится, Aspose.Cells для Python via .NET попробует рендерить с шрифтом, указанным против DefaultFont в [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

Чтобы соответствовать вашим ожиданиям, в [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) есть логическое свойство "**check_workbook_default_font**". Вы можете установить его в **false**, чтобы отключить использование шрифта по умолчанию рабочей книги, или оставить, чтобы приоритет имел настройка **default_font**.

## **Установите свойство DefaultFont объектов PdfSaveOptions/ImageOrPrintOptions**

Следующий пример кода открывает файл Excel. В ячейке A1 (на первом листе) установлен текст "Christmas Time Font text". Название шрифта — "Christmas Time Personal Use", которого нет на машине. Мы устанавливаем атрибут ***default_font*** в [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) в "Times New Roman". Также мы задаем булевое свойство **check_workbook_default_font** в значение **"false"**, что обеспечивает отображение текста в ячейке A1 шрифтом "Times New Roman" и исключает использование шрифта по умолчанию рабочей книги (в данном случае "Calibri"). Код сохраняет первый лист в формат PNG и TIFF, а также экспортирует в PDF.

{{% alert color="primary" %}}

Значение по умолчанию атрибута ***CheckWorkbookDefaultFont*** - **true**.

{{% /alert %}}

Это скриншот [шаблонного файла](49446913.xlsx), используемого в примере кода.

![todo:image_alt_text](1.png)

Это выходное изображение PNG после установки свойства [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) в "Times New Roman".

![todo:image_alt_text](2.png)

См. выходной файл [TIFF](48496672.tiff) изображения после установки свойства [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) на "Times New Roman".

См. выходной [PDF](48496673.pdf) файл после установки свойства [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) на "Times New Roman".

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

