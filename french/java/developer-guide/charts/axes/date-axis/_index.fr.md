---
title: Axe de date
description: Apprenez comment gérer l axe des dates dans Aspose.Cells for Java. Notre guide vous aidera à comprendre comment travailler avec différents formats de dates, échelles de temps et fréquences de libellés d axe.
keywords: Aspose.Cells for Java, axe des dates, gérer, formats de dates, échelles de temps, fréquences de libellés d axe.
type: docs
weight: 200
url: /fr/java/date-axis/
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un graphique à partir des données de la feuille de calcul qui utilise des dates, et que les dates sont tracées le long de l'axe horizontal (catégorie) dans le graphique, Aspose.cells change automatiquement l'axe de catégorie en axe de date (échelle de temps).
Un axe de date affiche les dates dans l'ordre chronologique à des intervalles ou unités de base spécifiques, tels que le nombre de jours, de mois ou d'années, même si les dates sur la feuille de calcul ne sont pas dans l'ordre séquentiel ou dans les mêmes unités de base.
Par défaut, Aspose.cells détermine les unités de base de l'axe de date en fonction de la plus petite différence entre deux dates dans les données de la feuille de calcul. Par exemple, si vous avez des données sur les prix des actions où la plus petite différence entre les dates est de sept jours, Excel définit l'unité de base en jours, mais vous pouvez changer l'unité de base en mois ou en années si vous voulez voir la performance des actions sur une plus longue période.
## **Gérez l'axe de date comme Microsoft Excel**
Veuillez consulter le code d'exemple suivant qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille de calcul. 
Ensuite, nous ajoutons un graphique et définissons le type du [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/) 
à [**TimeScale**](https://reference.aspose.com/cells/java/com.aspose.cells/categorytype/#TIME-SCALE) puis nous définissons les unités de base en jours.

![todo:image_alt_text](excel.png)

Le code d'exemple suivant génère le [fichier Excel de sortie](DateAxis.xlsx).

## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DateAxis.java" >}}
{{< app/cells/assistant language="java" >}}
