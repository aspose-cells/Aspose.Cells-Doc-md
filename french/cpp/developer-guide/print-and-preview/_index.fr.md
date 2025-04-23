---
title: Imprimer et prévisualiser le classeur avec C++
linktitle: Imprimer et prévisualiser
type: docs
weight: 70
url: /fr/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells prend en charge l impression et la prévisualisation des fichiers Excel sans installation de Microsoft Excel en utilisant C++.
---

{{% alert color="primary" %}}

Après la création d'une feuille de calcul, vous voulez souvent imprimer une copie papier. Cet article explique comment imprimer des feuilles de calcul avec Aspose.Cells.

{{% /alert %}}

## **Introduction à l'impression**

Microsoft Excel suppose que vous voulez imprimer l'ensemble de la zone de la feuille de calcul à moins que vous ne spécifiiez une sélection. Pour imprimer avec Aspose.Cells, importez d'abord l'espace de noms Aspose.Cells.Rendering dans le programme. Il possède plusieurs classes utiles, par exemple, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) et [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Aperçu avant impression**

Il peut arriver que des fichiers Excel comportant des millions de pages doivent être convertis en PDF ou en images. Le traitement de tels fichiers consommera beaucoup de temps et de ressources. Dans de tels cas, la fonction Aperçu avant impression du classeur et de la feuille de calcul pourrait s'avérer utile. Avant de convertir de tels fichiers, l'utilisateur peut vérifier le nombre total de pages et décider ensuite de les convertir ou non. Cet article met l'accent sur l'utilisation des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) pour déterminer le nombre total de pages.

Aspose.Cells fournit la fonction d'aperçu avant impression. Pour cela, l'API fournit les classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/). Pour créer l'aperçu avant impression du classeur entier, créez une instance de la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) en transmettant les objets [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) au constructeur. La classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) fournit une méthode [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) qui retourne le nombre de pages dans l'aperçu généré. De manière similaire à la classe [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/), la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) est utilisée pour générer un aperçu avant impression pour une feuille de calcul spécifique. Pour créer l'aperçu avant impression d'une feuille de calcul, créez une instance de la classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) en transmettant les objets [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) et [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) au constructeur. La classe [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) fournit également une méthode [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) qui retourne le nombre de pages dans l'aperçu généré.

Le code suivant montre l'utilisation à la fois des classes [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) et [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) en utilisant le [fichier Excel d'exemple](94896177.xlsx).

### **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Voici la sortie générée en exécutant le code ci-dessus.

### **Sortie console**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Sujets avancés**
- [Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Convertir une feuille de calcul en image - Supprimer les espaces autour des données](/cells/fr/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page](/cells/fr/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Conversion d'une feuille de calcul en image en utilisant des options d'image ou d'impression](/cells/fr/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Exporter une plage de cellules d'une feuille de calcul vers une image](/cells/fr/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Exporter une feuille de calcul ou un graphique en image avec une largeur et une hauteur souhaitées](/cells/fr/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extraire des images des feuilles de calcul en utilisant des options d'image ou d'impression](/cells/fr/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Générer une miniature de la feuille de calcul](/cells/fr/cpp/generate-thumbnail-of-the-worksheet/)
- [Afficher une page vierge lorsqu'il n'y a rien à imprimer](/cells/fr/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Configuration de la page et options d'impression](/cells/fr/cpp/page-setup-and-printing-options/)
- [Séquence de rendu des pages à l'aide des propriétés PageIndex et PageCount d'ImageOrPrintOptions](/cells/fr/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Rendre la feuille de calcul dans le contexte graphique](/cells/fr/cpp/render-worksheet-to-graphic-context/)
- [Spécifier un ensemble de polices individuelles ou privées pour le rendu du classeur](/cells/fr/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
