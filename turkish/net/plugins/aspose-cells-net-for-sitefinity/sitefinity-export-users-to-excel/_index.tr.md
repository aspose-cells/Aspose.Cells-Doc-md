---
title: Sitefinity Kullanıcıları Excel'e Aktarma
type: docs
weight: 20
url: /tr/net/sitefinity-export-users-to-excel/
---
**İçindekiler Özeti**

- [giriiş](#SitefinityExportUserstoExcel-Introduction)
- [Sistem Gereksinimleri ve Desteklenen Platformlar](#SitefinityExportUserstoExcel-SystemRequirementsandSupportedPlatforms) 
  - [sistem gereksinimleri](#SitefinityExportUserstoExcel-SystemRequirements)
  - [Desteklenen Platformlar](#SitefinityExportUserstoExcel-SupportedPlatforms)
- [Kaynak kodu](#SitefinityExportUserstoExcel-SourceCode) 
  - [Kaynak kodu nasıl yapılandırılır](#SitefinityExportUserstoExcel-Howtoconfigurethesourcecode)
- [Kurulum ve Kullanım](#SitefinityExportUserstoExcel-InstallationandUsage) 
  - [indiriliyor](#SitefinityExportUserstoExcel-Downloading)
  - [yükleme](#SitefinityExportUserstoExcel-Installing)
- [Kullanım ve Video Demosu](#SitefinityExportUserstoExcel-UsingandVideoDemo) 
  - [kullanma](#SitefinityExportUserstoExcel-Using)
  - [Video Demosu](#SitefinityExportUserstoExcel-VideoDemo)
- [Destek](#SitefinityExportUserstoExcel-Support)
- [Genişletin ve Katkıda Bulunun](#SitefinityExportUserstoExcel-ExtendandContribute)
## **giriiş**
Aspose .NET SiteFinity Modülü için Kullanıcıları Excel'e Aktar, geliştiricilerin SiteFinity Kullanıcılarını Microsoft Excel'e veya OpenOffice Elektronik Tablosuna aktarmalarına olanak tanır. Bu modül, Aspose.Cells tarafından sağlanan güçlü elektronik tablo oluşturma özelliğini göstermektedir.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**
### **sistem gereksinimleri**
Aspose.Cells .NET numaralı Sitefinity eklentilerini kurmak için aşağıdaki gereksinimleri karşılamanız gerekir:

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS

Bu Sitefinity Eklentisini kurarken herhangi bir sorun yaşarsanız lütfen bizimle iletişime geçmekten çekinmeyin.
### **Desteklenen Platformlar**
Eklenti, tüm sürümlerinde desteklenir.

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS
## **Kaynak kodu**
En son kaynak kodunu aşağıdaki konumlardan birinden alabilirsiniz.

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity)
### **Kaynak kodu nasıl yapılandırılır**
Kaynak kodunu açıp genişletmek için aşağıdakilerin kurulu olması gerekir.

- Visual Studio 2010 veya üzeri

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/Klonlayın.
1.  Visual Studio 2010'u açın ve Seçin**Dosya** > **Açık Proje**
1.  İndirdiğiniz en son kaynak koduna göz atın ve**.sln** dosya.
## **Kurulum ve Kullanım**
### **indiriliyor**
Aspose .NET Content Exporter for Sitefinity modülünü aşağıdaki konumlardan birinden indirebilirsiniz.

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases)
### **yükleme**
İndirdikten sonra, Eklentiyi Sitefinity web sitenize yüklemek için lütfen şu adımları izleyin:

**1. Adım: Dosyaları Sitefinity kurulumunuza kopyalayın**

Lütfen indirilen ZIP dosyasını çıkartın. Aşağıdakileri gerçekleştirmek için FTP'ye veya sunucudaki Sitefinity kurulum klasörüne doğrudan erişime ihtiyacınız olacak:

1.  Aspose.Cells.dll ve Aspose.SiteFinity.ExportUsersToExcel.dll'yi kopyalayın.**çöp Kutusu** Sitefinity kurulumunun klasörü.
1.  Kopyala**Eklentiler** Sitefinity kurulumunun kök dizinindeki klasör**çöp Kutusu** klasör bulunur.

**2. Adım: Aspose Sitefinity İçerik Dışa Aktarma eklentisini Sitefinity'ye kaydedin**

1. ' ile Sitefinity CMS'nize giriş yapın**yönetici** ' hesap. Giriş sayfasına şu adresten ulaşılabilir:<http://www.mywebsite.com/sitefinity>
1.  Tıklamak**Yönetim** ve daha sonra**Ayarlar**.
Temel Ayarlar sayfası görünür.
1.  Tıkla**Gelişmiş** bağlantı.
 Ayarlar sayfası görünür.
1.  Sol bölmede,**Araç kutuları** bunu takiben**Araç kutuları** , sonra**Sayfa Denetimleri**, **Bölümler** ve**İçerikAraç KutusuBölümü** , sonra**Aletler.**
1.  Tıklamak**Yeni oluşturmak**.
 Widget kayıt formu görünür.
1.  Form alanlarını aşağıdaki gibi doldurun:
 1. Emin olun**Etkinleştirilmiş** seçildi.
 1. ~/Addons/Aspose.SiteFinity.ExportUsersToExcel/AsposeExportUsersToExcel.ascx dosyasını ekleyin

 1. ` ` içinde**Kontrol CLR Tipi veya Sanal Yol** alan.
 1. Ekle**İsim**, **Başlık** ve**Tanım** aşağıdaki gibi:
 Aspose.SiteFinity.ExportUsersToExcel
 Aspose SiteFinity Kullanıcılarını Excel'e Aktar
 SiteFinity Kullanıcılarını Excel'e Aktarın
 1. Diğer tüm alanları olduğu gibi bırakabilirsiniz.
1.  Bittiğinde, tıklayın**Değişiklikleri Kaydet**.
 Widget, araç kutusuna kaydedilir ve Sitefinity'de kullanılabilir.
## **Kullanım ve Video Demosu**
### **kullanma**
Aspose Sitefinity Export Users to Excel eklentisini kurup yapılandırdıktan sonra, web sitenizde kullanmaya başlamak gerçekten çok basit. Başlamak için lütfen şu basit adımları izleyin:

1. Yönetici düzeyinde bir hesapla Sitefinity'de oturum açtığınızdan emin olun.
1. Dışa Aktarma eklentisini eklemek istediğiniz sayfaya gidin. Sayfanın düzenleme modunda açıldığından emin olun.
1.  itibaren**Widget'ları Sürükle** sağdaki menüden Aspose Kullanıcıları Excel'e Aktar'ı seçin ve konumuna sürükleyin.


Aspose Sitefinity Export Kullanıcılarını Excel'e başarıyla eklediniz.
### **Video Demosu**
 lütfen kontrol edin[video](https://www.youtube.com/watch?v=O1524u-Pom4) modülü çalışırken görmek için aşağıdaki
## **Destek**
Aspose'in ilk günlerinden itibaren müşterilerimize sadece iyi ürünler vermenin yeterli olmayacağını biliyorduk. Ayrıca iyi hizmet vermemiz gerekiyordu. Biz de geliştiriciyiz ve teknik bir sorun veya yazılımdaki bir tuhaflık, yapmanız gerekeni yapmanızı engellediğinde bunun ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. İster satın almış olsun ister bir değerlendirme yapıyor olsun, ürünümüzü kullanan herkes, tüm dikkatimizi ve saygımızı hak ediyor.

Sitefinity Modülleri için Aspose.Cells .NET ile ilgili her türlü sorun ve önerilerinizi aşağıdaki platformlardan herhangi birini kullanarak günlüğe kaydedebilirsiniz.

- [ Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)
## **Genişletin ve Katkıda Bulunun**
Aspose Sitefinity Widget'ları / Modülleri açık kaynaktır ve kaynak kodları aşağıda listelenen başlıca sosyal kodlama web sitelerinde mevcuttur. Geliştiricilerin kaynak kodunu indirmeleri ve işlevselliği kendi gereksinimlerine göre genişletmeleri önerilir.
