---
title: Sitefinity Kullanıcılarını Excel e Dışa Aktar
type: docs
weight: 20
url: /tr/net/sitefinity-export-users-to-excel/
---

**İçerik Özeti**

- [Giriş](#SitefinityExportUserstoExcel-Introduction)
- [Sistem Gereksinimleri ve Desteklenen Platformlar](#SitefinityExportUserstoExcel-SystemRequirementsandSupportedPlatforms) 
  - [Sistem Gereksinimleri](#SitefinityExportUserstoExcel-SystemRequirements)
  - [Desteklenen Platformlar](#SitefinityExportUserstoExcel-SupportedPlatforms)
- [Kaynak Kodu](#SitefinityExportUserstoExcel-SourceCode) 
  - [Kaynak kodunu yapılandırmak için](#SitefinityExportUserstoExcel-Howtoconfigurethesourcecode)
- [Kurulum ve Kullanım](#SitefinityExportUserstoExcel-InstallationandUsage) 
  - [İndirme](#SitefinityExportUserstoExcel-Downloading)
  - [Yüklemek](#SitefinityExportUserstoExcel-Installing)
- [Kullanımı ve Video Demosu](#SitefinityExportUserstoExcel-UsingandVideoDemo) 
  - [Kullanarak](#SitefinityExportUserstoExcel-Using)
  - [Video Demo](#SitefinityExportUserstoExcel-VideoDemo)
- [Destek](#SitefinityExportUserstoExcel-Support)
- [Genişletme ve Katkı Sağlama](#SitefinityExportUserstoExcel-ExtendandContribute)
## **Giriş**
Aspose .NET İhracat Kullanıcıları Excel'e SiteFinity Modülü, geliştiricilere SiteFinity Kullanıcılarını Microsoft Excel veya OpenOffice Tablo Çalışma Kitabına ihracat etme olanağı sağlar. Bu modül, Aspose.Cells tarafından sağlanan güçlü tablo oluşturma özelliğini sergilemektedir.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**
### **Sistem Gereksinimleri**
Aspose.Cells .NET için Sitefinity eklentilerini kurmak için aşağıdaki gereksinimleri karşılamalısınız:

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS

Bu Sitefinity Eklentisini kurarken herhangi bir sorunla karşılaşırsanız lütfen bizimle iletişime geçin.
### **Desteklenen Platformlar**
Eklenti tüm sürümlerde desteklenmektedir

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS
## **Kaynak Kodu**
En son kaynak kodunu aşağıdaki konumlardan birinden edinebilirsiniz

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity)
### **Kaynak kodunu yapılandırmak için**
Aşağıdakileri açıp kaynak kodunu genişletmek için aşağıdakilere sahip olmanız gerekir

- Visual Studio 2010 veya daha yükseği

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/kopyalayın.
1. Visual Studio 2010'u açın ve **Dosya** > **Proje Aç**'ı seçin
1. İndirdiğiniz en son kaynak koduna göz atın ve **.sln** dosyasını açın.
## **Kurulum ve Kullanım**
### **İndirme**
Aspose .NET Content Exporter for Sitefinity modülünü aşağıdaki konumlardan birinden indirebilirsiniz

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases)
### **Yüklemek**
İndirdikten sonra, lütfen Add-on'u Sitefinity web sitenize kurmak için aşağıdaki adımları izleyin:

**Adım 1: Dosyaları Sitefinity kurulumunuza kopyalayın**

Lütfen indirilen ZIP dosyasını çıkarın. Aşağıdakileri gerçekleştirmek için sunucudaki Sitefinity kurulum klasörüne FTP veya doğrudan erişiminiz olmalı:

1. Aspose.Cells.dll ve Aspose.SiteFinity.ExportUsersToExcel.dll dosyalarını Sitefinity kurulumunun **bin** klasörüne kopyalayın.
1. **Addons** klasörünü, **bin** klasörünün bulunduğu Sitefinity kurulumunun ana dizinine kopyalayın.

**Adım 2: Aspose Sitefinity Content Export eklentisini Sitefinity'de kaydedin**

1. Log into your Sitefinity CMS with an ‘**Administrator**’ account. The login page can be reached by <http://www.mywebsite.com/sitefinity>
1. **Yönetim**'e tıklayın ve ardından **Ayarlar**'a tıklayın.
   Temel Ayarlar sayfası görüntülenir.
1. **Gelişmiş** bağlantısına tıklayın.
   Ayarlar sayfası görüntülenir.
1. Sol tarafta **Araç Kutuları**'na ve ardından **Araç Kutuları'na**, **Sayfa Kontrolleri'ne**, **Bölümlere** ve **İçerik Araç Kutusu Bölümü'ne** ve ardından **Araçlar**'a tıklayın.
1. **Yeni oluştur**'a tıklayın.
   Widget kayıt formu görüntülenir.
1. Aşağıdaki şekilde form alanlarını doldurun: 
   1. **Etkin**'in seçili olduğundan emin olun.
   1. ~/Addons/Aspose.SiteFinity.ExportUsersToExcel/AsposeExportUsersToExcel.ascx ekleyin

   1. **Kontrol CLR Türü veya Sanal Yol** alanına ekleyin.
   1. Aşağıdaki gibi **Ad**, **Başlık** ve **Açıklama** ekleyin:
      Aspose.SiteFinity.ExportUsersToExcel
      Aspose Export SiteFinity Users to Excel
      SiteFinity Kullanıcılarını Excel'e Aktar
   1. Diğer tüm alanları olduğu gibi bırakabilirsiniz.
1. Tamamlandığınızda **Değişiklikleri Kaydet**'e tıklayın.
   Widget araç kutusuna kaydedilir ve Sitefinity'de kullanılabilir.
## **Kullanımı ve Video Demosu**
### **Kullanarak**
Aspose Sitefinity Export Users to Excel eklentisini kurduktan ve yapılandırdıktan sonra web sitenizde kullanmaya başlamak gerçekten basittir. Başlamak için lütfen aşağıdaki basit adımları izleyin:

1. Sitefinity'e Yönetici düzeyinde bir hesapla giriş yaptığınızdan emin olun.
1. Export eklentisini eklemek istediğiniz sayfaya gidin. Sayfanın düzenleme modunda olduğundan emin olun.
1. Sağdaki **Araçları Sürükle** menüsünden Aspose Excel Kullanıcılarını dışa aktar'ı seçin ve konumuna sürükleyin.


Aspose Sitefinity Kullanıcılarını Excel'e Başarıyla Eklediniz.
### **Video Demo**
Modülü eylem halinde görmek için lütfen [videoyu](https://www.youtube.com/watch?v=O1524u-Pom4) kontrol edin.
## **Destek**
Aspose'un ilk günlerinden itibaren, müşterilerimize sadece iyi ürünler sunmanın yeterli olmayacağını biliyorduk. Ayrıca iyi bir hizmet sunmamız gerekiyordu. Kendi geliştiricileri olduğumuz için, teknik bir sorun veya yazılımdaki bir tuhaflık sizi yapmanız gereken şeyden alıkoyduğunda ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. Ürünlerimizi kullanan herkes, bunları satın almış olsun veya değerlendirme yapılıyor olsun, tam dikket ve saygıyı hak ediyor.

Aspose.Cells .NET için Sitefinity Modülleri ile ilgili herhangi bir sorunu veya öneriyi aşağıdaki platformlardan herhangi birini kullanarak kaydedebilirsiniz

- [Github ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
## **Genişletme ve Katkı Sağlama**
Aspose Sitefinity Widget'ları / Modülleri açık kaynaklıdır ve kaynak kodları aşağıda listelenen büyük sosyal kodlama sitelerinde bulunmaktadır. Geliştiricilerin kaynak kodunu indirmeleri ve gereksinimlerine göre işlevselliği genişletmeleri teşvik edilir.
