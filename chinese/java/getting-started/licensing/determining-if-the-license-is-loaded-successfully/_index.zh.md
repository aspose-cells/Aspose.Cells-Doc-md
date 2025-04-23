---
title: 判断许可证是否成功加载
type: docs
weight: 210
url: /zh/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)属性，您可以使用它来确定许可证是否成功加载。如果您在设置许可证之前调用此方法，它将返回false，如果您在设置许可证之后调用此方法，它将返回true，表示许可证已成功加载。

{{% /alert %}}

## **确定许可证是否成功加载**

以下代码在设置许可证之前访问[**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)方法并返回false。然后加载许可证并再次访问属性，此时返回true。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **控制台输出**

这是上述示例代码的控制台输出

{{< highlight java >}}

false

true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
