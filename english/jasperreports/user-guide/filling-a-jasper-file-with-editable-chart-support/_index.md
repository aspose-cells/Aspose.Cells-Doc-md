---
title: Filling a .jasper File with Editable Chart Support
type: docs
weight: 10
url: /jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports requires a .jasper file to be filled to a .jrprint or a JasperPrint object before it can be exported to an XLS file. There's no modification needed for the .jrxml file whatsoever. The filling procedure stores internal representations of charts into the JasperPrint object which is then used to generate editable charts. 

{{% /alert %}} 

Please read JasperReports' documentation for detailed description of how to fill a report.

Here's an example:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
