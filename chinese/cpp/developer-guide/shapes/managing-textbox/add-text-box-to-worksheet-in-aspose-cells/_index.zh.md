---
title: 如何用C++向工作表添加/插入文本框
linktitle: 在工作表中添加文本框
type: docs
weight: 10
url: /zh/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: 如何在Aspose.Cells中用C++向工作表添加/插入文本框。
keywords: 在Aspose中向Excel工作表添加/插入文本框
---

在Excel中的工作表中添加文本框

在Excel（版本07及以上）中，有两个地方可以插入文本框。一个是在"插入-形状"中，另一个在“插入”选项的顶端菜单右侧。

### 方法一：

![1](1.png)

### 方法二：

![2](2.png)

## 如何创建

您可以创建水平或垂直文本框。

- 选择相应的选项（横向或纵向）
- 在页面上单击左键
- 按住左键并在页面上拖动一段距离
- 释放左键

现在您可以获得一个文本框。

## 在Aspose.Cells中的工作表中添加文本框

当你需要批量插入文本框到工作表时，手动插入方法显然是一场灾难。如果这让你困扰，我认为这份文档会帮到你。[Aspose.Cells](https://products.aspose.com/cells/) 为你提供了一个API，便于在代码中实现批量插入。

以下示例代码创建一个文本框。

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

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

你将获得一个类似 [结果文件](result.xlsx) 的文件。在文件中，你会看到以下内容：

![](52449.png)
