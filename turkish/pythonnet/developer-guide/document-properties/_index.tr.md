---
title: Belge Portal Yönetimi
linktitle: Belge Portalları
type: docs
weight: 80
url: /tr/python-net/managing-document-properties/
description: Belge özelliklerini Aspose.Cells for Python via .NET API leri aracılığıyla nasıl yönetileceğini öğrenin.
keywords: Belgeleri yönetmek için nasıl belge özelliklerini C# ile almak veya ayarlamak, C# kullanarak belge eklemek veya silmek, C# ile belge özelliklerine erişmek Aspose.Cells for Python via .NET API leri kullanılarak anlatılmaktadır.
---


## **Giriş**

Microsoft Excel, elektronik tablo dosyalarına özellik eklemek için yetenek sunmaktadır. Bu belge özellikleri kullanışlı bilgiler sağlar ve ayrıntıları aşağıdaki gibi 2 kategoriye ayrılmıştır.

- Sistem tanımlı (hazır) özellikler: Hazır özellikler belge başlığı, yazar adı, belge istatistikleri gibi belge hakkında genel bilgiler içerir.
- Kullanıcı tanımlı (özel) özellikler: Kullanıcı tanımlı özellikler son kullanıcı tarafından ad-değer çifti şeklinde tanımlanan özelleştirilmiş özelliklerdir.

{{% alert color="primary" %}}

Hazır ve özel özellikler hakkında bilinmesi gereken en önemli nokta hazır özelliklerin erişilebilir ve değiştirilebilir olduğudur, ancak oluşturulamaz veya kaldırılamaz. Öte yandan, özel özellikler oluşturulabilir ve yönetilebilir.

{{% /alert %}}

## **Microsoft Excel ile Belge Portalları Nasıl Yönetilir**

Microsoft Excel, Excel dosyalarının belge özelliklerini WYSIWYG yöntemiyle yönetmenize izin verir. Lütfen aşağıdaki adımları izleyerek Excel 2016'daki **Özellikler** iletişim kutusunu açın.

1. **Dosya** menüsünden **Bilgi**'yi seçin.

|**Bilgi Menüsünü Seçme**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **Özellikler** başlığına tıklayıp "Gelişmiş Özellikler”'i seçin.

|**Gelişmiş Özellikler Seçimini Tıklama**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Dosyanın belge özelliklerini yönetin.

|**Özellikler İletişim Kutusu**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Özellikler iletişim kutusunda Genel, Özet, İstatistikler, İçerik ve Gümrük gibi farklı sekmeler bulunur. Her sekme, dosya ile ilgili farklı türde bilgileri yapılandırmaya yardımcı olur. Gümrük sekmesi, özel özellikleri yönetmek için kullanılır.

## **Aspose.Cells Kullanarak Belge Portalları İle Nasıl Çalışılır**

Geliştiriciler, Aspose.Cells for Python via .NET API'lerini kullanarak belge özelliklerini dinamik olarak yönetebilir. Bu özellik, geliştiricilerin dosyayla birlikte kullanışlı bilgiler depolamasına olanak tanır, örneğin dosyanın ne zaman alındığı, işlendiği, zaman damgası ve benzeri.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, API ve Sürüm Numarası bilgilerini çıktı belgelerine doğrudan yazar. Örneğin, Belgeyi PDF'ye dönüştürürken, Aspose.Cells for Python via .NET 'Application' alanını 'Aspose.Cells', 'PDF Üretici' alanını ise 'Aspose.Cells for Python via .NET v17.9' değeriyle doldurur.

Lütfen unutmayın, Aspose.Cells for Python via .NET'nin bu bilgiyi çıktı belgelerinden değiştirmesini veya kaldırmasını sağlayamazsınız.

{{% /alert %}}


### **Özel Belge Özellikleri Nasıl Eklenir veya Kaldırılır**

Bu konunun başında daha önce açıkladığımız gibi, geliştiriciler yerleşik özellikler ekleyemez veya kaldıramaz çünkü bu özellikler sistem tanımlıdır, ancak kullanıcı tanımlı olduğu için özel özellikler eklemek veya kaldırmak mümkündür.

### **Özel Özellikler Nasıl Eklenir**

Aspose.Cells for Python via .NET API'leri, koleksiyona özel özellikler eklemek amacıyla {0} metodunu {1} sınıfı için açtı. {2} metodu, özellikleri Excel dosyasına ekler ve yeni belge özelliği için bir referans döndürür {}, nesnesi ile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Gelişmiş Konular**
- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Yerleşik Belge Özellikleri için ScaleCrop ve LinksUpToDate özelliklerini ayarlama](/cells/tr/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Aspose.Cells kullanarak Excel Dosyasının Belge Sürümünü Belirtme](/cells/tr/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Dahili Belge Özelliklerini Kullanarak Excel Dosyasının Dilini Belirtme](/cells/tr/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

