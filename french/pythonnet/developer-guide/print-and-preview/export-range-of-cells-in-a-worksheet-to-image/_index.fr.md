---
title: Exporter la plage de cellules dans une feuille de calcul en tant qu image
type: docs
weight: 60
url: /fr/python-net/export-range-of-cells-in-a-worksheet-to-image/
---

## **Scénarios d'utilisation possibles**

Vous pouvez créer une image d'une feuille de calcul en utilisant Aspose.Cells pour Python via .NET. Cependant, parfois vous souhaitez exporter uniquement une plage de cellules en tant qu'image. Cet article explique comment y parvenir.

## **Exporter une plage de cellules d'une feuille de calcul vers une image**

Pour prendre une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis définissez toutes les marges à 0. Définissez également [**ImageOrPrintOptions.one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/one_page_per_sheet) sur **true**. Le code suivant prend une image de la plage D8:G16. Ci-dessous se trouve une capture d'écran du [fichier Excel d'exemple](47153160.xlsx) utilisé dans le code. Vous pouvez essayer le code avec n'importe quel fichier Excel.

## **Capture d'écran du fichier Excel d'exemple et de son image exportée**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

L'exécution du code crée une image de la plage D8:G16 seulement.

**![todo:image_alt_text](Output-Image.png)**

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ExportRangeOfCellsInWorksheetToImage-1.py" >}}

