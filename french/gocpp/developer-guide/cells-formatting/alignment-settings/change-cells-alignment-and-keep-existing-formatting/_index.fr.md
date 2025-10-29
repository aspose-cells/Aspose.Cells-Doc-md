---
title: Changer l alignement des cellules et conserver la mise en forme existante avec Golang via C++
description: Utilisez la bibliothèque Aspose.Cells pour changer l alignement des cellules et conserver la mise en forme existante
keywords: Aspose.Cells, C++, alignement des cellules, conserver la mise en forme existante
type: docs
weight: 340
url: /fr/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez changer l'alignement de plusieurs cellules tout en conservant la mise en forme existante. Aspose.Cells vous permet de le faire en utilisant la propriété [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/). Si vous la définissez sur **true**, les changements d'alignement seront appliqués, sinon non. Notez que l'objet [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) est passé en paramètre à la méthode [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) qui applique en réalité la mise en forme à une plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338585.xlsx), crée la plage et centre l'alignement horizontalement et verticalement tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel en sortie](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant alignées au centre horizontalement et verticalement.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
