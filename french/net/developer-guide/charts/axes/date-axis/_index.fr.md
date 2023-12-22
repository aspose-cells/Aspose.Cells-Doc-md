---
title: Axe des dates
description: Apprenez à gérer l'axe des dates dans Aspose.Cells for .NET. Notre guide vous aidera à comprendre comment travailler avec différents formats de date, échelles de temps et fréquences d'étiquettes de graduation.
keywords: Aspose.Cells for .NET, date axis, manage, date formats, time scales, tick label frequencies.
type: docs
weight: 200
url: /fr/net/date-axis/
---
##  **Scénarios d'utilisation possibles**
Lorsque vous créez un graphique à partir de données de feuille de calcul qui utilise des dates et que les dates sont tracées le long de l'axe horizontal (catégorie) dans le graphique, Aspose.cells remplace automatiquement l'axe des catégories par un axe de date (échelle de temps).
Un axe des dates affiche les dates par ordre chronologique à des intervalles ou unités de base spécifiques, tels que le nombre de jours, de mois ou d'années, même si les dates sur la feuille de calcul ne sont pas dans un ordre séquentiel ou dans les mêmes unités de base.
Par défaut, Aspose.cells détermine les unités de base pour l'axe des dates en fonction de la plus petite différence entre deux dates dans les données de la feuille de calcul. Par exemple, si vous disposez de données sur les cours des actions pour lesquelles la plus petite différence entre les dates est de sept jours, Excel définit l'unité de base sur les jours, mais vous pouvez modifier l'unité de base sur les mois ou les années si vous souhaitez voir la performance de l'action sur une période plus longue. une période de temps plus longue.
##  **Gérer l'axe des dates comme Microsoft Excel**
 Veuillez consulter l'exemple de code suivant qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille de calcul.
 Ensuite, nous ajoutons un graphique et définissons le type de[**Axe**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 à[**Échelle de temps**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) puis définissez les unités de base sur Jours.

![tâche : image_alt_text](excel.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
