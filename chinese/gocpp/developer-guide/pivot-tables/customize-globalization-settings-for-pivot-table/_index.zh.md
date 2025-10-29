---
title: 使用 C++ 和 Golang 自定义数据透视表的国际化设置
linktitle: 自定义数据透视表的全球化设置
type: docs
weight: 50
url: /zh/go-cpp/customize-globalization-settings-for-pivot-table/
description: 学习如何使用Aspose.Cells for C++自定义数据透视表的全球化设置。
---

## **可能的使用场景**

有时你想根据需要自定义*总计、子总计、总览、小计、多选项、列标签、行标签、空值*的文本。Aspose.Cells for C++允许你自定义数据透视表的全球化设置，以应对这些场景。你还能使用此功能将标签更改为阿拉伯语、印地语、波兰语等其他语言。

## **自定义数据透视表的全球化设置**

以下示例代码说明如何为 C++ 中的数据透视表自定义全球化设置。它创建一个派生自 [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) 基类的类 *CustomPivotTableGlobalizationSettings*，并重写所有必要的方法。这些方法返回各种数据透视表元素的自定义文本。然后，代码将此实现分配给 [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) 属性。示例加载一个 [源 Excel 文件](40468488.xlsx)，刷新数据透视表并保存为 [输出 PDF](40468487.pdf)。下方截图显示了输出中的自定义标签。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
