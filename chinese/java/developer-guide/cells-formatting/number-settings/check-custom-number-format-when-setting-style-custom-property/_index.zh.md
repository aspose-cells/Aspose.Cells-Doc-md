---
title: 在设置Style.Custom属性时检查自定义数字格式
type: docs
weight: 160
url: /zh/java/check-custom-number-format-when-setting-style-custom-property/
---

## **可能的使用场景**

如果将无效的自定义数字格式分配给[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)属性，则Aspose.Cells不会抛出任何异常。但是，如果您想要Aspose.Cells检查分配的自定义数字格式是否有效，则请将[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)属性设置为**true**。

## **设置Style.Custom属性时检查自定义数字格式**

以下示例代码将无效的自定义数字格式分配给[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)属性。由于已将[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)属性设置为**true**，因此API将抛出CellsException，例如*Invalid number format*。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
{{< app/cells/assistant language="java" >}}
