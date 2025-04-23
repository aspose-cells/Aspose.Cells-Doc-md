---
title: Wie führt man Aspose.Cells in Blazor aus
type: docs
weight: 138
url: /de/net/how-to-run-aspose-cells-in-blazor/
description: Lernen Sie, wie man Aspose.Cells in Blazor WebAssembly und Blazor Server Apps ausführt.
keywords: C# Ausführung von Aspose.Cells in Blazor WebAssembly, Nutzung von Aspose.Cells in Blazor WebAssembly, Blazor WebAssembly Anwendung mit Aspose.Cells
---

## Übersicht

Blazor ist ein Web-Framework, das von Microsoft entwickelt wurde und es Entwicklern ermöglicht, interaktive, clientseitige Webanwendungen mit C# und .NET anstelle von JavaScript zu erstellen. Blazor kommt in zwei Haupt-Hosting-Modellen: **Blazor WebAssembly** und **Blazor Server**. Sie können **Aspose.Cells for .NET** direkt in beiden Modellen verwenden.

## Blazor WebAssembly-Anwendung mit Aspose.Cells

Blazor WebAssembly läuft clientseitig im Browser mit WebAssembly. Es ermöglicht Entwicklern, .NET-Anwendungen direkt im Browser auszuführen, ohne auf einen Server zum Rendern angewiesen zu sein. Ab **Aspose.Cells for .NET 25.1** kann Aspose.Cells direkt in der Blazor WebAssembly-App verwendet werden. In diesem Beispiel erstellen Sie eine einfache Blazor WebAssembly mit Aspose.Cells, rendern eine Excel-Datei mit Text und Formen in ein PNG-Bild und zeigen das Bild auf einer Seite an.

### Erstellen Sie eine Blazor WebAssembly-App

Lassen Sie uns am Beispiel des VS2022-Tools eine erste Blazor WebAssembly-App mit Aspose.Cells erstellen, folgen Sie den nachstehenden Schritten:

1. Erstellen Sie ein neues Projekt mit der Vorlage **Blazor WebAssembly Standalone App**.

   ![webassembly_projekt_template.jpg](webassembly_projekt_template.jpg)

2. Wählen Sie das Ziel-Framework, empfohlen .NET 8.0 oder höher.

   ![webassembly_framework_net9.jpg](webassembly_framework_net9.jpg)

3. Nach der Erstellung des Projekts, fügen Sie das Aspose.Cells Paket zum Projekt hinzu. Da Aspose.Cells auf SkiaSharp verweist, ist das "SkiaSharp.Views.Blazor" Paket erforderlich, um SkiaSharp in WebAssembly zum Laufen zu bringen.

   ```
   <PackageReference Include="Aspose.Cells" Version="25.1.1" />
   <PackageReference Include="SkiaSharp.Views.Blazor" Version="3.116.1" />
   ```

   *Bitte beachten Sie, dass die Version des hinzugefügten Pakets "SkiaSharp.Views.Blazor" mit der Version von "SkiaSharp" übereinstimmen sollte, die durch Aspose.Cells for .NET referenziert wird. Die Versionen von Aspose.Cells for .NET und die entsprechenden referenzierten "SkiaSharp" Versionen sind wie folgt beschrieben:*

   | Aspose.Cells for .NET |                SkiaSharp                |
   | :-------------------: | :-------------------------------------: |
   |       = 25.1.1        |                 3.116.1                 |
   |       >=25.1.2        | 2.88.9(net6.0, net8.0), 3.116.1(net9.0) |

4. Navigieren Sie zur Datei "Home.razor" im Ordner "Pages" im Projekt, fügen Sie Code hinzu, um einige Daten und Formen zu erstellen, und rendern Sie diese in ein Bild zur Anzeige.

   ![webassembly_code.jpg](webassembly_code.jpg)

5. Klicken Sie mit der rechten Maustaste auf das Projekt und wählen Sie "Veröffentlichen...", und veröffentlichen Sie das Projekt in einen Ordner mit oder ohne AOT-Option.

   ![webassembly_publish.jpg](webassembly_publish.jpg)

6. Nach der Veröffentlichung befinden sich die Ausgabedateien im Ordner `publish/wwwroot`. Diese Dateien sind statische Dateien (HTML, JS, CSS usw.), so dass sie gehostet werden können über:

   - **Lokaler Webserver** (z.B. `dotnet serve`, `nginx` oder `Apache`).
   - **Cloud-Hosting** (z.B. Azure, AWS, Netlify, GitHub Pages).

   Nehmen wir `dotnet serve` als Beispiel:

   - Installieren Sie das Tool `dotnet-serve` (falls noch nicht installiert):

     ```bash
     dotnet tool install -g dotnet-serve
     ```

   - Navigieren Sie zum veröffentlichten `wwwroot`-Verzeichnis.

   - Starten Sie den Server:

     ```bash
     dotnet serve
     ```

7. Öffnen Sie Ihren Browser und besuchen Sie die angezeigte Adresse (z.B. `http://localhost:1970`), das Ausgabebild wird auf der Seite angezeigt.

   ![webassembly_output.jgp](webassembly_output.jpg)

### Beispielcode in Blazor WebAssembly-Anwendung

Der folgende Beispielcode ist in der Datei Home.razor enthalten:

```cs
@page "/"
@using Aspose.Cells
@using Aspose.Cells.Drawing
@using Aspose.Cells.Rendering

<PageTitle>Home</PageTitle>

<h1>Aspose.Cells works in Blazor WebAssembly App</h1>

@if (imageSrc is not null)
{
    <img src="@imageSrc" alt="Output Image" style="float: left; margin-right: 10px;" />
}
else
{
    <p>Loading image...</p>
}

@code
{
    private string? imageSrc;

    protected override void OnInitialized()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "Aspose.Cells works in Blazor WebAssembly App!";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}
```

### Problembehandlung

Currently(Jan 2025) there is a known issue of `dotnet` in the case that publishing a Blazor WebAssembly project which targets to net8.0 with .NET 9.0 SDK(.NET 9.0 SDK is installed and .NET 8.0 SDK is uninstalled if you upgraded Visual Studio to the version v17.12.x). For more info, check the link: <https://github.com/dotnet/runtime/issues/109951>.

```
System.PlatformNotSupportedException: PlatformNotSupported_HybridGlobalization, HashCode
   at System.Globalization.CompareInfo.GetHashCodeOfStringCore(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(ReadOnlySpan`1 , CompareOptions )
   at System.Globalization.CompareInfo.GetHashCode(String , CompareOptions )
   at System.CultureAwareComparer.GetHashCode(String )
   at System.StringComparer.GetHashCode(Object )
```

Wenn dies Ihr Fall ist, gibt es drei Optionen zur Auswahl:

1. Installieren Sie das .NET 8.0 SDK neu (falls deinstalliert) und verwenden Sie eine "global.json"-Datei auf Projektebene (im selben Ordner wie die .sln-Datei), um das verwendete SDK anzugeben. Hier ist ein Beispiel für eine "global.json"-Datei:

   ```
   {
     "sdk": {
       "version": "8.0.300",
       "rollForward": "latestFeature"
     }
   }
   ```



2. Aktualisieren Sie die Projektdatei, um targeting net9.0.

3. Update Visual Studio to the version v17.12.4.(The issue <https://github.com/dotnet/runtime/issues/109951> is fixed.(updated on Jan 15, 2025))

## Blazor Server-Anwendung mit Aspose.Cells

In diesem Beispiel erstellen Sie eine einfache Blazor-Server-App, die einige Daten und Grafiken hinzufügt und sie in Bilder rendert, um auf der Webseite angezeigt werden zu können. Bei der Projektentwicklung können Sie die Optionen nach Ihren Bedürfnissen konfigurieren. Wenn Sie z.B. die Option "Docker aktivieren" auswählen, kann die Blazor-Anwendung in Docker gebaut und ausgeführt werden.

### Erstellen Sie eine Blazor-Serveranwendung

Verwenden wir das VS2022-Tool als Beispiel, um die erste Blazor-Server-App mit Aspose.Cells zu erstellen, folgen Sie den folgenden Schritten:
1. Wählen Sie Datei ->Neu ->Projekt und filtern Sie mit dem Stichwort blazer, um das entsprechende Projekttemplate auszuwählen.
<br>
<img src="1.png" width=70% />
1. Legen Sie den Projektnamen auf "BlazorTest" fest und wählen Sie den Pfad aus.
<br>
<img src="2.png" width=70% />
1. Konfigurieren Sie die Bibliotheken und andere Optionen, die im Projekt verwendet werden. Klicken Sie abschließend auf die Schaltfläche "Erstellen", um Ihr erstes Blazor-Projekt zu generieren.
<br>
<img src="3.png" width=70% />
1. Klicken Sie nach dem Betreten des Projekts auf "Abhängigkeiten" unter dem Projekt und wählen Sie "NuGet-Pakete verwalten...", um die Bibliothek Aspose.Cells hinzuzufügen.
<br>
<img src="4.png" width=70% />
1. Geben Sie Stichwörter zur Filterung ein und installieren Sie die neueste Aspose.Cells-Bibliothek. Gleichzeitig werden abhängige Bibliotheken wie SkiaSharp gleichzeitig installiert.
<br>
<img src="5.png" width=70% />
1. Doppelklicken Sie auf die Datei "Index.razor", um die erforderliche Bibliothek zu bearbeiten und zu importieren. Fügen Sie einige Daten und Grafiken hinzu und rendern Sie sie in Grafiken zur Anzeige.
<br>
<img src="6.png" width=70% />
1. Kompilieren und starten Sie das Projekt, und Sie erhalten die folgenden Ergebnisse.
<br>
<img src="7.png" width=70% />

### Beispielcode in der Anwendung für Blazor-Server

Der folgende Beispielcode ist in der Datei Index.razor enthalten:
```
@page "/"
@using SkiaSharp;
@using Aspose.Cells;
@using Aspose.Cells.Drawing;
@using Aspose.Cells.Rendering;


<PageTitle>Index</PageTitle>

<h1>Hello, world!</h1>

Welcome to your new app.

<SurveyPrompt Title="How is Blazor working for you?" />

<img src="@imageSrc" />

@code
{
    private string imageSrc;

    public Index()
    {
        imageSrc = "data:image/png;base64, " + Convert.ToBase64String(CreateFile());
    }

    private byte[] CreateFile()
    {
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        sheet.Cells["A1"].Value = "test data for blazor";

        sheet.PageSetup.PrintGridlines = true;
        sheet.PageSetup.PrintArea = "A1:F20";

        ShapeCollection shapes = sheet.Shapes;

        //Add rectangle shape
        shapes.AddRectangle(1, 0, 1, 0, 100, 150);

        //Add line shape
        shapes.AddLine(8, 0, 1, 0, 100, 150);

        //Add oval shape
        shapes.AddOval(13, 0, 1, 0, 100, 150);

        using MemoryStream ms = new();

        SheetRender render = new SheetRender(sheet, new ImageOrPrintOptions());
        render.ToImage(0, ms);

        return ms.ToArray();
    }
}

```
{{< app/cells/assistant language="csharp" >}}
