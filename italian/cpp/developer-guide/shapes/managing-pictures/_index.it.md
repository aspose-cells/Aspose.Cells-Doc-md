---
title: Gestione delle Immagini con C++
linktitle: Gestione delle immagini
type: docs
weight: 10
url: /it/cpp/managing-pictures/
description: Aggiungi, posiziona e gestisci immagini nei fogli di calcolo usando l API Aspose.Cells for C++.
---

Aspose.Cells consente ai programmatori di aggiungere immagini ai fogli di calcolo in fase di esecuzione. Inoltre, la posizione di queste immagini può essere controllata in fase di esecuzione, come discusso più in dettaglio nelle sezioni successive.

Questo articolo spiega come aggiungere immagini e come inserire un'immagine che mostra il contenuto di determinate celle.

## **Aggiunta di immagini**

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:
 Chiamare semplicemente il metodo [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) dell'[**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Il metodo [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome del file immagine**, il nome del file immagine, completo di percorso.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Posizionamento delle immagini**

Ci sono due possibili modi per controllare il posizionamento delle immagini utilizzando Aspose.Cells:

- Posizionamento proporzionale: definire una posizione proporzionale all'altezza e alla larghezza della riga.
- Posizionamento assoluto: definisce la posizione esatta sulla pagina in cui verrà inserita l'immagine, ad esempio 40 pixel a sinistra e 20 pixel sotto il bordo della cella.

### **Posizionamento proporzionale**

Gli sviluppatori possono posizionare le immagini in proporzione all'altezza della riga e alla larghezza della colonna usando le proprietà [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) e [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) dell'oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). È possibile ottenere un oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) passando l'indice dell'immagine dall'[**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/). Questo esempio posiziona un'immagine nella cella F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Posizionamento Assoluto**

Gli sviluppatori possono anche posizionare le immagini in modo assoluto utilizzando le proprietà [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) e [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) dell'oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Questo esempio posiziona un'immagine nella cella F6, 60 pixel a sinistra e 10 pixel dall'alto della cella.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Inserimento di un'immagine in base al riferimento della cella**

Aspose.Cells consente di visualizzare i contenuti di una cella del foglio di lavoro in una forma di immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Poiché la cella, o il range di celle, è collegata all'oggetto grafico, le modifiche apportate ai dati in quella cella o in quel range di celle appaiono automaticamente nell'oggetto grafico.

Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) dell'[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Specifica l'intervallo di celle usando l'attributo [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) dell'oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Aggiungi Impostazioni Icona Condizionale con il Testo della Cella](/cells/it/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/cpp/insert-a-linked-picture-from-web-address/)
- [Inserisci un'immagine basata sul riferimento della cella](/cells/it/cpp/insert-a-picture-based-on-cell-reference/)
- [Caricare un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="cpp" >}}
