---
title: Ihre erste Aspose.Cells Anwendung  Hallo Welt
type: docs
weight: 30
url: /de/java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

Dieses Anfängerthema zeigt, wie Entwickler mithilfe der einfachen API von Aspose.Cells eine einfache erste Anwendung ('Hello World') erstellen können. Die Anwendung erstellt eine Microsoft Excel-Datei mit den Worten 'Hello World' in einer bestimmten Zelle eines Arbeitsblatts.

{{% /alert %}}

### **Erstellen der Hello World-Anwendung**

Um die Hello World-Anwendung mit der Aspose.Cells-API zu erstellen:

1. Erstellen Sie eine Instanz der Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).
1. Die Lizenz anwenden:
   1. Wenn Sie eine Lizenz erworben haben, verwenden Sie die Lizenz in Ihrer Anwendung, um auf die volle Funktionalität von Aspose.Cells zuzugreifen.
   1. Wenn Sie die Evaluierungsversion des Komponenten verwenden (wenn Sie Aspose.Cells ohne Lizenz verwenden), überspringen Sie diesen Schritt.
1. Erstellen Sie eine neue Microsoft Excel-Datei oder öffnen Sie eine vorhandene Datei, in der Sie einige Texte hinzufügen/aktualisieren möchten.
1. Greifen Sie auf eine Zelle eines Arbeitsblatts in der Microsoft Excel-Datei zu.
1. Fügen Sie die Worte **Hallo Welt!** in eine zugängliche Zelle ein.
1. Generieren Sie die modifizierte Microsoft Excel-Datei.

Die folgenden Beispiele demonstrieren die obigen Schritte.

#### **Erstellen eines Arbeitsblatts**

Das folgende Beispiel erstellt ein neues Arbeitsblatt von Grund auf, schreibt die Worte 'Hallo Welt!' in die Zelle A1 des ersten Arbeitsblatts und speichert die Datei.

**Die generierte Tabelle** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Öffnen einer vorhandenen Datei**

Das folgende Beispiel öffnet eine vorhandene Microsoft Excel-Vorlagendatei namens **book1.xls**, schreibt die Worte 'Hallo Welt!' in die Zelle A1 im ersten Arbeitsblatt und speichert das Arbeitsblatt als neue Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
{{< app/cells/assistant language="java" >}}
