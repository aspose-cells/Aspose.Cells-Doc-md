---
title: رسم بياني إلى صورة باستخدام C++
linktitle: تحويل الرسم البياني إلى صورة
type: docs
weight: 46
url: /ar/cpp/chart-to-image/
description: تعلم كيفية استخدام Aspose.Cells for C++ لتحويل رسم بياني إلى تنسيق صورة، مثل JPEG أو PNG. سيرينا دليلنا كيفية تصدير رسم بياني من مايكرسوفت إكسل وحفظه كصورة مستقلة للاستخدام والمعالجة لاحقًا.
keywords: Aspose.Cells for C++، رسم بياني إلى صورة، مايكرسوفت إكسل، تحويل الصورة، تصدير، صورة مستقلة.
---

## **عرض الرسوم البيانية**

يدعم واجهات برمجة التطبيقات Aspose.Cells تحويل مخططات إكسل إلى تنسيقات صور بدون الحاجة إلى أدوات أو تطبيقات إضافية. لدعم التصيير، أتاح فصل [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) طرقًا مع تحميلات متعددة لتلبية متطلبات التطبيق بشكل أفضل.

### **عرض الرسوم البيانية كصور**

 طريقة [**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) لديها مجموعة متنوعة من التحميلات لدعم التصيير البسيط والمتقدم. إذا كان متطلب التطبيق هو تصيير المخطط بأبعاده الافتراضية، نوصي باستخدام طريقة [**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) كما يلي.

```c++
#include <iostream>
#include <fstream>
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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to image
    chart.ToImage(outDir + u"chartEMF_out.emf", ImageType::Emf);

    // Convert chart to Bitmap
    chart.ToImage(outDir + u"chartBMP_out.bmp", ImageType::Bmp);

    std::cout << "Chart converted to images successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

كما يمكن أيضًا تصيير الرسوم البيانية إلى صور بإعدادات متقدمة. لقد وفرت واجهات برمجة التطبيقات Aspose.Cells نسخة تحميل مفرطة من أسلوب [**Chart.ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/toimage/) التي تقبل نسخة من [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)، مما يتيح لك تحديد معلمات مثل الدقة، وضع التنعيم، تنسيق الصورة، وغيرها.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int32_t sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Get the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Create an instance of ImageOrPrintOptions and set a few properties
    ImageOrPrintOptions options;
    options.SetVerticalResolution(300);
    options.SetHorizontalResolution(300);

    // Convert chart to image with additional settings
    chart.ToImage(outDir + u"chartPNG_out.png", options);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **أنواع الرسوم البيانية المدعومة للعرض**

هناك بعض أنواع الرسوم البيانية التي لا تتم دعمها حاليًا للعرض. تحتوي مثل هذه الأنواع على **N** في العمود **مدعوم** للجدول أدناه.

|**نوع الرسم البياني**|**نوع الفرعي للرسم البياني**|**مدعوم**|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

في حال حاولت تصيير أنواع الرسوم البيانية غير المدعومة إلى صورة أو PDF، قد تتلقى صورًا بحجم 0 أو PDF فارغ.

{{% /alert %}}

## **مواضيع متقدمة**
- [تحويل الرسم البياني إلى PDF](/cells/ar/cpp/chart-to-pdf/)
