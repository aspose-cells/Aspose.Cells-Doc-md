---
title: Pivot Tablo Oluştur
type: docs
weight: 10
url: /tr/java/create-pivot-table/
---
## **Pivot Tablo Oluştur**

### **Aspose.Cells Kullanarak Pivot Tablo Oluşturun**

{{% alert color="primary" %}}

 Aspose.Cells ile elektronik tablolara pivot tablolar eklemek mümkündür. Aspose.Cells, özellikle pivot tablolar oluşturmak ve kontrol etmek için kullanılan bir dizi özel sınıfa sahiptir. Bu sınıflar, bir nesnenin özelliklerini oluşturmak ve ayarlamak için kullanılır.[**Pivot tablo**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)pivot tablo yapı taşları olarak kullanılan nesne.

Pivot tablo nesneleri şunlardır:

- [**PivotAlanı**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): pivot tablodaki bir alanı temsil eder.
- [**Özet Alan Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) tümünün bir koleksiyonunu temsil eder[**PivotAlanı**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)Pivot tablodaki nesneler.
- [**Pivot tablo**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): bir pivot tabloyu temsil eder.
- [**Özet Tablo Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): çalışma sayfasındaki tüm pivot tablo nesnelerinin koleksiyonunu temsil eder.

{{% /alert %}}

### **Basit Bir Pivot Tablo Oluşturma**

Aspose.Cells kullanarak bir pivot tablo oluşturmak için lütfen aşağıdaki adımları izleyin:

1.  kullanarak çalışma sayfası hücrelerine bazı veriler ekleyin.[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) nesnenin[**değer ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)yöntem. Bu veriler, pivot tablo için bir veri kaynağı olarak kullanılacaktır.
1. Çağırarak çalışma sayfasına bir pivot tablo ekleyin.[**Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) yöntemi[**Özet Tablo Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) sınıfında, kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)nesne.
1.  Erişmek[**Pivot tablo**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) gelen nesne[**Özet Tablo Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) geçerek[**Pivot tablo**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)dizin.
1.  Kapsüllenmiş pivot tablo nesnelerinden (yukarıda açıklanmıştır) herhangi birini kullanın.[**Pivot tablo**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)pivot tabloyu yönetmek için nesne.

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atarken, aralık sol üstten sağ alta doğru ayarlanmalıdır. Örneğin, "A1:C3" geçerlidir; "C3:A1" geçersiz.

{{% /alert %}}

Aşağıdaki kod örneği, yukarıda listelenen temel adımları izleyerek basit bir pivot tablonun nasıl oluşturulacağını gösterir. Kodu yürütürken, çalışma sayfasına bir pivot tablo eklenir:

**Karşılık gelen bir alana dayalı bir pivot tablo oluşturma**

![yapılacaklar:resim_alternatif_metin](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
