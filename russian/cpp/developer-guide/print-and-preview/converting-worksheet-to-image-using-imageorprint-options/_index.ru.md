---
title: Конвертация листа в изображение с помощью ImageOrPrintOptions и C++
linktitle: Конвертация листа в изображение
type: docs
weight: 90
url: /ru/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Узнайте, как конвертировать лист в файл изображения и применять различные параметры изображения и печати с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Этот документ предназначен для предоставления подробного понимания того, как конвертировать лист в файл изображения и применять различные параметры изображения и печати, такие как разрешение, сжатие TIFF, формат изображения и качество страницы.

{{% /alert %}}

## **Сохранение листов в изображения - различные подходы**

Иногда вам может понадобиться представить ваши рабочие листы в виде графического изображения. Возможно, вам нужно вставить изображения рабочих листов в ваши приложения или веб-страницы, вставить их в документ Word, PDF-файл, презентацию PowerPoint или использовать в других сценариях. Проще говоря, вы хотите, чтобы рабочий лист был отображен как изображение, чтобы использовать его в других местах. Aspose.Cells поддерживает преобразование рабочих листов в файлы изображений. Кроме того, Aspose.Cells поддерживает настройку различных параметров, таких как формат изображения, разрешение (по вертикали и горизонтали), качество изображения и другие параметры изображения и печати.

Вы можете рассмотреть использование автоматизации Office, однако у этого есть свои недостатки. Есть несколько причин и проблем, таких как безопасность, стабильность, масштабируемость, скорость, цена и функциональность. В кратце, существует множество причин, начиная с того, что сама Microsoft настоятельно не рекомендует автоматизацию Office из программных решений.

Эта статья показывает, как создать консольное приложение в Visual Studio, выполнить преобразование рабочего листа в изображение, используя различные параметры изображения и печати с помощью API Aspose.Cells.

Вам нужно включить пространство имен [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) в вашу программу/проект. Оно содержит несколько полезных классов, например, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) и так далее.

Класс [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) представляет рабочий лист для отображения изображений этого листа. Он имеет перегруженный метод [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), который может напрямую преобразовать рабочий лист в файл(ы) изображения, указав желаемые атрибуты или параметры. Он может возвращать объект Bitmap, а также сохранять изображение на диск или поток. Поддерживаются различные форматы изображений, такие как BMP, PNG, GIF, JPEG, TIFF, EMF и другие.

## **Использование Aspose.Cells для преобразования рабочего листа в изображение с помощью ImageOrPrint Опций**

### **Создание шаблонной рабочей книги в Microsoft Excel**

Я создал новую рабочую книгу в MS Excel и добавил некоторые данные в первый рабочий лист. Теперь я конвертирую рабочий лист “Sheet1” этой шаблонной книги в файл изображения “SheetImage.tiff” и применяю различные изображения, такие как горизонтальные и вертикальные разрешения, сжатие Tiff и другие.

### **Загрузите и установите Aspose.Cells**

Сначала необходимо [скачать](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. Установите его на ваш компьютер для разработки. Все компоненты [Aspose](http://www.aspose.com/) при установке работают в режиме оценки. Режим оценки не имеет временных ограничений и только вставляет водяные знаки в создаваемые документы.

### **Создайте проект**

Запустите Visual Studio и создайте новое консольное приложение. Этот пример покажет C++ консольное приложение.

### **Добавьте ссылки**

Этот проект будет использовать Aspose.Cells. Поэтому необходимо добавить ссылку на компонент Aspose.Cells в ваш проект. Например, добавьте ссылку на `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **Преобразование рабочего листа в файл изображения**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Опции конвертации**

Можно сохранить определенные страницы в виде изображения. Следующий код преобразует первый и второй рабочие листы книги в изображения JPG.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Преобразование изображений с помощью WorkbookRender**

TIFF изображение может содержать более одного кадра. Вы можете сохранить всю книгу как один TIFF-файл с несколькими кадрами или страницами:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
