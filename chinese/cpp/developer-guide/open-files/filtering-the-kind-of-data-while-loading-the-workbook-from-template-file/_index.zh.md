---
title: 用 C++ 过滤从模板文件加载工作簿时的数据类型
linktitle: 加载工作簿时的过滤数据
type: docs
weight: 400
url: /zh/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: 学习如何在使用 Aspose.Cells 与 C++ 加载模板文件时，过滤特定的数据类型。
---

{{% alert color="primary" %}}

有时，您希望在从模板文件构建工作簿时指定要加载的数据类型。过滤加载的数据可以提升性能，特别是在使用 [LightCells APIs](/cells/zh/cpp/using-lightcells-api/) 时。请使用 [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) 属性实现此功能。

{{% /alert %}}

以下示例代码仅在从[模板文件](5115552.xlsx)加载工作簿时加载形状对象，您可以从给定链接下载模板文件。下面的屏幕截图显示了[模板文件](5115552.xlsx)的内容，并且解释了红色和黄色背景中的数据将不会被加载，因为[**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/)属性已设置为[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

下面的屏幕截图显示了您可以从给定链接下载的[输出PDF](5115555.pdf)。在这里，您可以看到红色和黄色背景中的数据不存在，但所有形状都在那里。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
