---
title: 用C++管理工作簿
linktitle: 工作簿
type: docs
weight: 60
url: /zh/cpp/managing-workbooks-and-worksheets/
description: 学习如何通过Aspose.Cells for C++ API管理工作簿。
keywords: 如何用C++管理工作簿，管理工作簿和工作表，操作工作簿和工作表。
---

{{% alert color="primary" %}}

Aspose.Cells for C++提供了强大而灵活的API用于管理工作簿和工作表。本节介绍如何创建、打开和编程操作工作簿和工作表。

{{% /alert %}}

## **创建新工作簿**
创建新工作簿：

1. 创建[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的实例。
2. 使用[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)类添加工作表。
3. 使用[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法保存工作簿。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **打开已存在的工作簿**
打开已存在的工作簿：

1. 创建[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的实例，传入文件路径作为构造参数。
2. 使用[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)类访问工作表。
3. 根据需要修改工作簿。
4. 使用[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法保存工作簿。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **管理工作表**
Aspose.Cells for C++ 提供了多种管理工作表的方法，包括添加、删除和重命名工作表。

### **添加工作表**
添加新工作表：

1. 从工作簿中访问 [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 类。
2. 使用 [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) 方法添加新工作表。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **删除工作表**
删除工作表：

1. 从工作簿中访问 [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 类。
2. 使用 [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) 方法通过索引删除工作表。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **重命名工作表**
重命名工作表：

1. 从工作簿中访问 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类。
2. 使用 [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) 方法重命名工作表。

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **结论**
Aspose.Cells for C++ 提供了全面的工作簿和工作表管理工具。无论您需要创建新工作簿、打开现有工作簿或操作工作表，Aspose.Cells 都能轻松实现编程操作。
{{< app/cells/assistant language="cpp" >}}
