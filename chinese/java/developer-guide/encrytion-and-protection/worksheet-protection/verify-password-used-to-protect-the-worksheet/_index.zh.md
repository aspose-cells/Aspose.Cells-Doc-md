---
title: 验证用于保护工作表的密码
type: docs
weight: 290
url: /zh/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells API 已经通过引入一些有用的属性和方法来增强 [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) 类。其中之一是 [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) 方法，它允许使用 String 的实例指定密码，并验证该密码是否用于保护工作表。

{{% /alert %}}

## **验证用于保护工作表的密码**

如果指定的密码与用于保护给定工作表的密码匹配，则 [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) 方法返回 **true**，如果指定的密码不匹配则返回 **false**。下面的代码片段结合使用了 [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) 方法和 [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) 属性来检测密码保护，并验证密码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
