---
title: Axe des dates
type: docs
weight: 200
url: /fr/net/date-axis/
---
## **Scénarios d'utilisation possibles**
Lorsque vous créez un graphique à partir de données de feuille de calcul qui utilise des dates et que les dates sont tracées le long de l'axe horizontal (catégorie) dans le graphique, Aspose.cells change automatiquement l'axe des catégories en un axe de date (échelle de temps).
Un axe de date affiche les dates dans l'ordre chronologique à des intervalles ou unités de base spécifiques, tels que le nombre de jours, de mois ou d'années, même si les dates sur la feuille de calcul ne sont pas dans l'ordre séquentiel ou dans les mêmes unités de base.
Par défaut, Aspose.cells détermine les unités de base pour l'axe des dates en fonction de la plus petite différence entre deux dates dans les données de la feuille de calcul. Par exemple, si vous avez des données pour les prix des actions où la plus petite différence entre les dates est de sept jours, Excel définit l'unité de base sur les jours, mais vous pouvez modifier l'unité de base sur les mois ou les années si vous souhaitez voir les performances de l'action sur une plus longue période de temps.
## **Gérer l'axe de la date comme Microsoft Excel**
 Veuillez consulter l'exemple de code suivant qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille de calcul.
 Ensuite, nous ajoutons un graphique et définissons le type de[**Axe**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis) 
 à[**Échelle de temps**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/categorytype/) puis définissez les unités de base sur Jours.

![tâche : image_autre_texte](excel.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DateAxis.cs" >}}
