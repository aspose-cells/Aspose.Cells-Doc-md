---
title: 通过Golang用C++自动刷新Microsoft Excel中的OLE对象
linktitle: 自动刷新 OLE 对象
type: docs
weight: 270
url: /zh/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: 了解如何使用Golang通过C++用Aspose.Cells在Microsoft Excel中自动刷新OLE对象。
---

{{% alert color="primary" %}}

Aspose.Cells 提供了 [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) 属性，用于在在 Microsoft Excel 中打开文件时刷新 OLE 对象。借助此属性，OLE 对象将显示由 Microsoft Excel 生成的正确的 OLE 图像。

{{% /alert %}}

以下示例代码加载了带有非真实OLE图像的[示例Excel文件](5115231.xlsx)。OLE对象实际上是Microsoft Word文档，但示例Excel文件显示的动物图像而非Microsoft Word图像。不过，如果你打开[输出Excel文件](5115225.xlsx)，会看到Microsoft Excel显示了正确的OLE图像。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
