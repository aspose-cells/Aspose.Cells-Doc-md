---
title: Fylla en .jasper fil med stöd för redigerbara diagram
type: docs
weight: 10
url: /sv/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports kräver att en .jasper-fil fylls till en .jrprint eller en JasperPrint-objekt innan den kan exporteras till en XLS-fil. Det krävs ingen modifiering för .jrxml-filen alls. Fyllningsproceduren lagrar interna representationer av diagram i JasperPrint-objektet som sedan används för att generera redigerbara diagram. 

{{% /alert %}} 

Vänligen läs JasperReports dokumentation för detaljerad beskrivning av hur man fyller en rapport.

Här är ett exempel:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
