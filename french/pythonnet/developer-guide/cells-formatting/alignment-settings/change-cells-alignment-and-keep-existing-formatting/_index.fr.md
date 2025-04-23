---
title: Modifier l alignement des cellules et conserver la mise en forme existante
description: Utilisez la bibliothèque Aspose.Cells for Python via .NET pour changer l alignement des cellules et préserver la mise en forme existante
keywords: Aspose.Cells for Python via .NET, alignement des cellules en Python, préserver la mise en forme existante
type: docs
weight: 340
url: /fr/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez changer l'alignement de plusieurs cellules tout en conservant la mise en forme existante. Aspose.Cells pour Python via .NET vous permet de le faire en utilisant la propriété [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments). Si vous la définissez sur **true**, les changements d'alignement auront lieu, sinon non. Veuillez noter que l'objet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) est passé en paramètre à la méthode [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) qui applique effectivement la mise en forme à une plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338585.xlsx), crée la plage et centre l'alignement horizontalement et verticalement tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel en sortie](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant alignées au centre horizontalement et verticalement.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

