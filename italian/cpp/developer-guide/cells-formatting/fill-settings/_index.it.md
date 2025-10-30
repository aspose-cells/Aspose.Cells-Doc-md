---
title: Impostazioni di riempimento con C++
linktitle: Impostazioni di riempimento
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Supporta la configurazione delle impostazioni di riempimento delle celle, consentendo agli utenti di personalizzare lo sfondo e lo stile delle celle. Questo articolo introdurrà come usare la libreria Aspose.Cells per impostare le impostazioni di riempimento delle celle.
keywords: Aspose.Cells, Celle, Impostazioni di riempimento, Sfondo, Stile
type: docs
weight: 50
url: /it/cpp/cells-fill-settings/
---

## **Colori e motivi di sfondo**

Microsoft Excel può impostare i colori del primo piano (contorno) e lo sfondo (riempimento) delle celle e i motivi di sfondo.

Aspose.Cells supporta anche queste funzionalità in modo flessibile. In questo argomento, impariamo ad utilizzare queste funzionalità utilizzando Aspose.Cells.

### **Impostazione di colori e motivi di sfondo**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ciascun elemento della raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Il [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) ha i metodi [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) e [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) che vengono utilizzati per ottenere e impostare la formattazione di una cella. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fornisce proprietà per impostare i colori del primo piano e dello sfondo delle celle. Aspose.Cells fornisce un'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) che contiene un insieme di tipi predefiniti di motivi di sfondo che sono di seguito elencati.

|**Motivi di sfondo**|**Descrizione**|
| :- | :- |
|DiagonalCrosshatch|Rappresenta un motivo a croce diagonale|
|DiagonalStripe|Rappresenta un motivo a strisce diagonali|
|Gray6|Rappresenta un motivo grigio al 6.25%|
|Gray12|Rappresenta un motivo grigio al 12.5%|
|Gray25|Rappresenta un motivo grigio al 25%|
|Gray50|Rappresenta 50% modello grigio|
|Gray75|Rappresenta 75% modello grigio|
|HorizontalStripe|Rappresenta modello a strisce orizzontali|
|None|Rappresenta nessuno sfondo|
|ReverseDiagonalStripe|Rappresenta modello a strisce diagonali invertite|
|Solid|Rappresenta modello solido|
|ThickDiagonalCrosshatch|Rappresenta modello spesso di incroci diagonali|
|ThinDiagonalCrosshatch|Rappresenta modello sottile di incroci diagonali|
|ThinDiagonalStripe|Rappresenta modello sottile a strisce diagonali|
|ThinHorizontalCrosshatch|Rappresenta modello sottile di incroci orizzontali|
|ThinHorizontalStripe|Rappresenta modello sottile a strisce orizzontali|
|ThinReverseDiagonalStripe|Rappresenta modello sottile a strisce diagonali invertite|
|ThinVerticalStripe|Rappresenta modello sottile a strisce verticali|
|VerticalStripe|Rappresenta modello a strisce verticali|

Nell'esempio seguente, il colore dell'oggetto A1 è impostato ma A2 è configurato per avere sia colori di primo piano sia di sfondo con un modello di sfondo a strisce verticali.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Importante sapere**

{{% alert color="primary" %}}

- Per impostare il colore di primo piano o di sfondo di una cella, utilizzare le proprietà [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) o [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) dell'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Entrambe le proprietà avranno effetto solo se la proprietà [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) dell'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) è configurata.
- La proprietà [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) imposta il colore si sfumatura della cella.
  La proprietà [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) specifica il tipo di modello di sfondo utilizzato per il colore di primo piano o di sfondo. Aspose.Cells fornisce un'enumerazione, [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), che contiene un insieme di tipi di modelli di sfondo predefiniti.
- Se si seleziona il valore *BackgroundType.None* dall'enumerazione [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), il colore del primo piano non viene applicato.
  Allo stesso modo, il colore di sfondo non viene applicato se si selezionano i valori *BackgroundType.None* o *BackgroundType.Solid*.
- Quando si recupera il colore di sfondo di una cella, se [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) è *BackgroundType.None*, [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) restituirà *Color.Empty*.

{{% /alert %}}

### **Applicazione degli effetti di riempimento a sfumatura**

Per applicare i vostri desiderati effetti di riempimento a sfumatura alla cella, utilizzate il metodo [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) dell'oggetto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) di conseguenza.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Colori e Palette**

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile utilizzare non solo i colori esistenti nella palette ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla palette.

Questo argomento tratta come aggiungere colori personalizzati alla palette.

### **Aggiunta colori personalizzati alla palette**

Aspose.Cells supporta la palette a 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fornisce un metodo [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) che richiede i seguenti parametri per aggiungere un colore personalizzato alla modifica della palette:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
