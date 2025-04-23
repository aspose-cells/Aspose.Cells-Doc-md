---
title: Modifier l alignement des cellules et conserver la mise en forme existante
linktitle: Modifier l alignement des cellules et conserver la mise en forme existante
description: Utilisez la bibliothèque Aspose.Cells pour changer l alignement des cellules et préserver la mise en forme existante dans Node.js via C++
keywords: Aspose.Cells, Alignement des cellules, Préserver la mise en forme existante
type: docs
weight: 340
url: /fr/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Scénarios d'utilisation possibles**

 Parfois, vous souhaitez changer l'alignement de plusieurs cellules tout en conservant la mise en forme existante. Aspose.Cells for Node.js via C++ vous permet de le faire en utilisant la méthode [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-). Si vous la définissez **true**, les changements d'alignement auront lieu, sinon non. Notez que l'objet [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) est passé en paramètre à la méthode [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) qui applique effectivement la mise en forme à une plage de cellules.

## **Modifier l'alignement des cellules et conserver la mise en forme existante**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338585.xlsx), crée la plage et centre l'alignement horizontalement et verticalement tout en conservant le formatage existant intact. La capture d'écran suivante compare le fichier Excel d'exemple et le [fichier Excel en sortie](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant alignées au centre horizontalement et verticalement.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
