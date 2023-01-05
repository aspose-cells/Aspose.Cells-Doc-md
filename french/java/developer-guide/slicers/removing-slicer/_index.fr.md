---
title: Retrait du trancheur
type: docs
weight: 30
url: /fr/java/removing-slicer/
---
## **Scénarios d'utilisation possibles**
Si vous souhaitez supprimer le trancheur dans Microsoft Excel, sélectionnez-le simplement et appuyez sur le bouton*Effacer*bouton. De même, si vous souhaitez le supprimer à l'aide de Aspose.Cells API par programme, veuillez utiliser le[Feuille de calcul.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)) méthode. Cela supprimera le segment de la feuille de calcul.
## **Retrait du trancheur**
L'exemple de code suivant charge le[exemple de fichier Excel](67338504.xlsx)qui contient un segment existant. Il accède aux slicers puis le supprime. Enfin, il enregistre le classeur sous[fichier Excel de sortie](67338502.xlsx). La capture d'écran suivante montre le segment qui sera supprimé après l'exécution de l'exemple de code.

![tâche : image_autre_texte](removing-slicer_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
