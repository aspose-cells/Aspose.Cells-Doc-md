---
title: Pivot Tablo Ekle
linktitle: Pivot Tablolar
type: docs
weight: 160
url: /tr/net/create-pivot-table/
description: Excel elektronik tablo dosyalarının pivot tablolarını oluşturun ve biçimlendirin.
---
## **Pivot Tablo Oluştur**

Elektronik tablolara programlı olarak pivot tablolar eklemek için Aspose.Cells'i kullanmak mümkündür.

### **Pivot Tablo Nesne Modeli**

Aspose.Cells, özel bir dizi sınıf sağlar.[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) pivot tablolar oluşturmak ve kontrol etmek için kullanılan ad alanı. Bu sınıflar oluşturmak ve ayarlamak için kullanılır.[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)nesneler, bir pivot tablonun yapı taşları. nesneler:

- [**PivotAlanı**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) içindeki bir alanı temsil eder[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**Özet Alan Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) tümünün bir koleksiyonunu temsil eder.[**PivotAlanı**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) içindeki nesneler[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)çalışma sayfasındaki bir PivotTable'ı temsil eder.
- [**Özet Tablo Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) tümünün bir koleksiyonunu temsil eder.[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)bir çalışma sayfasındaki nesneler.

### **Aspose.Cells Kullanarak Basit Bir Pivot Tablo Oluşturma**

1. kullanarak bir çalışma sayfasına veri ekleyin.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesnenin[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntem.
 Bu veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1.  Çağırarak çalışma sayfasına bir pivot tablo ekleyin.[**Özet Tablolar**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) koleksiyonun[**Ekle**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)Worksheet nesnesinde kapsüllenen yöntem.
1.  Yeniye erişin[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) gelen nesne[**Özet Tablolar**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)PivotTable dizinini geçirerek toplama.
1.  herhangi birini kullanın[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)pivot tabloyu yönetmek için nesneler (yukarıda açıklanmıştır).

Örnek kodu çalıştırdıktan sonra, çalışma sayfasına bir pivot tablo eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atarken, aralık sol üstten sağ alta doğru olmalıdır. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" değildir.

{{% /alert %}}

## **ileri konular**
- [Konsolidasyon Fonksiyonu](/cells/tr/net/consolidation-function/)
- [Özet Tabloda özel sıralama](/cells/tr/net/custom-sorting-in-pivot-table/)
- [Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme](/cells/tr/net/customize-globalization-settings-for-pivot-table/)
- [Pivot Tablo Şeritlerini Devre Dışı Bırak](/cells/tr/net/disable-pivot-table-ribbons/)
- [Ebeveyn Pivot Tablosunun İç İçe veya Alt Pivot Tablolarını Bulun ve Yenileyin](/cells/tr/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Pivot Tabloyu Biçimlendirme](/cells/tr/net/formatting-pivot-table/)
- [Pivot Tablonun Dış Bağlantı Veri Kaynağını Alın](/cells/tr/net/get-external-connection-data-source-of-pivot-table/)
- [Pivot Tablo yenileme tarihini alın ve kim bilgilerine göre yenileyin](/cells/tr/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Pivot Tablodaki Pivot Alanlarını Gruplandırma](/cells/tr/net/group-pivot-fields-in-the-pivot-table/)
- [Excel dosyasını yüklerken Pivot Önbelleğe Alınmış Kayıtları Ayrıştırma](/cells/tr/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Özet Tablo ve Kaynak Veriler](/cells/tr/net/pivot-table-and-source-data/)
- [Pivot Tablo Verileri Gizle ve Sırala](/cells/tr/net/pivot-table-hide-and-sort-data/)
- [Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın](/cells/tr/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot Tabloyu ODS dosyasına kaydedin](/cells/tr/net/save-pivot-table-in-ods-file/)
- [Rapor filtre sayfaları seçeneğini göster](/cells/tr/net/show-report-filter-pages-option/)
- [Pivot Tabloda DataField'in veri görüntüleme biçimleriyle çalışma](/cells/tr/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
