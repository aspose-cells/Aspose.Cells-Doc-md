---
title: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest
type: docs
weight: 160
url: /de/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die Eigenschaft AutoRecover einer Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie ihn auf **false** für eine Arbeitsmappe setzen, deaktiviert Microsoft Excel die Automatische Wiederherstellung (AutoSave) für diese Excel-Datei.

Aspose.Cells bietet die [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)-Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

## Java-Code zur Festlegung der AutoRecover-Eigenschaft der Arbeitsmappe

Der folgende Code erläutert die Verwendung der [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)-Eigenschaft der Arbeitsmappe. Der Code liest zuerst den Standardwert dieser Eigenschaft, der **true** ist, setzt ihn dann auf **false** und speichert die Arbeitsmappe. Anschließend liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der zu diesem Zeitpunkt **false** ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Ausgabe des Beispielcodes generiert

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
