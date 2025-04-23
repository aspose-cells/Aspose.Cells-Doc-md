---
title: Çalışma Kitabından OLE Nesneleri Çıkarma
type: docs
weight: 110
url: /tr/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Bazı durumlarda çalışma kitabından OLE nesnelerini çıkarmak gerekebilir. Aspose.Cells, bu OLE nesnelerini çıkartmayı ve kaydetmeyi destekler.

Bu makale, Visual Studio.Net'te bir konsol uygulaması oluşturmayı ve birkaç basit kod satırıyla bir çalışma kitabından farklı OLE nesnelerini nasıl çıkaracağınızı gösterir.

{{% /alert %}}

## **Bir Çalışma Kitabından OLE Nesneleri Çıkarma**

### **Bir Şablon Çalışma Kitabı Oluşturma**

1. Microsoft Excel'de bir çalışma kitabı oluşturuldu.
1. İlk çalışsayfasına Microsoft Word belgesi, bir Excel çalışma kitabı ve bir PDF belgesi olarak OLE nesneleri eklendi.

|**OLE nesneleri bulunan şablon belge (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Ardından OLE nesneleri çıkarın ve bunları dosya türlerine göre sabit diske kaydedin.

### **Aspose.Cells'i İndirin ve Yükleyin**

1. [Aspose.Cells for .NET'i İndir](https://downloads.aspose.com/cells/net).
1. Geliştirme bilgisayarınıza kurun.

Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.

### **Bir Proje Oluşturun**

**Visual Studio.Net** başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek bir C# konsol uygulaması gösterecektir, ancak VB.NET'i de kullanabilirsiniz.

1. Referanslar Ekleyin
   1. Projenize Aspose.Cells bileşenine bir referans ekleyin, örneğin ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll gibi bir referans ekleyin.

### **OLE Nesnelerini Çıkarın**

Aşağıdaki kod, OLE nesnelerini bulma ve çıkartma işlemini gerçekleştirir. (DOC, XLS ve PDF dosyaları) diskte kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
