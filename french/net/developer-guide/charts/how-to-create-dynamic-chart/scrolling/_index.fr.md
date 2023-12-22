---
title: Comment créer un graphique à défilement dynamique
description: Apprenez à créer un graphique à défilement dynamique en utilisant le Aspose.Cells for .NET. Notre guide étape par étape vous montrera comment mettre en œuvre des transitions de données fluides et un défilement automatique dans votre graphique pour un affichage continu et mis à jour.
keywords: Aspose.Cells for .NET, Dynamic Scrolling Chart, Data Transitions, Smooth Scrolling, Continuous Display, Updating Visualization.
type: docs
weight: 75
url: /fr/net/create-dynamic-scrolling-chart/
---
##  **Scénarios d'utilisation possibles**
Le graphique à défilement dynamique est un type de représentation graphique utilisé pour afficher des données qui changent au fil du temps. Il est conçu pour fournir une vue en temps réel des données, permettant aux utilisateurs de suivre les mises à jour et les tendances en continu. Le graphique se met continuellement à jour à mesure que de nouvelles données sont ajoutées et défile automatiquement pour afficher les informations les plus récentes.

Les graphiques à défilement dynamiques sont couramment utilisés dans divers secteurs, tels que la finance, l'analyse boursière, le suivi météorologique et l'analyse des médias sociaux. Ils permettent aux utilisateurs de visualiser et d'analyser des modèles de données et de prendre des décisions éclairées basées sur des informations en temps réel.

Ces graphiques sont généralement interactifs, permettant à l'utilisateur de zoomer ou dézoomer, de faire défiler les données historiques et d'ajuster les intervalles de temps. Ils prennent souvent en charge plusieurs séries de données, offrant une vue complète des différentes mesures et de leurs corrélations.

Dans l’ensemble, les graphiques à défilement dynamiques sont des outils précieux pour surveiller et analyser les données de séries chronologiques, facilitant la prise de décision en temps réel et améliorant les capacités de visualisation des données.

##  **Utilisez Aspose Cells pour créer un graphique à défilement dynamique**
Dans les paragraphes suivants, nous allons vous montrer comment créer un graphique à défilement dynamique à l'aide de Aspose.Cells. Nous vous montrerons le code de l'exemple, ainsi que le fichier Excel créé avec ce code.

##  **Exemple de code**
 L'exemple de code suivant générera le[Fichier de graphique à défilement dynamique](DynamicScrollingChart.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-dynamic-scrolling-chart.cs" >}}

##  **Remarques**
Dans le fichier généré, vous pouvez opérer sur la barre de défilement, tandis que le graphique compte dynamiquement les 10 derniers ensembles de données. Cela se fait à l'aide de la formule « OFFSET » dans l'exemple de code :

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Vous pouvez essayer de remplacer le nombre « 10 » par « 15 » dans la cellule « Sheet1!$H$20 », et le graphique dynamique comptera les 15 derniers ensembles de données. Nous avons maintenant créé avec succès un graphique défilant dynamique en utilisant Aspose.Cells.
