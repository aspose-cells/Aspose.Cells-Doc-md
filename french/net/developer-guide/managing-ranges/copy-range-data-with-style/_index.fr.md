---
title: Copier les données de plage avec style
type: docs
weight: 610
url: /fr/net/copy-range-data-with-style/
---
{{% alert color="primary" %}}

[Copier uniquement les données de plage](/cells/fr/net/copy-range-data-only/) a expliqué comment copier les données d'une plage de cellules vers une autre plage. Plus précisément, le processus a appliqué un nouvel ensemble de styles aux cellules copiées. Aspose.Cells peut également copier une plage complète avec formatage. Cet article explique comment.

{{% /alert %}}

Aspose.Cells fournit une gamme de classes et de méthodes pour travailler avec des plages, par exemple,[**CréerPlage()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) et[**AppliquerStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Cet exemple :

1. Crée un classeur.
1. Remplit un certain nombre de cellules de la première feuille de calcul avec des données.
1.  Crée un[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range).
1.  Crée un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet avec les attributs de formatage spécifiés.
1. Applique le style à la plage de données.
1. Crée une deuxième plage de cellules.
1. Copie les données avec le formatage de la première plage vers la deuxième plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
