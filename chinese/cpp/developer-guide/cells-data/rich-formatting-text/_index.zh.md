---
title: 使用C++访问和修改单元格富文本部分
linktitle: 富格式文本
type: docs
weight: 40
url: /zh/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: 学习如何通过Aspose.Cells for C++ API访问和更新单元格富文本的部分内容。
keywords: 访问和更新单元格的富文本，获取单元格的富文本，编辑单元格的富文本，访问单元格的富文本，更新单元格的富文本，更改单元格的富文本
---

{{% alert color="primary" %}}

Aspose.Cells允许您访问和更新单元格的富文本的部分。为此，您可以使用[**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/)和[**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)方法。这些方法将返回并接受[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)对象数组，您可以使用它们来访问和更新字体的各种属性，如字体名称、字体颜色、粗体等。

{{% /alert %}}

## **访问和更新单元格的富文本部分**

以下代码展示了如何使用[源Excel文件](5112369.xlsx)的[**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/)和[**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/)方法。该文件中的A1单元格含有三个富文本部分，每个部分字体不同。代码访问这些部分，并将第一个部分的字体改为**"Arial"**。修改后，将工作簿保存为[输出Excel文件](5112366.xlsx)。

### C++代码示例：访问并更新富文本部分

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### 样本代码生成的控制台输出

使用[源Excel文件](5112369.xlsx)时的控制台输出：

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
