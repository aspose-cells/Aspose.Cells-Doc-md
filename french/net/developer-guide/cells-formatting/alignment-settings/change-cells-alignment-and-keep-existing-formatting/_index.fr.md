---
title: Modifier l'alignement Cells et conserver le formatage existant
description: Utilisez la bibliothèque Aspose.Cells pour modifier l'alignement des cellules et conserver le formatage existant
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /fr/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **Scénarios d'utilisation possibles**

Parfois, vous souhaitez modifier l’alignement de plusieurs cellules, mais également conserver le formatage existant. Aspose.Cells vous permet de le faire en utilisant le[**StyleFlag.Alignements**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) propriété. Si vous le définissez *true**, les changements d'alignement auront lieu sinon pas. Veuillez noter,[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) l'objet est passé en paramètre à[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)méthode qui applique réellement le formatage à une plage de cellules.

##  **Modifier l'alignement Cells et conserver le formatage existant**

 L'exemple de code suivant charge le[exemple de fichier Excel](67338585.xlsx) , crée la plage et le centre, l'aligne horizontalement et verticalement et conserve la mise en forme existante intacte. La capture d'écran suivante compare l'exemple de fichier Excel et[sortie du fichier Excel](67338586.xlsx) et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont désormais alignées au centre horizontalement et verticalement.

![tâche : image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
