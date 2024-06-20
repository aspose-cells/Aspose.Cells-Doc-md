---
title: Verificar Contraseña para modificar con Aspose.Cells
type: docs
weight: 190
url: /es/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Puede asignar una **Contraseña para abrir** y una **Contraseña para modificar** al crear sus libros de trabajo en Microsoft Excel. Por favor, consulte esta captura de pantalla que muestra la interfaz que Microsoft Excel proporciona para especificar estas contraseñas.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

A veces, es necesario comprobar si la contraseña dada coincide con la **Contraseña para modificar** de forma programática. Aspose.Cells proporciona el método [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) que se puede utilizar para verificar si la contraseña dada para modificar es correcta o no.

{{% /alert %}}

## Código Java para comprobar la Contraseña para modificar usando Aspose.Cells

El siguiente código de ejemplo carga el archivo de Excel fuente. Tiene una contraseña para abrir como *1234* y una contraseña para modificar como *5678*. El código primero verifica si *567* es la contraseña correcta para modificar y devuelve **falso**, y luego verifica si *5678* es la contraseña para modificar y devuelve **verdadero**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Resultado de la consola generado por el código Java

Aquí está el resultado de la consola del código de ejemplo anterior después de cargar el archivo de Excel fuente.

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
