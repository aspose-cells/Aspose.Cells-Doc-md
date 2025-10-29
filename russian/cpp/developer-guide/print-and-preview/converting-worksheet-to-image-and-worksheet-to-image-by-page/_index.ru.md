---
title: Преобразование листа в изображение и листа в изображение по страницам с C++
linktitle: Преобразование листа в изображение и Лист в изображение по странице
type: docs
weight: 80
url: /ru/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Узнайте, как преобразовать лист в изображение, а также лист с несколькими страницами — в изображение по каждой странице с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Этот документ предназначен для предоставления разработчикам подробного понимания того, как конвертировать лист в изображение, а также лист с несколькими страницами — в изображения по страницам.

Иногда может потребоваться представить рабочие листы в виде изображений, например, для использования их в приложениях или веб-страницах. Возможно, вам понадобится вставить изображения в документ Word, файл PDF, презентацию PowerPoint или использовать их в другом сценарии. Просто говоря, вам нужно отобразить рабочий лист в виде изображения. Aspose.Cells поддерживает преобразование рабочих листов в файлы изображений Microsoft Excel. Также Aspose.Cells поддерживает преобразование рабочей книги в несколько файлов изображений, по одному на страницу.

Вы можете использовать Office Automation для этого, однако у автоматизации Office есть свои недостатки. Есть несколько причин и проблем: например, безопасность, стабильность, масштабируемость/скорость, цена и функции. В кратце, причин много, и основная — то, что Microsoft сам настоятельно не рекомендует использовать Office Automation.

{{% /alert %}}

## **Использование Aspose.Cells для преобразования листа в файл изображения**

В этой статье показано, как создать консольное приложение в Visual Studio, преобразовать рабочий лист в изображение и преобразовать рабочий лист в одно изображение для каждого рабочего листа с помощью нескольких простейших строк кода, используя API Aspose.Cells.

Вам нужно включить пространство имен [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) в вашей программе/проекте. Он содержит несколько полезных классов, таких как [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) и так далее. Класс [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) представляет лист для отображения изображений листа и имеет перегруженный метод [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), который может напрямую сохранить лист в виде файлов изображений с любыми заданными атрибутами или настройками. Он возвращает объект `System.Drawing.Bitmap`, и вы можете сохранить файл изображения на диск/поток. Поддерживаются различные форматы изображений, например BMP, PNG, GIF, JPG, JPEG, TIFF, EMF и другие.

В этой статье объясняется, как:

- Преобразовать рабочий лист в изображение
- Преобразовать каждую страницу в рабочем листе в изображение

Это задача показывает, как использовать Aspose.Cells для преобразования рабочего листа из шаблонной рабочей книги в файл изображения.

### **Установка проекта**

1. Сначала [скачайте Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Установите его на вашем компьютере для разработки. Все компоненты [Aspose](http://www.aspose.com/), при установке, работают в режиме оценки. Этот режим не ограничен по времени и только вставляет водяные знаки в создаваемые документы. Теперь запустите Visual Studio и создайте новое консольное приложение. В данном примере используется консольное приложение на C++. Добавьте ссылку на Aspose.Cells в созданный проект.

### **Преобразовать рабочий лист в файл изображения**

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook.xlsx** (1 рабочий лист). Затем преобразуйте рабочий лист шаблона в файл изображения под названием SheetImage.jpg.

Ниже приведен используемый компонентом код для выполнения этой задачи. Он преобразует Sheet1 в **Testbook.xlsx** в файл изображения, чтобы показать, насколько легко осуществляется это преобразование.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Использование Aspose.Cells для преобразования листа в изображение по страницам**

В этом примере показано, как использовать Aspose.Cells для преобразования листа из шаблонной книги, которая содержит несколько страниц, в один файл изображения на каждой странице.

### **Конвертация листа в изображение по страницам**

Я создал новую рабочую книгу в Microsoft Excel и добавил некоторые данные в первый рабочий лист: **Testbook2.xlsx** (1 рабочий лист).

Теперь преобразуйте рабочий лист шаблона Sheet1 в файлы изображений (по одному файлу на страницу). Поскольку я уже создал консольное приложение для выполнения этой задачи, я пропущу шаги создания этого консольного приложения и перейду непосредственно к шагам преобразования рабочего листа.

Следующий код используется компонентом для выполнения задачи. Он конвертирует Sheet1 из Testbook2.xlsx в файлы изображений по страницам.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
