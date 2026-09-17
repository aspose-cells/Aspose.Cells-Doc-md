---
title: Excel Camera in Aspose.Cells for C++
linktitle: Excel Camera
description: Scopri come utilizzare Excel Camera in Aspose.Cells for C++ per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e conserva tutta la formattazione dell'origine.
keywords: Aspose.Cells, C++, Excel Camera, immagine dinamica, immagine collegata, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /it/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che riproduce un'immagine live di un intervallo di celle e fluttua sul livello di disegno come un'immagine ordinaria. Aspose.Cells supporta due modalità di creazione, un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantanea una tantum di un intervallo. Questo articolo illustra entrambi gli approcci, così potrai scegliere quello più adatto al tuo layout.

## Che cos'è Excel Camera?
Excel Camera è essenzialmente un oggetto Picture ancorato a una riga e colonna specifica sul livello di disegno del foglio di lavoro. A differenza di un'immagine inserita normalmente, la Camera è collegata a un intervallo di origine tramite una formula in stile A1, ad esempio `"A1:F10"`. Ogni volta che una cella all'interno di tale intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera conserva tutta la formattazione dell'area di origine — bordi, colori di sfondo, caratteri e formati numerici — quindi tutto ciò che è visibile all'interno delle celle appare anche nell'immagine della Camera. Questo rende la Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza scorrere o ripetere i dati. Si applicano due avvertenze: è necessario chiamare `UpdateSelectedValue()` prima di salvare la cartella di lavoro, e il file verrà esportato in HTML o PDF, perché tali formati si basano sui dati immagine incorporati anziché su un ricalcolo live.

## Metodo 1 — Aggiungere un'immagine Camera dinamica
La Camera dinamica è l'approccio più comune ed è la soluzione più vicina allo strumento Camera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una `Formula` che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, la chiamata a `UpdateSelectedValue()` aggiorna i dati immagine incorporati, così che siano sincronizzati con le celle che rispecchiano. La Camera non è implementata tramite una classe dedicata — è costruita interamente sul tipo standard `Picture`.
Le API chiave sono:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — aggiunge un'immagine ancorata alla riga e colonna specificate. Passando un `Vector<uint8_t>()` vuoto si crea un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.GetPictures().Get(int index)` — recupera uno specifico `Picture` dalla raccolta tramite indice.
- `Picture.SetFormula(U16String value)` — imposta il riferimento in stile A1 all'intervallo di origine che la Camera rispecchia, ad esempio `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — aggiorna i dati immagine incorporati dalle celle a cui fa riferimento `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati dell'immagine e la Camera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `Formula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Camera Dinamica: aggiungi un'immagine vuota, collegala tramite Formula a A1:F10, quindi aggiorna
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Metodo 2 — Aggiungere un'immagine Camera statica
La Camera statica è essenzialmente un'anteprima resa una tantum di un intervallo di celle. Invece di mantenere un collegamento live, viene reso l'intervallo in un buffer di byte `Vector<uint8_t>` una sola volta, e tale buffer viene passato direttamente a `Pictures.Add(row, col, data)`. Il contenuto dell'immagine viene quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine cambiano.
Le API chiave sono:
- `Cells.CreateRange(U16String address)` — crea un oggetto `Range` da un indirizzo in stile A1, ad esempio `U16String("A1:F10")`.
- `Range.ToImage(ImageOrPrintOptions options)` — rende l'intervallo in un buffer di byte `Vector<uint8_t>`. Passando `nullptr` si utilizzano le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — aggiunge l'immagine ancorata alla riga e colonna specificate, questa volta passando il buffer di byte prodotto da `Range.ToImage`.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo rende in byte di immagine tramite `Range.ToImage(nullptr)`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Fotocamera Statica: crea Range, converti in byte, aggiungi come immagine
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Scegliere tra dinamica e statica
- **Camera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `UpdateSelectedValue()` e conserva il comportamento di collegamento live per tutta la durata del file.
- **Camera statica:** un rendering una tantum che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della build anziché un mirror live dei dati.
Aspose.Cells supporta sia una Camera dinamica ad aggiornamento automatico, costruita su `Picture.Formula` più `UpdateSelectedValue()`, sia una Camera statica one-shot, costruita su `Range.ToImage` più `Vector<uint8_t>`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della build.

{{< app/cells/assistant language="cpp" >}}