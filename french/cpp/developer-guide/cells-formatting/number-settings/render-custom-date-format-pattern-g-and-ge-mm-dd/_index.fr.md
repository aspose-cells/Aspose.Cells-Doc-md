---
title: Rendu du motif de format de date personnalisé g et ge mm jj avec C++
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuilles de calcul qui supporte le rendu des dates en utilisant des motifs de format de date personnalisé g et ge . Cet article décrira comment rendre ces motifs de format de date personnalisé à l aide de la bibliothèque Aspose.Cells afin que les utilisateurs puissent contrôler la façon dont les dates sont affichées si besoin.
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul électronique, format de date personnalisé, rendu, motif g , motif ge , contrôle de l affichage
type: docs
weight: 160
url: /fr/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Aspose.Cells est maintenant capable de rendre les motifs de format de date personnalisés comme g, ge.mm.dd et similaires. Veuillez consulter le fichier Excel source joint (5112361.xlsx) et le PDF converti (5112360.pdf) par Aspose.Cells pour votre référence.

{{% /alert %}}

Le code d'exemple suivant convertit le fichier Excel source (5112361.xlsx) qui contient des valeurs de date avec des motifs de format personnalisés comme g et ge.mm.dd en un PDF de sortie (5112360.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
