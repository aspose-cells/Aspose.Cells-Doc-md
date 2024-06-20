---
title: Compilazione di un file .jasper con supporto per il grafico modificabile
type: docs
weight: 10
url: /it/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports richiede un file .jasper da compilare in un file .jrprint o in un oggetto JasperPrint prima di poter essere esportato in un file XLS. Non è necessaria alcuna modifica al file .jrxml. La procedura di compilazione memorizza le rappresentazioni interne dei grafici nell'oggetto JasperPrint che viene quindi utilizzato per generare grafici modificabili. 

{{% /alert %}} 

Si prega di leggere la documentazione di JasperReports per una descrizione dettagliata su come compilare un report.

Ecco un esempio:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
