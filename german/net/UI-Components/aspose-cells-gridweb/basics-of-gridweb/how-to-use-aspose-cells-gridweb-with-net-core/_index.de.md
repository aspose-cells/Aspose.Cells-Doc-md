---
title: Wie man Aspose.Cells.GridWeb mit .NET Core verwendet
type: docs
weight: 40
url: /de/net/aspose-cells-gridweb/how-to-use-aspose-cells-gridweb-with-net-core/
keywords: GridWeb,dotnetcore
description: Dieser Artikel führt ein, wie man GridWeb in einer .NET Core Webanwendung verwendet
---

{{% alert color="primary" %}} 

Dieses Thema erläutert, wie man Aspose.Cells.GridWeb mit .NET Core-Anwendungen unter Verwendung von Visual Studio.NET 2019 verwendet. Dieses Thema ist nützlich für Einsteiger-Entwickler, die mit Aspose.Cells.GridWeb arbeiten.

{{% /alert %}} 
## **Verwenden Sie Aspose.Cells.GridWeb mit .NET Core**
Dieses Thema zeigt, wie man Aspose.Cells.GridWeb durch die Erstellung einer Beispielseite in Visual Studio 2019 verwendet. Der Prozess wurde in Schritte unterteilt.
### **Schritt 1: Ein neues Projekt erstellen**
1. Öffnen Sie Visual Studio 2019.
1. Wählen Sie im **Datei**-Menü **Neu** und dann **Projekt** aus.
   Ein Dialogfeld zur Erstellung eines neuen Projekts wird geöffnet.
1. Wählen Sie **ASP.NET Core-Webanwendung** aus den installierten Projektvorlagen von Visual Studio und klicken Sie auf **Weiter**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1. Geben Sie einen Speicherort an, wo sich der Ort und der Name des Projekts befinden, und klicken Sie auf **Erstellen**.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1. Wählen Sie die Vorlage **Webanwendung (Modell-Präsentations-Steuerung)** aus und stellen Sie sicher, dass **ASP .NET Core 2.1** ausgewählt ist. 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1. Klicken Sie auf **Erstellen**.
### **Schritt 2: Überprüfen der ersten Ansicht**
Wenn das neu erstellte Projekt ausgeführt wird, wird die Standardvorlage im Browser wie im folgenden Bild gezeigt.



![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Schritt 3: Hinzufügen von Aspose.Cells.GridWeb**
1. Fügen Sie dem Projekt die folgenden NuGet-Pakete hinzu

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Fügen Sie das Aspose.Cells.GridWeb-Paket hinzu

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Fügen Sie folgendes in die Datei **_ViewImports.cshtml** im Views-Ordner ein.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Die Datei wird nach den Änderungen wie folgt aussehen

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Fügen Sie den folgenden Code in die Index-Methode des HomeController ein.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Denken Sie daran, den SessionStorePath und den ImportExcelFile-Pfad zu aktualisieren.

{{% /alert %}} 

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1. Fügen Sie den folgenden Code in die Datei **Index.cshtml** im Ansicht > Home-Verzeichnis ein.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Die Datei wird nach der Änderung wie folgt aussehen.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Fügen Sie Sessionunterstützung und GridScheduedService in die Startup.cs-Datei ein.
   1. Fügen Sie den folgenden Code-Schnipsel in der Methode ConfigureServices hinzu.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Fügen Sie den folgenden Code-Schnipsel in der Methode Configure hinzu.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Legen Sie den neuesten acw_client im Verzeichnis ab: **wwwroot/js** {{% alert color="primary" %}}   {{% /alert %}}
1. Fügen Sie **AcwController** in den Controllern hinzu, um die acw-Route zu behandeln, die alle Standardoperationen für die allgemeine Bearbeitungsaktionen bereitstellen kann.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Schritt 4: Testen der App**
Das Ausführen der App ergibt eine Ausgabe ähnlich der unten gezeigten Abbildung.

![todo:image_alt_text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
