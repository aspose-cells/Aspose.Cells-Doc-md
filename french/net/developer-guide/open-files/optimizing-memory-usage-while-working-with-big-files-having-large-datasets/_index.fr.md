---
title: Optimisation de l'utilisation de la mémoire lors de l'utilisation de fichiers volumineux contenant de grands ensembles de données
type: docs
weight: 180
url: /fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Lors de la création d'un classeur avec de grands ensembles de données ou de la lecture d'un gros fichier Excel Microsoft, la quantité totale de RAM que le processus prendra est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face au défi. Aspose.Cells fournit des options pertinentes et des appels API pour réduire, réduire et optimiser l'utilisation de la mémoire. En outre, cela peut aider le processus à fonctionner plus efficacement et plus rapidement.

 Utilisez le[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)option pour optimiser l'utilisation de la mémoire pour les données des cellules et réduire le coût global de la mémoire. Lors de la création d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Optimisation de la mémoire**

### **Lecture de gros fichiers Excel**

L'exemple suivant montre comment lire un gros fichier Excel Microsoft en mode optimisé.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Écrire de gros fichiers Excel**

L'exemple suivant montre comment écrire un jeu de données volumineux dans une feuille de calcul en mode optimisé.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Prudence**

 L'option par défaut,[**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)est appliqué pour toutes les versions. Dans certaines situations, telles que la création d'un classeur avec un grand ensemble de données pour les cellules, le[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)L'option peut optimiser l'utilisation de la mémoire et réduire le coût de la mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas particuliers tels que les suivants.

1. **Accéder au Cells de manière aléatoire et répétée** : La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une ligne, puis ligne par ligne. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) et[**Ligne**](https://reference.aspose.com/cells/net/aspose.cells/row) , les performances seraient maximisées avec[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Insertion et suppression de Cells et de lignes** : Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression pour Cells/Rows, la dégradation des performances sera notable pour*Préférence Mémoire* mode par rapport au*Normal*mode.
1. **Fonctionnement sur différents types Cell** : Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même que*Normal* mode mais s'il y a beaucoup de cellules vides, ou si les valeurs des cellules sont numériques, bool et ainsi de suite, le[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)l'option offrira de meilleures performances.
