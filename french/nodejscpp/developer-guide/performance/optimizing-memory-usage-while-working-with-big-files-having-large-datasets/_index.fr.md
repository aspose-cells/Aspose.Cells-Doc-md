---
title: Optimisation de l utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données
type: docs
weight: 110
url: /fr/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Lors de la construction d'un classeur avec de grands ensembles de données, ou de la lecture d'un gros fichier Microsoft Excel, la quantité totale de RAM que le processus va prendre est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face au défi. Aspose.Cells propose des options et des appels API pertinents pour réduire, réduire et optimiser l'utilisation de la mémoire. De plus, cela peut aider le processus à travailler de manière plus efficace et à s'exécuter plus rapidement.

Utiliser l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) pour optimiser l'utilisation de la mémoire utilisée pour les données des cellules afin de réduire le coût total de la mémoire. Lors de la construction d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).

{{% /alert %}}

## **Optimisation de la mémoire**

L'exemple suivant montre comment optimiser l'utilisation de la mémoire lors du travail avec de grandes données dans Aspose.Cells pour Node.js via C++.

{{< highlight cpp >}}

//This example shows how to optimize memory usage while working with large data in Aspose.Cells for Node.js via C++

const { Workbook, FileFormatType, MemorySetting } = require("aspose.cells.node");

var workbook = new Workbook(FileFormatType.Xlsx);

// apply the setting to existing "Sheet1"
workbook.getWorksheets().get(0).getCells().setMemorySetting(MemorySetting.MemoryPreference);

// apply the setting globally
workbook.getSettings().setMemorySetting(MemorySetting.MemoryPreference);

workbook.save("out.xlsx");

{{< /highlight >}}

## **Attention**

L'option par défaut, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) est appliquée pour toutes les versions. Pour certaines situations, telles que la construction d'un classeur avec un grand ensemble de données pour les cellules, l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) peut optimiser l'utilisation de la mémoire et réduire le coût de la mémoire pour l'application. Cependant, cette option peut dégrader les performances dans certains cas particuliers comme suit.

1. **Accéder de manière aléatoire et répétée aux cellules**: La séquence la plus efficace pour accéder à la collection de cellules est cellule par cellule dans une rangée, puis rangée par rangée. Surtout, si vous accédez aux lignes/cellules par l'énumérateur acquis à partir de [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) et [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), les performances seraient maximisées avec [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).
1. **Insertion & Suppression de cellules & de rangées**: Veuillez noter que s'il y a beaucoup d'opérations d'insertion/suppression de Cellules/Rangées, la dégradation des performances sera notable pour le mode [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) par rapport au mode [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/). 
1. **Traitement sur différents types de cellules**: Si la plupart des cellules contiennent des valeurs de chaîne ou des formules, le coût de la mémoire sera le même que le mode [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) mais s'il y a beaucoup de cellules vides, ou les valeurs des cellules sont numériques, booléennes, etc., l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) offrira de meilleures performances.

