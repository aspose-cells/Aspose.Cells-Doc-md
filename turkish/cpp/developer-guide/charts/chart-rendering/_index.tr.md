---
title: Grafik Oluşturma
type: docs
weight: 30
url: /tr/cpp/chart-rendering/
---
##  **Grafik Oluşturma**

Aspose.Cells API'ler, konu altında ayrıntılı olarak açıklanan Excel grafiklerinin gerçekliğini oluşturmayı destekler[Excel Grafiklerini Oluşturma ve Özelleştirme](/cells/tr/cpp/creating-and-customizing-charts/). Grafikleri resim & PDF biçiminde oluşturmak için Aspose.Cells API'lerinin kullanımını göstermek amacıyla, aşağıdaki kod parçasına göre Sütun türünde bir grafik oluşturacağız.

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **İşleme Grafikleri**

Aspose.Cells API'ler, herhangi bir ek araç veya uygulama gerektirmeden Excel Grafiklerini resimlere ve PDF formatlarına dönüştürmeyi destekler. Oluşturma desteğini sağlamak için Chart sınıfı, uygulama gereksinimlerine en iyi şekilde uyacak şekilde ToImage ve ToPdf yöntemlerini çeşitli aşırı yüklemelerle kullanıma sunmuştur.

###  **Grafikleri Görsellere Dönüştürme**

Chart.toImage yöntemi, basit ve gelişmiş oluşturmayı desteklemek için çok sayıda aşırı yüklemeye sahiptir. Eğer uygulama gereksinimi grafiğin varsayılan boyutlarında render edilmesi ise aşağıdaki gibi Chart.toImage metodunu kullanmanızı öneririz.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **PDF'e Grafik Oluşturma**

Grafiği PDF formatına dönüştürmek için Aspose.Cells API'leri, elde edilen PDF'i disk yolunda veya Akışta depolayabilme özelliğine sahip Chart.ToPdf yöntemini kullanıma sunmuştur.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **İşleme için Desteklenen Grafik Türleri**

Şu anda oluşturma için desteklenmeyen birkaç grafik türü vardır. Bu tür grafik türleri şunları içerir:****Desteklenen bölümündeki N****aşağıdaki tablonun sütunu.

|**Grafik tipi**|**Grafik alt türü**|**Destekleniyor**|
| :- | :- | :- |
|**Kolon**|Kolon|*Evet**|
| |SütunYığılmış|*Evet**|
| |SütunYüzde100Yığılmış|*Evet**|
| |Sütun3DKümelenmiş|*Evet**|
| |Sütun3DSığılmış|*Evet**|
| |Sütun3D100YüzdeYığınlanmış|*Evet**|
| |Sütun3D|*Evet**|
|**Çubuk**|Çubuk|*Evet**|
| |BarYığılmış|*Evet**|
| |Bar100PercentYığılmış|*Evet**|
| |Bar3DKümelenmiş|*Evet**|
| |Bar3DSığılmış|*Evet**|
| |Bar3D100YüzdeYığınlanmış|*Evet**|
|**Astar**|Astar|*Evet**|
| |HatYığılmış|*Evet**|
| |Line100PercentYığılmış|*Evet**|
| |LineWithDataMarkers|*Evet**|
| |LineStackedWithDataMarkers|*Evet**|
| |Line100PercentStackedWithDataMarkers|*Evet**|
| |Hat3D|*Evet**|
|**Turta**|Turta|*Evet**|
| |Pasta3D|*Evet**|
| |TurtaPasta|*Evet**|
| |Pasta Patladı|*Evet**|
| |Pie3DEpatladı|*Evet**|
| |Pasta Barı|*Evet**|
|**Dağılım**|Dağılım|*Evet**|
| |ScatterConnectedByCurvesWithDataMarker|*Evet**|
| |ScatterConnectedByCurvesWithoutDataMarker|*Evet**|
| |ScatterConnectedByLinesWithDataMarker|*Evet**|
| |ScatterConnectedByLinesWithoutDataMarker|*Evet**|
|**Alan**|Alan|*Evet**|
| |AlanYığılmış|*Evet**|
| |Alan100YüzdeYığınlanmış|*Evet**|
| |Alan3D|*Evet**|
| |Alan3Dyığılmış|*Evet**|
| |Alan3D100YüzdeYığınlanmış|*Evet**|
|**Tatlı çörek**|Tatlı çörek|*Evet**|
| |DonutPatladı|*Evet**|
|**Radar**|Radar|*Evet**|
| |RadarWithDataMarkers|*Evet**|
| |RadarDolu|*Evet**|
|**Yüzey**|Yüzey3D|N|
| |Yüzey Tel Çerçeve3D|N|
| |YüzeyKontur|N|
| |YüzeyKonturTel Çerçeve|N|
|**Kabarcık**|Kabarcık|*Evet**|
| |Kabarcık3D|N|
|Stoklamak|StokYüksekDüşükKapat|*Evet**|
| |HisseAçıkYüksekDüşükKapat|*Evet**|
| |Hisse HacmiYüksekDüşükKapat|*Evet**|
| |Hisse HacmiAçıkYüksekDüşükKapanış|*Evet**|
|**Silindir**|Silindir|*Evet**|
| |SilindirYığılmış|*Evet**|
| |SilindirYüzde100Yığılmış|*Evet**|
| |SilindirikBar|*Evet**|
| |SilindirikBarYığılmış|*Evet**|
| |SilindirikBar100PercentYığılmış|*Evet**|
| |Silindirik Sütun3D|*Evet**|
|**Koni**|Koni|*Evet**|
| |KoniYığılmış|*Evet**|
| |KoniYüzde100Yığılmış|*Evet**|
| |KonikBar|*Evet**|
| |KonikBarYığılmış|*Evet**|
| |KonikBar100YüzdeYığınlanmış|*Evet**|
| |Konik Sütun3D|*Evet**|
|**Piramit**|Piramit|*Evet**|
| |PiramitYığılmış|*Evet**|
| |PiramitYüzde100Yığılmış|*Evet**|
| |PiramitBar|*Evet**|
| |PiramitBarYığılmış|*Evet**|
| |PiramitBar100YüzdeYığınlanmış|*Evet**|
| |PiramitSütun3D|*Evet**|
|**Kutu Bıyık**|Kutu Bıyık|Y|
|**Huni**|Huni|*Evet**|
|**Pareto Hattı**|Pareto Hattı|*Evet**|
|**Güneş patlaması**|Güneş patlaması|*Evet**|
|**Ağaç haritası**|Ağaç haritası|*Evet**|
|**Şelale**|Şelale|*Evet**|
|**Histogram**|Histogram|Y|
|**Harita**|Harita|*N**|

{{% alert color="primary" %}}

Desteklenmeyen grafik türlerini görsele veya PDF'e dönüştürmeye çalışırsanız, 0 boyutlu görsellerle veya boş PDF ile karşılaşabilirsiniz.

{{% /alert %}}
