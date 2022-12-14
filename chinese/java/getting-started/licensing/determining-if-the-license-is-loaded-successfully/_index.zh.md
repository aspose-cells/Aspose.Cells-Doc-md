---
title: 判断License是否加载成功
type: docs
weight: 210
url: /zh/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

Aspose.Cells提供[**工作簿.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)可用于确定许可证是否成功加载的属性。如果在设置license之前调用该方法，返回false，如果在设置license之后调用该方法，返回true表示license加载成功。

{{% /alert %}}

## **判断License是否加载成功**

以下代码访问[**工作簿.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)设置许可证之前的方法，它返回 false。然后它加载许可证并再次访问现在返回 true 的属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **控制台输出**

这是上面示例代码的控制台输出

{{< highlight "java" >}}

false

true

{{< /highlight >}}
