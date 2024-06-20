---
title: Bilinen Sorun  Kişisel Site Koleksiyonlarına İzinler
type: docs
weight: 40
url: /tr/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint varsayılan olarak portal yöneticilerine kişisel siteleri yönetme için tam izin vermez. Bu nedenle portal yöneticileri tarafından kişisel site koleksiyonlarında etkinleştirme ve devre dışı bırakma başarısız olabilir. Kurulum sırasında etkinleştirme başarısız olduğunda veya etkisizleştirme bir parçası olarak devre dışı bırakma sırasında, devre dışı bırakma için son karşılama ekranında bir UnauthorizedAccessException görüntülenir.

{{% /alert %}} 
### **Kişisel Sitelere İzin Verme**
Bu sorun kurulum sırasında meydana geldiğinde, UnauthorizedAccessException Microsoft.SharePoint.SPFeature.Activate() SharePoint izleme günlüğüne kaydedilir. Devre dışı bırakma, kurulumun bir parçası olarak başarısız olduğunda, başarısız devre dışı bırakma(lar) için son kurulum ekranında bir UnauthorizedAccessException görüntülenir.

Bu sorunu önlemek için, portal yöneticilerine MySite Web uygulamasını yönetme izni verin:

1. **SharePoint Central Administration**'a gidin ve **Application Management** sekmesini seçin.
1. **Application Security** grubu altında **Web Uygulaması İçin Politika**'yı seçin.
1. Sağ taraftaki **Web Uygulaması** listesinde “My Site” için doğru Web Uygulamasını seçtiğinizden emin olun.
1. Sol üst köşede **Kullanıcı Ekle**'yi seçin.
1. **Kullanıcı Ekle** ekranında varsayılan olarak **Tüm Bölgeleri** seçin ve **İleri**'yi tıklayın.
1. “My Site” Web Uygulamanızın üzerinde kontrol sahibi olmasını istediğiniz uygun kullanıcı(aları) veya etkin dizin grubunu ekleyin.
1. Kontrol düzeyini seçin. 

   **Kullanıcı ekleme ve kontrol düzeyini belirleme** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. **Bitir**'e tıklayın.
