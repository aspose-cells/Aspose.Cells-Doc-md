---
title: Pivot Tablo Ekle
linktitle: Pivot Tabloları
type: docs
weight: 160
url: /tr/nodejs-cpp/create-pivot-table/
description: Excel elek tablo dosyalarının pivot tablolarını oluşturun ve biçimlendirin.
---

## **Pivot Tablosu Oluştur**

Aspose.Cells for Node.js via C++ kullanılarak, programatik olarak pivot tabloları hesaplara eklemek mümkündür.

### **Pivot Tablosu Nesne Modeli**

Aspose.Cells for Node.js via C++, pivot tabloları oluşturmak ve kontrol etmek için kullanılan özel sınıf setleri sağlar. Bu sınıflar, [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnelerini oluşturmak ve ayarlamak için kullanılır, bunlar pivot tablonun yapıtaşlarıdır. Nesneler:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield), bir [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) içindeki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection), [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) içindeki tüm [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) nesnelerinin bir koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), bir çalışma sayfasındaki bir PivotTable'ı temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), bir çalışma sayfasındaki tüm [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnelerinin bir koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Pivot Tablosu Oluşturma**

1. [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) nesnesinin [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) metodu kullanılarak bir çalışma sayfasına veri ekleyin.
   Bu veri, pivot tablosunun veri kaynağı olarak kullanılacaktır.
2. Çağrılan [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) metoduna (Worksheet nesnesinde kapsüllenmiş olan) [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) koleksiyonuna bir pivot tablosu ekleyin.
3. PivotTable endeksini geçerek [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) koleksiyonundan yeni [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnesine erişin.
4. Pivot tablosunu yönetmek için yukarıda açıklanan [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnelerinden herhangi birini kullanın.

Örnek kodu çalıştırdıktan sonra bir pivot tablosu çalışma sayfasına eklenir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atadığınızda, aralığın sol üstten sağ alta gitmesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.

{{% /alert %}}
