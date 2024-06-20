---
title: Verificar la contraseña utilizada para proteger la hoja de cálculo
type: docs
weight: 290
url: /es/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Las API de Aspose.Cells han mejorado la clase [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) al introducir algunas propiedades y métodos útiles. Uno de estos métodos es [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) que permite especificar una contraseña como una instancia de String y verifica si la misma contraseña se ha utilizado para proteger la Hoja de cálculo.

{{% /alert %}}

## **Verificar la Contraseña Utilizada para Proteger la Hoja de Cálculo**

El método [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) devuelve **verdadero** si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de cálculo dada, **falso** si la contraseña especificada no coincide. El siguiente fragmento de código utiliza el método [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) en conjunción con la propiedad [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) para detectar la protección con contraseña y verificar la contraseña.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
