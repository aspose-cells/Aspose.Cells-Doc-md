---
title: Подтвердите пароль, используемый для защиты рабочего листа
type: docs
weight: 290
url: /ru/java/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells API расширили возможности[**Защита**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) класс, введя некоторые полезные свойства и методы. Одним из таких методов является[**подтвердите пароль**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)), который позволяет указать пароль как экземпляр String и проверяет, использовался ли тот же пароль для защиты рабочего листа.

{{% /alert %}}

## **Подтвердите пароль, используемый для защиты рабочего листа**

[**Защита.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) метод возвращает**истинный** если указанный пароль совпадает с паролем, используемым для защиты данного рабочего листа,**ЛОЖЬ** если указанный пароль не совпадает. Следующий фрагмент кода использует[**Защита.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) метод в сочетании с[**Защита.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)свойство для обнаружения защиты паролем и проверяет пароль.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
