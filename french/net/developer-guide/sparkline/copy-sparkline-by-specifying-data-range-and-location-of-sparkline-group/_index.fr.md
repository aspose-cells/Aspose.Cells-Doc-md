---
title: Copier Sparkline en spécifiant la plage de données et l'emplacement du groupe Sparkline
type: docs
weight: 300
url: /fr/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel vous permet de copier un graphique sparkline en spécifiant la plage de données et l'emplacement d'un groupe de graphiques sparkline. Aspose.Cells prend en charge cette fonctionnalité.

{{% /alert %}}

Pour copier un graphique sparkline dans d'autres cellules dans Microsoft Excel :

1. Sélectionnez la cellule contenant le sparkline.
1.  Sélectionner**Modifier les données** du**Sparkline** partie de la**Concevoir** languette.
1.  Sélectionner**Modifier l'emplacement et les données du groupe**.
1. Spécifiez la plage de données et l'emplacement.
1.  Cliquez sur**D'ACCORD**.

Aspose.Cells fournit la méthode SparklineCollection.Add(dataRange, row, column) pour spécifier la plage de données et l'emplacement d'un groupe sparkline. L'exemple de code suivant charge le fichier Excel source comme indiqué dans la capture d'écran ci-dessus, puis accède au premier groupe de graphiques sparkline et ajoute des plages de données et des emplacements dans le groupe de graphiques sparkline. Enfin, il écrit le fichier Excel de sortie sur le disque, qui est également illustré dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
