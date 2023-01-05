---
title: 判断License是否加载成功
type: docs
weight: 260
url: /zh/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

Aspose.Cells提供[**工作簿.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)可用于确定许可证是否成功加载的属性。如果您在设置许可证之前访问此属性，它将返回**错误的**如果您在设置许可后调用此属性，它将返回**真的**表示许可证已成功加载。

{{% /alert %}}

## C# 判断License是否加载成功的代码

以下代码访问[**工作簿.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)设置许可证之前的财产，它返回**错误的**.然后它加载许可证并再次访问现在返回的属性**真的**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **控制台输出**

这是上述示例代码的控制台（调试）输出

{{< highlight "java" >}}

False

True

{{< /highlight >}}
