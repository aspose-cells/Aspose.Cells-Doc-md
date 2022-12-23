---
title: Ajuster le niveau de compression du classeur
type: docs
weight: 180
url: /fr/net/adjust-workbook-compression-level/
---
## **Ajuster le niveau de compression du classeur**

Les développeurs peuvent ajuster le niveau de compression du classeur lorsqu'ils travaillent avec des classeurs plus volumineux. Les développeurs peuvent donner la priorité aux tailles de fichiers plus petites par rapport au temps de traitement ou vice versa. Aspose.Cells fournit**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** énumération que vous pouvez utiliser pour définir le niveau de compression du classeur. Le**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)** L'énumération fournit les membres suivants.

- Niveau 1 : La compression la plus rapide mais la moins efficace.
- Niveau 2 : Un peu plus lent, mais meilleur, que le niveau 1.
- Niveau 3 : Un peu plus lent, mais meilleur, que le niveau 2.
- Niveau 4 : Un peu plus lent, mais meilleur, que le niveau 3.
- Niveau 5 : Un peu plus lent que le niveau 4, mais avec une meilleure compression.
- Level6 : Un bon équilibre entre vitesse et efficacité de compression.
- Level7 : Assez bonne compression !
- Level8 : Meilleure compression que Level7 !
- Niveau 9 : la "meilleure" compression, où meilleure signifie la plus grande réduction de la taille du flux de données d'entrée. C'est aussi la compression la plus lente.

 L'extrait de code suivant illustre l'utilisation de**[OoxmlCompressionType](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype)**énumération et compare le temps de conversion pour Level1, Level6 et Level9. Vous pouvez également comparer les tailles des fichiers générés.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
