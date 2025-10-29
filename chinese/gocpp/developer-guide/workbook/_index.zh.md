---
title: 通过C++使用Golang管理工作簿
linktitle: 工作簿
type: docs
weight: 60
url: /zh/go-cpp/managing-workbooks-and-worksheets/
description: 学习如何通过Aspose.Cells for C++ API管理工作簿。
keywords: 如何用C++管理工作簿，管理工作簿和工作表，操作工作簿和工作表。
---

{{% alert color="primary" %}}

Aspose.Cells for C++提供了强大而灵活的API用于管理工作簿和工作表。本节介绍如何创建、打开和编程操作工作簿和工作表。

{{% /alert %}}

## **创建新工作簿**
创建新工作簿：

1. 创建一个[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类的实例。
2. 使用[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)类添加工作表到工作簿中。
3. 使用[Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/)方法保存工作簿。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook.go" >}}
## **打开已存在的工作簿**
打开已存在的工作簿：

1. 创建一个[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类的实例并传入文件路径作为构造参数。
2. 使用[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)类访问工作表。
3. 根据需要修改工作簿。
4. 使用[Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/)方法保存工作簿。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-1.go" >}}
## **管理工作表**
Aspose.Cells for C++ 提供了多种管理工作表的方法，包括添加、删除和重命名工作表。

### **添加工作表**
添加新工作表：

1. 从工作簿中访问[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)。
2. 使用[Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_sheettype/)方法添加新的工作表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-2.go" >}}
### **删除工作表**
删除工作表：

1. 从工作簿中访问[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)。
2. 使用[RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat_string/)方法根据索引移除工作表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-3.go" >}}
### **重命名工作表**
重命名工作表：

1. 从工作簿中访问[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)类。
2. 使用[SetName](https://reference.aspose.com/cells/go-cpp/worksheet/setname/)方法重命名工作表。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Workbook-4.go" >}}
## **结论**
Aspose.Cells for C++ 提供了全面的工作簿和工作表管理工具。无论您需要创建新工作簿、打开现有工作簿或操作工作表，Aspose.Cells 都能轻松实现编程操作。
