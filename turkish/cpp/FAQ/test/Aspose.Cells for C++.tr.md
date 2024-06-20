# Excel Dosya Biçimleri için C++ Kütüphanesi

![Sürüm 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-mavi) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Ürün Sayfası](https://products.aspose.com/cells/cpp/) | [Belgeler](https://docs.aspose.com/cells/cpp/) | [Demolar](https://products.aspose.app/cells/family) | [API Referansı](https://reference.aspose.com/cells/cpp) | [Örnekler](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Sürümler](https://releases.aspose.com/cells/cpp/) | [Ücretsiz Destek](https://forum.aspose.com/c/cells) | [Geçici Lisans](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/), Microsoft Excel? dosyalarını Microsoft Office? veya Otomasyon gerekmeden oluşturmanıza, işlemenize ve dönüştürmenize yönelik yerel C++ kütüphanesidir. Excel C++ API, Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML ve CSV, TSV gibi diğer biçimleri destekler.

Geliştiricilere, C++ uygulamalarından elektronik tablo satır, sütun, veri, formül, özet tablolar, çalışma sayfaları, tablolar, çizelgeler ve çizim nesneleriyle çalışmalarına olanak tanır.

## Aspose.Cells for C++ Nedir?

Aspose.Cells for C++, C++ Uygulamalarınıza Elektronik Tablo oluşturma,düzenleme ve dönüştürme özelliklerini entegre etmek üzere yerleşik bir C++ API'dir. Microsoft Excel (XLS, XLSX, XLSB, CSV vb.) ve OpenOffice/LibreOffice (ODS) gibi birçok popüler elektronik tablo dosya biçimi ile çalışmayı destekler.

Aspose.Cells for C++'i, Microsoft Visual Studio gibi C++'ı destekleyen herhangi bir geliştirme ortamında 64-bit uygulamalar geliştirmek için kullanabilirsiniz. Aspose.Cells for C++, sadece kopyalayarak dağıtılabilen yerel bir derlemedir. Diğer hizmetler veya modüller hakkında endişelenmeniz gerekmez.

Aspose.Cells for C++, Microsoft Excel'deki yerleşik ve özel belge özellikleri üzerinde çalışmanıza olanak tanır. Excel Çalışma Kitaplarını PDF/A uyumlu dosyalara yüksek kaliteli bir şekilde dönüştürmeyi destekler. Formüller, özet tablolar, çalışma sayfaları, tablolar, aralıklar, çizelgeler, OLE nesneleri ve çok daha fazlasıyla çalışın.

## Excel Dosya İşleme Özellikleri

- Microsoft Excel olmadan bir elektronik tablo dosyasını açın.
- Yerel bilgisayarınızdaki bir yol aracılığıyla veya bir akış kullanarak [bir Excel dosyasını](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) açın.
- [Çalışma sayfasını](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) farklı görüntü biçimlerine dönüştürün.
- Seçiminize göre [koşullu biçimlendirme](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) uygulayın.
- Elektronik tablolarınızda [özet tabloları](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) manipüle edin.
- Biçimlendirmeyi kaybetmeden [tabloyu aralığa](https://docs.aspose.com/cells/cpp/tables-and-ranges/) dönüştürün.
- Satır ve sütun dizinini sağlayarak bir hücrenin adını alın ya da [hücrenin adından satır ve sütun dizinini] (https://docs.aspose.com/cells/cpp/names-and-indices/) alın.
- [Piramit grafik, Çizgi grafiği, Kabarcık grafiği] (https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/) veya özel bir grafik oluşturun.
- Desteklenen grafik türlerini resimlere veya PDF'ye [yansıtın] (https://docs.aspose.com/cells/cpp/chart-rendering/).
- [Çalışma sayfasına OLE nesnesi ekleyin] (https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Çalışma sayfasında bulunan tüm OLE nesnelerine [erişin] (https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

## Desteklenen Okuma ve Yazma Biçimleri

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Diğer:** HTML, MHTML

## Elektronik Tablo Belgelerini Farklı Biçimlerde Kaydetme

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Taşınabilir Belge Biçimi:** PDF, XPS
**Text:** CSV, TSV, TabDelimited\
**Görüntüler:** SVG, JPEG, PNG, BMP, GIF
**Web:** HTML, MHTML\
**Meta dosyası:** EMF
**Diğer** DIF

## Başlarken

 Aspose.Cells for C++'i denemek için hazır mısınız? Sadece Visual Studio'nun Paket Yöneticisi Konsolu'nda `Install-Package Aspose.Cells.Cpp` komutunu çalıştırarak NuGet paketini alabilirsiniz. Eğer zaten Aspose.Cells for C++'e sahipseniz ve sürümü yükseltmek istiyorsanız, lütfen en son sürümü almak için `Update-Package Aspose.Cells.Cpp` komutunu çalıştırın.

### C++ Kullanarak XLS'ten XLSX, XLSB ve CSV'ye Dönüştürme

API'nın çalışma şeklini görmek için aşağıdaki kod parçacığını çalıştırmayı deneyin veya diğer yaygın kullanım senaryoları için [GitHub Deposu'nu] (https://github.com/aspose-cells/Aspose.Cells-for-C) kontrol edin.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### C++ ile Özel Bir Excel Grafik Oluştur

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Ürün Sayfası](https://products.aspose.com/cells/cpp/) | [Belgeler](https://docs.aspose.com/cells/cpp/) | [Demolar](https://products.aspose.app/cells/family) | [API Referansı](https://reference.aspose.com/cells/cpp) | [Örnekler](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Sürümler](https://releases.aspose.com/cells/cpp/) | [Ücretsiz Destek](https://forum.aspose.com/c/cells) | [Geçici Lisans](https://purchase.aspose.com/temporary-license/)
