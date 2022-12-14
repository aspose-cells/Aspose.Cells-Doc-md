---
title: Arbeiten mit Visual Studio
type: docs
weight: 20
url: /de/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

In diesem Thema wird erläutert, wie Aspose.Cells.GridWeb in ASP.NET-Anwendungen mit Visual Studio.NET 2005 verwendet wird. Dieses Thema ist hilfreich für Entwickler auf Anfängerniveau, die mit Aspose.Cells.GridWeb arbeiten.

{{% /alert %}} 
## **Arbeiten mit Aspose.Cells.GridWeb unter Verwendung von Visual Studio 2013**
In diesem Thema wird gezeigt, wie Aspose.Cells.GridWeb verwendet wird, indem eine Beispielwebsite in Visual Studio 2013 erstellt wird. Der Prozess wurde in Schritte unterteilt.
### **Schritt 1: Erstellen einer neuen Website**
1. Öffnen Sie Visual Studio 2013.
1.  Von dem**Datei** Menü, auswählen**Neues Menü** , dann**Webseite**. 

![todo: Bild_alt_Text](working-with-visual-studio_1.png)


 Der Dialog Neue Website wird geöffnet.

1.  Auswählen**ASP.NET Website für Webformulare** aus von Visual Studio installierten Vorlagen.
1.  Wählen Sie den HTTP-Modus für den Speicherort der Website.

![todo: Bild_alt_Text](working-with-visual-studio_2.png)




1.  Geben Sie einen Speicherort an, an dem die Website-Dateien erstellt und gespeichert werden.
 1. Klicken Sie auf**Durchsuche** im Dialogfeld Neue Website.

![todo: Bild_alt_Text](working-with-visual-studio_3.png)



 Das Dialogfeld „Speicherort auswählen“ wird angezeigt.

1.  Drücke den**Lokaler IIS** Tab.
Alle Ordner und Webanwendungen, die in Ihrem IIS-Stammordner gespeichert sind, werden angezeigt (z. B.: C:\Inetpub\wwwroot).

![todo: Bild_alt_Text](working-with-visual-studio_4.png)




1. Erstellen Sie nun eine neue Webanwendung in Ihrem lokalen IIS, in der die Website-Dateien gespeichert werden.
 Im Dialogfeld "Speicherort auswählen" können Sie Webanwendungen oder virtuelle Verzeichnisse in Ihrem lokalen IIS erstellen und löschen. Um eine Webanwendung zu erstellen, klicken Sie auf eine Schaltfläche, wie unten in der Abbildung gezeigt.

![todo: Bild_alt_Text](working-with-visual-studio_5.png)



 Eine neue Webanwendung mit dem Standardnamen WebSite wird erstellt.

1. Benennen Sie die Webanwendung um. Wir haben es in GridWebOn2013 umbenannt.
1.  Klicken**Offen**. 

![todo: Bild_alt_Text](working-with-visual-studio_6.png)



 Sie kehren zum Dialogfeld „Neue Website“ zurück. Der Pfad zum Standort der Website ist auf eingestellt<http://localhost/GridWebOn2013>. 

1.  Klicken**OK** um Visual Studio eine Website erstellen zu lassen.

![todo: Bild_alt_Text](working-with-visual-studio_7.png)
### **Schritt 2: Quell- und Designansichten einer Webseite überprüfen**
 Eine Standardwebsite wurde von Visual Studio 2013 erstellt. Sie enthält eine default.aspx-Webseite mit etwas Dummy-Text und Markup.

**Quellansicht der Seite „default.aspx“.** 

![todo: Bild_alt_Text](working-with-visual-studio_8.png)



Alle Webseiten (einschließlich ASP.NET) können in zwei Modi geöffnet werden. Eine davon ist die Quellansicht, mit der Entwickler auf den Quellcode zugreifen und ihn ändern können. Der zweite Modus ist die Entwurfsansicht, die zum Entwerfen von Webseiten im WYSIWYG-Stil verwendet werden kann. Der obige Screenshot zeigt eine Quellansicht der Webseite default.aspx. Um die Entwurfsansicht anzuzeigen, klicken Sie auf**Entwurf**. 

**Entwurfsansicht der Seite „default.aspx“.** 

![todo: Bild_alt_Text](working-with-visual-studio_9.png)




Löschen Sie die von Visual Studio hinzugefügte Seite „Default.aspx“, und fügen Sie eine neue leere Seite „Default.aspx“ hinzu.

![todo: Bild_alt_Text](working-with-visual-studio_10.png)
### **Schritt 3: Hinzufügen von Aspose.Cells.GridWeb zur Webseite**
 Sie können das Steuerelement Aspose.Cells.GridWeb (oder GridWeb) einfach zu einer Webseite hinzufügen, indem Sie es aus der Toolbox ziehen.

![todo: Bild_alt_Text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Wenn Sie nicht wissen, wie Sie Aspose.Cells.GridWeb zur Toolbox hinzufügen, lesen Sie weiter[Integrieren Sie Aspose.Cells-Rastersteuerelemente in Visual Studio.NET](/cells/de/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 Sobald das GridWeb-Steuerelement auf der Webseite abgelegt wurde, würde es wie folgt gerendert werden:

![todo: Bild_alt_Text](working-with-visual-studio_12.png)



### **Schritt 4: Ändern Sie das Tag <!DOCTYPE>**
1.  Wechseln Sie zur Quellansicht und finden Sie Folgendes**<!DOCTYPE>** Tag im Quellcode:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  Wählen Sie das vollständige Tag aus.

![todo: Bild_alt_Text](working-with-visual-studio_13.png)




1.  Behalten, ändern oder löschen Sie die<!DOCTYPE>Schild.
1.  Oder ändern Sie die<!DOCTYPE> Tag mit folgendem:

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Schritt 5: Ändern der Größe von Aspose.Cells.GridWeb Control**
 Sie können die Breite und Höhe des GridWeb-Steuerelements ändern, nachdem Sie es auf die Website gezogen haben.

 In der Entwurfsansicht können Sie die Breite und Höhe des GridWeb ändern.

![todo: Bild_alt_Text](working-with-visual-studio_14.png)



### **Schritt 6: Konfigurieren der Eigenschaften von Aspose.Cells.GridWeb**
 Konfigurieren Sie die Aspose.Cells.GridWeb-Eigenschaften in WYSIWYG, indem Sie auf klicken**Eigenschaften** auf der rechten Seite der Visual Studio 2013-IDE.
 Ein Eigenschaftendialog wird angezeigt.

![todo: Bild_alt_Text](working-with-visual-studio_15.png)



Der Eigenschaftenbereich ermöglicht es, das Aussehen und Verhalten von GridWeb und einige andere Eigenschaften zu konfigurieren, um das Verhalten von GridWeb zu steuern.
### **Schritt 7: Ausführen Ihrer ersten Website mit Aspose.Cells.GridWeb**
 Erstellen und betreiben Sie die Website.

1.  Führen Sie die Website direkt aus Visual Studio aus, indem Sie STRG+F5 drücken oder klicken**Starten Sie das Debuggen**. 

![todo: Bild_alt_Text](working-with-visual-studio_16.png)

 Jetzt können Sie mit der GridWeb-Steuerung spielen.

**GridWeb-Steuerelement in Aktion** 

![todo: Bild_alt_Text](working-with-visual-studio_17.png)
