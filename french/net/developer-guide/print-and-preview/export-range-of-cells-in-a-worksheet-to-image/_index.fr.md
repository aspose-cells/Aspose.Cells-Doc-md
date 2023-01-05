---
title: Exporter la plage de Cells dans une feuille de calcul vers une image
type: docs
weight: 60
url: /fr/net/export-range-of-cells-in-a-worksheet-to-image/
---
## **Scénarios d'utilisation possibles**

Vous pouvez créer une image d'une feuille de calcul à l'aide de Aspose.Cells. Cependant, vous devez parfois exporter uniquement une plage de cellules d'une feuille de calcul vers une image. Cet article explique comment y parvenir.

## **Exporter la plage de Cells dans une feuille de calcul vers une image**

 Pour prendre une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis définissez toutes les marges sur 0. Définissez également[**ImageOrPrintOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/onepagepersheet) à**vrai** . Le code suivant prend une image de la plage D8:G16. Ci-dessous une capture d'écran du[exemple de fichier Excel](47153160.xlsx) utilisé dans le code. Vous pouvez essayer le code avec n'importe quel fichier Excel.

## **Capture d'écran d'un exemple de fichier Excel et de son image exportée**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

L'exécution du code crée une image de la plage D8:G16 uniquement.

**![todo:image_alt_text](Output-Image.png)**

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ExportRangeOfCellsInWorksheetToImage-1.cs" >}}
