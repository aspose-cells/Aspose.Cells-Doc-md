---
title: Convertir un fichier Excel au format PDF compatible avec PDFA 1a avec C++
linktitle: Convertir un fichier Excel au format PDF compatible avec PDFA 1a
type: docs
weight: 130
url: /fr/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Apprenez comment convertir des fichiers Excel en format PDF/A 1a conforme en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

PDF/A est une version spécifique de PDF conçue pour la conservation à long terme des documents. PDF/A est une version normalisée par ISO du format Portable Document (PDF) qui embed tous les polices utilisées dans le document au sein du fichier PDF. PDF/A diffère de PDF en interdisant certaines fonctionnalités, telles que la liaison de polices (contrairement à l’incorporation de polices) et le chiffrement. Aspose.Cells vous permet d'enregistrer les fichiers Excel en fichiers PDF conformes à PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u sont supportés). Ce sujet décrit comment sauvegarder un classeur Excel au format PDF/A conforme (PDF/A-1a).

## **Convertir le fichier Excel au format PDF Compatible avec PDF/A-1a**

Les développeurs peuvent utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) pour définir différents attributs pour la conversion. La définition de différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le PDF de sortie. La propriété la plus importante est [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) qui vous permet d'enregistrer les fichiers Excel au format PDF/A conforme.

Le code d'exemple suivant explique comment convertir le fichier Excel au format PDF compatible avec PDF/A-1a. Veuillez consulter son [PDF de sortie](outputCompliancePdfA1a.pdf) ainsi que la capture d'écran pour référence.

## **Capture d'écran**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
