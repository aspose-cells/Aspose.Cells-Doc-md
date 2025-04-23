---
title: Çalışma Kitabından OLE Nesneleri Çıkarma
type: docs
weight: 110
url: /tr/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

Bazen, bir çalışma kitabından OLE nesnelerini çıkarmanız gerekebilir. Aspose.Cells for Python via .NET, bu Ole nesnelerini çıkarmayı ve kaydetmeyi destekler.

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

### **Aspose.Cells for Python Excel Kütüphanesi Kullanarak OLE Nesnelerini Çıkarın**

Aşağıdaki kod, OLE nesnelerini bulma ve çıkartma işlemini gerçekleştirir. (DOC, XLS ve PDF dosyaları) diskte kaydedilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
