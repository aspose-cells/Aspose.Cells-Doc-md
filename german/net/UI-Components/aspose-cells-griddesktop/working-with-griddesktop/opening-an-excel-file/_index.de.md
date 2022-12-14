---
title: Öffnen einer Excel-Datei
type: docs
weight: 10
url: /de/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Ein einzigartiges Merkmal von Aspose.Cells Grid Suite ist die Kompatibilität mit Excel-Dateien. In diesem Thema zeigen wir, wie Benutzer Excel-Dateien in ihren Windows-Anwendungen mit dem Aspose.Cells.GridDesktop-Steuerelement öffnen können.

{{% /alert %}} 
## **Einführung**
 Um eine Excel-Datei mit Aspose.Cells.GridDesktop zu öffnen, müssen Sie eine Desktop-Anwendung mit GridDesktop Control darin erstellen. Wenn Sie nicht wissen, wie Sie das Aspose.Cells.GridDesktop-Steuerelement zu Ihrem Windows-Formular hinzufügen, sollten Sie sich auf beziehen[So verwenden Sie Aspose.Cells.GridDesktop](/cells/de/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop bietet drei verschiedene Möglichkeiten, eine Excel-Datei zu öffnen.

1. **Öffnen aus einer Datei**
1. **Öffnen einer CSV-Datei**
1. **Öffnen aus einem Stream**
## **Excel-Datei öffnen**
Erstellen Sie in diesem Beispiel eine Desktop-Anwendung und gehen Sie wie folgt vor.

- Fügen Sie dem Formular ein GridControl-Steuerelement hinzu.
- Fügen Sie drei Schaltflächen hinzu, deren Texteigenschaften wie folgt festgelegt sind:
  - **Excel-Datei öffnen**
  - **CSV-Datei öffnen**
  - **Aus Stream öffnen**
### **Öffnen aus einer Datei**
 Um den Inhalt aus einer Excel-Datei in das Aspose.Cells.GridDesktop-Steuerelement zu laden, müssen Sie eine Methode des Steuerelements aufrufen, um den Pfad der Excel-Datei anzugeben. Danach findet das Aspose.Cells.GridDesktop-Steuerelement automatisch die Datei aus dem angegebenen Pfad und zeigt ihren Inhalt an. Das Code-Snippet zum Laden des Inhalts einer Excel-Datei wird im folgenden Beispiel bereitgestellt. Erstellen Sie das Click-Ereignis der**Excel-Datei öffnen** Schaltfläche und fügen Sie den folgenden Code darin ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Das obige Code-Snippet kann von Entwicklern beliebig verwendet werden. Wenn Sie beispielsweise eine Excel-Datei automatisch laden möchten, wenn ein Windows-Formular geladen wird, können Sie diesen Code unter dem Load-Ereignis Ihres Formulars hinzufügen.
### **Öffnen einer CSV-Datei**
Aspose.Cells. Das GridDesktop-Steuerelement unterstützt auch das Laden von CSV-Dateien. Erstellen Sie das Click-Ereignis der**CSV-Datei öffnen** Schaltfläche und fügen Sie den folgenden Code darin ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Öffnen aus einem Stream**
 In unserer obigen Diskussion haben wir über das Laden einer Excel-Datei unter Verwendung ihres Dateipfads gesprochen, aber das Aspose.Cells.GridDesktop-Steuerelement unterstützt auch das Laden einer Excel-Datei aus einem Stream. Erstellen Sie das Click-Ereignis der**Aus Stream öffnen** Schaltfläche und fügen Sie den folgenden Code darin ein.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Die Verwendung von Dateien als Stream ist ein besserer Ansatz, um jegliche Art von Dateizugriff oder Probleme mit Freigabeverletzungen zu verhindern, da dieser Ansatz sicherstellt, dass alle Verbindungen zu den Dateien geschlossen werden, indem der Stream geschlossen wird.

{{% alert color="primary" %}} 

WICHTIG: Ein wichtiger zu diskutierender Punkt ist, dass das Aspose.Cells.GridDesktop-Steuerelement auch eine Methode namens LoadFromExcel enthält, die auch zum Laden des Inhalts einer Excel-Datei in das Grid verwendet wird. Aber diese Methode ist jetzt veraltet. Daher wird allen Entwicklern empfohlen, die ImportExcelFile-Methode zu verwenden, die robuster und effizienter ist als die veraltete.

{{% /alert %}}
