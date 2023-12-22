---
title: Pivot Tablo Ekle
linktitle: Pivot Tablolar
type: docs
weight: 160
url: /tr/python-net/create-pivot-table/
description: Aspose.Cells for Python via .NET ile Pivot Tablo oluşturun ve biçimlendirin.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **Pivot Tablo Oluştur**

Program aracılığıyla e-tablolara pivot tablolar eklemek için Aspose.Cells for Python via .NET'i kullanmak mümkündür.

###  **Pivot Tablo Nesne Modeli**

 Aspose.Cells for Python via .NET özel bir sınıf seti sunmaktadır.[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) Pivot tabloları oluşturmak ve kontrol etmek için kullanılan ad alanı. Bu sınıflar oluşturmak ve ayarlamak için kullanılır[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)nesneler, pivot tablonun yapı taşlarıdır. Nesneler şunlardır:

- [**Pivot Alanı**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) bir alanı temsil eder[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) tümünün bir koleksiyonunu temsil eder[**Pivot Alanı**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) içindeki nesneler[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)çalışma sayfasındaki PivotTable'ı temsil eder.
- [**PivotTableKoleksiyonu**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) tümünün bir koleksiyonunu temsil eder[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)çalışma sayfasındaki nesneler.

###  **Aspose.Cells Kullanarak Basit Bir Pivot Tablo Oluşturma**

1.  kullanarak çalışma sayfasına veri ekleyin.[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) nesnenin[**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) yöntem.
 Bu veriler pivot tablonun veri kaynağı olarak kullanılacaktır.
1.  çağırarak çalışma sayfasına bir pivot tablo ekleyin.[**PivotTable'lar**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) Koleksiyonun[**eklemek**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)Worksheet nesnesinde kapsüllenmiş olan yöntem.
1.  Yeniye erişin[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) gelen nesne[**PivotTable'lar**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)PivotTable dizinini geçirerek toplama.
1.  Aşağıdakilerden herhangi birini kullanın:[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)Pivot tabloyu yönetmek için nesneler (yukarıda açıklanmıştır).

Örnek kodu çalıştırdıktan sonra çalışma sayfasına bir pivot tablo eklenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atarken aralığın sol üstten sağ alta doğru gitmesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" değildir.

{{% /alert %}}

##  **İleri konular**
- [Konsolidasyon Fonksiyonu](/cells/tr/python-net/consolidation-function/)
- [Pivot Tabloda özel sıralama](/cells/tr/python-net/custom-sorting-in-pivot-table/)
- [Pivot Tablo için Genelleştirme Ayarlarını Özelleştirme](/cells/tr/python-net/customize-globalization-settings-for-pivot-table/)
- [Pivot Tablo Şeritlerini Devre Dışı Bırak](/cells/tr/python-net/disable-pivot-table-ribbons/)
- [Ana Pivot Tablonun Yuvalanmış veya Alt Pivot Tablolarını Bulma ve Yenileme](/cells/tr/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Pivot Tabloyu Biçimlendirme](/cells/tr/python-net/formatting-pivot-table/)
- [Pivot Tablonun Harici Bağlantı Veri Kaynağını Alma](/cells/tr/python-net/get-external-connection-data-source-of-pivot-table/)
- [Pivot Tablo yenileme tarihini alın ve kim bilgilerine göre yenileyin](/cells/tr/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Pivot Tablodaki Grup Pivot Alanları](/cells/tr/python-net/group-pivot-fields-in-the-pivot-table/)
- [Excel dosyasını yüklerken Pivot Önbelleğe Alınmış Kayıtları Ayrıştırma](/cells/tr/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Pivot Tablo ve Kaynak Veriler](/cells/tr/python-net/pivot-table-and-source-data/)
- [Pivot Tablo Verileri Gizle ve Sırala](/cells/tr/python-net/pivot-table-hide-and-sort-data/)
- [Hesaplanan Öğelere Sahip Pivot Tabloyu Yenileyin ve Hesaplayın](/cells/tr/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Pivot Tabloyu ODS dosyasına kaydedin](/cells/tr/python-net/save-pivot-table-in-ods-file/)
- [Rapor filtre sayfaları seçeneğini göster](/cells/tr/python-net/show-report-filter-pages-option/)
- [Pivot Table'da DataField'ın veri görüntüleme formatlarıyla çalışma](/cells/tr/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
