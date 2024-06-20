---
title: Dağıtım ve Aktivasyon
type: docs
weight: 20
url: /tr/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[Aspose.Cells for SharePoint Kurulumunu](/cells/tr/sharepoint/installing-aspose-cells-for-sharepoint/) bu makale kurulum sürecini açıklar. Bu makale, kurulum sürecinin nasıl dağıtıldığı ve etkinleştirildiğini açıklar.

{{% /alert %}} 
### **Dağıtım**
Aspose.Cells for SharePoint dağıtım sırasında aşağıdaki işlemleri gerçekleştirir:

1. **Aspose.Cells.SharePoint.dll**'yi Global Assembly Cache'e yükler ve **web.config** dosyasına bir SafeControl girişi ekler.
1. Özellik manifestini kurar ve diğer gerekli dosyaları ilgili dizinlere kopyalar.
1. Özelliği SharePoint veritabanına kaydeder ve özelliği etkinleme kapsamında etkinleştirmek üzere kullanılabilir hale getirir.
### **Etkinleştirme**
Aspose.Cells for SharePoint bir site (site koleksiyonu) düzeyinde özellik olarak paketlenmiştir ve site koleksiyonlarında etkinleştirilebilir veya devre dışı bırakılabilir. 

Etkinleştirme sırasında, özellik site koleksiyonunun ana web uygulamasının sanal dizinine bazı değişiklikler yapar:

1. Dönüştürme ayarları sayfasını sitemap dosyasına ekler.
1. Gerekli kaynak dosyalarını sanal dizindeki App_GlobalResources klasörüne kopyalar.
