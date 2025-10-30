---
title: Çalışma Kitabından OLE Nesnelerini Çıkarın Golang ile C++ kullanarak
linktitle: Çalışma Kitabından OLE Nesneleri Çıkarma
type: docs
weight: 110
url: /tr/go-cpp/extract-ole-objects-from-workbook/
description: Aspose.Cells kullanarak Golang ile C++ kullanarak çalışma kitabından OLE nesnelerini nasıl çıkaracağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen, çalışma kitabından OLE nesnelerini çıkarmanız gerekir. Aspose.Cells, bu OLE nesnelerini çıkarma ve kaydetmeyi destekler.

Bu makale, Visual Studio'da bir konsol uygulaması oluşturmayı ve birkaç basit kod satırıyla çalışma kitabından farklı OLE nesnelerini çıkarmayı gösterir.

{{% /alert %}}

## **Bir Çalışma Kitabından OLE Nesneleri Çıkarma**

### **Bir Şablon Çalışma Kitabı Oluşturma**

1. Microsoft Excel'de bir çalışma kitabı oluşturun.
1. İlk çalışma sayfasına bir Microsoft Word belgesi, bir Excel çalışma kitabı ve bir PDF belgesi OLE nesnesi olarak ekleyin.

|**OLE nesneleri bulunan şablon belge (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Daha sonra, OLE nesnelerini çıkarın ve ilgili dosya türleriyle sabit diske kaydedin.

### **Aspose.Cells'i İndirin ve Yükleyin**

1. [Aspose.Cells for C++ İndirme](https://downloads.aspose.com/cells/go-cpp/)
1. Geliştirme bilgisayarınıza kurun.

Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.

### **Bir Proje Oluşturun**

Başlat **Visual Studio** ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C++ konsol uygulamasını gösterecek.

1. Referanslar Ekleyin
   1. Projenize Aspose.Cells bileşenine referans ekleyin, örneğin, ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll’ye referans ekleyin.

### **OLE Nesnelerini Çıkarın**

Aşağıdaki kod, OLE nesnelerini bulma ve çıkarma işlemini gerçekleştirir. OLE nesneleri (DOC, XLS ve PDF dosyaları) diske kaydedilir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
