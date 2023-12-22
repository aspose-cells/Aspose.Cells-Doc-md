---
title: 判断License是否加载成功
type: docs
weight: 260
url: /zh/net/determining-if-the-license-is-loaded-successfully/
description: 了解如何通过 NET API 的 Aspose.Cells 检测许可证是否加载成功。
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells提供[**工作簿.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)您可以使用该属性来确定许可证是否已成功加载。如果您在设置许可证之前访问此属性，它将返回**错误的**如果您在设置许可证后调用此属性，它将返回**真的**表明License已加载成功。

{{% /alert %}}

##  C# 判断License是否加载成功的代码

以下代码访问[**工作簿.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)设置许可证之前的属性，它返回 *false**。然后它加载许可证并再次访问该属性，现在返回 *true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **控制台输出**

这是上述示例代码的控制台（调试）输出

{{< highlight "java" >}}

False

True

{{< /highlight >}}
