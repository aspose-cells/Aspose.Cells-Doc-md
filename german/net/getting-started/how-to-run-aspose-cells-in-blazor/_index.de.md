---
title: So führen Sie Aspose.Cells in Blazor aus
type: docs
weight: 138
url: /de/net/how-to-run-aspose-cells-in-blazor/
description: Erfahren Sie, wie Sie Aspose.Cells in Blazor ausführen.
keywords: C# Run Aspose.Cells in Blazor, Use Aspose.Cells in Blazor
---
##  Überblick

 Um Aspose.Cells in Blazor auszuführen, benötigen Sie die Plattformen .NET6 (oder höher). Im Vergleich zu früheren Plattformen (.netcore31 oder früher) besteht ein wichtiger Unterschied in der Grafikbibliothek. In diesem Beamten[Microsoft Dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), erklärt es für .NET6 oder spätere Versionen, dass die Grafikbibliothek „System.Drawing.Common“ nur unter Windows unterstützt wird, und gibt Empfehlungen zum Ersetzen der Grafikbibliothek.

Für das Produkt Apose.Cells haben wir die Evaluierung durchgeführt und die Migration der Grafikbibliothek abgeschlossen. Wir verwenden SkiaSharp anstelle von System.Drawing.Common in Nicht-Windows-Systemen, wie in der offiziellen Dokumentation von Microsoft empfohlen. Bitte beachten Sie, dass diese wichtige Änderung ab Aspose.Cells 22.10.1 oder höher für .Net6 wirksam wird.

##  Erste Blazor-Bewerbung mit Aspose.Cells

In diesem Beispiel erstellen Sie eine einfache Blazor-Serveranwendung, die einige Daten und Grafiken hinzufügt und diese in Bilder rendert, die auf der Webseite angezeigt werden. Während des Projekterstellungsprozesses können Sie Optionen entsprechend Ihren eigenen Anforderungen konfigurieren. Wenn Sie beispielsweise die Option „Docker aktivieren“ aktivieren, kann die Blazor-Anwendung dann in Docker erstellt und ausgeführt werden.

###  Erstellen Sie die erste Blazor-Anwendung

Lassen Sie uns das VS2022-Tool als Beispiel verwenden, um die erste Blazor-Anwendung mit Aspose.Cells zu erstellen. Führen Sie die folgenden Schritte aus:
1. Wählen Sie Datei ->Neu ->Projekt und filtern Sie nach dem Schlüsselwort „Blazer“, um die entsprechende Projektvorlage auszuwählen.
<br>
<img src="1.png" width=70% />
1. Legen Sie den Projektnamen auf „BlazorTest“ fest und wählen Sie den Pfad aus.
<br>
<img src="2.png" width=70% />
1. Konfigurieren Sie die im Projekt verwendeten Bibliotheken und anderen Optionen. Klicken Sie abschließend auf die Schaltfläche „Erstellen“, um Ihr erstes Blazer-Projekt zu erstellen.
<br>
<img src="3.png" width=70% />
1. Nachdem Sie das Projekt eingegeben haben, klicken Sie unter dem Projekt auf „Abhängigkeiten“ und wählen Sie „NuGet-Pakete verwalten …“, um die Bibliothek Aspose.Cells hinzuzufügen.
<br>
<img src="4.png" width=70% />
1. Geben Sie Schlüsselwörter zum Filtern ein und installieren Sie die neueste Aspose.Cells-Bibliothek. Gleichzeitig werden auch abhängige Bibliotheken wie SkiaSharp zusammen installiert.
<br>
<img src="5.png" width=70% />
1. Doppelklicken Sie auf die Datei „Index.razor“, um die erforderliche Bibliothek zu bearbeiten und zu importieren. Fügen Sie einige Daten und Grafiken hinzu und rendern Sie sie zur Anzeige in Grafiken.
<br>
<img src="5.png" width=70% />
1. Kompilieren Sie das Projekt und führen Sie es aus. Sie erhalten die folgenden Ergebnisse.
<br>
<img src="7.png" width=70% />

###  Beispielcode in der ersten Blazor-Anwendung

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