---
title: Comment créer un graphique roulant dynamique
description: Apprenez à créer un graphique glissant dynamique en utilisant le Aspose.Cells for .NET. Notre guide vous montrera comment mettre en œuvre des transitions de données fluides et des moyennes mobiles dans votre graphique pour un affichage continu et mis à jour.
keywords: Aspose.Cells for .NET, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /fr/net/create-dynamic-rolling-chart/
---
##  **Scénarios d'utilisation possibles**
Un graphique roulant dynamique fait référence à une représentation graphique qui affiche des points de données changeant et mis à jour constamment au fil du temps. Il s'agit d'un type de graphique qui se met continuellement à jour, présentant une fenêtre glissante des points de données les plus récents tout en supprimant les points de données plus anciens à mesure que de nouveaux arrivent.

Les graphiques glissants dynamiques sont couramment utilisés pour visualiser les tendances et les modèles en temps réel ou en streaming. Ils sont particulièrement utiles dans les scénarios où les aspects temporels et les changements au fil du temps sont critiques, comme l'analyse boursière, la surveillance météo ou le suivi des performances en direct.

Ces graphiques utilisent généralement des mécanismes d'animation ou de défilement automatique pour garantir que les informations les plus récentes sont toujours présentées. La longueur de la fenêtre déroulante peut être personnalisée pour afficher une période spécifique, telle que la dernière heure, le dernier jour ou la dernière semaine.

En résumé, un graphique dynamique est une représentation graphique continuellement mise à jour qui affiche les derniers points de données tout en supprimant les plus anciens, permettant aux utilisateurs d'observer les tendances et les modèles en temps réel.

##  **Utilisez Aspose Cells pour créer un graphique glissant dynamique**
Dans les paragraphes suivants, nous allons vous montrer comment créer un Dynamic Rolling Chart à l'aide de Aspose.Cells. Nous vous montrerons le code de l'exemple, ainsi que le fichier Excel créé avec ce code.

##  **Exemple de code**
 L'exemple de code suivant générera le[Fichier de graphique roulant dynamique](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-rolling-chart.cs" >}}

##  **Remarques**
Dans le fichier généré, vous pouvez continuer à ajouter des données dans les colonnes A et B, tandis que le graphique compte dynamiquement les 5 derniers ensembles de données. Cela se fait à l'aide de la formule « OFFSET » dans l'exemple de code :

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Vous pouvez essayer de remplacer le nombre « -5 » par « -10 » dans la formule, et le graphique dynamique comptera les 10 derniers ensembles de données. Nous avons maintenant créé avec succès un graphique glissant dynamique en utilisant Aspose.Cells.
