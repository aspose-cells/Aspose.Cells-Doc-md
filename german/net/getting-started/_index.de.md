---
title: Erste Schritte
type: docs
weight: 10
url: /de/net/getting-started/
---

{{% alert color="primary" %}} 

Diese Seite zeigt Ihnen, wie Sie Aspose Cells installieren und eine Hallo Welt-Anwendung erstellen.

{{% /alert %}}

## **Installation**

### **Installieren Sie Aspose.Cells über NuGet**

NuGet ist der einfachste Weg, um Aspose.Cells for .NET herunterzuladen und zu installieren. 

1. Öffnen Sie Microsoft Visual Studio und den NuGet-Paket-Manager. 
1. Suchen Sie nach "aspose.cells", um die gewünschte Aspose.Cells for .NET zu finden. 
1. Klicken Sie auf "Installieren", Aspose.Cells for .NET wird heruntergeladen und in Ihr Projekt eingebunden.
**![Aspose.Cells über NuGet installieren](install-through-nuget.png)**

Sie können es auch von der NuGet-Webseite für aspose.cells herunterladen: 
[Aspose.Cells for .NET NuGet-Paket](https://www.nuget.org/packages/Aspose.Cells/)

[Weitere Schritte für Details](/cells/de/net/installation/)

### **Aspose.Cells auf Windows installieren**

1. Laden Sie Aspose.Cells.msi von der folgenden Seite herunter:
[Aspose.Cells.msi herunterladen](https://downloads.aspose.com/cells/net/)
1. Doppelklicken Sie auf das Aspose Cells msi und folgen Sie den Anweisungen, um es zu installieren:

**![Aspose.Cells auf Windows installieren](install-on-windows.png)**

[Weitere Schritte für Details](/cells/de/net/installing-aspose-cells-on-windows/)

### **Aspose.Cells auf Linux installieren**

In diesem Beispiel verwende ich Ubuntu, um zu zeigen, wie Sie Aspose.Cells auf Linux verwenden können.

1. Erstellen Sie eine .netcore-Anwendung namens "AsposeCellsTest".
2. Öffnen Sie die Datei "AsposeCellsTest.csproj" und fügen Sie die folgenden Zeilen für Aspose.Cells-Paketverweise ein:
{{< highlight plain >}}
  <ItemGroup>
    <PackageReference Include="Aspose.Cells" Version="24.7" />
  </ItemGroup>
{{< /highlight >}}
3. Öffnen Sie das Projekt mit VSCode auf Ubuntu:
**![Aspose.Cells auf Linux installieren](install-on-linux.png)**
4. Führen Sie den Test mit folgendem Code aus:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnLinux.cs" >}}

Hinweis: Aspose.Cells For .NetStandard kann Ihre Anforderung auf Linux unterstützen.

Gilt für: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 und höhere Versionen.

### **Aspose.Cells auf MAC OS installieren**

In diesem Beispiel verwende ich macOS High Sierra, um zu zeigen, wie man Aspose.Cells auf MAC OS verwendet.

1. Erstellen Sie eine .netcore-Anwendung namens "AsposeCellsTest".
2. Öffnen Sie die Anwendung mit Visual Studio für Mac und installieren Sie dann Aspose.Cells über NuGet:
**![Aspose Cells auf macOS installieren](install-on-mac-os.png)**
3. Führen Sie den Test mit folgendem Code aus:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-StartOnMacOS.cs" >}}
4. Wenn Sie zeichenbezogene Funktionen verwenden müssen, installieren Sie bitte libgdiplus in macOS. Siehe:
[Wie installiert man libgdiplus in macOS](/cells/de/net/how-to-install-libgdiplus-in-macos/)

Hinweis: Aspose.Cells For .NetStandard kann Ihre Anforderung auf MAC OS unterstützen.

Gilt für: NetStandard2.0, NetCore2.1, NetCore3.1, Net5.0, Net6.0 und höhere Versionen.

### [**Run Aspose Cells in Docker**](/cells/de/net/how-to-run-aspose-cells-in-docker/)

### **Verwendung der Grafikbibliothek auf Nicht-Windows-Plattformen mit Net6**

Aspose.Cells für Net6 verwendet jetzt SkiaSharp als Grafikbibliothek, wie in [offizieller Erklärung von Microsoft](https://github.com/dotnet/designs/blob/f9d006073b7a019bd2021e99c66516447f7fb1a6/accepted/2021/system-drawing-win-only/system-drawing-win-only.md) empfohlen. Für weitere Details zur Verwendung von Aspose.Cells mit NET6 siehe [Wie führt man Aspose.Cells for .Net6 aus](/cells/de/net/how-to-run-aspose-cells-for-net6/).

## **Erstellen der Hello World-Anwendung**

Die folgenden Schritte erstellen die Hello World-Anwendung unter Verwendung der Aspose.Cells API:

1. Wenn Sie eine Lizenz haben, dann [wenden Sie diese an](/cells/de/net/licensing/).
   Wenn Sie die Evaluierungsversion verwenden, überspringen Sie die Lizenz-bezogenen Codezeilen.
1. Erstellen Sie eine Instanz der [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)-Klasse, um eine neue Excel-Datei zu erstellen oder eine vorhandene Excel-Datei zu öffnen.
1. Greifen Sie auf eine beliebige Zelle einer Arbeitsmappe in der Excel-Datei zu.
1. Fügen Sie die Worte **Hallo Welt!** in eine zugängliche Zelle ein.
1. Generieren Sie die modifizierte Microsoft Excel-Datei.

Die Implementierung der obigen Schritte wird in den folgenden Beispielen demonstriert.

### **Codesample: Erstellen einer neuen Arbeitsmappe**

Im folgenden Beispiel wird ein neues Arbeitsblatt von Grund auf erstellt, „Hello World!“ in Zelle A1 im ersten Arbeitsblatt eingefügt und als Excel-Datei gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Codesample: Öffnen einer vorhandenen Datei**

Im folgenden Beispiel wird eine vorhandene Microsoft Excel-Vorlagendatei „Sample.xlsx“ geöffnet, „Hello World!“ in Zelle A1 im ersten Arbeitsblatt eingefügt und als Excel-Datei gespeichert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
