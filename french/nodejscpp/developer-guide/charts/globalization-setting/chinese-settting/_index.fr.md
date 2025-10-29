---  
title: Convertir un graphique en image pour la région chinoise avec Node.js via C++  
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour configurer des graphiques pour les caractères et formats chinois, y compris les polices, tailles, orientations du texte et plus encore.  
keywords: Aspose.Cells pour Node.js, graphiques, configuration chinoise, polices, taille de police, direction du texte, support.  
linktitle: Définir la région chinoise  
type: docs  
weight: 9  
url: /fr/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
Dans ce sujet, nous vous montrerons comment définir la région chinoise pour un graphique.  
{{% /alert %}}  

## **Définit une classe d'héritage**  

Première étape, vous devez définir une classe "ChartChineseSetttings" qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Ensuite, en réécrivant les fonctions liées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.  
Exemple de code :  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "坐标轴标题";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return '百';
case AsposeCells.DisplayUnitType.Thousands:
return '千';
case AsposeCells.DisplayUnitType.TenThousands:
return '万';
case AsposeCells.DisplayUnitType.HundredThousands:
return '十万';
case AsposeCells.DisplayUnitType.Millions:
return '百万';
case AsposeCells.DisplayUnitType.TenMillions:
return '千万';
case AsposeCells.DisplayUnitType.HundredMillions:
return '亿';
case AsposeCells.DisplayUnitType.Billions:
return '十亿';
case AsposeCells.DisplayUnitType.Trillions:
return '兆';
default:
return '';
}
}

getChartTitleName() {
return "图表标题";
}

getLegendDecreaseName() {
return "减少";
}

getLegendIncreaseName() {
return "增加";
}

getLegendTotalName() {
return "汇总";
}

getOtherName() {
return "其他";
}

getSeriesName() {
return "系列";
}
}
```  

## **Configurer les paramètres chinois pour le graphique**  

À cette étape, vous utiliserez la classe "ChartChineseSetttings" que vous avez définie lors de l'étape précédente.  
Exemple de code :  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

{{< app/cells/assistant language="nodejs-cpp" >}}
