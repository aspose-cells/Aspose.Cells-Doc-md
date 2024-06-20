---
title: Verificar la contraseña utilizada para proteger la hoja de cálculo
type: docs
weight: 370
url: /es/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Las API de Aspose.Cells han mejorado la clase [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) al introducir algunas propiedades y métodos útiles. Uno de estos métodos es [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword), que permite especificar una contraseña como una instancia de *string* y verificar si la misma contraseña se ha utilizado para proteger la [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

El método [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) devuelve **true** si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de cálculo dada y **false** si la contraseña especificada no coincide. El siguiente fragmento de código utiliza el método [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) en conjunto con la propiedad [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) para detectar la protección con contraseña y verificar la contraseña.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
