--- 
title: Exporter les commentaires lors de l enregistrement d Excel en HTML avec C++ 
linktitle: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML 
type: docs 
weight: 40 
url: /fr/cpp/export-comments-while-saving-excel-file-to/ 
description: Découvrez comment exporter les commentaires lors de l enregistrement de fichiers Excel en HTML avec Aspose.Cells et C++. 
--- 

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, les commentaires ne sont pas exportés. Cependant, Aspose.Cells offre cette fonctionnalité via la propriété [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). Si vous la définissez à **true**, les commentaires présents dans votre fichier Excel seront également affichés dans le HTML.

## **Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML**

Le code d'exemple ci-dessous explique l'utilisation de la propriété [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). La capture d'écran montre l'effet du code sur le HTML lorsqu'il est défini à **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) et le [HTML généré](5052826.txt) en référence.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
