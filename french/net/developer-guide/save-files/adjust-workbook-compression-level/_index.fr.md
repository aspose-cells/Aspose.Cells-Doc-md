---
title: Ajuster le niveau de compression du classeur
type: docs
weight: 180
url: /fr/net/adjust-workbook-compression-level/
---

## **Ajuster le niveau de compression du classeur**

Les développeurs peuvent ajuster le niveau de compression du classeur lorsqu'ils travaillent avec des classeurs plus grands. Les développeurs peuvent privilégier des tailles de fichier plus petites par rapport au temps de traitement ou vice versa. Aspose.Cells fournit l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) que vous pouvez utiliser pour définir le niveau de compression du classeur. L'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) offre les membres suivants.

- Level1: La compression la plus rapide mais la moins efficace.
- Level2: Un peu plus lent, mais meilleur que le niveau 1.
- Level3: Un peu plus lent, mais meilleur que le niveau 2.
- Level4: Un peu plus lent, mais meilleur que le niveau 3.
- Level5: Un peu plus lent que le niveau 4, mais avec une meilleure compression.
- Level6: Un bon équilibre entre la vitesse et l'efficacité de la compression.
- Level7: Une assez bonne compression!
- Level8: Meilleure compression que le niveau 7!
- Level9: La compression "la meilleure", où meilleure signifie la plus grande réduction de la taille du flux de données d'entrée. Il s'agit également de la compression la plus lente.

Le code suivant démontre l'utilisation de l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) et compare le temps de conversion pour le Niveau1, Niveau6 et Niveau9. Vous pouvez également comparer les tailles des fichiers générés.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
