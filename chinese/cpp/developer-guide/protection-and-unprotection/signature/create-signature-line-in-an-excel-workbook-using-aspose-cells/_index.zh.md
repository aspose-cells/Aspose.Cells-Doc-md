---
title: 使用Aspose.Cells在C++中创建Excel工作簿中的签名行
linktitle: 在Excel工作簿中创建签名行
type: docs
weight: 150
url: /zh/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: 本文介绍如何使用C++代码结合Aspose.Cells for C++在Excel工作簿中创建签名行。
keywords: 在Excel工作簿中创建签名行，如何在Excel工作簿中创建签名行，如何添加签名行，如何向Excel文件添加签名行。
---

## **介绍**

Microsoft Excel提供了在Excel工作簿中添加 **签名行** 的功能。您可以通过单击 **插入** 选项卡，然后从 **文本** 组中选择 **签名行** 来添加签名行。

## **如何为Excel创建签名行**

Aspose.Cells也提供了这个功能，并为此暴露了 [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) 属性。本文将解释如何使用此属性来使用Aspose.Cells添加签名行。

以下示例代码使用 [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) 属性添加了一个签名行并保存了工作簿。

```cpp
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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
