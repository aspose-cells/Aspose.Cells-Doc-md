---
title: Pivot Tablo Ekle
description: Aspose.Cells for Python via .NET ile Pivot Tablosu oluşturma ve biçimlendirme.
linktitle: Pivot Tabloları
url: /tr/python-net/pivot-tables/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: Pivot Tablosu Oluştur, Pivot Tablosu Ekle, Pivot Tablosu Biçimlendir.
---

## **Pivot Tablosu Oluştur**
Aspose.Cells for Python via .NET kullanarak elektronik tablolara programlı olarak pivot tabloları eklemek mümkündür.

### **Pivot Tablosu Nesne Modeli**
Aspose.Cells for Python via .NET, bir pivot tablosu oluşturmak ve kontrol etmek için kullanılan [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) ad alanında özel bir sınıf seti sağlar. Bu sınıflar, bir pivot tablosunun yapı taşları olan [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) nesnelerini oluşturmak ve ayarlamak için kullanılır. Nesneler şunlardır:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/), bir [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) içindeki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection), [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) içindeki tüm [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) nesnelerinin bir koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable), bir çalışma sayfasındaki bir PivotTable'ı temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), bir çalışma sayfasındaki tüm [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) nesnelerinin bir koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Pivot Tablosu Oluşturma**
1. [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) nesnesinin [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) metodu kullanılarak bir çalışma sayfasına veri ekleyin.
   Bu veri, pivot tablosunun veri kaynağı olarak kullanılacaktır.
2. Çağrılan [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) metoduna (Worksheet nesnesinde kapsüllenmiş olan) [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) koleksiyonuna bir pivot tablosu ekleyin.
3. PivotTable endeksini geçerek [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) koleksiyonundan yeni [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) nesnesine erişin.
4. Pivot tablosunu yönetmek için yukarıda açıklanan [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) nesnelerinden herhangi birini kullanın.
Örnek kodu çalıştırdıktan sonra bir pivot tablosu çalışma sayfasına eklenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
Veri kaynağı olarak bir hücre aralığı atadığınızda, aralığın sol üstten sağ alta gitmesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## **Gelişmiş Konular**

{{< app/cells/assistant language="python-net" >}}