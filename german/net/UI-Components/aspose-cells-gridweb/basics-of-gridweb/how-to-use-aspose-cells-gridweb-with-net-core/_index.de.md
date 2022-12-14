---
title: So verwenden Sie Aspose.Cells.GridWeb mit .NET Core
type: docs
weight: 40
url: /de/net/how-to-use-aspose-cells-gridweb-with-net-core/
---
{{% alert color="primary" %}} 

In diesem Thema wird erläutert, wie Aspose.Cells.GridWeb mit .NET Core-Anwendungen unter Verwendung von Visual Studio.NET 2019 verwendet wird. Dieses Thema ist nützlich für Entwickler auf Anfängerniveau, die mit Aspose.Cells.GridWeb arbeiten.

{{% /alert %}} 
## **Verwenden Sie Aspose.Cells.GridWeb mit .NET Core**
In diesem Thema wird gezeigt, wie Sie Aspose.Cells.GridWeb verwenden, indem Sie eine Beispielwebsite in Visual Studio 2019 erstellen. Der Prozess wurde in Schritte unterteilt.
### **Schritt 1: Erstellen eines neuen Projekts**
1. Öffnen Sie Visual Studio 2019.
1.  Von dem**Datei** Menü, auswählen**Neu** , dann**Projekt**.
 Der Dialog Neues Projekt erstellen wird geöffnet.
1.  Auswählen**ASP.NET Core-Webanwendung** aus Visual Studio installierten Projektvorlagen und klicken Sie auf**Nächste**.

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_1.jpg)

1.  Geben Sie einen Ort an, wo der Ort und der Name des Projekts und klicken Sie auf**Schaffen**.

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_2.jpg)

1.  Wähle aus**Webanwendung (Model-View-Controller)** Vorlage und stellen Sie sicher, dass**ASP .NET Kern 2.1** ist ausgewählt.

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_3.jpg)

1.  Klicken**Schaffen**.
### **Schritt 2: Überprüfung der Ausgangsansicht**
Beim Ausführen des neu erstellten Projekts wird die Standardvorlage im Browser angezeigt, wie in der Abbildung unten gezeigt.



![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_4.jpg)
### **Schritt 3: Hinzufügen von Aspose.Cells.GridWeb**
1. Fügen Sie dem Projekt die folgenden Nuget-Pakete hinzu

<PackageReference Include="Microsoft.AspNetCore.App" />
<PackageReference Include="Microsoft.AspNetCore.Razor.Design" Version="2.1.2" PrivateAssets="All" />
<PackageReference Include="Newtonsoft.Json" Version="12.0.3" />
<PackageReference Include="System.Drawing.Common" Version="4.7.0" />
<PackageReference Include="System.Text.Encoding.CodePages" Version="4.7.0" />

1. Fügen Sie das Paket Aspose.Cells.GridWeb hinzu

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_5.jpg)

1. Fügen Sie Folgendes zur Datei **_ViewImports.cshtml** im Ordner „Views“ hinzu.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-ViewImports.cs" >}}

Die Datei sieht nach den Änderungen so aus

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_6.jpg)

1. Fügen Sie den folgenden Code in die Index-Methode des HomeControllers ein.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-HomeController.cs" >}}

{{% alert color="primary" %}} 

Denken Sie daran, den SessionStorePath und den ImportExcelFile-Pfad zu aktualisieren.

{{% /alert %}} 

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_7.jpg)

1.  Fügen Sie den folgenden Code in die**Index.cshtml** Datei im Verzeichnis View > Home.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-IndexView.cs" >}}

Die Datei sieht nach der Änderung so aus.

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_8.jpg)

1. Fügen Sie Sitzungsunterstützung und GridScheduedService in der Datei „Startup.cs“ hinzu
 1. Fügen Sie den folgenden Codeausschnitt in der ConfigureServices-Methode hinzu.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup1.cs" >}}

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_9.jpg)

1. Fügen Sie den folgenden Codeausschnitt in der Configure-Methode hinzu.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-Startup2.cs" >}}

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_10.jpg)

1. Legen Sie den neuesten acw_client im Verzeichnis ab: **wwwroot/js** {{% alert color="primary" %}} {{% /alert %}}
1.  Hinzufügen**AcwController**in Controllern, um mit der acw-Routenkarte umzugehen, die alle Standardoperationen für allgemeine Bearbeitungsaktionen bereitstellen kann.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "GridWebCore-AcwController.cs" >}}

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_11.jpg)
### **Schritt 4: Testen Sie die App**
Beim Ausführen der App wird die Ausgabe ähnlich der im Bild unten gezeigten ausgegeben.

![todo: Bild_alt_Text](how-to-use-aspose-cells-gridweb-with-net-core_12.jpg)
