---
title: Bilinen Sorun - Kişisel Site Koleksiyonlarına İlişkin İzinler
type: docs
weight: 40
url: /tr/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

SharePoint varsayılan olarak portal yöneticilerine kişisel siteleri yönetmek için tam izin vermez. Bu nedenle, kişisel site koleksiyonundaki etkinleştirme ve devre dışı bırakma, portal yöneticileri tarafından gerçekleştirildiğinde başarısız olabilir. Buna kurulum sırasında etkinleştirme ve devre dışı bırakma dahildir.

{{% /alert %}} 
### **Kişisel Sitelere İzin Verme**
Yükleme sırasında bu sorun oluştuğunda, SharePoint izleme günlüğüne Microsoft.SharePoint.SPFeature.Activate() konumunda bir UnauthorizedAccessException kaydedilir. Kaldırma işleminin bir parçası olarak devre dışı bırakma işlemi başarısız olduğunda, başarısız devre dışı bırakma(lar) için son kurulum ekranında bir UnauthorizedAccessException görüntülenir.

Bu sorunu önlemek için portal yöneticilerine MySite Web uygulamasını yönetme izni verin:

1.  git**SharePoint Merkezi Yönetimi** ve öğesini seçin**Uygulama yönetimi** sekme.
1.  Seçmek**Web Uygulaması Politikası** altında**Uygulama Güvenliği** grup.
1.  "Benim Sitem" için doğru Web Uygulamasını seçtiğinizden emin olun.**İnternet Uygulaması** sağdaki liste.
1.  Seçme**Kullanıcı Ekle** sol üstte
1.  Seçmek**Tüm Bölgeler** varsayılan olarak**Kullanıcı Ekle** ekran ve tıklayın**Sonraki**.
1. “Benim Sitem” Web Uygulamanız üzerinde kontrol sahibi olmasını istediğiniz uygun kullanıcıları veya aktif dizin grubunu ekleyin.
1.  Kontrol seviyesini seçin.

   **Kullanıcı ekleme ve kontrol seviyesini ayarlama** 

![yapılacaklar:resim_alternatif_Metin](known-issue-permissions-to-personal-site-collections_1.png)




1.  Tıklamak**Bitiş**.
