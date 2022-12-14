---
title: Dağıtım ve Aktivasyon
type: docs
weight: 20
url: /tr/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[SharePoint için Aspose.Cells'i yükleme](/cells/tr/sharepoint/installing-aspose-cells-for-sharepoint/) kurulum sürecinde size yol gösterir. Bu makalede, yükleme işleminin ne dağıtıldığı ve etkinleştirildiği açıklanmaktadır.

{{% /alert %}} 
### **dağıtım**
Aspose.Cells for SharePoint, dağıtım sırasında aşağıdaki eylemleri gerçekleştirir:

1.  Yüklemeler**Aspose.Cells.SharePoint.dll** Global Assembly Cache'e ekler ve bir SafeControl girişi ekler.**web.config** dosya.
1. Özellik bildirimini ve diğer gerekli dosyaları uygun dizinlere yükler.
1. Özelliği SharePoint veritabanına kaydeder ve özellik kapsamında etkinleştirme için kullanılabilir hale getirir.
### **Aktivasyon**
 Aspose.Cells for SharePoint, site (site koleksiyonu) düzeyinde bir özellik olarak paketlenmiştir ve site koleksiyonlarında etkinleştirilebilir ve devre dışı bırakılabilir.

Etkinleştirme sırasında özellik, site koleksiyonunun ana web uygulamasının sanal dizininde bazı değişiklikler yapar:

1. Site haritası dosyasına dönüştürme ayarları sayfası ekler.
1. Gerekli kaynak dosyalarını sanal dizindeki App_GlobalResources klasörüne kopyalar.
