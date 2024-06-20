---
title: Проверить использованный пароль для защиты рабочего листа
type: docs
weight: 370
url: /ru/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells APIs улучшили класс [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection), представив несколько полезных свойств и методов. Один из таких методов - [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword), который позволяет указать пароль в виде экземпляра *string* и проверить, был ли этот пароль использован для защиты [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

Метод [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) возвращает **true**, если указанный пароль совпадает с паролем, использованным для защиты указанного листа, и **false**, если указанный пароль не совпадает. Приведенный ниже код использует метод [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) в сочетании с свойством [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword), чтобы определить защиту пароля и проверить пароль.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
