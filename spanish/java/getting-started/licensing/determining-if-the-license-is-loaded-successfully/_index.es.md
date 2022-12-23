---
title: Determinar si la licencia se cargó correctamente
type: docs
weight: 210
url: /es/java/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**Libro de trabajo.tiene licencia()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)propiedad que puede utilizar para determinar si la licencia se carga correctamente o no. Si llama a este método antes de configurar la licencia, devolverá falso y si llama a este método después de configurar la licencia, devolverá verdadero, lo que indica que la licencia se ha cargado correctamente.

{{% /alert %}}

## **Determinar si la licencia se cargó correctamente**

 El siguiente código accede a la[**Libro de trabajo.tiene licencia()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed)antes de establecer una licencia y devuelve falso. Luego carga la licencia y vuelve a acceder a la propiedad, que ahora devuelve verdadero.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Salida de consola**

Aquí está la salida de la consola del código de muestra anterior

{{< highlight "java" >}}

false

true

{{< /highlight >}}
