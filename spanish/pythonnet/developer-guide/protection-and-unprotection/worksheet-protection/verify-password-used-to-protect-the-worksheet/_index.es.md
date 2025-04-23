---
title: Verificar la contraseña utilizada para proteger la hoja de cálculo
type: docs
weight: 370
url: /es/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Las APIs de Aspose.Cells para Python via .NET han mejorado la clase [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) al introducir algunas propiedades y métodos útiles. Uno de estos métodos es [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password), que permite especificar una contraseña como una instancia de *string* y verificar si la misma contraseña ha sido utilizada para proteger [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

El método [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) devuelve **true** si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de cálculo dada y **false** si la contraseña especificada no coincide. El siguiente fragmento de código utiliza el método [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) en conjunto con la propiedad [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) para detectar la protección con contraseña y verificar la contraseña.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

