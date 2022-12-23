---
title: Modifier l'alignement Cells et conserver la mise en forme existante
type: docs
weight: 260
url: /fr/java/change-cells-alignment-and-keep-existing-formatting/
---
## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez modifier l'alignement de plusieurs cellules, mais souhaitez également conserver la mise en forme existante. Aspose.Cells vous permet de le faire en utilisant le[**StyleFlag.Alignements**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) la propriété. Si vous le réglez**vrai** , des changements d'alignement auront lieu sinon. Veuillez noter,[**StyleDrapeau**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) objet est passé en paramètre à[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) méthode qui applique réellement la mise en forme à la plage de cellules.

## **Modifier l'alignement Cells et conserver la mise en forme existante**

L'exemple de code suivant charge le[exemple de fichier Excel](67338592.xlsx), crée la plage et le centre l'aligne horizontalement et verticalement et conserve la mise en forme existante intacte. La capture d'écran suivante compare l'exemple de fichier Excel et[fichier Excel de sortie](67338591.xlsx)et montre que tout le formatage existant des cellules est le même, sauf que les cellules sont maintenant centrées horizontalement et verticalement.

![tâche : image_autre_texte](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
