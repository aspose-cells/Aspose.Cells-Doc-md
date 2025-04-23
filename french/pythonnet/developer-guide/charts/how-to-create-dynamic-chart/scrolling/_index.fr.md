---
title: Comment créer un graphique dynamique déroulant
description: Apprenez comment créer un graphique à défilement dynamique en utilisant Aspose.Cells pour Python via .NET. Notre guide étape par étape vous montrera comment implémenter des transitions de données fluides et un défilement automatique dans votre graphique pour un affichage continu et à jour.
keywords: Aspose.Cells pour Python via .NET, Graphique à défilement dynamique, Transitions de données, Défilement fluide, Affichage continu, Mise à jour de la visualisation.
type: docs
weight: 75
url: /fr/python-net/create-dynamic-scrolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique déroulant est un type de représentation graphique utilisé pour afficher des données qui changent avec le temps. Il est conçu pour fournir une vue en temps réel des données, permettant aux utilisateurs de suivre les mises à jour et les tendances continues. Le graphique se met à jour en continu lorsque de nouvelles données sont ajoutées, et il défile automatiquement pour afficher les informations les plus récentes.

Les graphiques dynamiques déroulants sont couramment utilisés dans diverses industries, telles que la finance, l'analyse du marché boursier, le suivi météorologique et l'analyse des médias sociaux. Ils permettent aux utilisateurs de visualiser et d'analyser les motifs de données et de prendre des décisions éclairées en fonction des informations en temps réel.

Ces graphiques sont généralement interactifs, permettant à l'utilisateur de zoomer, de faire défiler les données historiques et d'ajuster les intervalles de temps. Ils prennent souvent en charge plusieurs séries de données, offrant une vue complète des différentes mesures et de leurs corrélations.

 Globalement, les graphiques dynamiques déroulants sont des outils précieux pour surveiller et analyser les données en séries chronologiques, faciliter la prise de décisions en temps réel et améliorer les capacités de visualisation des données.

## **Utilisez Aspose.Cells pour Python via .NET pour créer un graphique à défilement dynamique**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique à défilement dynamique en utilisant Aspose.Cells pour Python via .NET. Nous vous présenterons le code pour l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [Fichier de graphique dynamique déroulant](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-dynamic-scrolling-chart.py" >}}

## **Remarques**
Dans le fichier généré, vous pouvez agir sur la barre de défilement, tandis que le graphique compte dynamiquement les 10 derniers ensembles de données. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Vous pouvez essayer de changer le chiffre "10" par "15" dans la cellule "Sheet1!$H$20", et le graphique dynamique comptera les 15 dernières séries de données. Nous avons maintenant créé un graphique à défilement dynamique avec succès en utilisant Aspose.Cells pour Python via .NET.
