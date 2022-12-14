---
title: Microsoft Excel-Datei exportieren
type: docs
weight: 50
url: /de/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Es ist möglich, neue Microsoft Excel-Dateien zu erstellen oder vorhandene Microsoft Excel-Dateien auf Websites im GUI-Modus mit Aspose.Cells.GridWeb-Steuerelement zu bearbeiten. Die Dateien können dann in Excel-Dateien gespeichert werden. Aspose.Cells.GridWeb dient effektiv als Online-Tabellenkalkulationseditor. In diesem Thema wird beschrieben, wie Rasterinhalte in Excel-Dateien gespeichert werden.

{{% /alert %}} 
## **Excel-Dateien exportieren**
### **Als Datei exportieren**
So speichern Sie den Inhalt des Steuerelements Aspose.Cells.GridWeb als Excel-Datei:

1. Fügen Sie Ihrem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Speichern Sie Ihre Arbeit als Excel-Datei unter einem angegebenen Pfad.
1. Führen Sie die Anwendung aus.

{{% alert color="primary" %}} 

 Wenn Sie nicht wissen, wie Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular hinzufügen, sollten Sie sich auf beziehen[GridWeb zum Webformular hinzufügen](/cells/de/net/add-gridweb-to-web-form/)

{{% /alert %}} 

Wenn das Aspose.Cells.GridWeb-Steuerelement zu einem Windows-Formular hinzugefügt wird, wird das Steuerelement automatisch instanziiert und mit einer Standardgröße zum Formular hinzugefügt. Sie müssen kein Aspose.Cells.GridWeb-Steuerelementobjekt erstellen, alles, was Sie tun müssen, ist, das Steuerelement per Drag & Drop zu ziehen und zu verwenden.

Das folgende Codebeispiel veranschaulicht, wie Rasterinhalte in einer Excel-Datei gespeichert werden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Wenn Ihr Dateisystem NTFS ist, gewähren Sie Lese-/Schreibzugriff auf die Benutzerkonten ASPNET oder Jeder, oder Sie erhalten zur Laufzeit eine Zugriffsverweigerungsausnahme.

{{% /alert %}} 

Das obige Code-Snippet kann auf verschiedene Weise verwendet werden. Eine gängige Methode besteht darin, eine Schaltfläche hinzuzufügen, die den Rasterinhalt in einer Excel-Datei speichert, wenn darauf geklickt wird. Aspose.Cells.GridWeb bietet einen einfacheren Ansatz für Aufgaben. Aspose.Cells.GridWeb hat ein Ereignis namens SaveCommand. Der obige Codeausschnitt kann dem Ereignishandler des SaveCommand-Ereignisses hinzugefügt werden, wodurch Benutzer ihre Arbeit speichern können, indem sie auf das integrierte Aspose.Cells.GridWeb klicken**Speichern** Taste.

**Das SaveCommand-Ereignis von GridWeb** 

![todo: Bild_alt_Text](export-microsoft-excel-file_1.jpg)

**Grid-Inhalte in Excel speichern, indem Sie auf die integrierte Speichern-Schaltfläche von GridWeb klicken** 

![todo: Bild_alt_Text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 Wenn Sie in Visual Studio arbeiten, können Sie den Ereignishandler des SaveCommand-Ereignisses einfach erstellen, indem Sie auf das Ereignis in der Datei doppelklicken**Eigenschaften** Feld. Um mehr darüber zu erfahren, lesen Sie bitte[Arbeiten mit GridWeb-Ereignissen](/cells/de/net/working-with-gridweb-events/)

{{% /alert %}} 
### **Als Stream exportieren**
Es ist auch möglich, Grid-Inhalte in einem Stream (z. B. MemoryStream) zu speichern.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
