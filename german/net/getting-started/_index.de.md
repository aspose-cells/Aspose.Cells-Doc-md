---
title: Einstieg
type: docs
weight: 10
url: /de/net/getting-started/
---
{{% alert color="primary" %}} 

Auf dieser Seite erfahren Sie, wie Sie Aspose Cells installieren und eine Hello World-Anwendung erstellen.

{{% /alert %}}

## **Installation**

### **Installieren Sie Aspose.Cells bis NuGet**

 NuGet ist der einfachste Weg, Aspose.Cells for .NET herunterzuladen und zu installieren.

1.  Öffnen Sie Microsoft Visual Studio und NuGet Paket-Manager.
1.  Suchen Sie nach "aspose.cells", um die gewünschte Aspose.Cells for .NET zu finden.
1. Klicken Sie auf „Installieren“, Aspose.Cells for .NET wird heruntergeladen und in Ihrem Projekt referenziert.
**![Installieren Sie Aspose Cells bis NuGet](install-through-nuget.png)**

 Sie können es auch von der nuget-Webseite für aspose.cells herunterladen:
[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/)

[Mehr Schritt für Details](/cells/de/net/installation/)

### **Installieren Sie Aspose.Cells unter Windows**

1. Laden Sie Aspose.Cells.msi von der folgenden Seite herunter:
[Laden Sie Aspose.Cells.msi herunter](https://downloads.aspose.com/cells/net/)
1. Doppelklicken Sie auf die MSI-Datei Aspose Cells und befolgen Sie die Anweisungen zur Installation:

**![Installieren Sie Aspose Cells unter Windows](install-on-windows.png)**

[Mehr Schritt für Details](/cells/de/net/installing-aspose-cells-on-windows/)

### **Installieren Sie Aspose.Cells unter Linux**

In diesem Beispiel verwende ich Ubuntu, um zu zeigen, wie man mit der Verwendung von Aspose.Cells unter Linux beginnt.

1. Erstellen Sie eine .netcore-Anwendung namens „AsposeCellsTest“.
2. Öffnen Sie die Datei "AsposeCellsTest.csproj", fügen Sie die folgenden Zeilen für Aspose.Cells-Paketverweise hinzu:
{{< highlight "plain" >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="22.12" />
  </ItemGroup>
{{< /highlight >}}
3. Öffnen Sie das Projekt mit VSCode auf Ubuntu:
**![Installieren Sie Aspose Cells unter Linux](install-on-linux.png)**
4. Test mit folgendem Code ausführen:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Hinweis: Aspose.Cells für .NetStandard kann Ihre Anforderung unter Linux unterstützen.

Gilt für: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 und erweiterte Version.

### **Installieren Sie Aspose.Cells unter MAC OS**

In diesem Beispiel verwende ich macOS High Sierra, um zu zeigen, wie man mit der Verwendung von Aspose.Cells unter MAC OS beginnt.

1. Erstellen Sie eine .netcore-Anwendung namens „AsposeCellsTest“.
2. Öffnen Sie die Anwendung mit Visual Studio für Mac und installieren Sie dann Aspose Cells bis NuGet:
**![Installieren Sie Aspose Cells unter macOS](install-on-mac-os.png)**
3. Test mit folgendem Code ausführen:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Wenn Sie zeichnungsbezogene Funktionen verwenden müssen, installieren Sie bitte libgdiplus in macOS, siehe:
[So installieren Sie libgdiplus unter macOS](/cells/de/net/how-to-install-libgdiplus-in-macos/)

Hinweis: Aspose.Cells für .NetStandard kann Ihre Anforderung auf MAC OS unterstützen.

Gilt für: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 und erweiterte Version.

### **[Aspose Cells in Docker ausführen](/cells/net/how-to-run-aspose-cells-in-docker/)**

### **So verwenden Sie die Grafikbibliothek auf Nicht-Windows-Plattformen mit Net6**

 Aspose.Cells für Net6 verwendet jetzt SkiaSharp als Grafikbibliothek, wie in empfohlen[offizielle Erklärung von Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) . Weitere Einzelheiten zur Verwendung von Aspose.Cells mit NET6 finden Sie unter[So führen Sie Aspose.Cells für .Net6 aus](/cells/de/net/how-to-run-aspose-cells-for-net6/).

## **Erstellen der Hello World-Anwendung**

Die folgenden Schritte erstellen die Hello World-Anwendung unter Verwendung der Aspose.Cells API:

1.  Wenn Sie eine Lizenz haben, dann[Wende es an](/cells/de/net/licensing/).
 Wenn Sie die Evaluierungsversion verwenden, überspringen Sie die lizenzbezogenen Codezeilen.
1.  Erstellen Sie eine Instanz der[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse, um eine neue Excel-Datei zu erstellen, oder öffnen Sie eine vorhandene Excel-Datei.
1. Greifen Sie in der Excel-Datei auf eine beliebige Zelle eines Arbeitsblatts zu.
1.  Füge die Wörter ein**Hello World!** in eine zugegriffene Zelle.
1. Generieren Sie die geänderte Excel-Datei Microsoft.

Die Implementierung der obigen Schritte wird in den folgenden Beispielen demonstriert.

### **Codebeispiel: Erstellen einer neuen Arbeitsmappe**

Das folgende Beispiel erstellt eine neue Arbeitsmappe von Grund auf, fügt "Hello World!" in Zelle A1 im ersten Arbeitsblatt und speichert es als Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Codebeispiel: Öffnen einer vorhandenen Datei**

Das folgende Beispiel öffnet eine vorhandene Microsoft Excel-Vorlagendatei "Sample.xlsx", fügt "Hello World!" in Zelle A1 im ersten Arbeitsblatt und speichert es als Excel-Datei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
