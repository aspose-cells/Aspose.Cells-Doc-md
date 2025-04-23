---
title: Pivot Tablosu Oluştur
type: docs
weight: 10
url: /tr/java/create-pivot-table/
---

## **Pivot Tablosu Oluştur**

### **Aspose.Cells Kullanarak Pivot Tablosu Oluşturma**

{{% alert color="primary" %}}

Aspose.Cells ile elektronik tablolara pivot tabloları eklemek mümkündür. Aspose.Cells'ın özellikle pivot tablolarını oluşturmak ve kontrol etmek için kullanılan birkaç özel sınıfı vardır. Bu sınıflar, pivot tablolarının yapı taşları olarak kullanılır ve bunların özelliklerini ayarlamak için kullanılır.

Pivot tablosu nesneleri şunlardır:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): bir pivot tablosundaki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): pivot tablosundaki tüm [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) nesnelerinin bir koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): bir özet tabloyu temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): çalışma sayfasındaki tüm özet tablo nesnelerinin koleksiyonunu temsil eder.

{{% /alert %}}

### **Basit Bir Özet Tablo Oluşturma**

Aspose.Cells kullanarak bir özet tablo oluşturmak için lütfen aşağıdaki adımları izleyin:

1. Özet tablo için veri kaynağı olarak kullanılacak olan verileri [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) nesnesinin [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) yöntemini kullanarak çalışma sayfası hücrelerine ekleyin.
1. [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) sınıfının [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesnesine kapsüllenmiş [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) yöntemini çağırarak çalışma sayfasına bir özet tablo ekleyin.
1. [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) içinden [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) dizinini geçirerek [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) nesnesine erişin.
1. Yukarıda açıklanan özet tablo nesnelerinden herhangi birini [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) nesnesine kapsüllenmiş olarak kullanarak özet tabloyu yönetin.

{{% alert color="primary" %}}

Hücre aralığını veri kaynağı olarak atadığınızda, aralığın sol üstten sağ alta kadar ayarlanmış olması gerekir. Örneğin, "A1:C3" geçerlidir; "C3:A1" geçersizdir.

{{% /alert %}}

Aşağıdaki kod örneği, yukarıda listelenen temel adımları takip ederek basit bir özet tablo oluşturmanın nasıl yapıldığını göstermektedir. Kodu çalıştırdığınızda, bir özet tablosu çalışma sayfasına eklenir:

**İlgili alana dayalı bir özet tablo oluşturmak**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
