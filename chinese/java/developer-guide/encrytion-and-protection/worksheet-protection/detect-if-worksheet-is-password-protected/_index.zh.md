---
title: 检测工作表是否受密码保护
type: docs
weight: 280
url: /zh/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但电子表格本身可能受到保护或未受到保护。Aspose.Cells API提供了一种检测给定工作表是否受密码保护的方法。本文演示了使用Aspose.Cells for Java API实现相同功能。

{{% /alert %}}

## **检测工作表是否受密码保护**

Aspose.Cells for Java 8.7.0已公开了[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)属性，用于检测工作表是否受密码保护。布尔类型[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)字段返回**true**，如果[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)受到密码保护，返回**false**，如果没有。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
