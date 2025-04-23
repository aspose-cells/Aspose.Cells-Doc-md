---
title: Pdf с Node.js через C++
linktitle: Pdf
type: docs
weight: 220
url: /ru/nodejs-cpp/convert-excel-to-pdf/
description: Узнайте, как конвертировать книгу Excel в PDF с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells поддерживает преобразование книги Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.
{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными секторами и физическими лицами. Это стандартный формат документа, и разработчиков программного обеспечения часто просят найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ напрямую записывает информацию о API и номере версии в выходные документы. Например, при преобразовании документа в PDF, Aspose.Cells for Node.js via C++ заполняет поле **PDF Producer** значением, например 'Aspose.Cells v23.2'.

Обратите внимание, что вы можете изменить эту информацию в выходных документах с помощью свойства [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--).
{{% /alert %}}

### **Прямое преобразование**

Aspose.Cells for Node.js via C++ поддерживает преобразование электронных таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF, используя метод [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) класса [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-). Метод [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) возвращает член перечисления [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat), который преобразует нативные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), вызвав его пустой конструктор.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните любую работу (ввод данных, применение форматирования, задание формул, вставка изображений или других объектов рисования и т. д.) на электронной таблице, используя API Aspose.Cells.
1. После завершения кода таблицы вызовите метод [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) класса [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) для сохранения таблицы.

Формат файла должен быть PDF, поэтому выберите *Pdf* (предопределенное значение) из перечисления [**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) для создания окончательного документа PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **Расширенное преобразование**

Вы также можете использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) для установки различных атрибутов конвертации. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) позволяет контролировать настройки печати, шрифта, безопасности и сжатия для выходного PDF. 

Самым важным свойством является [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), позволяющий устанавливать уровень соответствия стандартам PDF. В настоящее время можно сохранять в форматах PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u. Обратите внимание, что при формате PDF/A размер выходного файла больше, чем у обычного файла PDF.

#### **Сохранение книги в формате PDF/A**

Ниже приведен фрагмент кода, демонстрирующий использование класса [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) для сохранения файлов Excel в формате PDF/A.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
Обратите внимание, что свойство [**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) было добавлено с выпуском Aspose.Cells for Node.js via C++ 5.3.0.
{{% /alert %}}

#### **Установить время создания PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) вы можете получать или устанавливать время создания PDF. В следующем коде демонстрируется использование свойства [**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--) для установки времени создания файла PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **Установите опцию ContentCopyForAccessibility**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) вы можете получать или устанавливать параметр PDF [**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--) для контроля доступа к содержимому в созданном PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **Экспорт пользовательских свойств в PDF**

С помощью класса [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) можно экспортировать пользовательские свойства из исходной книги в формат PDF. Перечислитель [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/) предназначен для указания способа экспорта свойств. Эти свойства можно увидеть в Adobe Acrobat Reader, нажав на файл, а затем на опцию свойств, как показано на следующем изображении. Файл шаблона "sourceWithCustProps.xlsx" можно загрузить [здесь](sourceWithCustProps.xlsx) для тестирования, а файл PDF "outSourceWithCustProps" доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **Атрибуты преобразования**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Excel в PDF от Aspose.Cells все еще имеет несколько ограничений. Карта заполнения не поддерживается при преобразовании в формат PDF. Кроме того, некоторые объекты рисования не поддерживаются хорошо.

В таблице ниже перечислены все функции, которые полностью или частично поддерживаются при экспорте в формат PDF с помощью Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты таблиц, но она идентифицирует те функции, которые не поддерживаются или поддерживаются частично для преобразования в PDF.

|**Элемент документа**|**Атрибут**|**Поддерживается**|**Примечания**|
| :- | :- | :- | :- |
|Выравнивание| |Да| |
|Настройки фона| |Да| |
|Граница|Цвет|Да| |
|Граница|Стиль линии|Да| |
|Граница|Толщина линии|Да| |
|Данные ячейки| |Да| |
|Комментарии| |Да| |
|Условное форматирование| |Да| |
|Свойства документа| |Да| |
|Объекты рисования| |Частично|Тени и трехмерные эффекты для объектов рисования плохо поддерживаются; WordArt и SmartArt поддерживаются частично.|
|Шрифт|Размер|Да| |
|Шрифт|Цвет|Да| |
|Шрифт|Стиль|Да| |
|Шрифт|Подчеркивание|Да| |
|Шрифт|Эффекты|Да| |
|Изображения| |Да| |
|Гиперссылка| |Да| |
|Диаграммы| |Частично|Карта диаграмм не поддерживается.|
|Объединенные ячейки| |Да| |
|Разрыв страницы| |Да| |
|Настройка страницы|Верхний/нижний колонтитул|Да| |
|Настройка страницы|Поля|Да| |
|Настройка страницы|Ориентация страницы|Да| |
|Настройка страницы|Размер страницы|Да| |
|Настройка страницы|Область печати|Да| |
|Настройка страницы|Печатные заголовки|Да| |
|Настройка страницы|Масштабирование|Да| |
|Высота строки/Ширина столбца| |Да| |
|Язык справа налево (RTL)| |Да| |

{{% alert color="primary" %}}
Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.
{{% /alert %}}

## **Продвинутые темы**
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Избегание пустой страницы в выходном PDF, когда нет ничего для печати](/cells/ru/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Изменить шрифт только для определенных символов Unicode при сохранении в формате PDF](/cells/ru/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Преобразовать файл XLSX в формат PDF](/cells/ru/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в формат PDF](/cells/ru/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создание PdfBookmarkEntry для листа с диаграммой](/cells/ru/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Заполнить все столбцы листа Excel на одной странице PDF](/cells/ru/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler](/cells/ru/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получить предупреждения о замене шрифта при преобразовании файла Excel](/cells/ru/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при преобразовании Excel в PDF](/cells/ru/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества создаваемых страниц - Преобразование Excel в PDF](/cells/ru/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в формат PDF](/cells/ru/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [Рендеринг офисных надстроек при преобразовании Excel в PDF](/cells/ru/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Отображать одну страницу PDF для каждого листа Excel - Преобразование Excel в PDF](/cells/ru/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells](/cells/ru/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Добавление изображений с изменением размера - Преобразование Excel в PDF](/cells/ru/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Сохранить каждый лист в отдельный файл PDF](/cells/ru/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF с обычным или минимальным размером](/cells/ru/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохранить указанные листы в формат PDF](/cells/ru/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [Защищенные документы в формате PDF](/cells/ru/nodejs-cpp/secure-pdf-documents/)
- [Указание способа пересечения строк в выходном PDF и изображении](/cells/ru/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
