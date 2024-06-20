---
title: Aspose.Cells Forms for Sitefinity
type: docs
weight: 10
url: /tr/net/aspose-cells-forms-for-sitefinity/
---

## **Giriş**

Aspose.Cells Sitefinity Modülü Dinamik Formlar kullanıcılara, Dinamik Anket ve Araştırmalar oluşturmalarına, kullanıcı girişini Excel elektronik tablosuna kaydetmelerine ve sonuçları Aspose.Cells kullanarak Excel, Metin, CSV ve OpenDocument Elektronik Tablosuna aktarmalarına olanak sağlar. Bu modül, Aspose.Cells for .NET tarafından sağlanan güçlü elektronik tablo oluşturma özelliğini sergiler.

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_1)</p><p></p>|
| :- |

### **Modül Özellikleri**

Bu modülün ilk sürümü, Form Oluşturma ve Aktarım sürecini basit ve kullanımı kolay hale getirmek için aşağıdaki özelliklerle zenginleştirilmiştir

- Excel'de Form Alan Ayarlarını Kaydet
- Formun Kullanıcı Giriş Verilerini Excel'e Kaydet
- Yeni Form Alanları Eklemeye ve Mevcutları Güncellemeye İzin Ver
- Metin Kutusu, Çoklu Satır Metin Kutusu, Radyo Düğmeleri, Onay Kutusu ve Açılır listeden, Açılır listedeki Öğeler türünde Alanlar Eklemeye İzin Ver
- Her Alan için Etiket Ekleme/Güncelleme İzin Ver
- Form Alanlarını Göster/Gizle
- İçeriğin uzunluğuna otomatik olarak uyum sağlama ve Başlık Sütunu biçimlendirme olarak Kalın Metin uygulama
- Verileri Microsoft Excel Belgesine Aktarma (.xls, .xlsx ve .xlsb)
- Verileri Sekme sınırlı metin belgesine aktarma (*.txt)
- Verileri CSV'ye Aktar (Virgülle Sınırlı) (*.csv)
- Verileri OpenDöküman Elektronik Tabloya Aktar (*.ods)
- İhracat öncesinde istenen çıkış biçimini seçme seçeneği.
- İhrac edilen belge, otomatik olarak indirilmek üzere tarayıcıya gönderilir.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**

Aspose.Cells .NET için Sitefinity eklentilerini kurmak için aşağıdaki gereksinimleri karşılamalısınız:

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS

Bu Sitefinity Eklentisini kurarken herhangi bir sorunla karşılaşırsanız lütfen bizimle iletişime geçin.

Eklenti tüm sürümlerde desteklenmektedir

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS

## **İndirme ve Kurulum**

### **İndirme**

Aspose .NET Content Exporter for Sitefinity modülünü aşağıdaki konumlardan birinden indirebilirsiniz

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)

### **Yüklemek**

İndirdikten sonra, lütfen Add-on'u Sitefinity web sitenize kurmak için aşağıdaki adımları izleyin:

**Adım 1: Dosyaları Sitefinity kurulumunuza kopyalayın**

Lütfen indirilen ZIP dosyasını çıkarın. Aşağıdakileri gerçekleştirmek için sunucudaki Sitefinity kurulum klasörüne FTP veya doğrudan erişiminiz olmalı:

1. **Aspose.Cells.dll** & **Aspose.Sitefinity.FormBuilder.dll** dosyalarını Sitefinity kurulumunun bin klasörüne kopyalayın.
1. **Addons** klasörünü, **bin** klasörünün bulunduğu yerin hemen üstüne kopyalayın.

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
      1. **Kontrol CLR Türü veya Sanal Yol** alanına. 
         1. **~/Addons/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx** ekleyin
      1. Aşağıdaki gibi **Ad**, **Başlık** ve **Açıklama** ekleyin: 
         1. Aspose **PageName** (Düzenle, Görüntüle, Dışa Aktar gibi) formunu SiteFinity kullanıcılarına sunar
         1. Aspose **PageName** Formu (Aspose Düzenle Formu, Aspose Görüntü Formu, Aspose Dışa Aktar Formu gibi)
         1. Sitefinity için **PageName** Form Oluşturucu ve Dışa Aktarıcı.
      1. Diğer tüm alanları olduğu gibi bırakabilirsiniz.
      1. Tamamlandığınızda **Değişiklikleri Kaydet**'e tıklayın.
      1. Widget, toolbox'ta kayıtlıdır ve Sitefinity'de kullanılabilir. (**Aşağıdaki Resme** **bakın**)

|<p>![todo:image_alt_text](picture1.png)</p><p></p>|
| :- |

## **Kullanımı ve Video Demosu**

### **Kullanarak**

Sitefinity Kullanıcıları için Aspose.Cells Dinamik Form Oluşturucu eklentisini kurup yapılandırdıktan sonra websitenizde kullanmaya başlamak gerçekten çok basittir. Başlamak için lütfen bu basit adımları takip edin:

1. Sitefinity'e Yönetici düzeyinde bir hesapla giriş yaptığınızdan emin olun.
1. Eklentiyi eklemek istediğiniz sayfaya gidin. Sayfanın düzenleme modunda açıldığından emin olun.
1. Sağdaki **Widgetları Sürükle** menüsünden Aspose Düzenle/Görüntü/Dışa Aktar Formunu seçin ve konumuna sürükleyin. (**Aşağıdaki Resme** **bakın**)

|<p>![todo:image_alt_text](aspose-cells-forms-for-sitefinity_2)</p><p></p>|
| :- |

Sitefinity sayfanıza başarıyla Aspose.Cells Dinamik Form Oluşturucusu modülünü eklediniz.

#### **Aspose Lisansı Nasıl Uygulanır?**

Bu Eklenti, Aspose.Cells'ın bir değerlendirme sürümünü kullanmaktadır. Değerlendirmenizle memnun kaldığınızda [Aspose Satın Alma Web Sitesi](https://purchase.aspose.com/buy)'nden bir lisans satın alabilirsiniz.
Değerlendirme iletilisini ve özellik kısıtlamalarını kaldırmak için ürün lisansı uygulanmalıdır. Ürünü satın aldıktan sonra bir lisans dosyası alacaksınız. Lisansı uygulamak için aşağıdaki adımları izleyin:

- Lisans dosyasının **Aspose.Total.lic** olarak adlandırıldığından emin olun
- **Aspose.Total.lic** dosyasını Sitefinity web sitenizin **App_Data** klasörüne yerleştirin, örneğin "Sitefinity Root Klasörü/App_Data/Aspose.Total.lic"

#### **Dinamik Form Ayarları**

1. Sitefinity'e giriş yaptığınızdan ve ilk satırın yanındaki **Görünüm** seçeneği düğmesine tıkladığınızdan emin olun.  
1. Etiketin yakınında bulunan **Düzenle** düğmesine tıklayın.
1. Birkaç önceden tanımlanmış alan bulunmaktadır, bunları sadece grid üzerinde **Düzenle**'ye tıklayarak düzenleyebilir/gizleyebilirsiniz.
1. **(TextBox, Çok Satırlı Metin Kutusu, Radyo Düğmeleri, Onay Kutuları, Açılır Liste, Başlık, Başarı Mesajı)** türünde yeni alanlar oluşturabilir/silebilir/güncelleyebilirsiniz

#### **Dinamik Form Gönder**

1. Alanları doldurun.
1. Verileri kaydetmek için **Gönder** düğmesine tıklayın.
1. Her **Gönder** düğmesi tıklaması yeni bir kaydı excel'e kaydeder.

#### **Kayıtlı Verileri Dışa Aktar**

1. Sitefinity'ye giriş yaptığınızdan emin olun, Sayfalar menüsüne gidin ve eylem sütununun yanındaki ilk sıra görünüm seçeneği düğmesine tıklayın
1. **Dışa Aktar Simgesi**'ne Fare ile gelin ve **onit**i tıklayın dışa aktar sayfası açılacaktır
1. **Dışa Aktarım Türü**nü Seçin
1. **Veri Dışa Aktar**'a Tıklayın
1. Dışa Aktarılan veri dosyası dışa aktarma türüne göre indirilmek/ açılmak üzere açılacaktır.

Aspose Sitefinity Kullanıcılarını Excel'e Başarıyla Eklediniz.

### **Video Demo**

Modülü uygulamada görmek için lütfen [videoyu](https://www.youtube.com/watch?v=La5WMCvafR0) kontrol edin.

## **Destek, Genişletme ve Katkıda Bulunma**

### **Destek**

Aspose'un ilk günlerinden itibaren, müşterilerimize sadece iyi ürünler sunmanın yeterli olmayacağını biliyorduk. Ayrıca iyi bir hizmet sunmamız gerekiyordu. Kendi geliştiricileri olduğumuz için, teknik bir sorun veya yazılımdaki bir tuhaflık sizi yapmanız gereken şeyden alıkoyduğunda ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. Ürünlerimizi kullanan herkes, bunları satın almış olsun veya değerlendirme yapılıyor olsun, tam dikket ve saygıyı hak ediyor.
Aspose.Cells .NET için Sitefinity Modülleri ile ilgili herhangi bir sorunu veya öneriyi aşağıdaki platformlardan herhangi birini kullanarak kaydedebilirsiniz

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Genişletme ve Katkı Sağlama**

#### **Kaynak Kodu**

En son kaynak kodunu şuradan indirebilirsiniz:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET)

#### **Kaynak kodunu nasıl yapılandıracağınız**

Aşağıdakileri açıp kaynak kodunu genişletmek için aşağıdakilere sahip olmanız gerekir

- Visual Studio 2013 veya daha üstü

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/kopyalayın.
1. Visual Studio 2013'ü açın ve **Dosya** > **Projeyi Aç** seçin
1. İndirdiğiniz en son kaynak koduna göz atın ve **.sln** dosyasını açın.
