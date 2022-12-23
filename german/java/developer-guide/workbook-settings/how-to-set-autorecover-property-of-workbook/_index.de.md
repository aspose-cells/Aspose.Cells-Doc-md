---
title: So legen Sie die AutoRecover-Eigenschaft von Workbook fest
type: docs
weight: 160
url: /de/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die AutoRecover-Eigenschaft der Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist**wahr** . Wenn Sie es einstellen**FALSCH** In einer Arbeitsmappe deaktiviert Microsoft Excel die automatische Wiederherstellung (automatisches Speichern) für diese Excel-Datei.

 Aspose.Cells bietet[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) -Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

## Java-Code zum Festlegen der AutoRecover-Eigenschaft von Workbook

 Der folgende Code erklärt die Verwendung[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) Eigentum der Arbeitsmappe. Der Code liest zuerst den Standardwert dieser Eigenschaft, der ist**wahr** , dann setzt es es als**FALSCH** und speichert die Arbeitsmappe. Dann liest es die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der zu diesem Zeitpunkt falsch ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Durch Beispielcode generierte Ausgabe

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
