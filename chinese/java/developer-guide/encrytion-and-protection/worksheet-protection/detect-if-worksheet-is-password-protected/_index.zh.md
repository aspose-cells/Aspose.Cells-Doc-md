---
title: 检测工作表是否受密码保护
type: docs
weight: 280
url: /zh/java/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但是，电子表格本身可能会或可能不会受到保护。 Aspose.Cells API 提供了检测给定工作表是否受密码保护的方法。本文演示了使用 Aspose.Cells for Java API 来实现相同的目的。

{{% /alert %}}

## **检测工作表是否受密码保护**

Aspose.Cells for Java 8.7.0暴露了[**保护.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)属性来检测工作表是否受密码保护。布尔型[**保护.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)现场回报**真的**如果[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)受密码保护并且**错误的**如果不。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
