---
title: Copier Sparkline en spécifiant la plage de données et la localisation du groupe Sparkline avec Golang via C++
linktitle: Copier une mini courbe en spécifiant la plage de données et la localisation
type: docs
weight: 300
url: /fr/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Apprenez comment copier des mini courbes en spécifiant la plage de données et la localisation avec Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel vous permet de copier une sparkline en spécifiant la plage de données et l'emplacement d'un groupe de sparkline. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}

Pour copier une sparkline vers d'autres cellules dans Microsoft Excel:

1. Sélectionnez la cellule contenant la sparkline.
1. Sélectionnez **Modifier les données** dans la section **Sparkline** de l'onglet **Conception**.
1. Sélectionnez **Modifier l'emplacement du groupe et les données**.
1. Spécifiez la plage de données et l'emplacement.
1. Cliquez sur **OK**.

Aspose.Cells fournit la méthode `SparklineCollection.Add(dataRange, row, column)` pour spécifier la plage de données et la localisation d'un groupe de mini-courbes. Le code d'exemple suivant charge le fichier Excel source comme montré dans la capture d'écran ci-dessus, accède au premier groupe de mini-courbes et ajoute des plages de données et des localisations dans le groupe de mini-courbes. Enfin, il écrit le fichier Excel de sortie sur le disque, également affiché dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
