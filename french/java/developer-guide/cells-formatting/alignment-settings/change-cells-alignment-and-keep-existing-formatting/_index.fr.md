---
title: Modifier l alignement des cellules et conserver la mise en forme existante
type: docs
weight: 260
url: /fr/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

Parfois, vous voulez changer l'alignement de plusieurs cellules mais aussi conserver le formatage existant. Aspose.Cells vous permet de le faire en utilisant la propriété [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments). Si vous le définissez sur **true**, les changements d'alignement auront lieu sinon non. Veuillez noter que l'objet [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) est passé en paramètre à la méthode [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) qui applique réellement le formatage à la plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338592.xlsx), crée la plage et l'aligne horizontalement et verticalement au centre tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel de sortie](67338591.xlsx) et montre que tout le formatage existant des cellules est le même, à l'exception du nouvel alignement horizontal et vertical au centre des cellules.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
