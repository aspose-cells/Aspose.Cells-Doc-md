---
title: Unione e separazione di celle con C++
linktitle: Unione e separazione di celle
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo, che supporta l’unione e la separazione delle celle. Questo articolo introdurrà come unire e separare le celle usando la libreria Aspose.Cells, e come personalizzare lo stile della cella unita.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, unisci celle, separa celle, impostazioni di stile, stili personalizzati
type: docs
weight: 190
url: /it/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta questa funzionalità e può anche unire celle in un foglio di lavoro. È possibile anche separare o dividere le celle unite. Il riferimento della cella unita è il riferimento per la cella in alto a sinistra nell'intervallo selezionato originale.

{{% /alert %}} 

## **Introduzione**
Non si desidera sempre lo stesso numero di celle in ogni riga o colonna. Ad esempio, si potrebbe voler inserire un titolo in una cella che si estende su diverse colonne. Oppure, se si crea una fattura, potrebbe essere necessario meno colonne per il totale. Per rendere una cella da due o più celle, unirle. Microsoft Excel consente agli utenti di selezionare i file e unirli per strutturare il foglio di calcolo nel modo desiderato.

{{% alert color="primary" %}} 

Si noti che quando le celle vengono unite, viene conservato solo il dato nelle celle in alto a sinistra. Se ci sono dati nelle altre celle nell'intervallo, questi dati vengono eliminati.
Anche la formattazione si basa sulla cella di riferimento in modo che quando si uniscono le celle, le impostazioni di formattazione della cella in alto a sinistra nell'intervallo vengano applicate sulla cella unita. Quando la cella viene divisa, le nuove celle mantengono le proprie impostazioni di formato originali.

{{% /alert %}} 

## **Unione di celle in un foglio di lavoro**
### **Unione di celle in Microsoft Excel**
I seguenti passaggi descrivono come unire celle nel foglio di lavoro utilizzando MS Excel.

1. Copiare i dati che si desidera nella cella in alto a sinistra nell'intervallo.
1. Selezionare le celle che si desidera unire.
1. Per unire le celle in una riga o colonna e centrare i contenuti della cella, fare clic sull'icona **Unisci e centrato** sulla barra degli strumenti **Formattazione**.

### **Unione di celle con Aspose.Cells**
 La classe `Aspose::Cells::Cells` ha alcuni metodi utili per il compito. Ad esempio, il metodo `Merge()` unisce le celle in una singola cella all’interno di un intervallo specificato.

Nell'esempio seguente viene mostrato come unire le celle (C6:E7) in un foglio di lavoro.

```cpp
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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Dividere (Separare) celle unite**
### **Utilizzando Microsoft Excel**
I seguenti passaggi descrivono come dividere le celle unite usando Microsoft Excel.

1. Seleziona la cella unita.
   Quando le celle sono state unite, **Unisci e centra** è selezionato sulla barra degli strumenti **Formattazione**.
1. Fai clic su **Unisci e centra** sulla barra degli strumenti **Formattazione**.

### **Usare Aspose.Cells**
 La classe `Aspose::Cells::Cells` ha un metodo chiamato `UnMerge()` che divide le celle nel loro stato originale. Il metodo separa le celle usando il riferimento delle celle nell’intervallo di celle unite.

L'esempio seguente mostra come dividere le celle unite (C6). L'esempio utilizza il file creato nel precedente esempio e divide le celle unite.

```cpp
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Rileva le celle unite in un foglio di lavoro](/cells/it/cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="cpp" >}}
