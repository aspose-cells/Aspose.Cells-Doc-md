---
title: Преобразовать Excel в PDF с помощью C++
linktitle: Преобразование Excel в PDF
type: docs
weight: 220
url: /ru/cpp/convert-excel-to-pdf/
description: Узнайте, как преобразовать рабочие книги Excel в формат PDF с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование рабочих книг Excel в PDF. В этом примере мы увидим полное преобразование книги Excel в PDF.

{{% /alert %}}

## **Преобразование книги Excel в PDF**

Файлы PDF широко используются для обмена документами между организациями, государственными структурами и отдельными лицами. Это стандартный формат документа, и разработчикам часто требуется найти способ преобразовать файлы Microsoft Excel в документы PDF.

Aspose.Cells поддерживает преобразование файлов Excel в PDF и поддерживает высокую визуальную точность при преобразовании.

{{% alert color="primary" %}}

Aspose.Cells for C++ напрямую записывает информацию о API и номере версии в выходные документы. Например, при рендеринге документа в PDF, Aspose.Cells for C++ заполняет поле **Производитель PDF** значением, например 'Aspose.Cells v23.2'.

Обратите внимание, что вы можете изменить эту информацию в выходных документах, используя свойство [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getproducer/).

{{% /alert %}}

### **Прямое преобразование**

Aspose.Cells for C++ поддерживает преобразование из таблиц в PDF независимо от другого программного обеспечения. Просто сохраните файл Excel в PDF, используя метод [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Метод [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) предоставляет член перечисления [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/), который преобразует нативные файлы Excel в формат PDF.

Следуйте нижеприведенным шагам, чтобы непосредственно преобразовать электронные таблицы Excel в формат PDF:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), вызвав его конструктор без параметров.
1. Вы можете открыть/загрузить существующий файл шаблона, или пропустить этот шаг, если создаете книгу из нуля.
1. Выполните работу (ввод данных, применение форматирования, установка формул, вставка изображений или других графических объектов и т.д.) на листе, используя API Aspose.Cells.
1. Когда код для листа завершен, вызовите метод [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) для сохранения листа.

Формат файла должен быть PDF, поэтому выберите *Pdf* (предопределенное значение) из перечисления [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/), чтобы сгенерировать итоговый PDF документ.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"output.pdf";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the document in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Document saved successfully in PDF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Расширенное преобразование**

Также вы можете использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) для установки различных атрибутов преобразования. Настройка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) позволяет контролировать параметры печати, шрифта, безопасности и сжатия для выходного PDF.

Самое важное свойство — это [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), которое позволяет установить уровень соответствия стандартам PDF. В настоящее время можно сохранять в PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u. Обратите внимание, что при использовании формата PDF/A размер итогового файла больше, чем у обычного PDF.

#### **Сохранение книги в формате PDF/A**

Ниже приведен пример кода, демонстрирующий, как использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) для сохранения файлов Excel в PDF/A-совместимый формат PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate new workbook
    Workbook workbook;

    // Insert a value into the A1 cell in the first worksheet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(U16String(u"Testing PDF/A"));

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set the compliance type
    pdfSaveOptions.SetCompliance(PdfCompliance::PdfA1b);

    // Save the file
    workbook.Save(outDir + u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file created successfully with PDF/A-1b compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Обратите внимание, свойство [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) было добавлено с выпуском Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Установить время создания PDF**

С классом [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) вы можете получать или устанавливать время создания PDF. Следующий код демонстрирует использование свойства [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcreatedtime/) для установки времени создания файла PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"Book1.xlsx";

    // Load excel file containing charts
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions options;
	options.SetCreatedTime(Date{ 2025,01,01 });

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(srcDir + u"output.pdf", options);

    std::cout << "Workbook saved to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Установите опцию ContentCopyForAccessibility**

С классом [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) вы можете получать или устанавливать опцию [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) PDF для контроля доступа к содержимому в преобразованном PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"BookWithSomeData.xlsx";

    // Load excel file containing some data
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOpt;

    // Create an instance of PdfSecurityOptions
    PdfSecurityOptions securityOptions;

    // Set AccessibilityExtractContent to false
    securityOptions.SetAccessibilityExtractContent(false);

    // Set the security option in the PdfSaveOptions
    pdfSaveOpt.SetSecurityOptions(securityOptions);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(outDir + u"outFile.pdf", pdfSaveOpt);

    std::cout << "Workbook saved to PDF format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Экспорт пользовательских свойств в PDF**

С классом [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) вы можете экспортировать пользовательские свойства исходной книги в PDF. Для указания способа экспорта свойств предоставляется перечислитель [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/). Эти свойства можно просматривать в Adobe Acrobat Reader, нажав файл и выбрав свойства, как показано на следующем изображении. Шаблон файла «sourceWithCustProps.xlsx» можно скачать [здесь](sourceWithCustProps.xlsx) для тестирования, а выходной PDF-файл «outSourceWithCustProps» доступен [здесь](outSourceWithCustProps.pdf) для анализа.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load excel file containing custom properties
    U16String inputFilePath(u"sourceWithCustProps.xlsx");
    Workbook workbook(inputFilePath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set CustomPropertiesExport property to PdfCustomPropertiesExport::Standard
    pdfSaveOptions.SetCustomPropertiesExport(PdfCustomPropertiesExport::Standard);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    U16String outputFilePath(u"outSourceWithCustProps.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Атрибуты преобразования**

Мы работаем над улучшением функций преобразования с каждым новым выпуском. Преобразование Excel в PDF с помощью Aspose.Cells все еще имеет некоторые ограничения. MapChart не поддерживается при конвертации в формат PDF. Также некоторые объекты рисования не поддерживаются хорошо.

Следующая таблица перечисляет все функции, которые полностью или частично поддерживаются при экспорте в PDF с использованием Aspose.Cells. Эта таблица не является окончательной и не охватывает все атрибуты таблицы, но выявляет те функции, которые не поддерживаются или частично поддерживаются при конвертации в PDF.

| **Элемент документа** | **Атрибут** | **Поддерживается** | **Примечания** |
| :- | :- | :- | :- |
| Выравнивание |  | Да |  |
| Настройки фона |  | Да |  |
| Граница | Цвет | Да |  |
| Граница | Стиль линии | Да |  |
| Граница | Толщина линии | Да |  |
| Данные ячейки |  | Да |  |
| Комментарии |  | Да |  |
| Условное форматирование |  | Да |  |
| Свойства документа |  | Да |  |
| Объекты рисования |  | Частично | Тени и 3D-эффекты для объектов рисования не поддерживаются хорошо; WordArt и SmartArt частично поддерживаются. |
| Шрифт | Размер | Да |  |
| Шрифт | Цвет | Да |  |
| Шрифт | Стиль | Да |  |
| Шрифт | Подчеркивание | Да |  |
| Шрифт | Эффекты | Да |  |
| Изображения |  | Да |  |
| Гиперссылка |  | Да |  |
| Диаграммы |  | Частично | MapChart не поддерживается. |
| Объединенные ячейки |  | Да |  |
| Разрыв страницы |  | Да |  |
| Настройка страницы | Верхний/нижний колонтитул | Да |  |
| Настройка страницы | Поля | Да |  |
| Настройка страницы | Ориентация страницы | Да |  |
| Настройка страницы | Размер страницы | Да |  |
| Настройка страницы | Область печати | Да |  |
| Настройка страницы | Заголовки печати | Да |  |
| Настройка страницы | Масштабирование | Да |  |
| Высота строки/ширина столбца |  | Да |  |
| Связь с RTL (слева направо) языком |  | Да |  |

{{% alert color="primary" %}}

Если в вашей таблице есть формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) перед преобразованием таблицы в PDF. Это обеспечит перерасчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}

## **Продвинутые темы**
- [Добавление закладок PDF с именованными местами назначения](/cells/ru/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Изменить шрифт только для определенных символов Unicode при сохранении в формате PDF](/cells/ru/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Преобразовать файл XLSX в формат PDF](/cells/ru/cpp/convert-xlsx-file-to-pdf-format/)
- [Преобразование файла Excel в формат PDF, совместимый с PDFA-1a](/cells/ru/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Преобразовать файл XLS с изображениями или диаграммами в формат PDF](/cells/ru/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Создание PdfBookmarkEntry для листа с диаграммой](/cells/ru/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Заполнить все столбцы листа Excel на одной странице PDF](/cells/ru/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Получить DrawObject и Bound при преобразовании в формат PDF с использованием класса DrawObjectEventHandler](/cells/ru/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Получить предупреждения о замене шрифта при преобразовании файла Excel](/cells/ru/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Игнорировать ошибки при преобразовании Excel в PDF](/cells/ru/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Ограничение количества создаваемых страниц - Преобразование Excel в PDF](/cells/ru/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Печать комментариев при сохранении в формат PDF](/cells/ru/cpp/print-comments-while-saving-to-pdf/)
- [Рендеринг офисных надстроек при преобразовании Excel в PDF](/cells/ru/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Отображать одну страницу PDF для каждого листа Excel - Преобразование Excel в PDF](/cells/ru/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells](/cells/ru/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Добавление изображений с изменением размера - Преобразование Excel в PDF](/cells/ru/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Сохранить каждый лист в отдельный файл PDF](/cells/ru/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Сохранить Excel в PDF с обычным или минимальным размером](/cells/ru/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Сохранить указанные листы в формат PDF](/cells/ru/cpp/save-specified-worksheets-to-pdf/)
- [Защищенные документы в формате PDF](/cells/ru/cpp/secure-pdf-documents/)
- [Указание способа пересечения строк в выходном PDF и изображении](/cells/ru/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
