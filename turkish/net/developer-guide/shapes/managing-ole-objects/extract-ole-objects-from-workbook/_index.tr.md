---
title: OLE Nesnelerini Çalışma Kitabından Çıkarın
type: docs
weight: 110
url: /tr/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

Bazen bir çalışma kitabından OLE nesnelerini ayıklamanız gerekir. Aspose.Cells, bu Ole nesnelerinin çıkarılmasını ve kaydedilmesini destekler.

Bu makale, Visual Studio.Net'te bir konsol uygulamasının nasıl oluşturulacağını ve birkaç basit kod satırıyla bir çalışma kitabından farklı OLE nesnelerinin nasıl çıkarılacağını gösterir.

{{% /alert %}}

## **Bir Çalışma Kitabından OLE Nesnelerini Çıkarma**

### **Şablon Çalışma Kitabı Oluşturma**

1. Microsoft Excel'de bir çalışma kitabı oluşturuldu.
1. İlk çalışma sayfasına OLE nesneleri olarak bir Microsoft Word belgesi, bir Excel çalışma kitabı ve bir PDF belgesi ekleyin.

|**OLE nesneleri (OleFile.xls) içeren şablon belgesi**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](extract-ole-objects-from-workbook_1.png)|

Daha sonra OLE nesnelerini ayıklayın ve ilgili dosya türleriyle sabit diske kaydedin.

### **İndirin ve yükleyin Aspose.Cells**

1. [İndir Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Geliştirme bilgisayarınıza kurun.

Tüm Aspose bileşenleri kurulduğunda değerlendirme modunda çalışır. Değerlendirme modunun zaman sınırı yoktur ve yalnızca üretilen belgelere filigran ekler.

### **Proje Oluştur**

Başlama**Visual Studio.Net** ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C# konsol uygulamasını gösterecektir, ancak VB.NET'i de kullanabilirsiniz.

1. Referans Ekle
 1. Projenize Aspose.Cells bileşenine bir referans ekleyin, örneğin ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll'ye bir referans ekleyin

### **OLE Nesnelerini Çıkarın**

Aşağıdaki kod, OLE nesnelerini bulma ve ayıklama işini yapar. OLE nesneleri (DOC, XLS ve PDF dosyaları) diske kaydedilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
