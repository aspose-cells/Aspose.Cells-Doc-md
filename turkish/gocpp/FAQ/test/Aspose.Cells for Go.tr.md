# Excel Dosya Formatları İçin Go Kütüphanesi

![Versiyon 24.11.0](https://img.shields.io/badge/go-v24.11.0-mavi)

[Ürün Sayfası](https://products.aspose.com/cells/go-cpp/) | [Dokümantasyon](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Referansı](https://reference.aspose.com/cells/go-cpp) | [Örnekler](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Yayınlar](https://releases.aspose.com/cells/go-cpp/) | [Ücretsiz Destek](https://forum.aspose.com/c/cells) | [Geçici Lisans](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) yerli bir Go kütüphanesidir ve Microsoft Office veya Otomasyon gerekmeden Microsoft Excel dosyalarını oluşturma, manipulate etme, işleme ve dönüştürme işlemlerini yapabilir. Excel Go API, Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML ve CSV, TSV gibi diğer formatları da destekler.

Geliştiricilerin kendi Go uygulamalarından elektronik tablo satırları, sütunlar, veriler, formüller, pivot tablolar, çalışma sayfaları, tablolar, grafikler ve çizim nesnleri ile çalışmasına olanak tanır.

## Aspose.Cells for Go via C++ nedir?

Aspose.Cells for Go via C++, Elektronik Tablo oluşturma, manipulasyon ve dönüşüm özelliklerini Go Uygulamalarınıza entegre etmek için yerel Go yerinde API'sidir. Microsoft Excel (XLS, XLSX, XLSB, CSV vb.) ve OpenOffice/LibreOffice (ODS) gibi birçok popüler elektronik tablo dosya formatıyla çalışma desteği sağlar.

Aspose.Cells for Go via C++'yi, Microsoft Visual Studio gibi Go destekleyen herhangi bir geliştirme ortamında 64-bit uygulamalar geliştirmek için kullanabilirsiniz. Aspose.Cells for Go via C++ yerel bir topludur ve sadece kopyalayarak dağıtılabilir. Diğer hizmetler veya modüller hakkında endişelenmenize gerek yoktur.

Aspose.Cells for Go via C++, Microsoft Excel'deki yerleşik ve özel belge özellikleriyle çalışmanıza olanak tanır. Excel Çalışma Kitaplarının PDF/A uyumlu dosyalara yüksek kaliteli dönüştürmesini destekler. Formüller, pivot tablolar, çalışma sayfaları, tablolar, aralıklar, grafikler, OLE nesneleri ve daha fazlasıyla çalışabilirsiniz.

## Excel Dosya İşleme Özellikleri

- Microsoft Excel olmadan bir elektronik tablo dosyasını açın.
- [Bir Excel dosyasını](https://docs.aspose.com/cells/go/different-ways-to-open-files/) yerel bilgisayardan veya bir akış kullanarak açın.
- [Çalışma sayfasını](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) farklı görüntü formatlarına dönüştürün.
- [Koşullu biçimlendirmeyi](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) tercihlerinize göre uygulayın.
- [Pivot tabloları](https://docs.aspose.com/cells/go/manipulate-pivot-table/) elektronik tablolarınızda manipulasyon yapın.
- [Tabloyu aralık olarak](https://docs.aspose.com/cells/go/tables-and-ranges/) dönüştürün ve biçimlendirmeyi kaybetmeyin.
- Satır ve sütun indekslerini sağlayarak hücrenin adını alın, aynı zamanda hücrenin adından [satır ve sütun indeksini](https://docs.aspose.com/cells/go/names-and-indices/) alın.
- [Piramit grafiği, çizgi grafiği, balon grafiği](https://docs.aspose.com/cells/go/creating-and-customizing-charts/) veya özel grafik oluşturun.
- Desteklenen grafik türlerini resme veya PDF'ye [şekillendirin](https://docs.aspose.com/cells/go/chart-rendering/).
- [Çalışma sayfasına bir OLE nesnesi ekleyin](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Çalışma sayfasındaki tüm OLE nesnelerine erişin ve [çıkartın](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

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

Aspose.Cells for Go via C++'yi denemeye hazır mısınız? Sadece `go get -u github.com/aspose-cells/aspose-cells-go-cpp` komutunu çalıştırın ve go dosyanızdan `github.com/aspose-cells/aspose-cells-go-cpp`'yi içe aktarın. Zaten Aspose.Cells for Go via C++'ye sahipseniz ve sürümünü yükseltmek istiyorsanız, en yeni sürümü almak için `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` komutunu çalıştırın.

### Go kullanarak XLS'i XLSX, XLSB ve CSV'ye dönüştürün

Aşağıdaki kod parçacığını çalıştırarak API'nin nasıl çalıştığını görebilir veya diğer yaygın kullanım senaryoları için [GitHub Deposu](https://github.com/aspose-cells/aspose-cells-go-cpp) nu kontrol edebilirsiniz.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Go ile Özel bir Excel Grafiği Oluşturun

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Ürün Sayfası](https://products.aspose.com/cells/go-cpp/) | [Dokümantasyon](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [API Referansı](https://reference.aspose.com/cells/go-cpp) | [Örnekler](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Yayınlar](https://releases.aspose.com/cells/go-cpp/) | [Ücretsiz Destek](https://forum.aspose.com/c/cells) | [Geçici Lisans](https://purchase.aspose.com/temporary-license/)
