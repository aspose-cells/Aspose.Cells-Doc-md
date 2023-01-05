---
title: Microsoft Excel-Datei importieren
type: docs
weight: 40
url: /de/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Wie Aspose.Cells.GridDesktop kann das Aspose.Cells.GridWeb-Steuerelement Microsoft Excel-Dateien öffnen und laden – komplett mit Daten, Formatierungen, Diagrammen, Bildern usw. – jedoch in Webanwendungen. In diesem Thema wird erläutert, wie.

{{% /alert %}} 
## **Importieren Sie Excel-Dateien**
### **Aus Datei importieren**
So öffnen Sie eine Excel-Datei mit dem Aspose.Cells.GridWeb-Steuerelement:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Importieren Sie die Excel-Datei, indem Sie den Dateipfad angeben.
1. Führen Sie die Anwendung aus.

{{% alert color="primary" %}} 

 Wenn Sie nicht wissen, wie Sie das Steuerelement zu einem Webformular hinzufügen, lesen Sie weiter[GridWeb zum Webformular hinzufügen](/cells/de/net/add-gridweb-to-web-form/).

{{% /alert %}} 

Wenn das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular hinzugefügt wird, wird das Steuerelement automatisch instanziiert und mit einer Standardgröße zum Formular hinzugefügt. Sie müssen kein Aspose.Cells.GridWeb-Steuerelementobjekt erstellen, alles, was Sie tun müssen, ist, das Steuerelement per Drag & Drop zu ziehen und zu verwenden.

Um jedoch den Inhalt aus einer Excel-Datei in das Aspose.Cells.GridWeb-Steuerelement zu laden, müssen Sie die ImportExcelFile-Methode aufrufen, um den Pfad der Excel-Datei anzugeben. Danach findet das Aspose.Cells.GridWeb-Steuerelement automatisch die Datei aus dem angegebenen Pfad und zeigt ihren Inhalt an. Unten finden Sie ein Code-Snippet, das den Inhalt einer Excel-Datei lädt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


Das obige Code-Snippet kann beliebig verwendet werden. Um beispielsweise eine Excel-Datei automatisch zu laden, wenn ein Webformular geladen wird, fügen Sie diesen Code zum Page_Load-Ereignis des Formulars hinzu. Wenn Sie eine Datei öffnen möchten, wenn auf eine Schaltfläche geklickt wird, fügen Sie dem Webformular eine Schaltfläche hinzu und schreiben Sie den obigen Code unter das Click-Ereignis der Schaltfläche.

**Beim Klicken auf eine Schaltfläche wird eine Excel-Datei geladen** 

![todo: Bild_alt_Text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Wenn es sich bei Ihrem Dateisystem um NTFS handelt, sollten Sie den Benutzerkonten ASPNET oder Jeder die Lesezugriffsberechtigung erteilen, da Sie sonst zur Laufzeit eine Zugriffsverweigerungsausnahme erhalten.

{{% /alert %}} 
### **Aus Stream importieren**
Das Aspose.Cells.GridWeb-Steuerelement kann nicht nur Excel-Dateien aus einer Datei öffnen, sondern auch Excel-Dateien aus einem Stream laden. Die Verwendung von Dateien als Stream ist ein besserer Ansatz, um jegliche Art von Dateizugriff oder Probleme mit Freigabeverletzungen zu verhindern, da dieser Ansatz sicherstellt, dass alle Verbindungen zu den Dateien geschlossen werden, indem der Stream geschlossen wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
