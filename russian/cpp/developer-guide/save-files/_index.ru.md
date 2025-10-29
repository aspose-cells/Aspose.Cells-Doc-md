---
title: Различные способы сохранения файлов с помощью C++
linktitle: Сохранить файлы
type: docs
weight: 40
url: /ru/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ может сохранять файлы в различные форматы. Сохраняйте файлы в PDF. Сохраняйте файлы в HTML. Сохраняйте файлы в DOCX. Сохраняйте файлы в PPTX. Сохраняйте файлы в JSON. Сохраняйте файлы в MHTML.
keywords: Aspose.Cells сохраняет Excel в PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML и другие, используя C++, сохраняйте или конвертируйте рабочую книгу в PDF, HTML, JSON, TXT, SQL на C++
---

{{% alert color="primary" %}}

Aspose.Cells делает возможным создание и сохранение файлов. В этой статье объясняются различные способы сохранения файлов.

{{% /alert %}}

## **Различные способы сохранения файлов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel и обеспечивает необходимые свойства и методы для работы с файлами Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) предоставляет метод [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/), используемый для сохранения файлов Excel. Метод [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) имеет множество перегрузок, которые используются для сохранения файлов различными способами.

Формат файла, в который файл сохраняется, определяется перечислением [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)

|**Типы форматов файлов**|**Описание**|
| :- | :- |
|CSV|Представляет собой файл CSV|
|Excel97To2003|Представляет файл Excel 97 - 2003|
|Xlsx|Представляет файл Excel 2007 XLSX|
|Xlsm|Представляет файл Excel 2007 XLSM|
|Xltx|Представляет шаблон файла Excel 2007 XLTX|
|Xltm|Представляет макросов Excel 2007 XLTM|
|Xlsb|Представляет двоичный файл Excel 2007 XLSB|
|SpreadsheetML|Представляет файл XML электронной таблицы|
|TSV|Представляет собой файл значений, разделенных табуляцией|
|TabDelimited|Представляет файл текста с табуляцией|
|ODS|Представляет собой файл ODS|
|Html|Представляет файл(ы) HTML|
|MHtml|Представляет файл(ы) MHTML|
|Pdf|Представляет файл PDF|
|XPS|Представляет документ XPS|
|TIFF|Представляет файл формата Tagged Image File Format (TIFF)|

## **Как сохранить файл в разных форматах**

Для сохранения файлов в хранилище необходимо указать имя файла (с полным путем к хранилищу) и желаемый формат файла (из перечисления [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) при вызове метода [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объекта [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

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
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Как сохранить книгу в Pdf**
Формат портативного документа (PDF) - это тип документа, созданный Adobe еще в 1990 годах. Цель этого формата файла заключалась во введении стандарта для представления документов и других справочных материалов в формате, независимом от прикладного программного обеспечения, аппаратного обеспечения и операционной системы. Формат файла PDF обладает полной способностью содержать информацию, такую как текст, изображения, гиперссылки, форм-поля, мультимедийные элементы, цифровые подписи, вложения, метаданные, геопространственные объекты и 3D-объекты, которые могут стать частью исходного документа.

Следующие коды показывают, как сохранить книгу в формате PDF с помощью Aspose.Cells:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Как сохранить книгу в формате текста или CSV**

Иногда вам может потребоваться конвертировать или сохранить книгу с несколькими листами в текстовом формате. Для текстовых форматов (например, TXT, TabDelim, CSV и т. д.) как Microsoft Excel, так и Aspose.Cells по умолчанию сохраняют только содержимое активного листа.

В следующем примере кода объясняется, как сохранить всю книгу в текстовом формате. Загрузите исходную книгу, которая может быть любым файлом электронных таблиц Microsoft Excel или OpenOffice (например, XLS, XLSX, XLSM, XLSB, ODS и т. д.) с любым количеством листов.

При выполнении кода он преобразует данные всех листов рабочей книги в формат TXT

Вы можете изменить тот же пример, чтобы сохранить файл в формате CSV. По умолчанию, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) — запятая, поэтому не указывайте разделитель при сохранении в формате CSV. Обратите внимание: если вы используете тестовую версию и даже если свойство [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) установлено в true, программа все равно экспортирует только один лист.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Как сохранить файл в текстовые файлы с пользовательским разделителем**

Текстовые файлы содержат данные электронных таблиц без форматирования. Файл представляет собой своего рода обычный текстовый файл, который может содержать некоторые настраиваемые разделители между его данными.

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
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Как сохранить файл в поток**

Для сохранения файлов в поток создайте объект *MemoryStream* или *FileStream* и сохраните файл в этот объект потока, вызвав метод [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объекта объекта [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Укажите желаемый формат файла, используя перечисление [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) при вызове метода [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```

## **Как сохранить файл Excel в файлы Html и Mht**
Aspose.Cells просто может сохранить файл Excel, JSON, CSV или другие файлы, которые могут быть загружены Aspose.Cells, в файлы .html и .mht.
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
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Как сохранить файл Excel в форматы OpenOffice (ODS, SXC, FODS, OTS)**
Мы можем сохранить файлы в формате OpenOffice: ODS, SXC, FODS, OTS и т. д.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Как сохранить файл Excel в формат JSON или XML**

JSON (JavaScript Object Notation) – это открытый стандартный файловый формат для обмена данными, который использует удобочитаемый текст для хранения и передачи данных. JSON-файлы сохраняются с расширением .json. JSON требует меньше форматирования и является хорошей альтернативой XML. JSON происходит из JavaScript, но является независимым от языка форматом данных. Создание и разбор JSON поддерживается многими современными языками программирования. application/json – это тип медиа-формат, используемый для JSON.

Aspose.Cells поддерживает сохранение файлов в форматах JSON или XML.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Продвинутые темы**
- [Настройка уровня сжатия книги Excel](/cells/ru/cpp/adjust-workbook-compression-level/)
- [Сохранить книгу в формате Strict Open XML Spreadsheet](/cells/ru/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Сохранение файла в объект ответа](/cells/ru/cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="cpp" >}}
