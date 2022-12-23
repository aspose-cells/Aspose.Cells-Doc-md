---
title: Ajuster le niveau de compression du classeur
type: docs
weight: 130
url: /fr/java/adjust-workbook-compression-level/
---
## **Ajuster le niveau de compression du classeur**

Les développeurs peuvent ajuster le niveau de compression du classeur lorsqu'ils travaillent avec des classeurs plus volumineux. Les développeurs peuvent donner la priorité aux tailles de fichiers plus petites par rapport au temps de traitement ou vice versa. Aspose.Cells fournit**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)**énumération que vous pouvez utiliser pour définir le niveau de compression du classeur. Le**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** L'énumération fournit les membres suivants.

- **[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**: La compression la plus rapide mais la moins efficace.
- **[LEVEL_2](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_2)**: Un peu plus lent, mais mieux, que le niveau 1.
- **[LEVEL_3](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_3)**Un peu plus lent, mais mieux, que le niveau 2.
- **[LEVEL_4](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_4)**: Un peu plus lent, mais mieux, que le niveau 3.
- **[LEVEL_5](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_5)**: Un peu plus lent que le niveau 4, mais avec une meilleure compression.
- **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)**: Un bon équilibre entre vitesse et efficacité de compression.
- **[LEVEL_7](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_7)**: Assez bonne compression !
- **[LEVEL_8](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_8)**: Meilleure compression que Level7 !
- **[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**La "meilleure" compression, où meilleure signifie la plus grande réduction de la taille du flux de données d'entrée. C'est aussi la compression la plus lente.

L'extrait de code suivant illustre l'utilisation de**[OoxmlCompressionType](https://reference.aspose.com/cells/java/com.aspose.cells/OoxmlCompressionType)** énumération et compare le temps de conversion pour**[LEVEL_1](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_1)**, **[LEVEL_6](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_6)** , et**[LEVEL_9](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompressiontype#LEVEL_9)**. Vous pouvez également comparer les tailles des fichiers générés.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AdjustCompressionLevel-1.java" >}}
