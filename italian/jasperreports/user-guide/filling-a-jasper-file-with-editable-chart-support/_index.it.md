---
title: Compilazione di un file .jasper con supporto grafico modificabile
type: docs
weight: 10
url: /it/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 Aspose.Cells for JasperReports richiede che un file .jasper venga inserito in un oggetto .jrprint o JasperPrint prima che possa essere esportato in un file XLS. Non è necessaria alcuna modifica per il file .jrxml. La procedura di riempimento memorizza le rappresentazioni interne dei grafici nell'oggetto JasperPrint che viene quindi utilizzato per generare grafici modificabili.

{{% /alert %}} 

Si prega di leggere la documentazione di JasperReports per una descrizione dettagliata di come compilare un rapporto.

Ecco un esempio:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
