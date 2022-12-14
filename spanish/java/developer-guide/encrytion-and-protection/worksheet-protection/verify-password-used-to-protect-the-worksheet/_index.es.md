---
title: Verificar la contraseña utilizada para proteger la hoja de trabajo
type: docs
weight: 290
url: /es/java/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells Las API han mejorado la[**Proteccion**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) class introduciendo algunas propiedades y métodos útiles. Uno de esos métodos es el[**Verificar contraseña**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)que permite especificar una contraseña como instancia de String y verifica si se ha utilizado la misma contraseña para proteger la hoja de trabajo.

{{% /alert %}}

## **Verificar la contraseña utilizada para proteger la hoja de trabajo**

 los[**Protección.verificar contraseña**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) el método devuelve**verdadero** si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja de trabajo dada,**falso** si la contraseña especificada no coincide. El siguiente fragmento de código utiliza el[**Protección.verificar contraseña**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String) ) método junto con[**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword)propiedad para detectar la protección de contraseña y verifica la contraseña.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
