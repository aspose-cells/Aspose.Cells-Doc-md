---
title: Attribuer la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions pour avoir priorité avec C++
linktitle: Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions afin de lui donner la priorité
type: docs
weight: 30
url: /fr/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Apprenez à prioriser les paramètres de police lors de la sauvegarde de documents avec Aspose.Cells en C++.
---

## **Scénarios d'utilisation possibles**

En définissant la propriété **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), vous pourriez vous attendre à ce que l'enregistrement en PDF ou en image définit cette police par défaut pour tout le texte dans un classeur qui a une police manquante (non installée).

En général, lors de l'enregistrement en PDF ou en image, Aspose.Cells tentera d'abord de définir la police par défaut du classeur (c'est-à-dire Workbook.DefaultStyle.Font). Si la police par défaut du classeur ne peut toujours pas afficher/rendre le texte correctement, alors Aspose.Cells essaiera de rendre avec la police mentionnée contre l'attribut DefaultFont dans [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

Pour répondre à votre attente, nous avons une propriété booléenne nommée "**CheckWorkbookDefaultFont**" dans [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). Vous pouvez la définir sur **false** pour désactiver la tentative avec la police par défaut du classeur ou laisser le réglage **DefaultFont** dans [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) avoir la priorité.

## **Définir la propriété DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

Le code d'exemple suivant ouvre un fichier Excel. La cellule A1 (dans la première feuille) a un texte défini sur "Christmas Time Font text". Le nom de la police est "Christmas Time Personal Use" qui n'est pas installée sur la machine. Nous définissons l'attribut **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) à "Times New Roman". Nous configurons également la propriété booléenne **CheckWorkbookDefaultFont** à **"false"** pour garantir que le texte de la cellule A1 est rendu avec la police "Times New Roman" et ne doit pas utiliser la police par défaut du classeur ("Calibri" dans ce cas). Le code rend la première feuille en formats PNG et TIFF. Finalement, il la rend en format PDF.

{{% alert color="primary" %}}

La valeur par défaut de l'attribut **CheckWorkbookDefaultFont** est **true**.

{{% /alert %}}

Il s'agit de la capture d'écran du [fichier modèle](49446913.xlsx) utilisé dans le code exemple.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Voici l’image PNG de sortie après avoir réglé la propriété [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) à "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Voir l’image [TIFF](48496672.tiff) de sortie après avoir réglé la propriété [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) à "Times New Roman".

Voir le fichier PDF [40496673.pdf](48496673.pdf) après avoir défini la propriété [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) sur "Times New Roman".

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
