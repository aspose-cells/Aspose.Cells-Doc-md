---
title: Excel dosyalarında Pivot Tablo ve Pivot Grafikler oluşturmayı öğrenin, Aspose.Cells kullanarak Golang ile C++ aracılığıyla.
linktitle: Özet Tabloları ve Özet Grafikler Oluşturma
type: docs
weight: 20
url: /tr/go-cpp/create-pivot-tables-and-pivot-charts/
description: Learn how to create pivot tables and pivot charts in Excel files using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Bir pivot tablo, kayıtların etkileşimli bir özetidir. Örneğin, bir çalışma sayfasında yüzlerce fatura kaydı olabilir. Bir pivot tablo, faturaları müşteri, ürün veya tarihe göre toplamlandırabilir. Microsoft Excel ile, pivot tablodaki bilgileri yeni bir konuma sürükleyerek hızla yeniden düzenlemek mümkündür.

Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells, [pivot tablolar](/cells/tr/cpp/create-pivot-tables-and-pivot-charts/) ve [pivot grafikler](/cells/tr/cpp/create-pivot-tables-and-pivot-charts/) destekler.

{{% /alert %}}

## **Özet Tabloları ve Grafikler Eklemek**

Aspose.Cells, özet tabloları oluşturmak için kullanılan özel bir sınıf kümesi sağlar. Bu sınıflar, PivotTable nesnelerini oluşturmak ve ayarlamak için kullanılır ve temel PivotTable nesnesinin yapı taşları olarak hareket ederler:

- **PivotField**, pivot tablo raporundaki bir alan.
- **PivotFields**, bir pivot tabloda bulunan tüm PivotField nesnelerinin koleksiyonu.
- **PivotTable**, bir çalışma sayfasında bir PivotTable raporu.
- **PivotTables**, çalışma sayfasındaki tüm PivotTable nesnelerinin koleksiyonu.

### **Aspose.Cells'i kullanmaya hazırlık**

1. Aspose.Cells'i indirin ve kurun:
   1. [Aspose.Cells İndirin](https://downloads.aspose.com/cells/go-cpp/)
   1. Geliştirme bilgisayarınıza kurun.
      Tüm [Aspose](http://www.aspose.com/) bileşenleri kurulduktan sonra değerlendirme modunda çalışır. Değerlendirme modu zaman limiti olmadan çalışır ve sadece üretilen belgelere filigran ekler. Bileşeni tam kapasiteyle kullanmak için geçerli bir lisansa sahip olmanız gerekir.
1. Bir proje oluşturun:
   1. C++ IDE'nizi başlatın (ör., Visual Studio).
   1. Yeni bir konsol uygulaması oluşturun.
1. Referanslar ekleyin:
   Projenize Aspose.Cells bileşenine referans ekleyin, örneğin, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Pivot Tablo Ekleme**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir hücreye veri eklemek için `Cell` nesnesinin `PutValue` metodunu kullanın. Ayrıca, zaten veriyle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1. `PivotTables` koleksiyonunu `Add` yöntemiyle (`Worksheet` nesnesine kapsüllenmiş) kullanarak yeni bir pivot tablo ekleyin.
1. `PivotTables` koleksiyonundan yeni `PivotTable` nesnesine erişin ve onun indeksini kullanın. `PivotTable` nesnesine kapsüllenmiş herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **Pivot Grafik Ekleme**

Aspose.Cells kullanarak bir PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin `PivotSource` özelliğini, mevcut bir pivot tabloya referans olacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
