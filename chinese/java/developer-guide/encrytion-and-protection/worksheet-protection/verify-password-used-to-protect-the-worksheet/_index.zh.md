---
title: 验证用于保护工作表的密码
type: docs
weight: 290
url: /zh/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells API 通过引入一些有用的属性和方法增强了 [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) 类。其中一种方法是 [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) 方法，它允许将密码作为 String 实例指定，并验证是否使用相同密码保护了工作表。

{{% /alert %}}

## **验证用于保护工作表的密码**

如果指定的密码与所给工作表所使用的密码匹配，[**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) 方法返回 **true**，否则返回 **false**。以下代码片段结合使用 [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) 方法和 [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) 属性检测密码保护，并验证密码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
