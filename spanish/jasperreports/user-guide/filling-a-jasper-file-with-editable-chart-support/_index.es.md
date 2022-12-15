---
title: Llenar un archivo .jasper con compatibilidad con gráficos editables
type: docs
weight: 10
url: /es/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports requiere que se complete un archivo .jasper en un objeto .jrprint o JasperPrint antes de poder exportarlo a un archivo XLS. No se necesita ninguna modificación para el archivo .jrxml en absoluto. El procedimiento de llenado almacena representaciones internas de gráficos en el objeto JasperPrint que luego se utiliza para generar gráficos editables.

{{% /alert %}} 

Lea la documentación de JasperReports para obtener una descripción detallada de cómo completar un informe.

Aquí hay un ejemplo:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
