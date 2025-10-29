---
title: Проверить использованный пароль для защиты рабочего листа
type: docs
weight: 370
url: /ru/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

API Aspose.Cells для Python via .NET улучшили класс [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection), добавив несколько полезных свойств и методов. Одним из таких методов является [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password), который позволяет указать пароль как экземпляр *string* и проверить, был ли этот пароль использован для защиты [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

Метод [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) возвращает **true**, если указанный пароль совпадает с паролем, использованным для защиты указанного листа, и **false**, если указанный пароль не совпадает. Приведенный ниже код использует метод [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) в сочетании с свойством [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password), чтобы определить защиту пароля и проверить пароль.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

{{< app/cells/assistant language="python-net" >}}
