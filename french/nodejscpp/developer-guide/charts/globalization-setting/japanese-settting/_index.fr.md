---  
title: Convertir un graphique en image pour la région japonaise avec Node.js via C++  
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour configurer le graphique pour le japonais. Notre guide vous montrera comment configurer des graphiques pour supporter les caractères et formats japonais, y compris les polices, la taille, la direction du texte, et plus encore.  
keywords: Aspose.Cells for Node.js via C++, Graphiques, configuration japonaise, police, taille de police, direction du texte, support.  
linktitle: Définir la région japonaise  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
Dans ce sujet, nous allons vous montrer comment définir la région japonaise pour un graphique.  
{{% /alert %}}  

## **Définit une classe d'héritage**  

Première étape, vous devez définir une classe "ChartJapaneseSettings" qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/).  
Ensuite, en réécrivant les fonctions liées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.  
Exemple de code :  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "軸タイトル";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return "百";
case AsposeCells.DisplayUnitType.Thousands:
return "千";
case AsposeCells.DisplayUnitType.TenThousands:
return "万";
case AsposeCells.DisplayUnitType.HundredThousands:
return "10万";
case AsposeCells.DisplayUnitType.Millions:
return "百万";
case AsposeCells.DisplayUnitType.TenMillions:
return "千万";
case AsposeCells.DisplayUnitType.HundredMillions:
return "億";
case AsposeCells.DisplayUnitType.Billions:
return "10億";
case AsposeCells.DisplayUnitType.Trillions:
return "兆";
default:
return '';
}
}

getChartTitleName() {
return "グラフ タイトル";
}

getLegendDecreaseName() {
return "削減";
}

getLegendIncreaseName() {
return "ぞうか";
}

getLegendTotalName() {
return "すべての";
}

getOtherName() {
return "その他";
}

getSeriesName() {
return "シリーズ";
}
}
```  

## **Configurer le paramètre japonais pour le graphique**  

Dans cette étape, vous utiliserez la classe "ChartJapaneseSettings" que vous avez définie dans l'étape précédente.  
Exemple de code :  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
```

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus selon vos paramètres.  

## **Conclusion**  

Dans cet exemple, si vous ne définissez pas la région japonaise pour un graphique, les éléments de graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.  
Après l'opération ci-dessus, nous pouvons obtenir une image de graphique de sortie avec la région japonaise.  

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|  
| :- | :- | :- |  
|Nom du titre de l'axe|軸タイトル|Titre de l'axe|  
|Nom de l'unité de l'axe|百,千...|Centaines, Milliers...|  
|Nom du titre du graphique|グラフ タイトル|Titre du graphique|  
|Nom de l'augmentation de la légende|ぞうか|Augmentation|  
|Nom de la diminution de la légende|削減|Diminution|  
|Nom total de la légende|すべての|Total|  
|Autre nom|その他|Autre|  
|Nom de la série|シリーズ|Série|  

{{< app/cells/assistant language="nodejs-cpp" >}}
