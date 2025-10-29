---  
title: Utilisation de la classe ChartGlobalizationSettings pour définir différentes langues pour le composant graphique avec Node.js via C++  
linktitle: Utilisation de la classe ChartGlobalizationSettings pour définir une langue différente pour le composant de graphique  
description: Apprenez comment utiliser la classe ChartGlobalizationSettings dans Aspose.Cells for Node.js via C++ pour définir différentes langues pour les composants du graphique. Notre guide vous aidera à comprendre comment localiser les éléments, les étiquettes et les légendes du graphique.  
keywords: Aspose.Cells for Node.js via C++, création de graphique, mondialisation du graphique, langues, localisation, ChartGlobalizationSettings, éléments, étiquettes, légendes.  
type: docs  
weight: 2200  
url: /fr/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Scénarios d'utilisation possibles**  

Les API Aspose.Cells ont exposé la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) pour gérer les scenarios où l'utilisateur souhaite configurer les composants du graphique en différentes langues et créer des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul.  

## **Introduction à la classe ChartGlobalizationSettings**  

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) propose actuellement les 8 méthodes suivantes qui peuvent être surchargées dans une classe personnalisée pour traduire, par exemple, le nom de AxisTitle, le nom de AxisUnit, le nom de ChartTitle, etc., dans différentes langues.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--) : Obtient le nom du titre de l'axe.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-) : Obtient le nom de l'unité d'axe.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--) : Obtient le nom du titre du graphique.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--) : Obtient le nom de la diminution pour la légende.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--) : obtient le nom de Increase pour la légende.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--) : Obtient le nom du total pour la légende.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--) : Obtient le nom des étiquettes "Autre" pour le graphique.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--) : Obtient le nom des séries dans le graphique.  

### **Traduction personnalisée**  
Voici, nous allons créer un graphique en cascade basé sur les données suivantes. Les noms des composants du graphique seront affichés en anglais dans le graphique. Nous utiliserons un exemple de langue turque pour montrer comment afficher le titre du graphique, les noms d'augmentation/diminution de la légende, le nom total et le titre de l'axe en turc.   

![todo:image_alt_text](sample.png)  

## **Code d'exemple**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](waterfall.xlsx).  

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TurkeyChartGlobalizationSettings extends AsposeCells.ChartGlobalizationSettings {
getChartTitleName() {
return "Grafik Başlığı"; // Chart Title
}
getLegendIncreaseName() {
return "Artış"; // Increase
}
getLegendDecreaseName() {
return "Düşüş"; // Decrease
}
getLegendTotalName() {
return "Toplam"; // Total
}
getAxisTitleName() {
return "Eksen Başlığı"; // Axis Title
}
}

async function chartGlobalizationSettingsTest() {
// Create an instance of existing Workbook
const dataDir = path.join(__dirname, "data");
const pathName = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(pathName);

// Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
workbook.getSettings().getGlobalizationSettings().setChartSettings(new TurkeyChartGlobalizationSettings());

// Get the worksheet 
const worksheet = workbook.getWorksheets().get(0);
const chartCollection = worksheet.getCharts();

// Load the chart from source worksheet
const chart = chartCollection.get(0);

// Chart Calculate
chart.calculate();

// Get the chart title
const title = chart.getTitle();
console.log("\nWorkbook chart title: " + title.getText());

const legendEntriesLabels = chart.getLegend().getLegendLabels();

// Output the name of the Legend 
legendEntriesLabels.forEach(label => {
console.log("\nWorkbook chart legend: " + label);
```  

## Sortie générée par le code d'exemple  

Il s'agit de la sortie de la console du code d'exemple ci-dessus.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
