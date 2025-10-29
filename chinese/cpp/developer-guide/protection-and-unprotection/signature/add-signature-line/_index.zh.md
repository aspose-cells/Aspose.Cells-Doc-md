---
title: 使用C++向工作表添加签名行
linktitle: 添加签名行
type: docs
weight: 200
url: /zh/cpp/add-signature-line/
description: 本文介绍如何使用C++代码结合Aspose.Cells for C++向工作表添加签名行。
keywords: 向工作表添加签名行，如何向工作表添加签名行，如何向工作表添加签名行，如何向工作表添加签名行。
---

## **介绍**

Aspose.Cells 提供了 [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) 属性来添加工作表的签名行。

## **如何向工作表添加签名行**

 以下示例代码演示了如何使用 [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) 属性在工作表中添加签名行。截图显示了执行后示例代码对示例Excel文件的效果。

![todo:image_alt_text](add-signature-line.png)

## **示例代码**

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb;

    SignatureLine signatureLine;
    signatureLine.SetSigner(u"Aspose.Cells");
    signatureLine.SetTitle(u"signed by Aspose.Cells");

    wb.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, signatureLine);

    U16String certificatePath = srcDir + u"rsa2048.pfx";
    U16String password = u"123456";

    std::time_t now = std::time(nullptr);
    struct tm now_tm;
    localtime_s(&now_tm, &now);

    Date currentDate{
        now_tm.tm_year + 1900,
        now_tm.tm_mon + 1,
        now_tm.tm_mday,
        now_tm.tm_hour,
        now_tm.tm_min,
        now_tm.tm_sec,
        0
    };

    DigitalSignature signature(certificatePath, password, u"test Microsoft Office signature line", currentDate);

    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);

    wb.SetDigitalSignature(dsCollection);

    U16String outputPath = srcDir + u"signatureLine.xlsx";
    wb.Save(outputPath);

    std::cout << "Workbook with signature line saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
