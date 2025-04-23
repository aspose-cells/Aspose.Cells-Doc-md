---
title: HTML с помощью Node.js через C++
linktitle: HTML
type: docs
weight: 230
url: /ru/nodejs-cpp/convert-excel-to-html/
---

## **Преобразование книги Excel в HTML**
API Aspose.Cells поддерживает экспорт таблиц в формат HTML. В этом случае Aspose.Cells использует класс [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions), чтобы дать возможность управлять несколькими аспектами итогового HTML.

Пример кода ниже демонстрирует, как сохранить рабочую книгу как HTML-файл с помощью Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **Преобразование книги Excel в файлы MHTML**
MHTML объединяет обычный HTML с внешними ресурсами (то есть содержимым, которое обычно связано, например, изображения, анимации, аудио и так далее) в один файл. Они используются для электронных писем с расширением .mht. Aspose.Cells поддерживает чтение и запись MHTML файлов.

Пример кода ниже показывает, как сохранить рабочую книгу как MHTML-файл с помощью Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **Продвинутые темы**
- [Автоматическая подгонка столбцов и строк при загрузке HTML в Рабочей книге](/cells/ru/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Избегайте экспоненциальной записи больших чисел при импорте из HTML](/cells/ru/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Изменить тип HTML ссылки](/cells/ru/nodejs-cpp/change-the-html-link-target-type/)
- [Преобразование Excel в HTML со всплывающей подсказкой](/cells/ru/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ru/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Удаление избыточных пробелов после переноса строки при импорте HTML](/cells/ru/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Отключить отображение устаревших комментариев при сохранении в HTML](/cells/ru/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Отключить экспорт фреймовых сценариев и свойств документа](/cells/ru/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel в HTML - использование параметра PresentationPreference для лучшего макета](/cells/ru/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Исключить неиспользуемые стили во время преобразования Excel в HTML](/cells/ru/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Развертывание текста справа налево при экспорте файла Excel в HTML](/cells/ru/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Экспорт условного форматирования данных, цветовой шкалы и набора значков при преобразовании Excel в HTML](/cells/ru/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Экспортировать комментарии при сохранении файла Excel в HTML](/cells/ru/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Экспортировать свойства рабочей книги и листа в формате HTML при конвертации Excel в HTML](/cells/ru/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Экспорт Excel в HTML с сеткой](/cells/ru/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Экспортировать диапазон области печати в HTML](/cells/ru/nodejs-cpp/export-print-area-range-to/)
- [Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами](/cells/ru/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Экспорт CSS таблицы рабочего листа отдельно в выходном HTML](/cells/ru/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML](/cells/ru/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId](/cells/ru/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Предотвратить экспорт скрытого содержимого листа при сохранении в HTML](/cells/ru/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Предоставление пути к экспортированному файлу HTML листа через интерфейс IFilePathProvider](/cells/ru/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Распознавание самозакрывающихся тегов](/cells/ru/nodejs-cpp/recognise-self-closing-tags/)
- [Визуализация градиентного заливки для WordArt при преобразовании таблиц в HTML](/cells/ru/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Установить ширину столбца в масштабируемую единицу, например em или процент](/cells/ru/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML](/cells/ru/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType](/cells/ru/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Поддерживайте макет тегов DIV при загрузке HTML в книгу Excel](/cells/ru/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Включить пользовательские свойства CSS при сохранении в HTML](/cells/ru/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
