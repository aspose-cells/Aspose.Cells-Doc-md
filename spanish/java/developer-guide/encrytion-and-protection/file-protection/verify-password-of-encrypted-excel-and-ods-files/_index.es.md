---
title: Verificar contraseña de archivos cifrados
type: docs
weight: 10
url: /es/java/verify-password-of-encrypted-excel-and-ods-files/
description: Verifique la contraseña de los archivos cifrados de Excel (xlsx, xlsb, xls, xlsm) y Open office (ODS) usando los códigos Java.
---
{{% alert color="primary" %}}
Si los archivos de Excel (xlsx, xlsb, xls, xlsm) y Open office (ODS) están bloqueados con contraseña, Aspose.Cells for Java admite la verificación de contraseña simple sin analizar datos específicos de los archivos.
{{% /alert %}}

## **Verificar la contraseña del archivo encriptado**

 Para verificar la contraseña del archivo cifrado, Aspose.Cells for Java proporciona la[**Verificar contraseña**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String))método. Los métodos aceptan dos parámetros, el flujo de archivos y la contraseña que debe verificarse.
 El siguiente fragmento de código demuestra el uso de la[**Verificar contraseña**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword(java.io.InputStream,%20java.lang.String)) método para verificar si la contraseña proporcionada es válida o no.

### **Código de muestra:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

