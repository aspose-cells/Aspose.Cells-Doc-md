---
title: Individuelle oder private Schriftarten für die Arbeitsmappendarstellung mit C++ spezifizieren
linktitle: Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben
type: docs
weight: 40
url: /de/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ eine individuelle oder private Schriftartensatz für die Arbeitsmappendarstellung festlegen.
---

## **Mögliche Verwendungsszenarien**

Im Allgemeinen geben Sie das Verzeichnis der Schriftarten oder die Schriftartenliste für alle Arbeitsmappen an, aber manchmal müssen Sie eine individuelle oder private Schriftartensatz für Ihre Arbeitsmappen festlegen. Aspose.Cells stellt die [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) Klasse bereit, mit der Sie die individuelle oder private Schriftartensatz für Ihre Arbeitsmappe festlegen können.

## **Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben**

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](67338268.xlsx) mit ihrem individuellen oder privaten Schriftartensatz, der mit der [**IndividualFontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/individualfontconfigs/) Klasse festgelegt ist. Bitte sehen Sie sich auch die [Beispielschriftart](67338271.zip) an, die im Code verwendet wird, sowie das durch sie generierte [Output-PDF](67338269.pdf). Der folgende Screenshot zeigt, wie das Ausgabe-PDF aussieht, wenn die Schriftart erfolgreich gefunden wird.

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path of your custom font directory
    U16String customFontsDir(u"C:\\TempDir\\CustomFonts");

    // Specify individual font configs custom font directory
    IndividualFontConfigs fontConfigs;

    // If you comment this line or if custom font directory is wrong or 
    // if it does not contain required font then output pdf will not be rendered correctly
    fontConfigs.SetFontFolder(customFontsDir, false);

    // Specify load options with font configs
    LoadOptions opts(LoadFormat::Xlsx);
    opts.SetFontConfigs(fontConfigs);

    // Load the sample Excel file with individual font configs
    Workbook wb(u"sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx", opts);

    // Save to PDF format
    wb.Save(u"outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved to PDF with custom font configurations successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
