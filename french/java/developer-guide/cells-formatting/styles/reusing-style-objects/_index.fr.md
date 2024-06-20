---
title: Réutilisation d objets de style
type: docs
weight: 60
url: /fr/java/reusing-style-objects/
---

{{% alert color="primary" %}}

Réutiliser les objets de style peut économiser de la mémoire et rendre le programme plus rapide à exécuter.

{{% /alert %}}

Pour appliquer une mise en forme à une grande plage de cellules dans une feuille de calcul :

1. Créer un objet de style.
1. Spécifier les attributs.
1. Appliquer le style aux cellules dans la plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Le même processus que celui discuté ci-dessus pourrait également être accompli comme suit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

Parce que les méthodes [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) et [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) utilisent beaucoup moins de mémoire et sont efficaces, l'ancienne propriété *Cell.getStyle()* qui consommait beaucoup de mémoire inutile, a été supprimée avec la version *Aspose.Cells 7.1.0*.

{{% /alert %}}
