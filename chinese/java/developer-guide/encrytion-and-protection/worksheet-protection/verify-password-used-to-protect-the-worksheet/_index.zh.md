---
title: 验证用于保护工作表的密码
type: docs
weight: 290
url: /zh/java/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells API增强了[**保护**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection)通过引入一些有用的属性和方法来类。一种这样的方法是[**验证密码**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)允许将密码指定为 String 的实例，并验证是否已使用相同的密码来保护工作表。

{{% /alert %}}

## **验证用于保护工作表的密码**

这[**保护.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) 方法返回**真的**如果指定的密码与用于保护给定工作表的密码匹配，**错误的**如果指定的密码不匹配。下面的一段代码使用了[**保护.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) 方法连同[**保护.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)属性检测密码保护，并验证密码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
