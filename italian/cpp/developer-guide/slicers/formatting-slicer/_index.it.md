---
title: Formattare lo slicer con C++
linktitle: Formattazione del filtro
type: docs
weight: 20
url: /it/cpp/formatting-slicer/
description: Formatta i slicer in Microsoft Excel utilizzando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Puoi formattare il slicer in Microsoft Excel impostando il numero di colonne o lo stile, ecc. Aspose.Cells permette anche di farlo utilizzando le proprietà [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/) e [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/).

## **Formattazione del selettore**

Vedi il codice seguente; carica il [file Excel di esempio](67338473.xlsx) che contiene un slicer. Accede al slicer, imposta il numero di colonne e il tipo di stile e lo salva come [file Excel di output](67338474.xlsx). Lo screenshot mostra come appare il slicer dopo l'esecuzione del codice di esempio.

![todo:image_alt_text](formatting-slicer_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
