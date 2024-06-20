---
title: Convertir le graphique en image pour la région chinoise
description: Apprenez à utiliser Aspose.Cells for .NET définit la configuration chinoise pour les graphiques. Notre guide démontrera comment configurer les graphiques pour prendre en charge les caractères chinois et les formats, y compris les polices, les tailles, les directions de texte, et plus encore.
keywords: Aspose.Cells for .NET, Graphiques, Configuration chinoise, Polices, Taille de police, Direction du texte, Support.
linktitle: Définir la région chinoise
type: docs
weight: 9
url: /fr/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Dans ce sujet, nous vous montrerons comment définir la région chinoise pour un graphique.

{{% /alert %}}

## **Définit une classe d'héritage**

Première étape, vous devez définir une classe "ChartChineseSetttings" qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Ensuite, en réécrivant les fonctions liées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.
Exemple de code :
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Configurer les paramètres chinois pour le graphique**

À cette étape, vous utiliserez la classe "ChartChineseSetttings" que vous avez définie lors de l'étape précédente.
Exemple de code :

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus selon vos paramètres.

## **Conclusion**

Dans cet exemple, si vous ne définissez pas la région chinoise pour un graphique, les éléments du graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.
Après l'opération ci-dessus, nous pouvons obtenir une image de graphique de sortie avec une région chinoise.

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|
| :- | :- | :- |
|Nom du titre de l'axe|坐标轴标题|Titre de l'axe|
|Nom de l'unité de l'axe|百,千...|Centaines, Milliers...|
|Nom du titre du graphique|图表标题|Titre du graphique|
|Nom de Légende Augmentation|增加|Augmentation|
|Nom de Légende Diminution|减少|Diminution|
|Nom de Légende Total|汇总|Total|
|Autre Nom|其他|Autre|
|Nom de Série|系列|Série|
