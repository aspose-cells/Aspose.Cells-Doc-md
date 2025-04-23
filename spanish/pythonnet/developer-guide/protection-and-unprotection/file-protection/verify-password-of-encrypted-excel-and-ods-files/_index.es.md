---
title: Verificar contraseña de archivos cifrados
type: docs
weight: 10
url: /es/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Verificar la contraseña de archivos de Excel cifrados (xlsx, xlsb, xls, xlsm) y de Open office (ODS) usando códigos de CShape.
---

{{% alert color="primary" %}}
Si los archivos de Excel (xlsx, xlsb, xls, xlsm) y de Open office (ODS) están bloqueados con contraseña, Aspose soporta una verificación simple de contraseña sin analizar datos específicos de los archivos.
{{% /alert %}}

## **Verificar la contraseña del archivo cifrado**

Para verificar la contraseña del archivo cifrado, Aspose.Cells para Python via .NET proporciona el método [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). Estos métodos aceptan dos parámetros, el flujo del archivo y la contraseña que necesita ser verificada.
El siguiente fragmento de código muestra el uso del método [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) para verificar si la contraseña proporcionada es válida o no.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


