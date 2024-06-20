---
title: Ausfüllen einer .jasper Datei mit unterstützter bearbeitbarer Grafik
type: docs
weight: 10
url: /de/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports erfordert, dass eine .jasper-Datei zu einer .jrprint- oder einem JasperPrint-Objekt ausgefüllt wird, bevor sie in eine XLS-Datei exportiert werden kann. Es ist keine Modifikation an der .jrxml-Datei erforderlich. Der Ausfüllvorgang speichert interne Repräsentationen von Diagrammen im JasperPrint-Objekt, das dann zur Generierung von bearbeitbaren Diagrammen verwendet wird. 

{{% /alert %}} 

Bitte lesen Sie die Dokumentation von JasperReports für eine ausführliche Beschreibung, wie ein Bericht ausgefüllt wird.

Hier ist ein Beispiel:

**Java**

{{< highlight csharp >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
