---
title: 确定许可证是否成功加载
type: docs
weight: 260
url: /zh/net/determining-if-the-license-is-loaded-successfully/
description: 通过Aspose.Cells for NET APIs学习如何检测许可证是否成功加载。
keywords: 如何在C#中检测许可证是否成功加载，使用C#确定许可证是否成功加载，通过C#检查许可证是否成功加载，检查许可证的状态。
---

{{% alert color="primary" %}}

Aspose.Cells提供了一个[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)属性，您可以用来确定许可证是否成功加载。如果您在设置许可证之前访问此属性，它将返回**false**，如果您在设置许可证后调用此属性，它将返回**true**，表示许可证已经成功加载。

{{% /alert %}}

## 用于确定许可证是否成功加载的C#代码

以下代码在设置许可证之前访问了[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)属性，返回**false**。然后加载许可证并再次访问属性，现在返回**true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **控制台输出**

以下是上面示例代码的控制台（调试）输出。

{{< highlight java >}}

False

True

{{< /highlight >}}
