---
title: 设置 Style.Custom 属性时检查自定义数字格式
type: docs
weight: 160
url: /zh/java/check-custom-number-format-when-setting-style-custom-property/
---
## **可能的使用场景**

如果您将无效的自定义数字格式分配给[**风格.定制**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)property 那么 Aspose.Cells 将不会抛出任何异常。但是，如果您希望 Aspose.Cells 应该检查分配的自定义数字格式是否有效，请设置[**工作簿.设置.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)财产给**真的**.

## **设置 Style.Custom 属性时检查自定义数字格式**

以下示例代码将无效的自定义数字格式分配给[**风格.定制**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)财产。由于我们已经设置[**工作簿.设置.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)财产给**真的**，因此 API 将抛出 CellsException 例如*数字格式无效*.

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
