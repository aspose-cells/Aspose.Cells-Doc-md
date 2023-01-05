---
title: Réutilisation des objets de style
type: docs
weight: 60
url: /fr/java/reusing-style-objects/
---
{{% alert color="primary" %}}

La réutilisation d'objets de style peut économiser de la mémoire et accélérer l'exécution du programme.

{{% /alert %}}

Pour appliquer une mise en forme à une large plage de cellules dans une feuille de calcul :

1. Créez un objet de style.
1. Spécifiez les attributs.
1. Appliquez le style aux cellules de la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Le même processus que décrit ci-dessus pourrait également être accompli comme suit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 Parce que le[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) et[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) ) utilisent beaucoup moins de mémoire et sont efficaces, plus les anciennes*Cell.getStyle()* propriété qui consommait beaucoup de mémoire inutile, a été supprimée avec la sortie de*Aspose.Cells 7.1.0*.

{{% /alert %}}
