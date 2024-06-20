---
title: Microsoft Excel Datei exportieren
type: docs
weight: 50
url: /de/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb, exportieren
description: Dieser Artikel erläutert, wie eine Datei in GridWeb exportiert werden kann.
---

{{% alert color="primary" %}} 

Es ist möglich, neue oder vorhandene Microsoft Excel-Dateien auf Websites im GUI-Modus mit der Aspose.Cells.GridWeb-Steuerung zu erstellen oder zu manipulieren. Die Dateien können dann als Excel-Dateien gespeichert werden. Aspose.Cells.GridWeb dient effektiv als Online-Tabellenkalkulationseditor. In diesem Thema wird beschrieben, wie Gitterinhalte in Excel-Dateien gespeichert werden können.

{{% /alert %}} 
## **Excel-Dateien exportieren**
### **Exportieren als Datei**
Um den Inhalt der Aspose.Cells.GridWeb-Steuerelement als Excel-Datei zu speichern:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular hinzu.
1. Speichern Sie Ihre Arbeit als Excel-Datei an einem bestimmten Pfad.
1. Führen Sie die Anwendung aus.

{{% alert color="primary" %}} 

Wenn Sie nicht wissen, wie Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular hinzufügen, sollten Sie sich auf [Add GridWeb to Web Form](/cells/de/net/aspose-cells-gridweb/add-gridweb-to-web-form/) beziehen

{{% /alert %}} 

Wenn das Aspose.Cells.GridWeb-Steuerelement zu einem Windows-Formular hinzugefügt wird, wird das Steuerelement automatisch instanziiert und mit einer standardmäßigen Größe dem Formular hinzugefügt. Sie müssen kein Aspose.Cells.GridWeb-Steuerelementobjekt erstellen, sondern müssen nur das Steuerelement per Drag & Drop hinzufügen und verwenden.

Das untenstehende Codebeispiel zeigt, wie der Inhalte des Gitters in eine Excel-Datei gespeichert werden.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

Wenn Ihr Dateisystem NTFS ist, gewähren Sie Lese-/Schreibzugriff auf die Benutzerkonten ASPNET oder Jeder, ansonsten erhalten Sie zur Laufzeit eine Zugriffsverweigerungsausnahme.

{{% /alert %}} 

Der obige Code-Schnipsel kann auf verschiedene Weisen verwendet werden. Eine übliche Methode besteht darin, eine Schaltfläche hinzuzufügen, die den Rasterinhalt beim Klicken in eine Excel-Datei speichert. Aspose.Cells.GridWeb bietet einen einfacheren Ansatz für diese Aufgabe. Aspose.Cells.GridWeb hat ein Ereignis namens Speichern-Befehl. Der obige Code-Schnipsel kann dem Ereignisbehandler des Speichern-Befehls hinzugefügt werden, was es Benutzern ermöglicht, ihre Arbeit durch Klicken auf die integrierte **Speichern**-Schaltfläche von Aspose.Cells.GridWeb zu speichern.

**Das Speichern-Befehlsereignis des GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**Speichern des Rasterinhalts in Excel durch Klicken auf die integrierte Speichern-Schaltfläche von GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

Wenn Sie in Visual Studio arbeiten, können Sie den Ereignishandler des Speichern-Befehlsereignisses ganz einfach erstellen, indem Sie doppelt auf das Ereignis im **Eigenschaften**-Bereich klicken. Weitere Informationen hierzu finden Sie unter [Arbeiten mit GridWeb-Ereignissen](/cells/de/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **Exportieren als Stream**
Es ist auch möglich, den Rasterinhalt in einem Stream (z. B. MemoryStream) zu speichern.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
