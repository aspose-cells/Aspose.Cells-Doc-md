---
title: 使用C++在共享工作簿中更新保存历史记录的天数
linktitle: 在共享工作簿中保留修订日志的更新日志
type: docs
weight: 80
url: /zh/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: 学习如何使用Aspose.Cells的C++ API更新共享工作簿中保存历史的天数。
---

## **可能的使用场景**

当您分享一个工作簿时，您会得到一个选项***保留N天的更改历史***，如下截图所示。您可以使用Aspose.Cells的[**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/)属性来更新保留历史的天数。

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **在共享工作簿中保留修订日志的更新日志**

以下示例代码创建一个空白工作簿，然后共享它并将修订日志天数修改为7天，通常是30天。请参考代码生成的[输出Excel文件](60489773.xlsx)。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
