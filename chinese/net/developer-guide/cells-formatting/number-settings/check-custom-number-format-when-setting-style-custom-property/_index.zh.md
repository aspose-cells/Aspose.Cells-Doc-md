---
title: 设置 Style.Custom 属性时检查自定义数字格式
type: docs
weight: 170
url: /zh/net/check-custom-number-format-when-setting-style-custom-property/
---
## **可能的使用场景**

如果您将无效的自定义数字格式分配给[**风格.定制**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)属性，则 Aspose.Cells 不会抛出任何异常。但是如果你想让 Aspose.Cells 检查指定的自定义号码格式是否有效，那么请设置[**工作簿.设置.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)财产给**真的**.

## **设置 Style.Custom 属性时检查自定义数字格式**

以下示例代码将无效的自定义数字格式分配给[**风格.定制**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)财产。因为，我们已经设定[**工作簿.设置.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)财产给**真的**，因此它会抛出异常，例如无效的数字格式。请阅读代码中的注释以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
