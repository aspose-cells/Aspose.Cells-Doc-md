---
title: Erste Schritte
type: docs
weight: 10
url: /de/net/getting-started/
---
{{% alert color="primary" %}} 

Auf dieser Seite erfahren Sie, wie Sie Aspose Cells installieren und eine Hello World-Anwendung erstellen.

{{% /alert %}}

##  **Installation**

###  **Installieren Sie Aspose.Cells bis NuGet**

 NuGet ist der einfachste Weg, Aspose.Cells for .NET herunterzuladen und zu installieren.

1.  Öffnen Sie Microsoft Visual Studio und NuGet Paketmanager.
1.  Durchsuchen Sie „aspose.cells“, um die gewünschte Aspose.Cells for .NET zu finden.
1. Klicken Sie auf „Installieren“. Aspose.Cells for .NET wird heruntergeladen und in Ihrem Projekt referenziert.
**![Aspose Cells bis NuGet installieren](install-through-nuget.png)**

 Sie können es auch von der Webseite nuget für aspose.cells herunterladen:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

[Weitere Schritte für Details](/cells/de/net/installation/)

###  **Installieren Sie Aspose.Cells unter Windows**

1. Laden Sie Aspose.Cells.msi von der folgenden Seite herunter:
[Laden Sie Aspose.Cells.msi herunter](https://downloads.aspose.com/cells/net/)
1. Doppelklicken Sie auf die MSI-Datei Aspose Cells und befolgen Sie die Anweisungen, um sie zu installieren:

**![Aspose Cells unter Windows installieren](install-on-windows.png)**

[Weitere Schritte für Details](/cells/de/net/installing-aspose-cells-on-windows/)

###  **Installieren Sie Aspose.Cells unter Linux**

In diesem Beispiel verwende ich Ubuntu, um zu zeigen, wie man Aspose.Cells unter Linux verwendet.

1. Erstellen Sie eine .netcore-Anwendung mit dem Namen „AsposeCellsTest“.
2. Öffnen Sie die Datei „AsposeCellsTest.csproj“ und fügen Sie die folgenden Zeilen für Aspose.Cells-Paketreferenzen hinzu:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="23.12" />
  </ItemGroup>
{{< /highlight >}}
3. Öffnen Sie das Projekt mit VSCode unter Ubuntu:
**![Aspose Cells unter Linux installieren](install-on-linux.png)**
4. Führen Sie den Test mit dem folgenden Code aus:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Hinweis: Aspose.Cells Für .NetStandard kann Ihre Anforderung unter Linux unterstützt werden.

Gilt für: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 und die erweiterte Version.

###  **Installieren Sie Aspose.Cells unter MAC OS**

In diesem Beispiel verwende ich macOS High Sierra, um zu zeigen, wie man mit der Verwendung von Aspose.Cells unter MAC OS beginnt.

1. Erstellen Sie eine .netcore-Anwendung mit dem Namen „AsposeCellsTest“.
2. Öffnen Sie die Anwendung mit Visual Studio für Mac und installieren Sie dann Aspose Cells bis NuGet:
**![Aspose Cells unter macOS installieren](install-on-mac-os.png)**
3. Führen Sie den Test mit dem folgenden Code aus:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Wenn Sie zeichnungsbezogene Funktionen verwenden müssen, installieren Sie bitte libgdiplus in macOS, siehe:
[So installieren Sie libgdiplus unter macOS](/cells/de/net/how-to-install-libgdiplus-in-macos/)

Hinweis: Aspose.Cells Für .NetStandard kann Ihre Anforderung unter MAC OS unterstützt werden.

Gilt für: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 und die erweiterte Version.

###  **[Aspose Cells in Docker ausführen](/cells/net/how-to-run-aspose-cells-in-docker/)**

###  **So verwenden Sie die Grafikbibliothek auf Nicht-Windows-Plattformen mit Net6**

 Aspose.Cells für Net6 verwendet jetzt SkiaSharp als Grafikbibliothek, wie in empfohlen[offizielle Stellungnahme von Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Weitere Einzelheiten zur Verwendung von Aspose.Cells mit NET6 finden Sie unter[So führen Sie Aspose.Cells für .Net6 aus](/cells/de/net/how-to-run-aspose-cells-for-net6/).

##  **Erstellen der Hello World-Anwendung**

Mit den folgenden Schritten wird die Anwendung Hello World unter Verwendung von Aspose.Cells API erstellt:

1.  Wenn Sie eine Lizenz haben, dann[Wende es an](/cells/de/net/licensing/).
 Wenn Sie die Testversion verwenden, überspringen Sie die lizenzbezogenen Codezeilen.
1.  Erstellen Sie eine Instanz von[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, um eine neue Excel-Datei zu erstellen oder eine vorhandene Excel-Datei zu öffnen.
1. Greifen Sie auf jede gewünschte Zelle eines Arbeitsblatts in der Excel-Datei zu.
1.  Fügen Sie die Wörter ein**Hello World!** in eine Zelle, auf die zugegriffen wird.
1. Generieren Sie die geänderte Excel-Datei Microsoft.

Die Umsetzung der oben genannten Schritte wird in den folgenden Beispielen demonstriert.

###  **Codebeispiel: Erstellen einer neuen Arbeitsmappe**

Das folgende Beispiel erstellt eine neue Arbeitsmappe von Grund auf und fügt „Hello World!“ ein. in Zelle A1 im ersten Arbeitsblatt eingefügt und als Excel-Datei gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Codebeispiel: Öffnen einer vorhandenen Datei**

Das folgende Beispiel öffnet eine vorhandene Microsoft Excel-Vorlagendatei „Sample.xlsx“ und fügt „Hello World!“ ein. in Zelle A1 im ersten Arbeitsblatt eingefügt und als Excel-Datei gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
