---
title: GridWeb zum Webformular hinzufügen
type: docs
weight: 10
url: /de/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

Dieses Thema enthält eine grundlegende Schritt-für-Schritt-Anleitung für Anfänger, um ihnen beim Erstellen und Verwenden des Aspose.Cells.GridWeb-Steuerelements in Webanwendungen zu helfen.

{{% /alert %}} 
## **Erstellen und Verwenden von Aspose.Cells.GridWeb Control**
### **Schritt 1: Erstellen eines Webanwendungsprojekts**
Erstellen Sie zunächst ein Webanwendungsprojekt, in dem das Aspose.Cells.GridWeb-Steuerelement verwendet werden soll:

1. Öffnen Sie Visual Studio.
1.  Von dem**Datei** Menü, auswählen**Neu** gefolgt von**Projekt**. 

![todo: Bild_alt_Text](add-gridweb-to-web-form_1.png)



Ein Dialogfeld „Neues Projekt“ wird angezeigt.

1.  Auswählen**ASP.NET Webanwendung** für die gewünschte Sprache.

![todo: Bild_alt_Text](add-gridweb-to-web-form_2.png)

1.  Auswählen**Webformulare** Schablone.

![todo: Bild_alt_Text](add-gridweb-to-web-form_3.png)

1. Fügen Sie dem Projekt ein neues Webformular hinzu.
### **Schritt 2: Steuerelement in das Webformular einbetten**
 Ziehen Sie das Aspose.Cells.GridWeb-Steuerelement per Drag & Drop aus der Visual Studio-Toolbox in das Webformular.

![todo: Bild_alt_Text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 Um zu erfahren, wie Sie Aspose.Cells Grid-Steuerelemente zur Visual Studio-Toolbox hinzufügen, lesen Sie bitte[Integrieren Sie Aspose.Cells.Grid Controls mit Visual Studio.NET](/cells/de/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

 Wenn das Steuerelement zum Formular hinzugefügt wurde, wird es wie folgt gerendert:

![todo: Bild_alt_Text](add-gridweb-to-web-form_5.png)
### **Schritt 3: Steuerung der Größenänderung**
Das Formular wird in einer Standardgröße gerendert. Passen Sie die Größe an, indem Sie die Ränder oder Ecken ziehen.

![todo: Bild_alt_Text](add-gridweb-to-web-form_6.png)
### **Schritt 4: Festlegen der Steuerelementeigenschaften**
 Aspose.Cells. GridWeb Control kann auch über verschiedene Eigenschaften konfiguriert werden.

![todo: Bild_alt_Text](add-gridweb-to-web-form_7.png)

Viele Eigenschaften des Steuerelements können über den Eigenschaftendialog angepasst werden. Zu den grundlegenden Eigenschaften gehören Höhe, Breite, Farbe und visuelle Stile. Zu den erweiterten Eigenschaften gehören der Bearbeitungsmodus, der Sitzungsmodus und der Doppelklickmodus. Darüber hinaus ist es möglich, benutzerdefinierte Event-Handler im Eigenschaften-Dialog festzulegen.

Es gibt auch einige zusätzliche Konfigurationstools für Aspose.Cells.GridWeb, die am unteren Rand des Eigenschaftendialogs als Hyperlinks angezeigt werden, oder klicken Sie mit der rechten Maustaste auf das GridWeb-Steuerelement, um sie zu finden. Zu diesen Konfigurationstools gehören:

- Benutzerdefinierte Befehlsschaltflächen
#### **Benutzerdefinierte Befehlsschaltflächen**
So öffnen Sie den Editor für benutzerdefinierte Befehlsschaltflächen:
 Klicken Sie mit der rechten Maustaste auf das GridWeb-Steuerelement, und wählen Sie es aus**Benutzerdefinierte Befehlsschaltflächen**. 

![todo: Bild_alt_Text](add-gridweb-to-web-form_8.png)



 Das Dialogfeld CustomCommandButton Collection Editor wird angezeigt.

![todo: Bild_alt_Text](add-gridweb-to-web-form_9.png)

Das Dialogfeld ermöglicht es Entwicklern, benutzerdefinierte Befehlsschaltflächen im GridWeb-Steuerelement hinzuzufügen und zu entfernen.


### **Wichtig**
Aspose.Cells. GridWeb stellt auch seine Ressourcendateien mit dem Steuerelement bereit. Das „acw_client" ist ein Ordner (@ Ihrem Installationsverzeichnis), der Dateien und Aspose.Cells enthält. GridWeb verwendet diesen Ordner, um seine interne Konfiguration und andere Funktionen zu verwalten, er enthält Skriptdateien, Bilddateien und andere Dateien, um das Verhalten von GridWeb festzulegen und andere Vorgänge festzulegen config-Datei wird verwendet, um die eingebetteten Client-Ressourcen (Bilder, Skripte usw.) zu verwalten. Außerdem würden Sie, wenn Sie die Webanwendung mit GridWeb-Steuerung bereitstellen müssen, auch die Datei „acw_client"-Verzeichnis in Ihren Projektordner, zumindest konnte Ihre Webanwendung (die über den Server bereitgestellt wird) es nicht finden. Sie können den Ressourcenordner jederzeit angeben, indem Sie die folgenden Codezeilen in den Konfigurationsabschnitt einfügen (z. B. in die Datei web.config in Ihrer .config-Datei). VS.NET Projekt):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

Der Pfad bezieht sich immer auf das Projektverzeichnis. Sie sollten kein Verzeichnis außerhalb des Projektverzeichnisses verwenden. Daher ist es notwendig, das Verzeichnis "acw_client" (@ Ihren GridWeb-Installationsordner) in das Verzeichnis/Unterverzeichnis des Projekts zu kopieren.

{{% /alert %}}
### **Schritt 5: Ausführen der Webanwendung**
 Führen Sie die Anwendung aus, indem Sie Strg+F5 drücken oder auf klicken**Anfang** Taste.

 Wenn die Anwendung in einem Browser ausgeführt wird, wird die Seite WebForm1.aspx angezeigt, die jetzt ein leeres Aspose.Cells.GridWeb-Steuerelement enthält. Fügen Sie Zellen Werte hinzu, indem Sie darauf klicken. Es ist auch möglich, andere Aufgaben auszuführen, wie z. B. das Ändern der Höhe einer Zeile oder der Breite einer Spalte, das Kopieren (Strg+C) oder Ausschneiden (Strg+X) von Zelldaten in die Zwischenablage und das Einfügen (Strg+V) von Daten in die Zelle . Um weitere Vorgänge auszuführen, klicken Sie mit der rechten Maustaste auf das Steuerelement, um die vollständige Liste der Optionen anzuzeigen.

**Kontextmenü des GridWeb-Steuerelements** 

![todo: Bild_alt_Text](add-gridweb-to-web-form_10.png)
