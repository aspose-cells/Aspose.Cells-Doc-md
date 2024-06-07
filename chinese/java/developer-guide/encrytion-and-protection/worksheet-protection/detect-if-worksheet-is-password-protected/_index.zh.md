---
title: 检测工作表是否受密码保护
type: docs
weight: 280
url: /zh/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

可以分别保护工作簿和工作表。例如，电子表格可能包含一个或多个受密码保护的工作表，但电子表格本身可以或不可以受保护。Aspose.Cells API 提供了检测给定工作表是否受密码保护的方法。本文演示了使用 Aspose.Cells for Java API 实现相同的功能。

{{% /alert %}}

## **检测工作表是否受密码保护**

Aspose.Cells for Java 8.7.0 已公开了 [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) 属性以检测工作表是否受密码保护。Boolean 类型 [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) 字段如果 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 受密码保护会返回 **true**，否则返回 **false**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
