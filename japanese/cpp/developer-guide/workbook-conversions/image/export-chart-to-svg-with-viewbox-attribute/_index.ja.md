---
title: viewBox属性を持つSVGへのエクスポートチャート（C++使用）
linktitle: viewBox属性を使用してチャートをSVG形式にエクスポート
type: docs
weight: 280
url: /ja/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.CellsとC++を使用してviewBox属性を持つSVG形式にチャートをエクスポートします。
---

{{% alert color="primary" %}}

デフォルトでは、チャートをSVG形式にエクスポートするとき、そのXMLには**viewBox**属性が含まれません。しかし、Aspose.Cellsは、**true**に設定された場合に**viewBox**属性でチャートをSVG形式でエクスポートする[**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/)プロパティを提供します。

{{% /alert %}}

## viewBox属性を含むSVG形式でチャートをエクスポート

次のコードサンプルは、viewBox属性を含むSVG形式でチャートをエクスポートします。

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

    // Create workbook object from source file
    U16String sampleChartBook = srcDir + u"SampleChartBook.xlsx";
    Workbook workbook(sampleChartBook);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options with SVGFitToViewPort true
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Svg);
    opts.SetSVGFitToViewPort(true);

    // Save the chart to svg format
    U16String outputSvg = srcDir + u"Image_out.svg";
    chart.ToImage(outputSvg, opts);

    std::cout << "Chart saved successfully in SVG format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

チャートのSVGをNotepadで開くと、次のような**viewBox**属性が見つかります。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
