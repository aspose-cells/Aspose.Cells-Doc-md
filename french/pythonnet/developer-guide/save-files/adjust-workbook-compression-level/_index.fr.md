---
title: Ajuster le niveau de compression du classeur
type: docs
weight: 180
url: /fr/python-net/adjust-workbook-compression-level/
---

## **Ajuster le niveau de compression du classeur**

Les développeurs peuvent ajuster le niveau de compression du classeur lorsqu’ils travaillent avec des classeurs plus volumineux. Les développeurs peuvent privilégier des tailles de fichiers plus petites ou un traitement plus rapide. Aspose.Cells pour Python via .NET fournit l’énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) que vous pouvez utiliser pour définir le niveau de compression du classeur. L’énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) fournit les membres suivants.

- Level1: La compression la plus rapide mais la moins efficace.
- Level2: Un peu plus lent, mais meilleur que le niveau 1.
- Level3: Un peu plus lent, mais meilleur que le niveau 2.
- Level4: Un peu plus lent, mais meilleur que le niveau 3.
- Level5: Un peu plus lent que le niveau 4, mais avec une meilleure compression.
- Level6: Un bon équilibre entre la vitesse et l'efficacité de la compression.
- Level7: Une assez bonne compression!
- Level8: Meilleure compression que le niveau 7!
- Level9: La compression "la meilleure", où meilleure signifie la plus grande réduction de la taille du flux de données d'entrée. Il s'agit également de la compression la plus lente.

Le code suivant démontre l'utilisation de l'énumération [**OoxmlCompressionType**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompressiontype) et compare le temps de conversion pour le Niveau1, Niveau6 et Niveau9. Vous pouvez également comparer les tailles des fichiers générés.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-AdjustCompressionLevel-1.py" >}}

