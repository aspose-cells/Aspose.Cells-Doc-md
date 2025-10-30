---
title: Modifica l allineamento delle celle e conserva la formattazione esistente con C++
description: Utilizzare la libreria Aspose.Cells per modificare l allineamento delle celle e preservare la formattazione esistente
keywords: Aspose.Cells, C++, allineamento celle, preserva la formattazione esistente
type: docs
weight: 340
url: /it/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Possibili Scenari di Utilizzo**

A volte vuoi cambiare l'allineamento di più celle ma vuoi anche conservare la formattazione esistente. Aspose.Cells ti permette di farlo usando la proprietà [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/). Se impostata a **true**, avverranno modifiche nell'allineamento, altrimenti no. Nota che l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) viene passato come parametro al metodo [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) che applica effettivamente la formattazione a un intervallo di celle.

## **Modifica dell'allineamento delle celle e mantenimento della formattazione esistente**

Il seguente codice di esempio carica il [file Excel di esempio](67338585.xlsx), crea l'intervallo e centra l'allineamento in modo orizzontale e verticale e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e il [file Excel di output](67338586.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa tranne che le celle sono ora allineate al centro in modo orizzontale e verticale.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing cells with formatting.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleChangeCellsAlignmentAndKeepExistingFormatting.xlsx");

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create cells range.
    Range rng = ws.GetCells().CreateRange(u"B2:D7");

    // Create style object.
    Style st = wb.CreateStyle();

    // Set the horizontal and vertical alignment to center.
    st.SetHorizontalAlignment(TextAlignmentType::Center);
    st.SetVerticalAlignment(TextAlignmentType::Center);

    // Create style flag object.
    StyleFlag flag;

    // Set style flag alignments true. It is the most crucial statement.
    // Because if it is false, no changes will take place.
    flag.SetAlignments(true);

    // Apply style to range of cells.
    rng.ApplyStyle(st, flag);

    // Save the workbook in XLSX format.
    wb.Save(outputDir + u"outputChangeCellsAlignmentAndKeepExistingFormatting.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
