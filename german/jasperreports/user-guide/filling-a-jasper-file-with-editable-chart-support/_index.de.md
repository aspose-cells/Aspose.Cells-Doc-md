---
title: Füllen einer .jasper-Datei mit bearbeitbarer Diagrammunterstützung
type: docs
weight: 10
url: /de/jasperreports/filling-a-jasper-file-with-editable-chart-support/
---
{{% alert color="primary" %}} 

 Aspose.Cells für JasperReports erfordert, dass eine .jasper-Datei in ein .jrprint- oder ein JasperPrint-Objekt gefüllt wird, bevor sie in eine XLS-Datei exportiert werden kann. Für die .jrxml-Datei ist keinerlei Änderung erforderlich. Die Füllprozedur speichert interne Darstellungen von Diagrammen im JasperPrint-Objekt, das dann verwendet wird, um bearbeitbare Diagramme zu erzeugen.

{{% /alert %}} 

Bitte lesen Sie die Dokumentation von JasperReports für eine detaillierte Beschreibung, wie ein Bericht ausgefüllt wird.

Hier ist ein Beispiel:

**Java**

{{< highlight "csharp" >}}

 JasperPrint jasperPrint = JasperFillManager.fillReport(jasperFileName, parameters, getConnection());



{{< /highlight >}}
