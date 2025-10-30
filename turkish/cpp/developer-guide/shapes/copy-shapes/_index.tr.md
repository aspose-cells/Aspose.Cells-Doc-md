---
title: Çalışma Sayfaları Arasında Şekil Kopyalama C++ ile
linktitle: Şekilleri Kopyalama
type: docs
weight: 200
url: /tr/cpp/copy-shapes-between-worksheets/
description: Aspose.Cells kullanarak çalışma sayfaları arasında şekil, grafik ve diğer çizim nesnelerini nasıl kopyalayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen, bir çalışma sayfasındaki öğeleri, örneğin resimler, grafikler ve diğer çizim nesnelerini, diğer çalışma sayfalarına kopyalamanız gerekebilir. Aspose.Cells bu özelliği destekler. Grafikler, resimler ve diğer nesneler en yüksek hassasiyetle kopyalanabilir.

Bu makale, çalışsayfalar arasında şekillerin nasıl kopyalanacağı konusunda size detaylı bir anlayış sağlar.

{{% /alert %}}

## **Bir Resmi Bir Çalışsayfasından Başka Birine Kopyalama**

Bir resmi bir çalışsayfasından diğerine kopyalamak için aşağıdaki örnek kodda gösterildiği gibi [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) yöntemini kullanın.

```cpp
#include <iostream>
#include <memory>
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PictureCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Picture from the "Picture" worksheet
    Worksheet pictureSheet = workbook.GetWorksheets().Get(u"Picture");
    Picture picturesource = pictureSheet.GetPictures().Get(0);

    // Get picture data
    Vector<uint8_t> pictureData = picturesource.GetData();

    // Copy the picture to the Result Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetPictures().Add(picturesource.GetUpperLeftRow(), picturesource.GetUpperLeftColumn(), pictureData, picturesource.GetWidthScale(), picturesource.GetHeightScale());

    // Save the Worksheet
    workbook.Save(outputFilePath);

    std::cout << "Picture copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bir Grafik Bir Çalışsayfasından Diğerine Kopyalama**

Aşağıdaki kod, bir çalışsayfasından diğerine bir grafik kopyalamak için [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) yönteminin kullanımını göstermektedir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Chart from the "Chart" worksheet
    Worksheet chartSheet = workbook.GetWorksheets().Get(u"Chart");
    Chart chartSource = chartSheet.GetCharts().Get(0);

    // Get the ChartShape object
    ChartShape cshape = chartSource.GetChartObject();

    // Copy the Chart to the "Result" Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(cshape, 20, 0, 2, 0);

    // Save the Workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Denetimleri ve Diğer Çizim Nesnelerini Bir Çalışsayfasından Diğerine Kopyalama**

Kontroller ve diğer çizim nesnelerini kopyalamak için, aşağıdaki örnekte gösterildiği gibi [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcopy/) yöntemini kullanın.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample2.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ControlsCopied_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Shapes from the "Control" worksheet
    Worksheet controlSheet = workbook.GetWorksheets().Get(u"Control");
    ShapeCollection shapes = controlSheet.GetShapes();

    // Copy the Textbox to the Result Worksheet
    Worksheet resultSheet = workbook.GetWorksheets().Get(u"Result");
    resultSheet.GetShapes().AddCopy(shapes.Get(0), 5, 0, 2, 0);

    // Copy the Oval Shape to the Result Worksheet
    resultSheet.GetShapes().AddCopy(shapes.Get(1), 10, 0, 2, 0);

    // Save the Worksheet
    workbook.Save(outputFilePath);

    std::cout << "Shapes copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
