---
title: HTML с C++
linktitle: HTML
type: docs
weight: 230
url: /ru/cpp/convert-excel-to-html/
description: Преобразуйте Excel в HTML и MHTML форматы с помощью Aspose.Cells и C++.
---

## **Преобразование книги Excel в HTML**
API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions), чтобы дать возможность управлять несколькими аспектами итогового HTML.

Пример кода ниже показывает, как сохранить рабочую книгу в виде HTML файла с помощью C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Преобразование книги Excel в файлы MHTML**
MHTML объединяет обычный HTML с внешними ресурсами (то есть содержимым, которое обычно связано, например, изображения, анимации, аудио и так далее) в один файл. Они используются для электронных писем с расширением .mht. Aspose.Cells поддерживает чтение и запись MHTML файлов.

Пример кода ниже показывает, как сохранить рабочую книгу в виде файла MHTML с помощью C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге](/cells/ru/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Избегайте экспоненциальной записи больших чисел при импорте из HTML](/cells/ru/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [Изменить тип HTML ссылки](/cells/ru/cpp/change-the-html-link-target-type/)
- [Преобразование Excel в HTML со всплывающей подсказкой](/cells/ru/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ru/cpp/create-transparent-image-of-excel-worksheet/)
- [Удаление избыточных пробелов после переноса строки при импорте HTML](/cells/ru/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Отключить отображение устаревших комментариев при сохранении в HTML](/cells/ru/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Отключить экспорт фреймовых сценариев и свойств документа](/cells/ru/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel в HTML - использование параметра PresentationPreference для лучшего макета](/cells/ru/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Исключить неиспользуемые стили во время преобразования Excel в HTML](/cells/ru/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Развертывание текста справа налево при экспорте файла Excel в HTML](/cells/ru/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML](/cells/ru/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Экспортировать комментарии при сохранении файла Excel в HTML](/cells/ru/cpp/export-comments-while-saving-excel-file-to/)
- [Экспортировать свойства рабочей книги и листа в формате HTML при конвертации Excel в HTML](/cells/ru/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Экспорт Excel в HTML с сеткой](/cells/ru/cpp/export-excel-to-html-with-gridlines/)
- [Экспортировать диапазон области печати в HTML](/cells/ru/cpp/export-print-area-range-to/)
- [Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами](/cells/ru/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Экспорт CSS таблицы рабочего листа отдельно в выходном HTML](/cells/ru/cpp/export-worksheet-css-separately-in-output/)
- [Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML](/cells/ru/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId](/cells/ru/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Предотвратить экспорт скрытого содержимого листа при сохранении в HTML](/cells/ru/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Распознавание самозакрывающихся тегов](/cells/ru/cpp/recognise-self-closing-tags/)
- [Визуализация градиентного заливки для WordArt при преобразовании таблиц в HTML](/cells/ru/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Установить ширину столбца в масштабируемую единицу, например em или процент](/cells/ru/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML](/cells/ru/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType](/cells/ru/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Поддерживайте макет тегов DIV при загрузке HTML в книгу Excel](/cells/ru/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [Включить пользовательские свойства CSS при сохранении в HTML](/cells/ru/cpp/enable-css-custom-properties-while-saving-to-html/)
