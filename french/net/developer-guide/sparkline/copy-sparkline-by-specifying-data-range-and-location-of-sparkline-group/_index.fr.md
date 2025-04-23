---
title: Copier le mini graphique en spécifiant la plage de données et l emplacement du groupe de mini graphiques
type: docs
weight: 300
url: /fr/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
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

Aspose.Cells fournit la méthode SparklineCollection.Add(dataRange, row, column) pour spécifier la plage de données et l'emplacement d'un groupe de sparkline. Le code d'exemple suivant charge le fichier Excel source tel qu'indiqué dans la capture d'écran ci-dessus, puis accède au premier groupe de sparkline et ajoute des plages de données et des emplacements dans le groupe de sparkline. Enfin, il écrit le fichier Excel de sortie sur le disque, qui est également montré dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
