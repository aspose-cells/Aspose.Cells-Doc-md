---
title: Convertir un graphique en image pour la région chinoise
description: Découvrez comment utiliser Aspose.Cells for .NET pour définir la configuration chinoise pour les graphiques. Notre guide vous montrera comment configurer des graphiques pour prendre en charge les caractères et formats chinois, y compris les polices, les tailles, les directions de texte, etc.
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: Définir la région chinoise
type: docs
weight: 9
url: /fr/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

Dans cette rubrique, nous allons vous montrer comment définir la région chinoise pour un graphique.

{{% /alert %}}

##  **Définit une classe d'héritage**

 Première étape, vous devez définir une classe "ChartChineseSetttings" qui hérite de[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Ensuite, en réécrivant les fonctions associées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.
Exemple de code :
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Configurer le paramètre chinois pour le graphique**

Dans cette étape, vous utiliserez la classe « ChartChineseSetttings » que vous avez définie à l’étape précédente.
Exemple de code :

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus en fonction de vos paramètres.

##  **Conclusion**

Dans cet exemple, si vous ne définissez pas la région chinoise pour un graphique, les éléments suivants du graphique peuvent être affichés dans la langue par défaut, telle que l'anglais.
Après l’opération ci-dessus, nous pouvons obtenir une image graphique de sortie avec la région chinoise.

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|
| :- | :- | :- |
|Nom du titre de l'axe|坐标轴标题|Titre de l'axe|
|Nom de l'unité de l'axe|百,千...|Des centaines, des milliers...|
|Nom du titre du graphique|图表标题|Titre du graphique|
|Légende Augmenter le nom|增加|Augmenter|
|Légende Diminuer le nom|减少|Diminuer|
|Légende Total Nom|汇总|Total|
|Autre nom|其他|Autre|
|Nom de la série|系列|Série|
