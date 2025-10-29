---
title: 使用C++调整工作簿压缩级别
linktitle: 调整工作簿压缩级别
type: docs
weight: 180
url: /zh/cpp/adjust-workbook-compression-level/
description: 学习如何使用Aspose.Cells for C++调整工作簿的压缩级别以优化文件大小和处理时间。
---

## **调整工作簿压缩级别**

开发人员在处理较大的工作簿时可以调整工作簿的压缩级别。 开发人员可以优先考虑较小的文件大小，也可以优先考虑处理时间。 Aspose.Cells 提供了一个枚举 [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/)，您可以用它来设置工作簿的压缩级别。 [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) 枚举提供以下成员。

- Level1：最快但效果最差的压缩。
- Level2：比级别1稍慢，但更好。
- Level3: 稍慢于级别2，但更好。
- Level4: 稍慢于级别3，但更好。
- Level5: 比级别4略慢，但压缩效果更好。
- Level6: 速度和压缩效率的良好平衡。
- Level7: 压缩效果相当不错！
- Level8: 比Level7压缩更好！
- Level9: "最佳"压缩，指的是数据流大小降低最多。也是最慢的压缩。

以下代码片段演示了使用 [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) 枚举，并比较了 Level1、Level6 和 Level9 的转换时间。 您还可以比较生成文件的大小。

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
