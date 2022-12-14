---
title: Fylla en .jasper-fil med stöd för redigerbara diagram
type: docs
weight: 10
url: /sv/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 Aspose.Cells för JasperReports kräver att en .jasper-fil fylls i till ett .jrprint- eller ett JasperPrint-objekt innan den kan exporteras till en XLS-fil. Det behövs ingen modifiering alls för .jrxml-filen. Ifyllningsproceduren lagrar interna representationer av diagram i JasperPrint-objektet som sedan används för att generera redigerbara diagram.

{{% /alert %}} 

Läs JasperReports dokumentation för detaljerad beskrivning av hur man fyller i en rapport.

Här är ett exempel:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
