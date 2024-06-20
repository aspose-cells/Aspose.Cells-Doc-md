---
title: Verificar contraseña de archivos cifrados
type: docs
weight: 10
url: /es/net/verify-password-of-encrypted-excel-and-ods-files/
description: Verificar la contraseña de archivos de Excel cifrados (xlsx, xlsb, xls, xlsm) y de Open office (ODS) usando códigos de CShape.
---

{{% alert color="primary" %}}
Si los archivos de Excel (xlsx, xlsb, xls, xlsm) y de Open office (ODS) están bloqueados con contraseña, Aspose soporta una verificación simple de contraseña sin analizar datos específicos de los archivos.
{{% /alert %}}

## **Verificar la contraseña del archivo cifrado**

Para verificar la contraseña del archivo cifrado, Aspose.Cells for .NET proporciona el método [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Estos métodos aceptan dos parámetros, el flujo de archivo y la contraseña que se necesita verificar.
El siguiente fragmento de código muestra el uso del método [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) para verificar si la contraseña proporcionada es válida o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

