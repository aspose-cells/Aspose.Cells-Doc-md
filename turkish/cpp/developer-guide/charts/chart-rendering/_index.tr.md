---
title: Grafik Oluşturma
type: docs
weight: 30
url: /tr/cpp/chart-rendering/
---
## **Grafik Oluşturma**

Aspose.Cells API'ler, konu altında ayrıntılı olarak açıklandığı gibi çeşitli Excel grafikleri oluşturmayı destekler[Excel Grafikleri Oluşturma ve Özelleştirme](/cells/tr/cpp/creating-and-customizing-charts/). Grafikleri görüntü & PDF biçiminde işlemek için Aspose.Cells API'lerinin kullanımını göstermek için, aşağıdaki parçacığa göre Sütun türünde bir grafik oluşturacağız.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **Oluşturma Grafikleri**

Aspose.Cells API'leri, Excel Grafiklerini herhangi bir ek araç veya uygulama gerektirmeden resimlere ve PDF biçimlerine dönüştürmeyi destekler. Oluşturma desteği sağlamak için Chart sınıfı, uygulama gereksinimlerine en iyi şekilde uyacak şekilde ToImage & ToPdf yöntemlerini çeşitli aşırı yüklemelerle kullanıma sunmuştur.

### **Grafikleri Görüntülere Dönüştürme**

Chart.toImage yöntemi, basit ve gelişmiş işlemeyi desteklemek için çok sayıda aşırı yüklemeye sahiptir. Uygulama gereksinimi, grafiği varsayılan boyutlarında oluşturmaksa, Chart.toImage yöntemini aşağıdaki gibi kullanmanızı öneririz.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Tabloyu PDF'e Oluşturma**

Grafiği PDF biçiminde işlemek için Aspose.Cells API'leri, elde edilen PDF'i disk yolunda veya Akışta depolama yeteneğiyle Chart.ToPdf yöntemini kullanıma sundu.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Oluşturma için Desteklenen Grafik Türleri**

Şu anda işleme için desteklenmeyen birkaç grafik türü vardır. Bu tür grafik türleri şunları içerir:**içinde N****Aşağıdaki tablonun desteklenen** sütunu.

|**Grafik tipi**|**Grafik alt türü**|**desteklenen**|
|:- |:- |:- |
|**Kolon**|Kolon|**e**|
||SütunYığılmış|**e**|
||Sütun100YığılmışYüzde|**e**|
||Sütun3Dkümelenmiş|**e**|
||Sütun3DSığılmış|**e**|
||Sütun3D100YığılmışYüzde|**e**|
||Sütun3D|**e**|
|**Bar**|Bar|**e**|
||Çubuk Yığılmış|**e**|
||Bar100YığılmışYüzde|**e**|
||Bar3Dkümelenmiş|**e**|
||Bar3DSyığılmış|**e**|
||Bar3D100YığılmışYüzde|**e**|
|**Astar**|Astar|**e**|
||Sıra Yığılmış|**e**|
||Line100PercentYığılmış|**e**|
||LineWithDataMarkers|**e**|
||LineStackedWithDataMarkers|**e**|
||Line100PercentStackedWithDataMarkers|**e**|
||Çizgi3D|**e**|
|**Turta**|Turta|**e**|
||Pasta3D|**e**|
||Turta Turtası|**e**|
||PastaPatladı|**e**|
||Pie3DEpatladı|**e**|
||pasta çubuğu|**e**|
|**Dağılım**|Dağılım|**e**|
||DağılımConnectedByCurvesWithDataMarker|**e**|
||ScatterConnectedByCurvesWithoutDataMarker|**e**|
||ScatterConnectedByLinesWithDataMarker|**e**|
||ScatterConnectedByLinesWithoutDataMarker|**e**|
|**Alan**|Alan|**e**|
||Yığılmış Alan|**e**|
||Alan100YığılmışYüzde|**e**|
||Alan3D|**e**|
||Alan3Dyığınlanmış|**e**|
||Alan3D100YığılmışYüzde|**e**|
|**Tatlı çörek**|Tatlı çörek|**e**|
||DonutPatladı|**e**|
|**Radar**|Radar|**e**|
||RadarWithDataMarkers|**e**|
||Radar Dolu|**e**|
|**Yüzey**|Yüzey3D|N|
||SurfaceWireframe3D|N|
||Yüzey Konturu|N|
||Yüzey Kontur Tel Kafes|N|
|**kabarcık**|kabarcık|**e**|
||Bubble3D|N|
|Stoklamak|StokYüksekDüşükKapat|**e**|
||StokAçıkYüksekDüşükKapat|**e**|
||StokHacimYüksekDüşükKapat|**e**|
||Stok HacmiAçıkYüksekDüşükKapalı|**e**|
|**silindir**|silindir|**e**|
||Silindir Yığılmış|**e**|
||Cylinder100PercentYığılmış|**e**|
||Silindirik Çubuk|**e**|
||Silindirik ÇubukYığılmış|**e**|
||SilindirikÇubukYüzde100Yığılmış|**e**|
||Silindirik Sütun3D|**e**|
|**koni**|koni|**e**|
||koni yığılmış|**e**|
||Koni100YüzdeYığılmış|**e**|
||Konik Çubuk|**e**|
||Konik ÇubukYığılmış|**e**|
||ConicalBar100PercentYığılmış|**e**|
||Konik Sütun3D|**e**|
|**Piramit**|Piramit|**e**|
||PiramitYığılmış|**e**|
||Piramit100YüzdeYığılmış|**e**|
||PiramitBar|**e**|
||PiramitÇubuğuYığılmış|**e**|
||PiramitBar100PercentYığınlanmış|**e**|
||PiramitSütun3D|**e**|
|**KutuBıyık**|KutuBıyık|Y|
|**Huni**|Huni|**e**|
|**ParetoLine**|ParetoLine|**e**|
|**güneş patlaması**|güneş patlaması|**e**|
|**ağaç haritası**|ağaç haritası|**e**|
|**Şelale**|Şelale|**e**|
|**histogram**|histogram|Y|
|**Harita**|Harita|**N**|

{{% alert color="primary" %}}

Desteklenmeyen grafik türlerini resim veya PDF'e dönüştürmeye çalışırsanız, 0 boyutlu resimler veya boş PDF ile sonuçlanabilirsiniz.

{{% /alert %}}
