---
title: Arbeiten mit Visual Studio
type: docs
weight: 20
url: /de/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: Dieser Artikel zeigt, wie GridWeb in Visual Studio verwendet werden kann.
---

{{% alert color="primary" %}} 

In diesem Thema wird erklärt, wie Aspose.Cells.GridWeb in ASP.NET-Anwendungen unter Verwendung von Visual Studio.NET 2005 verwendet werden kann. Dieses Thema ist für Anfänger-Entwickler, die mit Aspose.Cells.GridWeb arbeiten, nützlich.

{{% /alert %}} 
## **Arbeiten mit Aspose.Cells.GridWeb unter Verwendung von Visual Studio 2013**
In diesem Thema wird gezeigt, wie Aspose.Cells.GridWeb durch die Erstellung einer Beispielwebsite in Visual Studio 2013 verwendet werden kann. Der Prozess wurde in Schritte unterteilt.
### **Schritt 1: Erstellen einer neuen Website**
1. Öffnen Sie Visual Studio 2013.
1. Wählen Sie im **Datei**-Menü **Neues Menü** und dann **Website** aus. 

![todo:image_alt_text](working-with-visual-studio_1.png)


Der Dialog Neues Website wird geöffnet. 

1. Wählen Sie **ASP.NET-Webformularwebsite** aus den installierten Vorlagen von Visual Studio.
1. Wählen Sie den HTTP-Modus für den Speicherort der Website aus. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Geben Sie einen Speicherort an, an dem die Website-Dateien erstellt und gespeichert werden. 
   1. Klicken Sie im Dialogfeld Neues Website auf **Durchsuchen**. 

![todo:image_alt_text](working-with-visual-studio_3.png)



Das Dialogfeld Standort auswählen wird angezeigt. 

1. Klicken Sie auf die Registerkarte **Lokales IIS**.
   Alle Ordner und Webanwendungen, die in Ihrem IIS-Stammverzeichnis (z. B.: C:\Inetpub\wwwroot) gespeichert sind, werden angezeigt. 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Erstellen Sie nun eine neue Webanwendung in Ihrem lokalen IIS, in der die Website-Dateien gespeichert werden.
   Der Dialogfeld 'Standort auswählen' ermöglicht das Erstellen und Löschen von Webanwendungen oder virtuellen Verzeichnissen in Ihrem lokalen IIS. Um eine Webanwendung zu erstellen, klicken Sie auf eine Schaltfläche, wie in der Abbildung unten gezeigt. 

![todo:image_alt_text](working-with-visual-studio_5.png)



Eine neue Webanwendung mit dem Standardnamen 'WebSite' wird erstellt. 

1. Benennen Sie die Webanwendung um. Wir haben sie in 'GridWebOn2013' umbenannt.
1. Klicken Sie auf **Öffnen**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Klicken Sie auf **OK**, damit Visual Studio eine Website erstellt. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Schritt 2: Quell- & Designansichten einer Webseite überprüfen**
Ein Standard-Website wurde von Visual Studio 2013 erstellt. Sie enthält eine 'default.aspx'-Webseite mit etwas Dummy-Text und Markup. 

**Quellansicht der 'default.aspx'-Seite** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Alle Webseiten (einschließlich ASP.NET) können in zwei Modi geöffnet werden. Einer ist die Quellansicht, die es Entwicklern ermöglicht, auf den Quellcode zuzugreifen und diesen zu ändern. Der zweite Modus ist die Designansicht, die verwendet werden kann, um Webseiten auf eine WYSIWYG-Art zu entwerfen. Das obige Screenshot zeigt eine Quellansicht der 'default.aspx'-Webseite. Um die Designansicht anzuzeigen, klicken Sie auf **Design**. 

**Designansicht der 'default.aspx'-Seite** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Löschen Sie die von Visual Studio hinzugefügte 'Default.aspx'-Seite und fügen Sie eine neue leere 'Default.aspx'-Seite hinzu.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Schritt 3: Hinzufügen von Aspose.Cells.GridWeb zur Webseite**
Sie können einfach die Aspose.Cells.GridWeb (oder GridWeb) Steuerelement zu einer Webseite hinzufügen, indem Sie es aus der Toolbox ziehen. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Wenn Sie nicht wissen, wie Sie Aspose.Cells.GridWeb zur Toolbox hinzufügen können, verweisen Sie auf [Integrieren von Aspose.Cells Grid Controls mit Visual Studio.NET](/cells/de/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

Sobald das GridWeb-Steuerelement zur Webseite hinzugefügt wird, wird es so gerendert: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Wählen Sie den kompletten Tag aus. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Schritt 5: Ändern der Größe des Aspose.Cells.GridWeb-Steuerelements**
Nachdem Sie das GridWeb-Steuerelement zur Website gezogen haben, können Sie die Breite und Höhe des GridWeb-Steuerelements ändern. 

In der Designansicht können Sie die Breite und Höhe des GridWeb ändern. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Schritt 6: Konfigurieren der Eigenschaften von Aspose.Cells.GridWeb**
Konfigurieren Sie die Eigenschaften des Aspose.Cells.GridWeb in WYSIWYG, indem Sie auf die Schaltfläche **Eigenschaften** auf der rechten Seite der Visual Studio 2013 IDE klicken. 
Es wird ein Eigenschaften-Dialogfeld angezeigt. 

![todo:image_alt_text](working-with-visual-studio_15.png)



Das Eigenschaftenfenster ermöglicht es, das Aussehen und Verhalten des GridWeb sowie einige andere Eigenschaften zu konfigurieren.
### **Schritt 7: Ausführen Ihrer ersten Website mit Aspose.Cells.GridWeb**
Bauen und starten Sie die Webseite. 

1. Starten Sie die Webseite direkt aus Visual Studio, indem Sie Strg+F5 drücken oder auf **Debugging starten** klicken. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Nun können Sie mit der GridWeb-Steuerung spielen. 

**GridWeb-Steuerung in Aktion** 

![todo:image_alt_text](working-with-visual-studio_17.png)
