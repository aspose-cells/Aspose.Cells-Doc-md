---
title: Ihre erste Aspose.Cells Bewerbung - Hello World
type: docs
weight: 30
url: /de/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Dieses Tutorial zeigt, wie Sie eine allererste Anwendung (Hello World) mit Aspose.Cells' einfach API erstellen. Diese einfache Anwendung erstellt eine Microsoft Excel-Datei mit dem Text 'Hello World' in einer bestimmten Arbeitsblattzelle.

{{% /alert %}}

## **Erstellen der Hello World-Anwendung**

Die folgenden Schritte erstellen die Hello World-Anwendung unter Verwendung der Aspose.Cells API:

1.  Erstellen Sie eine Instanz der[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse.
1.  Wenn Sie eine Lizenz haben, dann[Wende es an](/cells/de/net/licensing/).
 Wenn Sie die Evaluierungsversion verwenden, überspringen Sie die lizenzbezogenen Codezeilen.
1. Erstellen Sie eine neue Excel-Datei oder öffnen Sie eine vorhandene Excel-Datei.
1. Greifen Sie in der Excel-Datei auf eine beliebige Zelle eines Arbeitsblatts zu.
1.  Füge die Wörter ein**Hello World!** in eine zugegriffene Zelle.
1. Generieren Sie die geänderte Excel-Datei Microsoft.

Die Implementierung der obigen Schritte wird in den folgenden Beispielen demonstriert.

### **Codebeispiel: Erstellen einer neuen Arbeitsmappe**

Das folgende Beispiel erstellt eine neue Arbeitsmappe von Grund auf neu, schreibt Hello World! in Zelle A1 auf dem ersten Arbeitsblatt und speichert die Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Codebeispiel: Öffnen einer vorhandenen Datei**

Das folgende Beispiel öffnet eine vorhandene Excel-Vorlagendatei Microsoft mit dem Namen "Sample.xlsx", gibt "Hello World!" Text in die Zelle A1 im ersten Arbeitsblatt und speichert die Arbeitsmappe.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
