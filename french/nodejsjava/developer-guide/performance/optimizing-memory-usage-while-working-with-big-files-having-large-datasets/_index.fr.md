---
title: Optimisation de l'utilisation de la mémoire lors de l'utilisation de fichiers volumineux contenant de grands ensembles de données
type: docs
weight: 110
url: /fr/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Lors de la création d'un classeur avec de grands ensembles de données ou de la lecture d'un gros fichier Excel Microsoft, la quantité totale de RAM que le processus prendra est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face au défi. Aspose.Cells fournit des options pertinentes et des appels API pour réduire, réduire et optimiser l'utilisation de la mémoire. En outre, cela peut aider le processus à fonctionner plus efficacement et à s'exécuter plus rapidement.

 Utilisation[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option pour optimiser la mémoire utilisée pour les données des cellules afin de réduire le coût global de la mémoire. Lors de la création d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut[**Réglage de la mémoire.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimisation de la mémoire**

L'exemple suivant montre comment optimiser l'utilisation de la mémoire tout en travaillant avec des données volumineuses dans Aspose.Cells pour Node.js via Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Mise en garde**

 L'option par défaut,[**Réglage de la mémoire.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)est appliqué pour toutes les versions. Dans certaines situations, telles que la création d'un classeur avec un grand ensemble de données pour les cellules, le[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)L'option peut optimiser l'utilisation de la mémoire et réduire le coût de la mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas particuliers tels que les suivants.

1. **Accéder au Cells de manière aléatoire et répétée** : La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une ligne, puis ligne par ligne. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) et[**Ligne**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , les performances seraient maximisées avec[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Insertion et suppression de Cells et de lignes** : Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression pour Cells/Rows, la dégradation des performances sera notable pour[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) mode par rapport au[**Réglage de la mémoire.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)mode.
1. **Fonctionnement sur différents types Cell** : Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même que[**Réglage de la mémoire.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)mode mais s'il y a beaucoup de cellules vides, ou si les valeurs des cellules sont numériques, bool et ainsi de suite, le[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)l'option offrira de meilleures performances.

