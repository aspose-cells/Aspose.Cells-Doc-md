---
title: 用C++获取或设置嵌入OLE对象的类标识符
linktitle: 获取或设置嵌入式OLE对象的类标识符
type: docs
weight: 200
url: /zh/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: 学习如何使用Aspose.Cells和C++获取或设置嵌入OLE对象的类标识符。
---

## **可能的使用场景**
Aspose.Cells提供了[OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/)属性，可用于获取或设置嵌入OLE对象的类标识符。OLE对象类标识符实际上是GUID（全局唯一标识符）。GUID总长度为16字节，因此类别标识符也是16字节长。它们通常在Windows注册表中找到，向宿主应用程序提供有关如何打开包含各种嵌入资源的OLE对象的信息。

## **获取或设置嵌入的OLE对象的类标识符**
下图显示了从[示例Excel文件](5115190.xls)中读取的OLE对象类别标识符（GUID），该文件包含嵌入的PowerPoint OLE对象。

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **示例代码**
请参见执行以下示例代码的结果，使用[示例Excel文件](5115190.xls)，其控制台输出显示了OLE对象的类别标识符（即GUID）。打印的GUID与截图中的完全相同。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **控制台输出**
这是上述样本代码执行时与[示例excel文件](5115190.xls)一起的控制台输出。

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
