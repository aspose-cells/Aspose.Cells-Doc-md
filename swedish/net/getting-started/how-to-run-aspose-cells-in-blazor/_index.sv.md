---
title: Hur man kör Aspose.Cells i Blazor
type: docs
weight: 138
url: /sv/net/how-to-run-aspose-cells-in-blazor/
description: Lär dig hur man kör Aspose.Cells i Blazor.
keywords: C# Kör Aspose.Cells i Blazor, Använd Aspose.Cells i Blazor, Blazor Server applikation med Aspose.Cells
---

## Översikt

För att köra Aspose.Cells i Blazor krävs .NET6 (eller senare) plattformar, jämfört med tidigare plattformar (.netcore31 eller tidigare), är en viktig skillnad grafikbiblioteket. I detta officiella [Microsoftdokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), förklaras att för .NET6 eller senare släpp kommer grafikbiblioteket "System.Drawing.Common" endast stödjas på Windows, och ger rekommendationer för att ersätta grafikbiblioteket.

För Apose.Cells-produkten har vi genomfört utvärderingen och slutfört migreringen av grafikbiblioteket. Vi använder SkiaSharp istället för System.Drawing.Common i icke-Windows-system, som föreslagits i Microsofts officiella dokumentation. Observera att denna kritiska ändring kommer att träda i kraft i Aspose.Cells 22.10.1 eller senare för .Net6.

## Blazor Server-applikation med Aspose.Cells

I det här exemplet skapar du en enkel blazor server-applikation som lägger till lite data och grafik, och renderar dem till bilder för att visa på webbsidan. Under projekt skapandet kan du konfigurera alternativ enligt dina egna behov. När du till exempel markerar alternativet "Aktivera Docker" kan blazor-applikationen sedan byggas och köras i Docker.

### Skapa Blazor Server-applikation

Låt oss använda verktyget VS2022 som ett exempel för att skapa den första blazor-applikationen med Aspose.Cells, följ stegen nedan:
1. Välj Fil ->Ny ->Projekt och filtrera med hjälp av nyckelordet blazer för att välja den motsvarande projektmallen.
<br>
<img src="1.png" width=70% />
1. Ange projektets namn till "BlazorTest" och välj sökvägen.
<br>
<img src="2.png" width=70% />
1. Konfigurera bibliotek och andra alternativ i projektet. Klicka sedan på "Skapa"-knappen för att generera ditt första blazer-projekt.
<br>
<img src="3.png" width=70% />
1. Efter att ha kommit in i projektet, klicka på "Beroenden" under projektet och välj "Hantera NuGet-paket..." för att lägga till Aspose.Cells-biblioteket.
<br>
<img src="4.png" width=70% />
1. Ange nyckelord för filtrering och installera det senaste Aspose.Cells-biblioteket. Samtidigt kommer beroende bibliotek som SkiaSharp också att installeras samtidigt.
<br>
<img src="5.png" width=70% />
1. Dubbelklicka på filen "Index.razor" för att redigera och importera det nödvändiga biblioteket. Lägg till lite data och grafik, och rendera dem till grafik för att visa.
<br>
<img src="5.png" width=70% />
1. Kompilera och kör projektet, och du kommer att få följande resultat.
<br>
<img src="7.png" width=70% />

### Exempelkod i Blazor Server-applikation

Följande exempelkod ingår i filen Index.razor:
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
