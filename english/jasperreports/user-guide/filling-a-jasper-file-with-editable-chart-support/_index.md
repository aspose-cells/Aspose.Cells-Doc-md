---
title: Filling a .jasper File with Editable Chart Support
type: docs
weight: 10
url: /jasperreports/filling-a-jasper-file-with-editable-chart-support/
ai_search_scope: cells_jasperreports
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports requires a .jasper file to be filled into a .jrprint or a JasperPrint object before it can be exported to an XLS file. There's no modification needed for the .jrxml file whatsoever. The filling procedure stores internal representations of charts into the JasperPrint object, which is then used to generate editable charts. 

{{% /alert %}} 

Please read JasperReports' documentation for a detailed description of how to fill a report.

Here's an example:

**Java**

{{< highlight java >}}
JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());
{{< /highlight >}}
