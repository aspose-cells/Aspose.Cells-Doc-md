---  
title: Créer un objet Style en utilisant la classe CellsFactory avec C++  
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableurs offrant un objet style pour styliser les cellules. Cet article explique comment créer un objet style de cellule en utilisant la classe CellsFactory dans la bibliothèque Aspose.Cells afin que les utilisateurs puissent personnaliser l apparence des cellules selon leurs besoins.  
keywords: Aspose.Cells, bibliothèque C++, feuille de calcul électronique, objet style, style de cellule, personnalisation  
type: docs  
weight: 70  
url: /fr/cpp/create-style-object-using-cellsfactory-class/  
---  

## **Créer un objet Style en utilisant la classe CellsFactory**  
Le code d'exemple suivant crée un objet [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) en utilisant la classe [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory) puis définit le style par défaut du classeur. Téléchargez le [fichier Excel de sortie](5115153.xlsx) pour voir les résultats de ce code à titre de référence.  

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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
