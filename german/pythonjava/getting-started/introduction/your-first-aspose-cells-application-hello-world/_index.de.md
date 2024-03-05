---
title: Ihre erste Aspose.Cells Bewerbung - Hello World
type: docs
weight: 30
url: /de/python-java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Dieses Anfängerthema zeigt, wie Entwickler eine einfache erste Anwendung (Hello World) mit Aspose.Cells' einfach API erstellen können. Die Anwendung erstellt eine Microsoft-Excel-Datei mit den Wörtern Hello World in einer bestimmten Zelle eines Arbeitsblatts.

{{% /alert %}}

### **Erstellen der Hello World-Anwendung**

So erstellen Sie die Anwendung Hello World mit Aspose.Cells API:

1.  Erstellen Sie eine Instanz der**[Arbeitsmappe](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**Klasse.
1. Wenden Sie die Lizenz an:
1. Wenn Sie eine Lizenz erworben haben, verwenden Sie die Lizenz in Ihrer Anwendung, um Zugriff auf die volle Funktionalität von Aspose.Cells zu erhalten
 1. Wenn Sie die Evaluierungsversion der Komponente verwenden (wenn Sie Aspose.Cells ohne Lizenz verwenden), überspringen Sie diesen Schritt.
1. Erstellen Sie eine neue Microsoft Excel-Datei oder öffnen Sie eine vorhandene Datei, in der Sie Text hinzufügen/aktualisieren möchten.
1. Greifen Sie auf eine beliebige Zelle eines Arbeitsblatts in der Excel-Datei Microsoft zu.
1.  Füge die Wörter ein**Hello World!** in eine zugegriffene Zelle.
1. Generieren Sie die geänderte Excel-Datei Microsoft.

Die folgenden Beispiele veranschaulichen die obigen Schritte.

#### **Erstellen einer Arbeitsmappe**

Das folgende Beispiel erstellt eine neue Arbeitsmappe von Grund auf, schreibt die Wörter "Hello World!" in Zelle A1 auf dem ersten Arbeitsblatt und speichert die Datei.

**Die generierte Tabelle** 

![todo: Bild_alt_Text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFile.py" >}}

#### **Öffnen einer bestehenden Datei**

 Das folgende Beispiel öffnet eine vorhandene Microsoft Excel-Vorlagendatei mit dem Namen**book1.xls**Sie schreibt die Worte "Hello World!" in Zelle A1 im ersten Arbeitsblatt und speichert die Arbeitsmappe als neue Datei.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpeningExistingFile.py" >}}
