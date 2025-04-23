---
title: Installieren Sie Aspose Cells über NuGet
type: docs
weight: 30
url: /de/net/installation/
---


## **Installieren Sie Aspose.Cells for .NET über NuGet**
NuGet ist der einfachste Weg, um Aspose APIs für .NET herunterzuladen und zu installieren. Öffnen Sie Microsoft Visual Studio und den NuGet-Paket-Manager. Suchen Sie "aspose", um die gewünschte Aspose-API zu finden. Klicken Sie auf "Installieren", die ausgewählte API wird heruntergeladen und in Ihrem Projekt referenziert.

Hinweis: Sie können die NuGet-Website für aspose.cells für weitere Informationen besuchen: 
[Aspose.Cells for .NET NuGet-Paket](https://www.nuget.org/packages/Aspose.Cells/)

### **Installieren Sie Aspose.Cells mithilfe des Paket-Manager-GUI**
Befolgen Sie diese Schritte, um das Aspose.Cells-Komponente mithilfe des Paket-Manager-GUI zu referenzieren:

- Öffnen Sie Ihre Lösung/Ihr Projekt in Visual Studio.
- Klicken Sie auf  **Tools**  ->  **Paket-Manager-Bibliothek**  ->  **NuGet-Pakete verwalten** aus der Lösung. Sie können auch einfach auf das gleiche Symbol über den Solution Explorer zugreifen. Klicken Sie mit der rechten Maustaste auf die Lösung oder das Projekt und wählen Sie **NuGet-Pakete verwalten** im Kontextmenü.
- Wählen Sie  **Online**  im linken Menü aus und geben Sie "Aspose.Cells" in das Suchfeld ein, um das Aspose.Cells .NET-Paket zu finden.
- Klicken Sie auf die Schaltfläche **Installieren** neben dem Eintrag Aspose.Cells for .NET, um die neueste Version in Ihr Projekt zu installieren.
### **Installieren Sie Aspose.Cells mithilfe der Paket-Manager-Konsole.**
Sie können die folgenden Schritte befolgen, um das Aspose.Cells-Komponente mithilfe der Paket-Manager-Konsole zu referenzieren:

- Öffnen Sie Ihre Lösung/Ihr Projekt in Visual Studio.
- Wählen Sie **Tools** -> **Paket-Manager** -> **Paket-Manager-Konsole** im Menü aus, um die Paket-Manager-Konsole zu öffnen.
  - Geben Sie den Befehl "Install-Package Aspose.Cells" ein und drücken Sie die Eingabetaste, um die neueste Vollversion in Ihre Anwendung zu installieren. Alternativ können Sie dem Befehl das Suffix "-Prerelease" hinzufügen, um anzugeben, dass auch die neueste Version mit Hotfixes installiert werden soll.
- Sie sehen, dass der Hinweis "Aspose.Cells herunterladen ..." unten links im Fenster erscheint und der Downloadvorgang läuft.
- Sobald der Download abgeschlossen ist, sehen Sie die folgenden Bestätigungsmeldungen. Wenn Sie nicht mit der Aspose EULA vertraut sind, ist es eine gute Idee, die Lizenz unter der angegebenen URL zu lesen.
- Jetzt sollten Sie feststellen, dass Aspose.Cells erfolgreich zu Ihrer Anwendung hinzugefügt und referenziert wurde.
## **Referenzieren von Aspose.Cells aus einem .NET-Projekt**
Um Aspose.Cells in einer Anwendung zu verwenden, fügen Sie eine Referenz hinzu. Um eine Referenz mithilfe von Visual Studio hinzuzufügen:

1. Im **Lösungs-Explorer** den Projektordner auswählen, zu dem Sie eine Referenz hinzufügen möchten.
1. Klicken Sie mit der rechten Maustaste auf den **Verweise**-Knoten für das Projekt und wählen Sie aus dem Menü **Verweis hinzufügen**.
1. Wählen Sie im Dialogfeld **Verweis hinzufügen** den .NET-Tab (standardmäßig ausgewählt). Wenn Sie den MSI-Installer verwendet haben, erscheint Aspose.Cells im oberen Bereich.
1. Wählen Sie es aus und klicken Sie auf **Auswählen**.

Wenn Sie die DLL heruntergeladen oder entpackt haben:

1. Suchen Sie die Datei Aspose.Cells.dll mithilfe der Schaltfläche **Durchsuchen**. Aspose.Cells sollte im **Ausgewählte Komponenten**-Bereich des Dialogfelds erscheinen.
1. Klicken Sie auf **OK**. Die Aspose.Cells-Referenz erscheint unter dem **Verweise**-Knoten des Projekts.
### **Referenzierung der Komponente aus einem VS.NET 2010-Clientprofil-Projekt**
Wenn das Zielrahmenwerk Ihres Projekts .NET Framework 3.5/4 Clientprofil ist, verwenden Sie die Aspose.Cells.dll-Komponentendatei im net_ClientProfile-Ordner Ihres Installationsverzeichnisses. Zum Beispiel:

- Im **Lösung-Explorer** von VS.NET 2010 für Ihr Projekt mit der rechten Maustaste auf **Verweise** klicken und **Verweis hinzufügen** auswählen.
- Wählen Sie die Registerkarte **Durchsuchen** im Dialogfeld und klicken Sie auf den Dropdown-Pfeil Suchen.
- Suchen und wählen Sie die Aspose.Cells.dll-Komponentendatei in Ihrem Installationsverzeichnis, zum Beispiel: .../Programme/Aspose/Aspose.Cells for .NET/Bin/net_ClientProfile/ **(Stellen Sie sicher, dass Sie das Produkt mit dem MSI-Installationsprogramm auf Ihrem Computer installiert haben.)**
- Klicken Sie auf **OK**, um das Dialogfeld zu schließen.

{{% alert color="primary" %}} 

Wenn das Ziel Framework Ihres VS.NET 2010-Projekts " .NET Framework 4" oder ein anderes ist, verwenden Sie einfach die Aspose.Cells.dll-Komponentendatei im net4.0/net2.0-Ordner.

{{% /alert %}} 
## **Verweisen auf Aspose.Cells Grid-Steuerungen aus einem .NET-Projekt**
Um eine Rastersteuerung in Ihrer Anwendung zu verwenden, fügen Sie einen Verweis darauf hinzu. Um eine Rastersteuerung in Visual Studio zu referenzieren, gehen Sie wie folgt vor:

- Im **Lösung-Explorer** expandieren Sie den Projektknoten, für den Sie einen Verweis hinzufügen möchten.
- Klicken Sie mit der rechten Maustaste auf den **Verweise**-Knoten für das Projekt und wählen Sie **Verweis hinzufügen** im Menü aus.
- Wählen Sie im Dialogfeld **Verweis hinzufügen** das **.NET-Tab** (standardmäßig ausgewählt). Wenn Sie das MSI-Installationsprogramm verwendet haben, um Aspose.Cells for .NET zu installieren, erscheinen Aspose.Cells.GridDesktop und Aspose.Cells.GridWeb im oberen Bereich.
- Wählen Sie sie aus und klicken Sie auf **Auswählen**.
- Die Verweise auf Aspose.Cells.GridDesktop und Aspose.Cells.GridWeb erscheinen unter dem Verweise-Knoten des Projekts.

Wenn Sie nur die DLL heruntergeladen und entpackt haben:

- Suchen Sie die Dateien Aspose.Cells.GridDesktop.dll und Aspose.Cells.GridWeb.dll mit der Schaltfläche Durchsuchen. Aspose.Cells Grid Suite wurde referenziert und sollte im **Ausgewählte Komponenten**-Bereich des Dialogfelds erscheinen.
- Klicken Sie auf **OK**.
## **Deinstallieren von Aspose.Cells for .NET**
Wenn Sie das MSI-Installationsprogramm verwendet haben, um Aspose.Cells for .NET zu installieren, befolgen Sie diese Schritte, um die Komponente und die Steuerungen, die zugehörigen Demos und Dokumentationen vollständig zu entfernen:

- Wählen Sie im **Start**-Menü **Einstellungen** aus, gefolgt von **Systemsteuerung**.
- Klicken Sie auf **Programme hinzufügen/entfernen**.
- Wählen Sie Aspose.Cells for .NET (Version) aus.
- Klicken Sie auf **Ändern/Entfernen**, um Aspose.Cells zu entfernen.
{{< app/cells/assistant language="csharp" >}}
