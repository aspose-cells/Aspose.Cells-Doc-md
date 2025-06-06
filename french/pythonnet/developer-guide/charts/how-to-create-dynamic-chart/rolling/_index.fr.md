---
title: Comment créer un graphique dynamique roulant
description: Apprenez comment créer un graphique coulissant dynamique avec Aspose.Cells pour Python via .NET. Notre guide vous montrera comment implémenter des transitions de données fluides et des moyennes mobiles dans votre graphique pour une visualisation continue et mise à jour.
keywords: Aspose.Cells pour Python via .NET, graphique coulissant dynamique, transitions de données, moyennes mobiles, affichage continu, mise à jour de la visualisation.
type: docs
weight: 74
url: /fr/python-net/create-dynamic-rolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique roulant se réfère à une représentation graphique qui affiche des points de données constamment en mouvement et se met à jour au fil du temps. Il s'agit d'un type de graphique qui se met continuellement à jour, présentant une fenêtre roulante des points de données les plus récents tout en éliminant les anciens points de données au fur et à mesure que de nouveaux arrivent.

Les graphiques dynamiques roulants sont couramment utilisés pour visualiser les tendances et les motifs dans les données en temps réel ou en continu. Ils sont particulièrement utiles dans des scénarios où les aspects temporels et les changements au fil du temps sont critiques, comme l'analyse du marché boursier, la surveillance météorologique ou le suivi des performances en direct.

Ces graphiques utilisent généralement des mécanismes d'animation ou de défilement automatique pour garantir que les informations les plus récentes sont toujours présentées. La longueur de la fenêtre roulante peut être personnalisée pour afficher une période de temps spécifique, comme la dernière heure, le jour ou la semaine.

En résumé, un graphique dynamique roulant est une représentation graphique continuellement mise à jour qui affiche les derniers points de données tout en éliminant les anciens, permettant aux utilisateurs d'observer les tendances et les motifs en temps réel.

## **Utilisez Aspose.Cells pour Python via .NET pour créer un graphique coulissant dynamique**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique dynamique à balayage en utilisant Aspose.Cells pour Python via .NET. Nous vous présenterons le code pour l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Rolling Chart](DynamicRollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-rolling-chart.py" >}}

## **Remarques**
Dans le fichier généré, vous pouvez continuer à ajouter des données dans les colonnes A et B, tandis que le graphique comptera dynamiquement les 5 ensembles de données les plus récents. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Vous pouvez essayer de changer le chiffre "-5" par "-10" dans la formule, et le graphique dynamique comptera les 10 dernières séries de données. Nous avons maintenant créé un graphique à balayage dynamique avec succès en utilisant Aspose.Cells pour Python via .NET.
