---
title: Optimisation de l utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données
type: docs
weight: 110
url: /fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Lors de la construction d'un classeur avec de grands ensembles de données, ou de la lecture d'un gros fichier Microsoft Excel, la quantité totale de RAM que le processus va prendre est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face au défi. Aspose.Cells propose des options et des appels API pertinents pour réduire, réduire et optimiser l'utilisation de la mémoire. De plus, cela peut aider le processus à travailler de manière plus efficace et à s'exécuter plus rapidement.

Utiliser l'option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) pour optimiser l'utilisation de la mémoire utilisée pour les données des cellules afin de réduire le coût total de la mémoire. Lors de la construction d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimisation de la mémoire**

### **Lecture de gros fichiers Excel**

L'exemple suivant montre comment lire un gros fichier Microsoft Excel en mode optimisé.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Écriture de gros fichiers Excel**

L'exemple suivant montre comment écrire un grand ensemble de données dans une feuille de calcul en mode optimisé.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Attention**

L'option par défaut, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) est appliquée pour toutes les versions. Pour certaines situations, telles que la construction d'un classeur avec un grand ensemble de données pour les cellules, l'option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) peut optimiser l'utilisation de la mémoire et réduire le coût de la mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas particuliers comme suit.

1. **Accéder de manière aléatoire et répétée aux cellules**: La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une rangée, puis rangée par rangée. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) et [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row), les performances seraient maximisées avec [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE).
1. **Insertion & Suppression de cellules & de rangées**: Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression de Cellules/Rangées, la dégradation des performances sera notable pour le mode [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) par rapport au mode [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL). 
1. **Traitement sur différents types de cellules**: Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même que le mode [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) mais s'il y a beaucoup de cellules vides, ou les valeurs des cellules sont numériques, booléennes, etc., l'option [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY-PREFERENCE) offrira de meilleures performances.
{{< app/cells/assistant language="java" >}}
