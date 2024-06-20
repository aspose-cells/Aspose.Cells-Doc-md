---
title: Modifier l alignement des cellules et conserver la mise en forme existante
description: Utilisez la bibliothèque Aspose.Cells pour changer l alignement des cellules et conserver la mise en forme existante
keywords: Aspose.Cells, C#, Alignement des cellules, préserver la mise en forme existante
type: docs
weight: 340
url: /fr/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez modifier l'alignement de plusieurs cellules tout en conservant le formatage existant. Aspose.Cells vous permet de le faire en utilisant la propriété [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments). Si vous le définissez sur **true**, les modifications apportées à l'alignement auront lieu sinon non. Veuillez noter que l'objet [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) est passé en paramètre à la méthode [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) qui applique effectivement le formatage à une plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338585.xlsx), crée la plage et centre l'alignement horizontalement et verticalement tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel en sortie](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant alignées au centre horizontalement et verticalement.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
