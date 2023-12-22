---
title: Come eseguire Aspose.Cells in Blazor
type: docs
weight: 138
url: /it/net/how-to-run-aspose-cells-in-blazor/
description: Scopri come eseguire Aspose.Cells in Blazor.
keywords: C# Run Aspose.Cells in Blazor, Use Aspose.Cells in Blazor
---
##  Panoramica

 Per eseguire Aspose.Cells in Blazor, sono necessarie le piattaforme .NET6 (o successive), rispetto alle piattaforme precedenti (.netcore31 o precedenti), una differenza importante riguarda la libreria grafica. In questo ufficiale[Microsoft Documento](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), spiega per .NET6 o versioni successive che la libreria grafica "System.Drawing.Common" sarà supportata solo su Windows e fornisce consigli per sostituire la libreria grafica.

Per il prodotto Apose.Cells, abbiamo condotto la valutazione e completato la migrazione della libreria grafica. Usiamo SkiaSharp invece di System.Drawing.Common nei sistemi non Windows, come suggerito nella documentazione ufficiale di Microsoft. Tieni presente che questa modifica critica avrà effetto a partire da Aspose.Cells 22.10.1 o versioni successive per .Net6.

##  Prima applicazione Blazor con Aspose.Cells

In questo esempio si crea una semplice applicazione server Blazor che aggiunge alcuni dati ed elementi grafici e ne esegue il rendering in immagini da visualizzare nella pagina Web. Durante il processo di creazione del progetto, puoi configurare le opzioni in base alle tue esigenze. Ad esempio, quando selezioni l'opzione "Abilita Docker", l'applicazione Blazor può quindi essere creata ed eseguita in Docker.

###  Creare la prima applicazione Blazor

Usiamo lo strumento VS2022 come esempio per creare la prima applicazione blazor con Aspose.Cells, segui i passaggi seguenti:
1. Selezionare File ->Nuovo ->Progetto e filtrare utilizzando la parola chiave blazer per selezionare il modello di progetto corrispondente.
<br>
<img src="1.png" width=70% />
1. Impostare il nome del progetto su "BlazorTest" e selezionare il percorso.
<br>
<img src="2.png" width=70% />
1. Configurare le librerie e altre opzioni utilizzate nel progetto. Infine, fai clic sul pulsante "Crea" per generare il tuo primo progetto blazer.
<br>
<img src="3.png" width=70% />
1. Dopo aver inserito il progetto, fare clic su "Dipendenze" sotto il progetto e selezionare "Gestisci pacchetti NuGet..." per aggiungere la libreria Aspose.Cells.
<br>
<img src="4.png" width=70% />
1. Inserisci le parole chiave per filtrare e installa l'ultima libreria Aspose.Cells. Contemporaneamente verranno installate insieme anche le librerie dipendenti come SkiaSharp.
<br>
<img src="5.png" width=70% />
1. Fare doppio clic sul file "Index.razor" per modificare e importare la libreria richiesta. Aggiungi alcuni dati ed elementi grafici e trasformali in grafica per la visualizzazione.
<br>
<img src="5.png" width=70% />
1. Compila ed esegui il progetto e otterrai i seguenti risultati.
<br>
<img src="7.png" width=70% />

###  Codice di esempio nella prima applicazione Blazor

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