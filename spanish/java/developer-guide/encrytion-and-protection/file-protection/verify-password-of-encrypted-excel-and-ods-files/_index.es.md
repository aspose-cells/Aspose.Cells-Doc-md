---
title: Verificar contraseña de archivos cifrados
type: docs
weight: 10
url: /es/java/verify-password-of-encrypted-excel-and-ods-files/
description: Verifica la contraseña de archivos Excel cifrados (xlsx, xlsb, xls, xlsm) y de Open office (ODS) utilizando códigos Java.
---

{{% alert color="primary" %}}
Si los archivos Excel (xlsx, xlsb, xls, xlsm) y Open office (ODS) están bloqueados con una contraseña, Aspose.Cells for Java admite la verificación de contraseña simple sin analizar datos específicos de los archivos.
{{% /alert %}}

## **Verificar la contraseña del archivo cifrado**

Para verificar la contraseña del archivo cifrado, Aspose.Cells for Java proporciona el método [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)). Los métodos aceptan dos parámetros, la secuencia de archivo y la contraseña que se debe verificar.
El siguiente fragmento de código muestra el uso del método [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) para verificar si la contraseña proporcionada es válida o no.

### **Código de Ejemplo:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

