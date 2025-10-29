---
title: 用C++将XLSB修订转为XLSM
linktitle: 将XLSB文件的修订版本转换为XLSM
type: docs
weight: 290
url: /zh/cpp/convert-revision-of-xlsb-to-xlsm/
description: 学习如何用Aspose.Cells将XLSB文件的修订转换为XLSM格式。
---

{{% alert color="primary" %}} 

Aspose.Cells现已支持将XLSB文件中的修订完整转换为XLSM文件。修订存放在路径\xl\revisions中。通过更改XLSB文件扩展名为ZIP即可查看。路径\xl\revisions包含以.bin结尾的文件。

当你用Aspose.Cells将XLSB文件转换为XLSM文件时，这些.bin文件会成功转换为.xml文件，这在两个截图中有所显示。

{{% /alert %}} 

以下代码示例演示了如何用Aspose.Cells将XLSB文件转换为XLSM格式。

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
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
