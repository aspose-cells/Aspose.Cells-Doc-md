---
title: Optimisation de l utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données
type: docs
weight: 180
url: /fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Lors de la création d'un classeur avec de grands ensembles de données, ou de la lecture d'un gros fichier Microsoft Excel, la quantité totale de RAM prise par le processus est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face à ce défi. Aspose.Cells propose des options et des appels d'API pertinents pour réduire et optimiser l'utilisation de la mémoire. De plus, cela peut aider le processus à fonctionner de manière plus efficace et plus rapide.

Utilisez l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) pour optimiser l'utilisation de la mémoire pour les données des cellules et réduire le coût total de la mémoire. Lors de la création d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Optimisation de la mémoire**

### **Lecture de gros fichiers Excel**

L'exemple suivant montre comment lire un gros fichier Microsoft Excel en mode optimisé.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Écriture de gros fichiers Excel**

L'exemple suivant montre comment écrire un grand ensemble de données dans une feuille de calcul en mode optimisé.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Attention**

L'option par défaut, [**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) est appliquée pour toutes les versions. Pour certaines situations, telles que la création d'un classeur avec un grand ensemble de données pour les cellules, l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) peut optimiser l'utilisation de la mémoire et réduire le coût de mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas spéciaux comme suit.

1. **Accéder de manière aléatoire et répétée aux cellules**: La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une rangée, puis rangée par rangée. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) et [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), les performances seraient maximisées avec [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Insertion et suppression de cellules et de lignes** : Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression de Cellules/Lignes, la dégradation des performances sera notable en mode *MemoryPreference* par rapport au mode *Normal*.
1. **Opérer sur différents types de cellules** : Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même qu'en mode *Normal*, mais s'il y a beaucoup de cellules vides, ou que les valeurs des cellules sont numériques, booléennes, et ainsi de suite, l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) offrira de meilleures performances.
{{< app/cells/assistant language="csharp" >}}
