---
title: Copier les données de la plage avec style
type: docs
weight: 610
url: /fr/net/copy-range-data-with-style/
---

{{% alert color="primary" %}}

[Copier uniquement les données de la plage](/cells/fr/net/copy-range-data-only/) explique comment copier les données d'une plage de cellules vers une autre plage. En particulier, cela applique un nouvel ensemble de styles aux cellules copiées. Aspose.Cells peut également copier une plage avec mise en forme. Cet article explique comment.

{{% /alert %}}

Aspose.Cells propose toute une gamme de classes et de méthodes pour travailler avec des plages, par exemple, [**CreateRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index), [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) et [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/applystyle).

Cet exemple :

1. Crée un classeur.
1. Remplit un certain nombre de cellules dans la première feuille de calcul avec des données.
1. Crée un [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).
1. Crée un objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) avec des attributs de mise en forme spécifiés.
1. Applique le style à la plage de données.
1. Crée un deuxième groupe de cellules.
1. Copie les données avec la mise en forme de la première plage vers la deuxième plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeDataWithStyle-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
