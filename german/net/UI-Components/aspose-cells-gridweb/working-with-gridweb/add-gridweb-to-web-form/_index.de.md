---
title: GridWeb zu Webform hinzufügen
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/add-gridweb-to-web-form/
keywords: GridWeb,webform,form
description: Dieser Artikel zeigt, wie man mit Webformularen in GridWeb arbeitet.
---

{{% alert color="primary" %}} 

Dieser Artikel bietet Anfängern eine grundlegende schrittweise Anleitung, wie sie die Aspose.Cells.GridWeb-Steuerung in Webanwendungen erstellen und verwenden können.

{{% /alert %}} 
## **Erstellen & Verwenden der Aspose.Cells.GridWeb-Steuerung**
### **Schritt 1: Erstellen eines Webanwendungsprojekts**
Erstellen Sie zunächst ein Webanwendungsprojekt, in dem Sie die Aspose.Cells.GridWeb-Steuerung verwenden:

1. Öffnen Sie Visual Studio.
1. Wählen Sie im Menü **Datei** zunächst **Neu**, gefolgt von **Projekt** aus. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



Ein Dialogfeld für ein neues Projekt wird angezeigt.

1. Wählen Sie die gewünschte Sprache für **ASP.NET-Webanwendung** aus. 

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1. Wählen Sie die Vorlage **Webformulare** aus. 

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Fügen Sie ein neues Webformular dem Projekt hinzu.
### **Schritt 2: Einbetten der Steuerelemente in das Webformular**
Ziehen Sie das Aspose.Cells.GridWeb-Steuerelement aus dem Visual Studio-Toolbox auf das Webformular. 

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

Lesen Sie [Integrieren von Aspose.Cells.Grid-Steuerungselementen mit Visual Studio.NET](/cells/de/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/), um zu erfahren, wie Aspose.Cells Grid-Steuerungselemente zur Visual Studio-Toolbox hinzugefügt werden.

{{% /alert %}} 

Wenn das Steuerelement dem Formular hinzugefügt wurde, wird es so gerendert: 

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Schritt 3: Größenanpassung des Steuerelements**
Das Formular wird standardmäßig in einer bestimmten Größe gerendert. Passen Sie die Größe an, indem Sie die Ränder oder Ecken ziehen. 

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Schritt 4: Festlegen der Steuerelementeigenschaften**
Auch das Aspose.Cells.GridWeb-Steuerelement kann mit verschiedenen Eigenschaften konfiguriert werden. 

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

Es ist möglich, viele Eigenschaften des Steuerelements mit dem Eigenschaften-Dialog anzupassen. Zu den grundlegenden Eigenschaften gehören Höhe, Breite, Farbe und visuelle Stile. Zu den erweiterten Eigenschaften gehören der Bearbeitungsmodus, der Sitzungsmodus und der Doppelklickmodus. Darüber hinaus ist es möglich, benutzerdefinierte Ereignishandler im Eigenschaften-Dialog festzulegen.

Es gibt auch zusätzliche Konfigurationstools für Aspose.Cells.GridWeb, die am unteren Rand des Eigenschaften-Dialogs als Hyperlinks eingesehen werden können oder mit einem Rechtsklick auf das GridWeb-Steuerelement gefunden werden können. Zu diesen Konfigurationstools gehören:

- Benutzerdefinierte Befehlsschaltflächen
#### **Benutzerdefinierte Befehlsschaltflächen**
So öffnen Sie den Editor für benutzerdefinierte Befehlsschaltflächen:
Klicken Sie mit der rechten Maustaste auf das GridWeb-Steuerelement und wählen Sie **Benutzerdefinierte Befehlsschaltflächen**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



Der Dialog für den Editor der CustomCommandButton-Sammlung wird angezeigt. 

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

Der Dialog ermöglicht es Entwicklern, benutzerdefinierte Befehlsschaltflächen im GridWeb-Steuerelement hinzuzufügen und zu entfernen.


### **Wichtig**
Aspose.Cells.GridWeb stellt auch seine Ressourcendateien mit dem Steuerelement bereit. Der Ordner "acw_client" ist ein Verzeichnis, das Dateien enthält, die von Aspose.Cells.GridWeb zur Verwaltung seiner internen Konfiguration und anderer Funktionen verwendet werden. Es enthält Skriptdateien, Bilddateien und andere Dateien zur Spezifizierung des Verhaltens von GridWeb und zur Durchführung anderer Operationen. Die Konfigurationsdatei wird verwendet, um die eingebetteten Client-Ressourcen (Bilder, Skripte usw.) zu verwalten. Darüber hinaus, wenn Sie die Webanwendung mit dem GridWeb-Steuerelement bereitstellen müssen, sollten Sie auch das Verzeichnis "acw_client" in Ihren Projektordner kopieren, da Ihre Webanwendung (deployed over the server) es sonst nicht finden könnte. Sie können den Ressourcenordner jederzeit angeben, indem Sie die folgenden Zeilen Code in den Konfigurationsabschnitt hinzufügen (z. B. in die web.config-Datei in Ihrem VS.NET-Projekt):



|<p>{{< highlight java >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
| :- |


{{% alert color="primary" %}}

Der Pfad ist immer mit dem Verzeichnis des Projekts verbunden. Sie sollten kein Verzeichnis außerhalb des Verzeichnisses des Projekts verwenden. Daher ist es notwendig, das Verzeichnis "acw_client" (in Ihrem GridWeb-Installationsverzeichnis) in das Verzeichnis/Unterverzeichnis des Projekts zu kopieren.

{{% /alert %}}
### **Schritt 5: Webanwendung ausführen**
Führen Sie die Anwendung durch Drücken von Strg+F5 oder Klicken auf die **Start**-Schaltfläche aus. 

Wenn die Anwendung in einem Browser ausgeführt wird, wird die Seite WebForm1.aspx angezeigt, die jetzt eine leere Aspose.Cells.GridWeb-Steuerung enthält. Fügen Sie Werte zu Zellen hinzu, indem Sie auf sie klicken. Es ist auch möglich, andere Aufgaben auszuführen, wie das Ändern der Höhe einer Zeile oder der Breite einer Spalte, das Kopieren (Strg+C) oder Ausschneiden (Strg+X) von Zellendaten in die Zwischenablage und das Einfügen (Strg+V) von Daten in die Zelle. Um weitere Operationen auszuführen, klicken Sie mit der rechten Maustaste auf die Steuerung, um die vollständige Liste der Optionen anzuzeigen. 

**Kontextmenü der GridWeb-Steuerung** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
