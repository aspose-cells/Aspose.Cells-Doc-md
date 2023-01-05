---
title: Verifique la contraseña para modificar usando Aspose.Cells
type: docs
weight: 190
url: /es/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Puede asignar un**Contraseña para abrir** y un**Contraseña para modificar** mientras crea sus libros de trabajo en Microsoft Excel. Consulte esta captura de pantalla que muestra la interfaz Microsoft que proporciona Excel para especificar estas contraseñas.

![todo:imagen_alternativa_texto](check-password-to-modify-using-aspose-cells_1.png)

 A veces, es necesario comprobar si la contraseña proporcionada coincide con la**Contraseña para modificar** programáticamente. Aspose.Cells proporciona[**libro de trabajo.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) método que puede usar para verificar si la contraseña dada para modificar es correcta o no.

{{% /alert %}}

## Java código para verificar Contraseña para modificar usando Aspose.Cells

 Los siguientes códigos de muestra cargan el[Excel fuente](5473057.xlsx) expediente. Tiene una contraseña para abrir como*1234* y contraseña para modificar como*5678* . El código primero comprueba si*567* es la contraseña correcta para modificar y vuelve**falso** y luego comprueba si*5678* es contraseña para modificar y vuelve**verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Salida de consola generada por el código Java

 Aquí está la salida de la consola del código de muestra anterior después de cargar el[Excel fuente](5473057.xlsx) expediente.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
