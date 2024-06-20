---
title: Determinar si la licencia se cargó correctamente
type: docs
weight: 210
url: /es/java/determining-if-the-license-is-loaded-successfully/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la propiedad [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) que puedes usar para determinar si la licencia se cargó correctamente o no. Si llamas a este método antes de configurar la licencia, devolverá falso y si llamas a este método después de configurar la licencia, devolverá true indicando que la licencia se ha cargado exitosamente.

{{% /alert %}}

## **Determinando si la licencia se cargó exitosamente**

El siguiente código accede al método [**Workbook.isLicensed()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#IsLicensed) antes de establecer una licencia y devuelve false. Luego carga la licencia y accede a la propiedad nuevamente, que ahora devuelve true.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeterminetheLicenseLoadedSuccessfully-DeterminetheLicenseLoadedSuccessfully.java" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código de ejemplo anterior

{{< highlight java >}}

false

true

{{< /highlight >}}
