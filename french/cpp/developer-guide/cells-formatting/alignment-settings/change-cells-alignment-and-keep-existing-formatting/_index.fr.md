---
title: Modifier l alignement des cellules et conserver la mise en forme existante avec C++
description: Utilisez la bibliothèque Aspose.Cells pour changer l alignement des cellules et conserver la mise en forme existante
keywords: Aspose.Cells, C++, alignement des cellules, conserver la mise en forme existante
type: docs
weight: 340
url: /fr/cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez changer l'alignement de plusieurs cellules tout en conservant la mise en forme existante. Aspose.Cells vous permet de le faire en utilisant la propriété [**GetAlignments()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getalignments/). Si vous la définissez sur **true**, les changements d'alignement seront appliqués, sinon non. Notez que l'objet [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) est passé en paramètre à la méthode [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) qui applique en réalité la mise en forme à une plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338585.xlsx), crée la plage et centre l'alignement horizontalement et verticalement tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel en sortie](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant alignées au centre horizontalement et verticalement.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

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
