---
title: Ajout de texte enrichi HTML dans la cellule avec C++
linktitle: Valeur de chaîne HTML
type: docs
weight: 50
url: /fr/cpp/adding-html-rich-text-inside-the-cell/
description: Découvrez comment ajouter du texte enrichi HTML dans la cellule via l’API Aspose.Cells for C++.
keywords: Ajouter du texte enrichi HTML dans la cellule, Définir du texte enrichi HTML dans la cellule, Ajouter du texte enrichi HTML dans la cellule
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion de HTML orienté Microsoft Excel en format XLS/XLSX. Cela signifie que le HTML généré par Microsoft Excel peut être converti en format XLS/XLSX en utilisant Aspose.Cells.

De même, s'il y a un HTML simple, Aspose.Cells peut le convertir en HTML Rich Text. Aspose.Cells fournit la méthode [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) qui peut prendre un HTML simple et le convertir en texte de cellule formaté.

{{% /alert %}}

L'exemple de code ci-dessous vous montre comment ajouter du texte enrichi HTML dans la cellule. Veuillez consulter la capture d'écran du fichier Excel de sortie.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Articles Connexes

- [Afficher des puces en définissant la valeur de la cellule à l'aide de HTML](/cells/fr/cpp/display-bullets-by-setting-cell-value-using/)
- [Obtenir une chaîne HTML5 à partir de la cellule](/cells/fr/cpp/get-html5-string-from-cell/)
{{< app/cells/assistant language="cpp" >}}
