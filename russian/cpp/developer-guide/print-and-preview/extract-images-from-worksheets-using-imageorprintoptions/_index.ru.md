---
title: Извлечение изображений из рабочих листов с помощью ImageOrPrintOptions и C++
linktitle: Извлечение изображений из рабочих листов
type: docs
weight: 140
url: /ru/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Узнайте, как извлекать изображения из рабочих листов Excel и сохранять их на локальный диск с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Пользователи Microsoft Excel могут добавлять изображения в электронные таблицы. С помощью Aspose.Cells можно читать изображения из файлов Microsoft Excel и сохранять их на локальный диск. В этой статье показано, как это сделать.

{{% /alert %}} 

Приведенный ниже образец кода показывает, как извлечь изображения из файла Excel и сохранить их.

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

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
