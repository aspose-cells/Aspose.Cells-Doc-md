---
title: Проверить использованный пароль для защиты рабочего листа
type: docs
weight: 290
url: /ru/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

API Aspose.Cells улучшило класс [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection), представив несколько полезных свойств и методов. Один из таких методов - [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)), который позволяет указать пароль как экземпляр строки и проверить, был ли использован такой же пароль для защиты Листа.

{{% /alert %}}

## **Проверить Пароль, Используемый для Защиты Листа**

Метод [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) возвращает **true**, если указанный пароль совпадает с паролем, использованным для защиты данного листа, **false**, если указанный пароль не совпадает. Приведенный ниже код использует метод [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) совместно с свойством [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword), чтобы обнаружить защиту пароля и проверить пароль.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
