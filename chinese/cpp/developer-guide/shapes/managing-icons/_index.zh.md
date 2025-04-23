---
title: 使用C++向工作表添加图标
linktitle: 管理图标
type: docs
weight: 100
url: /zh/cpp/insert-svg-to-excel/
description: 学习如何使用 Aspose.Cells 和 C++ 向 Excel 工作表添加图标。
---

## 在Aspose.Cells中向工作表添加图标

如果您需要使用[Aspose.Cells](https://products.aspose.com/cells/)在Excel文件中添加'图标'，那么本文档可以为您提供一些帮助。

对应于插入图标操作的Excel界面如下：

![](1.png)

- 选择要插入到工作表中的图标的位置
- 左键单击*插入*->*图标*
- 在打开的窗口中，选择上图中红色矩形所示的图标
- 左键单击 *插入*，它将被插入到Excel文件中。

效果如下:

![](2.png)

这里，我们准备了 *示例代码* 来帮助你使用 [Aspose.Cells](https://products.aspose.com/cells/) 插入图标。还包括必要的 [示例文件](sample.xlsx) 和图标 [资源文件](icon.zip)。我们使用Excel界面插入了一个图标，与 [资源文件](icon.zip) 在 [示例文件](sample.xlsx) 中具有相同的显示效果。

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

当您在项目中执行上述代码时，将获得以下结果:

![](3.png)
