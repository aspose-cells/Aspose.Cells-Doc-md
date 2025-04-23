---
title: Настройка шрифтов для рендеринга таблиц с помощью Node.js через C++
linktitle: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Узнайте, как настраивать шрифты для рендеринга таблиц с помощью Aspose.Cells for Node.js via C++. Убедитесь, что необходимые шрифты доступны для оптимальной точности конвертации.
---

## **Возможные сценарии использования**

API Aspose.Cells позволяют отображать таблицы в изображениях и конвертировать их в PDF и XPS форматы. Для максимальной точности конвертации необходимо, чтобы используемые в таблице шрифты были доступны в стандартной директории шрифтов операционной системы. Если необходимые шрифты отсутствуют, API попытается заменить их доступными шрифтами.

## **Выбор шрифтов**

Ниже приведен процесс, который API Aspose.Cells следует за кулисами.

1. API пытается найти шрифты на файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если API не может найти шрифты с точно таким же именем, он пытается использовать шрифт по умолчанию, указанный в свойстве [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) книги.
1. Если API не может найти шрифт, определенный в свойстве [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) книги, он пытается использовать шрифт, указанный в свойствах [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) или [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--).
1. Если API не может найти шрифт, определенный в свойствах [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) или [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), он пытается использовать шрифт, указанный в свойстве [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--).
1. Если API не может найти шрифт, определенный в свойстве [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--), он пытается выбрать наиболее подходящие шрифты из всех доступных шрифтов.
1. Наконец, если API не может найти шрифты на файловой системе, он визуализирует электронную таблицу с использованием шрифта Arial.

## **Установка пользовательских каталогов шрифтов**

API Aspose.Cells ищут нужные шрифты в стандартной директории шрифтов операционной системы. Если шрифты не найдены там, поиск продолжается по пользовательским (настроенным) каталогам. Класс [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) предоставляет несколько способов задания пользовательских директорий шрифтов, как описано ниже.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Этот метод полезен, если нужно установить только одну папку.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Этот метод полезен, когда шрифты находятся в нескольких папках, и пользователь хочет установить каждую папку отдельно, а не объединить все шрифты в одну папку.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Этот механизм полезен, когда пользователь хочет загружать шрифты из нескольких папок или одного файла шрифта или данных шрифта из массива байтов.

{{% alert color="primary" %}}

Оба метода [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) и [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) принимают второй параметр типа Boolean. Передача **true** в качестве второго параметра направит API Aspose.Cells на поиск файлов шрифтов в подпапках.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеперечисленных методов в начале приложения, то есть; перед вызовом любых других объектов API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Если все вышеперечисленные методы используются для установки источников шрифтов, то только последние настройки будут применены.

{{% /alert %}}

## **Механизм подстановки шрифтов**

API Aspose.Cells также позволяют указывать заменяющий шрифт для рендеринга. Это полезно, когда необходимый шрифт недоступен на машине, где выполняется конвертация. Пользователи могут задать список имен шрифтов для замены оригинальных. Для этого API предоставляет метод [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-), который принимает 2 параметра. Первый — это строка **string**, указывающая имя шрифта для замены. Второй — это массив строк **string**, содержащий список имен шрифтов для замены исходного.

Вот простой сценарий использования.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Сбор информации**

Помимо вышеуказанных методов, API Aspose.Cells позволяют собирать информацию о выбранных источниках и заменах шрифтов.

1. Метод [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) возвращает массив типа [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase), содержащий список указанных источников шрифтов. Если источники не заданы, метод [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) возвратит пустой массив.
1. Метод [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) принимает параметр типа **string**, позволяющий указать имя шрифта, для которого задана замена. Если для указанного шрифта замена не задана, метод [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) вернет null.

## **Продвинутые темы**
- [Установите шрифт по умолчанию при отображении электронной таблицы в изображения](/cells/ru/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Установите свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions для приоритета](/cells/ru/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Поддерживаемые форматы шрифтов](/cells/ru/nodejs-cpp/supported-font-formats/)
- [Электронная таблица в изображение - установите формат пикселей для визуализированного изображения](/cells/ru/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
