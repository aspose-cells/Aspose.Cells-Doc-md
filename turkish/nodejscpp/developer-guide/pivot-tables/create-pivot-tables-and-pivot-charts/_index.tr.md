---
title: Özet Tabloları ve Özet Grafikler Oluşturma
type: docs
weight: 20
url: /tr/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Aspose.Cells for Node.js via C++ ile Pivot Tablo ve Pivot Grafik ekleme Yöntemi.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js kütüphanesi ile, Pivot Tablo ve Pivot Grafik Ekleme.
---

{{% alert color="primary" %}}

Bir özet tablo, kayıtların etkileşimli bir özeti. Örneğin, bir çalışma sayfasındaki bir listede yüzlerce fatura girişiniz olabilir. Bir özet tablo, faturaları müşteri, ürün veya tarihe göre toplayabilir. Microsoft Excel ile özet tablonun düğmeleri sürüklenerek bilgileri hızlı bir şekilde yeniden düzenlemek mümkündür.

Bir özet grafik, bir özet tablonun verilerinin etkileşimli grafiksel bir temsilidir. Özet grafikler Excel 2000'de tanıtılmıştır. Özet grafik kullanmak, özet tablonun alt toplamlarını ve toplamlarını otomatik olarak oluşturduğu için verileri anlamak daha da kolaylaştırır.

Aspose.Cells for Node.js via C++, [pivot tablolar](/cells/tr/nodejs-cpp/create-pivot-tables-and-pivot-charts/) ve [pivot grafikler](/cells/tr/nodejs-cpp/create-pivot-tables-and-pivot-charts/) destekler.

{{% /alert %}}

## **Aspose.Cells for Node.js via C++ Kullanarak Pivot Tablo ve Grafikler Ekleme**

 Aspose.Cells for Node.js via C++, pivot tablolar oluşturmak için kullanılan özel sınıf setleri sağlar. Bu sınıflar, PivotTablo nesneleri oluşturmak ve ayarlamak için kullanılır, bunlar ise temel yapıtaşlarıdır:

- PivotField, bir özet tablo raporundaki bir alan.
- PivotFields, bir özet tablodaki tüm PivotField nesnelerinin koleksiyonu.
- PivotTable, bir çalışma sayfasındaki bir PivotTable raporu.
- PivotTables, çalışma sayfasındaki tüm PivotTable nesnelerinin koleksiyonu.

### **Aspose.Cells for Node.js via C++ kullanmak için Hazırlık**
1. NPM'den Aspose.Cells for Node.js via C++ kurun, komut şöyle kullanılır: $ npm install aspose.cells.node.
1. Ayrıca, “Aspose.Cells for Node.js via C++” kurulumuyla ilgili adım adım talimatları takip edebilirsiniz.


### **Aspose.Cells for Node.js via C++ Kullanarak Pivot Tablo Ekleme Yöntemi**

Aspose.Cells for Node.js via C++ kullanarak pivot tablo oluşturmak için:

1. Hücre nesnesinin put_value methodunu kullanarak bir çalışma sayfasına veri ekleyin. Ayrıca veri ile doldurulmuş bir şablon dosyası da kullanabilirsiniz. Veri, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. Yeni PivotTable nesnesine PivotTables koleksiyonundan endeksini geçerek erişin. # PivotTable nesnesinde kapsanan herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Aspose.Cells for Node.js via C++ Kullanarak Pivot Grafik Ekleme Yöntemi**

Aspose.Cells for Node.js via C++ kullanarak PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
