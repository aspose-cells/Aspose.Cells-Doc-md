---
title: Come eseguire Aspose.Cells in Blazor
type: docs
weight: 138
url: /it/net/how-to-run-aspose-cells-in-blazor/
description: Scopri come eseguire Aspose.Cells in Blazor.
keywords: C# Esegui Aspose.Cells in Blazor, Utilizza Aspose.Cells in Blazor, Applicazione del server Blazor con Aspose.Cells
---

## Panoramica

Per eseguire Aspose.Cells in Blazor, è necessario utilizzare le piattaforme .NET6 (o successive); rispetto alle piattaforme precedenti (.netcore31 o precedenti), una differenza importante riguarda la libreria grafica. In questo documento ufficiale [Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), si spiega che per .NET6 o versioni successive la libreria grafica "System.Drawing.Common" sarà supportata solo in Windows e fornisce raccomandazioni per sostituire la libreria grafica.

Per il prodotto Apose.Cells, abbiamo condotto la valutazione e completato la migrazione della libreria grafica. Utilizziamo SkiaSharp invece di System.Drawing.Common nei sistemi non Windows, come suggerito nella documentazione ufficiale di Microsoft. Si prega di notare che questo cambiamento critico avrà effetto in Aspose.Cells 22.10.1 o successivo per .Net6.

## Applicazione del server Blazor con Aspose.Cells

In questo esempio, crei un'applicazione semplice del server blazor che aggiunge alcuni dati e grafici, e li rende in immagini da visualizzare sulla pagina web. Durante il processo di creazione del progetto, è possibile configurare le opzioni in base alle proprie esigenze. Ad esempio, quando si seleziona l'opzione "Abilita Docker", l'applicazione blazor può essere quindi compilata ed eseguita in Docker.

### Crea Applicazione del server Blazor

Utilizziamo lo strumento VS2022 come esempio per creare la prima applicazione blazor con Aspose.Cells, segui i passaggi seguenti:
1. Seleziona File -> Nuovo -> Progetto e filtra utilizzando la parola chiave blazer per selezionare il modello di progetto corrispondente.
<br>
<img src="1.png" width=70% />
1. Imposta il nome del progetto su "BlazorTest" e seleziona il percorso.
<br>
<img src="2.png" width=70% />
1. Configura le librerie e le altre opzioni utilizzate nel progetto. Infine, fai clic sul pulsante "Crea" per generare il tuo primo progetto blazer.
<br>
<img src="3.png" width=70% />
1. Dopo aver inserito il progetto, fai clic su "Dipendenze" sotto il progetto e seleziona "Gestisci pacchetti NuGet..." per aggiungere la libreria Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. Inserisci parole chiave per filtrare e installare la libreria Aspose.Cells più recente. Contestualmente verranno installate anche le librerie dipendenti come SkiaSharp.
<br>
<img src="5.png" width=70% />
1. Fai doppio clic sul file "Index.razor" per modificare ed importare la libreria richiesta. Aggiungi alcuni dati e grafici e renderli in grafici da visualizzare.
<br>
<img src="5.png" width=70% />
1. Compila ed esegui il progetto, otterrai i seguenti risultati.
<br>
<img src="7.png" width=70% />

### Codice di esempio in applicazione server Blazor

Il seguente codice di esempio è incluso nel file Index.razor:
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
