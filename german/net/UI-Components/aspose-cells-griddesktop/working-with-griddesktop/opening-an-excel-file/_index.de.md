---
title: Öffnen einer Excel Datei
type: docs
weight: 10
url: /de/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop, öffnen, Datei
description: Dieser Artikel zeigt, wie eine Datei im GridDesktop geöffnet werden kann.
---

{{% alert color="primary" %}} 

Ein einzigartiges Merkmal des Aspose.Cells Grid Suite ist seine Kompatibilität mit Excel-Dateien. In diesem Thema zeigen wir, wie Benutzer Excel-Dateien in ihren Windows-Anwendungen mithilfe der Aspose.Cells.GridDesktop-Steuerung öffnen können.

{{% /alert %}} 
## **Einführung**
Um eine Excel-Datei mit Aspose.Cells.GridDesktop zu öffnen, müssen Sie eine Desktop-Anwendung mit der GridDesktop-Steuerung erstellen. Wenn Sie nicht wissen, wie Sie die Aspose.Cells.GridDesktop-Steuerung Ihrem Windows-Formular hinzufügen können, sollten Sie sich auf [So verwenden Sie Aspose.Cells.GridDesktop](/cells/de/net/how-to-use-aspose-cells-griddesktop/) beziehen.

Aspose.Cells.GridDesktop bietet drei verschiedene Möglichkeiten zum Öffnen einer Excel-Datei.

1. **Öffnen aus einer Datei**
1. **Öffnen einer CSV-Datei**
1. **Öffnen aus einem Stream**
## **Excel-Datei öffnen**
Erstellen Sie in diesem Beispiel eine Desktop-Anwendung und führen Sie folgende Schritte aus.

- Fügen Sie dem Formular eine GridControl-Steuerung hinzu.
- Fügen Sie drei Schaltflächen hinzu, deren Texteigenschaften wie folgt festgelegt sind:
  - **Excel-Datei öffnen**
  - **CSV-Datei öffnen**
  - **Aus einem Stream öffnen**
### **Aus einer Datei öffnen**
Um den Inhalt einer Excel-Datei zur Aspose.Cells.GridDesktop-Steuerung zu laden, müssen Sie eine Methode der Steuerung aufrufen, um den Pfad der Excel-Datei anzugeben. Danach findet die Aspose.Cells.GridDesktop-Steuerung automatisch die Datei im angegebenen Pfad und zeigt ihren Inhalt an. Der Codeausschnitt zum Laden des Inhalts einer Excel-Datei ist im folgenden Beispiel angegeben. Erstellen Sie das Click-Ereignis der **Excel-Datei öffnen**-Schaltfläche und fügen Sie den folgenden Code ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Der obige Codeausschnitt kann von Entwicklern in beliebiger Weise verwendet werden. Wenn Sie beispielsweise automatisch eine Excel-Datei laden möchten, wenn ein Windows-Formular geladen wird, können Sie diesen Code unter das Load-Ereignis Ihres Forms hinzufügen.
### **Öffnen einer CSV-Datei**
Die Aspose.Cells.GridDesktop-Steuerung unterstützt auch das Laden von CSV-Dateien. Erstellen Sie das Click-Ereignis der **CSV-Datei öffnen**-Schaltfläche und fügen Sie den folgenden Code ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Aus einem Stream öffnen**
In unserer obigen Diskussion haben wir das Laden einer Excel-Datei anhand ihres Dateipfads besprochen, aber die Aspose.Cells.GridDesktop-Steuerung unterstützt auch das Laden einer Excel-Datei aus einem Stream. Erstellen Sie das Click-Ereignis der **Aus einem Stream öffnen**-Schaltfläche und fügen Sie den folgenden Code ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Die Verwendung einer Datei als Stream ist ein besseres Vorgehen, um jegliche Art von Dateizugriffs- oder Freigabeverletzungsproblemen zu verhindern, da dieses Vorgehen gewährleistet, dass alle Verbindungen zu den Dateien durch Schließen des Streams geschlossen werden.

{{% alert color="primary" %}} 

WICHTIG: Ein wichtiger Punkt, der zu diskutieren ist, ist, dass Aspose.Cells.GridDesktop-Steuerelement auch eine Methode namens LoadFromExcel enthält, die ebenfalls zum Laden des Inhalts einer Excel-Datei in das Grid verwendet wird. Diese Methode ist jedoch jetzt veraltet. Daher wird allen Entwicklern empfohlen, die Methode ImportExcelFile zu verwenden, die robuster und effizienter als die veraltete ist.

{{% /alert %}}
