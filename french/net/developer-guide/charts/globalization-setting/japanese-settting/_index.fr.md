---
title: Convertir le graphique en image pour la région japonaise
linktitle: Définir la région japonaise
type: docs
weight: 10
url: /fr/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

Dans cette rubrique, nous allons vous montrer comment définir la région japonaise pour un graphique.

{{% /alert %}}

##  **Définit une classe d'héritage**

 Première étape, vous devez définir une classe "ChartJapaneseSettings" qui hérite de[**Paramètres de globalisation du graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Ensuite, en réécrivant les fonctions associées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.
Exemple de code :
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Configurer le paramètre japonais pour le graphique**

Dans cette étape, vous utiliserez la classe "ChartJapaneseSetttings" que vous avez définie à l'étape précédente.
Exemple de code :

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus en fonction de vos paramètres.

##  **Conclusion**

Dans cet exemple, si vous ne définissez pas la région japonaise pour un graphique, les éléments de graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.
Après l'opération ci-dessus, nous pouvons obtenir une image graphique de sortie avec la région japonaise.

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|
| :- | :- | :- |
|Nom du titre de l'axe|軸タイトル|Titre de l'axe|
|Nom de l'unité de l'axe|百,千...|Des centaines, des milliers...|
|Nom du titre du graphique|グラフ タイトル|Titre du graphique|
|Légende Augmenter le nom|ぞうか|Augmenter|
|Légende Réduire le nom|削減|Diminuer|
|Légende Total Nom|すべての|Total|
|Autre nom|その他|Autre|
|Nom de la série|シリーズ|Série|
