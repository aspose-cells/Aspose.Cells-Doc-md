---
title: Microsoft Excel Datei importieren
type: docs
weight: 40
url: /de/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb importieren
description: Dieser Artikel zeigt, wie man in GridWeb eine Datei importiert.
---

{{% alert color="primary" %}} 

Wie Aspose.Cells.GridDesktop kann die Aspose.Cells.GridWeb-Kontrolle Microsoft Excel-Dateien öffnen und laden - komplett mit Daten, Formatierung, Diagrammen, Bildern usw. - jedoch in Webanwendungen. Dieses Thema erläutert dies.

{{% /alert %}} 
## **Excel-Dateien importieren**
### **Aus Datei importieren**
Um eine Excel-Datei mithilfe der Aspose.Cells.GridWeb-Kontrolle zu öffnen:

1. Fügen Sie der Webformular die Aspose.Cells.GridWeb-Kontrolle hinzu.
1. Importieren Sie die Excel-Datei, indem Sie den Dateipfad angeben.
1. Führen Sie die Anwendung aus.

{{% alert color="primary" %}} 

Wenn Sie nicht wissen, wie Sie die Kontrolle zu einer Webformular hinufügen, sehen Sie sich [Fügen von GridWeb zu Webformular](/cells/de/net/aspose-cells-gridweb/add-gridweb-to-web-form/) an.

{{% /alert %}} 

Wenn die Aspose.Cells.GridWeb-Kontrolle zu einem Webformular hinzugefügt wird, wird die Kontrolle automatisch instanziiert und mit einer Standardgröße dem Formular hinzugefügt. Sie müssen kein Aspose.Cells.GridWeb-Kontrollobjekt erstellen, ziehen Sie einfach die Kontrolle und beginnen Sie, sie zu verwenden.

Um jedoch den Inhalt einer Excel-Datei in die Aspose.Cells.GridWeb-Kontrolle zu laden, müssen Sie die Methode ImportExcelFile aufrufen, um den Pfad der Excel-Datei anzugeben. Danach findet die Aspose.Cells.GridWeb-Kontrolle automatisch die Datei aus dem angegebenen Pfad und zeigt ihren Inhalt an. Ein Codeausschnitt, der den Inhalt einer Excel-Datei lädt, wird unten bereitgestellt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Der obige Codeausschnitt kann beliebig verwendet werden. Wenn Sie beispielsweise eine Excel-Datei automatisch laden möchten, wenn ein Webformular geladen wird, fügen Sie diesen Code dem Page_Load-Ereignis des Formulars hinzu. Wenn Sie eine Datei öffnen möchten, wenn auf eine Schaltfläche geklickt wird, fügen Sie dem Webformular eine Schaltfläche hinzu und schreiben Sie den obigen Code unter das Click-Ereignis der Schaltfläche.

**Eine Excel-Datei wird geladen, wenn auf eine Schaltfläche geklickt wird** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Wenn Ihr Dateisystem NTFS ist, sollten Sie Lesezugriffsberechtigungen für die ASPNET- oder Everyone-Benutzerkonten gewähren, oder Sie erhalten zur Laufzeit eine Zugriffsverweigerungsausnahme.

{{% /alert %}} 
### **Import von Stream**
Der Aspose.Cells.GridWeb-Steuerelement kann Excel-Dateien nicht nur aus einer Datei öffnen, sondern auch aus einem Stream laden. Die Verwendung einer Datei als Stream ist ein besserer Ansatz, um Probleme mit Dateizugriff oder -freigabe zu verhindern, da dieser Ansatz das Schließen aller Verbindungen zu den Dateien durch das Schließen des Streams sicherstellt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
