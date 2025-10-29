---
title: Définir la police par défaut lors de la rendu d une feuille de calcul en HTML avec C++
linktitle: Définir la police par défaut lors du rendu de la feuille de calcul en HTML
type: docs
weight: 370
url: /fr/cpp/set-default-font-while-rendering-spreadsheet-to/
description: Apprenez comment définir la police par défaut lors de la rendu d une feuille de calcul en HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Aspose.Cells vous permet de définir la police par défaut lors de la rendu d'une feuille de calcul en HTML. Veuillez utiliser [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/) à cette fin. Cette propriété est utile lorsqu'il y a des cellules dans une feuille de calcul avec des polices invalides ou inexistantes. Ces cellules seront alors rendues avec la police spécifiée par la propriété [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Définir la police par défaut lors du rendu de la feuille de calcul en HTML

Le code d'exemple suivant crée un classeur et ajoute un texte dans la cellule B4 de la première feuille de calcul et défini sa police sur une police inconnue/inexistante. Ensuite, il sauvegarde le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

 La capture d'écran montre l'effet de la définition de différents noms de police par défaut via la propriété [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Le code génère le [fichier HTML de sortie avec Courier New](5115516), le [fichier HTML de sortie avec Arial](5115518), et le [fichier HTML de sortie avec Times New Roman](5115517).

## Code d'exemple

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

    // Create workbook object and access first worksheet
    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"B4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell B4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    cell.SetStyle(st);

    // Now save the workbook in html format and set the default font to Courier New
    HtmlSaveOptions opts;
    opts.SetDefaultFontName(u"Courier New");
    wb.Save(outDir + u"out_courier_new_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Arial
    opts.SetDefaultFontName(u"Arial");
    wb.Save(outDir + u"out_arial_out.htm", opts);

    // Now save the workbook in html format once again but set the default font to Times New Roman
    opts.SetDefaultFontName(u"Times New Roman");
    wb.Save(outDir + u"times_new_roman_out.htm", opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
