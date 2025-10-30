---  
title: ChartGlobalizationSettings Sınıfını kullanarak Node.js ile Grafik Bileşenine Farklı Diller Ayarlama  
linktitle: Farklı Dil için Grafik Bileşeni Olarak ChartGlobalizationSettings Sınıfını Kullanma  
description: Aspose.Cells for Node.js via C++ te ChartGlobalizationSettings sınıfını kullanmayı öğrenin. Bu kılavuz, grafik öğeleri, etiketler ve açıklamalar gibi yerelleştirme konusunda size yardımcı olacak.  
keywords: Aspose.Cells for Node.js via C++, grafik oluşturma, grafik küreselleştirme, diller, yerelleştirme, ChartGlobalizationSettings, öğeler, etiketler, açıklamalar.  
type: docs  
weight: 2200  
url: /tr/nodejs-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells API'leri, kullanıcıların grafik bileşenlerini farklı dillere ayarlamak ve bir hesap tablosundaki Alt Toplamlar için özel etiketler belirlemek istedikleri durumları ele almak amacıyla [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) sınıfını ortaya çıkardı.  

## **ChartGlobalizationSettings Sınıfına Giriş**  

Şu anda, [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) sınıfı, farklı dillerdeki Eksen Başlığı adları, Eksen Birimi adları, Grafik Başlığı adları gibi, özelleştirilebilir 8 yöntemi sunar, ve bu yöntemler bir özel sınıfta geçersiz kılınabilir.  
1. [**ChartGlobalizationSettings.getAxisTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisTitleName--): Eksen için Başlık adını alır.  
1. [**ChartGlobalizationSettings.getAxisUnitName(DisplayUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getAxisUnitName-displayunittype-): Eksen Birimi için Adı alır.  
1. [**ChartGlobalizationSettings.getChartTitleName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getChartTitleName--): Grafik Başlığının adını alır.  
1. [**ChartGlobalizationSettings.getLegendDecreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendDecreaseName--): Efsane için Azalma adını alır.  
1. [**ChartGlobalizationSettings.getLegendIncreaseName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendIncreaseName--): Efsane için Artışın adını alır.  
1. [**ChartGlobalizationSettings.getLegendTotalName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getLegendTotalName--): Efsane için Toplam adını alır.  
1. [**ChartGlobalizationSettings.getOtherName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getOtherName--): Grafikte "Diğer" etiketlerinin adını alır.  
1. [**ChartGlobalizationSettings.getSeriesName()**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/#getSeriesName--): Grafikteki Serilerin adını alır.  

### **Özel dil çevirisi**  
Burada, aşağıdaki verilere dayalı bir su dalgası grafiği oluşturacağız. Grafik bileşenlerinin adları, İngilizce olarak grafikte gösterilecektir. Grafik Başlığı, Efsane Artış/Azalma adları, Toplam adı ve Eksen Başlığı'nın Türkçe olarak nasıl gösterileceğini göstermek için bir Türkçe dil örneği kullanacağız.  

![todo:image_alt_text](sample.png)  

## **Örnek Kod**  
Aşağıdaki örnek kod, [örnek Excel dosyasını](waterfall.xlsx) yükler.  

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

Örneğin ürettiği çıktı  

Yukarıdaki örnek kodun konsol çıktısı budur.  

{{< highlight javascript >}}  

Workbook chart title: Grafik Başlığı  

Workbook chart legend: Artış  

Workbook chart legend: Düşüş  

Workbook chart legend: Toplam  

Workbook category axis title: Eksen Başlığı  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
