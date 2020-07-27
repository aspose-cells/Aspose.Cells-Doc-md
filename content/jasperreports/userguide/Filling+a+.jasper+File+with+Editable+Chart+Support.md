+++
title = "Filling a .jasper File with Editable Chart Support" 
description = "" 
weight = 8023 
+++

Aspose.Cells for JasperReports : Filling a .jasper File with Editable Chart Support  

# Aspose.Cells for JasperReports : Filling a .jasper File with Editable Chart Support


Aspose.Cells for JasperReports requires a .jasper file to be filled to a .jrprint or a JasperPrint object before it can be exported to an XLS file. There's no modification needed for the .jrxml file whatsoever. The filling procedure stores internal representations of charts into the JasperPrint object which is then used to generate editable charts.

Please read JasperReports' documentation for detailed description of how to fill a report.

Here's an example:

**Java**

{{< code lang="java" >}}
JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());
 
{{< /code >}}

