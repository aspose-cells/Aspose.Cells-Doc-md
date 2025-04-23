---  
title: Supprimer les styles inutilisés dans le classeur avec C++  
linktitle: Supprimer les styles inutilisés dans le classeur  
type: docs  
weight: 340  
url: /fr/cpp/remove-unused-styles-inside-the-workbook/  
description: Supprimer les styles inutilisés dans un classeur Excel en utilisant Aspose.Cells avec C++.  
---  

{{% alert color="primary" %}}  

Les styles inutilisés dans les fichiers Excel prennent non seulement de la place mais causent également des problèmes de performance lors de la conversion en différents formats comme PDF, HTML, etc. Aspose.Cells fournit la [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) pour supprimer tous les styles inutilisés à l'intérieur du classeur.  

{{% /alert %}}  

Le code suivant explique l'utilisation de [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/). Le code charge le [fichier Excel modèle](5115520.xlsx) que vous pouvez télécharger via le lien fourni. Il contient un style inutilisé nommé **AsposeStyle** ; ce style et tous les autres styles inutilisés seront supprimés après exécution du code.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
