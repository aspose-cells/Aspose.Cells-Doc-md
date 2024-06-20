---
title: Llenando un archivo .jasper con soporte de gráficos editables
type: docs
weight: 10
url: /es/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports requiere que se llene un archivo .jasper con un archivo .jrprint o un objeto JasperPrint antes de exportarlo a un archivo XLS. No se necesita ninguna modificación en el archivo .jrxml en absoluto. El procedimiento de llenado almacena representaciones internas de gráficos en el objeto JasperPrint que luego se utiliza para generar gráficos editables. 

{{% /alert %}} 

Por favor, lea la documentación de JasperReports para obtener una descripción detallada de cómo llenar un informe.

Aquí tienes un ejemplo:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
