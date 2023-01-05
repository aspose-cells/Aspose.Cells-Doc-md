---
title: Copier les données de plage avec style
type: docs
weight: 340
url: /fr/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[Copier uniquement les données de plage](/cells/fr/java/copy-range-data-only/) a expliqué comment copier les données d'une plage de cellules vers une autre plage. Aspose.Cells peut également copier une plage complète avec formatage. Cet article explique comment.

{{% /alert %}} 
## **Copier les données de plage avec style**
Aspose.Cells fournit une gamme de classes et de méthodes pour travailler avec des plages, par exemple,[createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StyleDrapeau](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [appliquerStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), etc.

Cet exemple :

1. Crée un classeur.
1. Remplit un certain nombre de cellules de la première feuille de calcul avec des données.
1. Crée une plage.
1. Crée un objet de style avec des attributs de mise en forme spécifiés.
1. Applique le style à la plage de données.
1. Crée une deuxième plage de cellules.
1. Copie les données avec le formatage de la première plage vers la deuxième plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

