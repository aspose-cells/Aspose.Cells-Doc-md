---
title: Copier les données de la plage avec style
type: docs
weight: 340
url: /fr/java/copy-range-data-with-style/
---

{{% alert color="primary" %}} 

[Copier uniquement les données de la plage](/cells/fr/java/copier-uniquement-les-donnees-de-la-plage/) explique comment copier les données d'une plage de cellules vers une autre plage. Aspose.Cells peut également copier une plage avec le formatage complet. Cet article explique comment.

{{% /alert %}} 
## **Copier les données de la plage avec le style**
Aspose.Cells fournit une gamme de classes et méthodes pour travailler avec des plages, par exemple, [createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-), [StyleFlag](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [applyStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-), etc.

Cet exemple :

1. Crée un classeur.
1. Remplit un certain nombre de cellules dans la première feuille de calcul avec des données.
1. Crée une plage.
1. Crée un objet de style avec des attributs de mise en forme spécifiés.
1. Applique le style à la plage de données.
1. Crée un deuxième groupe de cellules.
1. Copie les données avec la mise en forme de la première plage vers la deuxième plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

{{< app/cells/assistant language="java" >}}
