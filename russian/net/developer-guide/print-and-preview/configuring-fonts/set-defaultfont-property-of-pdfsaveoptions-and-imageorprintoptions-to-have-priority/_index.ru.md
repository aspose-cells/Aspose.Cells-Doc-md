---
title: Установите свойство DefaultFont PdfSaveOptions и ImageOrPrintOptions, чтобы иметь приоритет
type: docs
weight: 30
url: /ru/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Возможные сценарии использования**

 При установке**Шрифт по умолчанию** свойство**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** а также**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, вы можете ожидать, что при сохранении в PDF или изображение для этого DefaultFont будет установлен весь текст в книге с отсутствующим (не установленным) шрифтом.

 Как правило, при сохранении в PDF или изображение Aspose.Cells сначала пытается установить шрифт Workbook по умолчанию (т. е. Workbook.DefaultStyle.Font). Если шрифт рабочей книги по умолчанию по-прежнему не может правильно отображать/отображать текст, тогда Aspose.Cells попытается отобразить шрифт, указанный в атрибуте DefaultFont в**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

Чтобы оправдать ваши ожидания, у нас есть логическое свойство с именем "**CheckWorkbookDefaultFont** " в**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** . Вы можете установить его на**ЛОЖЬ**чтобы отключить использование шрифта книги по умолчанию или разрешить**Шрифт по умолчанию** установка в**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** иметь приоритет.

## **Установите свойство DefaultFont для PdfSaveOptions/ImageOrPrintOptions**

 Следующий пример кода открывает файл Excel. В ячейке A1 (на первом листе) установлен текст «Текст шрифта Christmas Time». Название шрифта «Christmas Time Personal Use» не установлено на машине. Мы устанавливаем***Шрифт по умолчанию*** атрибут**[PdfSaveOptions] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** в «Таймс Нью Роман». Мы также устанавливаем**CheckWorkbookDefaultFont** логическое свойство для**"ЛОЖЬ"** что гарантирует, что текст ячейки A1 отображается шрифтом «Times New Roman» и не должен использовать шрифт книги по умолчанию (в данном случае «Calibri»). Код преобразует первый рабочий лист в форматы изображений PNG и TIFF. Наконец, он преобразуется в формат файла PDF.

{{% alert color="primary" %}}

 Значение по умолчанию***CheckWorkbookDefaultFont*** атрибут**истинный**.

{{% /alert %}}

 Это скриншот из[файл шаблона](49446913.xlsx) используется в примере кода.

![дело:изображение_альтернативный_текст](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Это выходное изображение PNG после установки**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**собственность "Таймс Нью Роман".

![дело:изображение_альтернативный_текст](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 Посмотреть результат[ТИФФ](48496672.tiff) изображение после установки**[ImageOrPrintOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**собственность "Таймс Нью Роман".

Посмотреть результат[PDF](48496673.pdf)файл после установки**[PdfSaveOptions.DefaultFont] (https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**собственность "Таймс Нью Роман".

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
