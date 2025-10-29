---
title: Copier le mini graphique en spécifiant la plage de données et l emplacement du groupe de mini graphiques
type: docs
weight: 300
url: /fr/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel vous permet de copier un sparkline en spécifiant la gamme de données et l'emplacement du groupe de sparklines. Aspose.Cells pour Python via .NET supporte cette fonctionnalité.

{{% /alert %}}

Pour copier une sparkline vers d'autres cellules dans Microsoft Excel:

1. Sélectionnez la cellule contenant la sparkline.
1. Sélectionnez **Modifier les données** dans la section **Sparkline** de l'onglet **Conception**.
1. Sélectionnez **Modifier l'emplacement du groupe et les données**.
1. Spécifiez la plage de données et l'emplacement.
1. Cliquez sur **OK**.

Aspose.Cells pour Python via .NET fournit la méthode SparklineCollection.Add(gammeDeDonnées, ligne, colonne) pour spécifier la gamme de données et l’emplacement d’un groupe de sparklines. Le code d’exemple charge le fichier Excel source comme indiqué dans la capture d’écran ci-dessus, puis accède au premier groupe de sparklines et ajoute des gammes de données et des emplacements dans le groupe. Enfin, il enregistre le fichier Excel de sortie sur le disque, qui est également montré dans la capture d’écran.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
