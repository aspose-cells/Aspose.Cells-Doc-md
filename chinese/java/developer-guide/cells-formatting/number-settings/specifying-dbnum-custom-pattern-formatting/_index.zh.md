---
title: 指定使用DBNum自定义模式格式
type: docs
weight: 170
url: /zh/java/specifying-dbnum-custom-pattern-formatting/
---

## **可能的使用场景**

Aspose.Cells 支持 *DBNum* 自定义模式格式。例如，如果您的单元格值为 123，并且您将其自定义格式指定为 [DBNum2][$-804]General，则它将显示为 壹佰贰拾叁。您可以使用 [**Cell.getStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) 和 [**Style.setCustom()**](https://reference.aspose.com/cells/java/com.aspose.cells/style/#setCustom-java.lang.String-) 方法指定单元格的自定义格式。

## **示例代码**

以下示例代码说明了如何指定*DBNum*自定义模式格式。请检查其[output PDF](43352082.pdf)了解更多帮助。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingDBNumCustomPatternFormatting.java" >}}
