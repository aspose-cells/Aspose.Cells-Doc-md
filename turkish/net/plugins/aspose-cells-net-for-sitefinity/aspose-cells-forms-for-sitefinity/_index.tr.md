---
title: Aspose.Cells Sitefinity Formları
type: docs
weight: 10
url: /tr/net/aspose-cells-forms-for-sitefinity/
---
## **giriiş**

Aspose.Cells Sitefinity Modülü için Dinamik Formlar, kullanıcıların Dinamik Anket ve Anketler Oluşturmasına, kullanıcı girdisini Excel Elektronik Tablosuna kaydetmesine ve Aspose.Cells'i kullanarak sonuçları Excel, Metin, CSV ve OpenDocument Elektronik Tablosuna Dışa Aktarmasına olanak tanır. Bu modül, Aspose.Cells for .NET tarafından sağlanan güçlü elektronik tablo oluşturma özelliğini gösterir.

|<p>![yapılacaklar:resim_alternatif_Metin](aspose-cells-forms-for-sitefinity_1)</p><p></p>|
|:- |

### **Modül Özellikleri**

Modülün bu ilk sürümü, Form Oluşturma ve Dışa Aktarma sürecini basit ve kullanımı kolay hale getirmek için aşağıdaki özelliklerle zenginleştirilmiştir.

- Excel'de Form Alanı Ayarlarını Kaydet
- Formun Kullanıcı Giriş Verilerini Excel'e Kaydet
- Yeni Eklemeye ve Mevcut Form Alanlarını Güncellemeye İzin Ver
- TextBox, Multiline TextBox, RadioButtons, CheckBox ve DropDownList, DropDownList Öğeleri tip Alanları Eklemeye İzin Ver
- Her Alan için Etiket Eklemeye/Güncellemeye İzin Ver
- Form Alanlarını Göstermeye/Gizlemeye İzin Ver
- Sütunları içeriğin uzunluğuna Otomatik Sığdır ve Başlık Sütunu biçimlendirmesini Kalın Metin olarak uygula
- Verileri Microsoft Excel Belgelerine Aktar (.xls, .xlsx ve .xlsb)
- Verileri Sekmeyle ayrılmış metin belgesine (*.txt) Aktar
- Verileri CSV'ye Aktar (Virgülle ayrılmış) (*.csv)
- Verileri OpenDocument Elektronik Tablosuna Aktarın (*.ods)
- Dışa aktarmadan önce istenen çıktı formatını seçme seçeneği.
- Dışa aktarılan belge, indirilmek üzere otomatik olarak tarayıcıya gönderilir.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**

Aspose.Cells .NET numaralı Sitefinity eklentilerini kurmak için aşağıdaki gereksinimleri karşılamanız gerekir:

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS

Bu Sitefinity Eklentisini kurarken herhangi bir sorun yaşarsanız lütfen bizimle iletişime geçmekten çekinmeyin.

Eklenti, tüm sürümlerinde desteklenir.

- ASP.NET 4.0 üzerinde çalışan Sitefinity CMS

## **İndirme ve Yükleme**

### **indiriliyor**

Aspose .NET Content Exporter for Sitefinity modülünü aşağıdaki konumlardan birinden indirebilirsiniz.

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/SiteFinity/Aspose.SiteFinity.FormBuilder.ToExcel)

### **yükleme**

İndirdikten sonra, Eklentiyi Sitefinity web sitenize yüklemek için lütfen şu adımları izleyin:

**1. Adım: Dosyaları Sitefinity kurulumunuza kopyalayın**

Lütfen indirilen ZIP dosyasını çıkartın. Aşağıdakileri gerçekleştirmek için FTP'ye veya sunucudaki Sitefinity kurulum klasörüne doğrudan erişime ihtiyacınız olacak:

1.  kopyala**Aspose.Cells.dll** & **Aspose.Sitefinity.FormBuilder.dll**Sitefinity kurulumunun bin klasörü klasörüne.
1. Kopyala**Eklentiler**Sitefinity kurulumunun kök dizinindeki klasör**çöp Kutusu**klasör bulunur.

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
 1. içinde**Kontrol CLR Tipi veya Sanal Yol** alan.
 1. Ekle**~/Addons/Aspose.SiteFinity.FormBuilder.ToExcel/Edit.ascx**
 1. Ekle**İsim**, **Başlık** ve**Tanım** aşağıdaki gibi:
         1. Aspose  **Sayfa ismi**(Düzenle, Görüntüle, Dışa Aktar gibi) formunu SiteFinity Kullanıcılarına
         1. Aspose **Sayfa ismi** Form (Aspose Formu Düzenle , Aspose Formu Görüntüle , Aspose Dışa Aktarma Formu gibi)
         1. **Sayfa ismi** Sitefinity için Form Oluşturucu ve Dışa Aktarıcı.
 1. Diğer tüm alanları olduğu gibi bırakabilirsiniz.
 1. Bittiğinde tıklayın**Değişiklikleri Kaydet**.
 1. Widget, araç kutusuna kaydedilir ve Sitefinity'de kullanılabilir. (**Görmek** **Resmin altında**)

|<p>![yapılacaklar:resim_alternatif_Metin](picture1.png)</p><p></p>|
|:- |

## **Kullanım ve Video Demosu**

### **kullanma**

Aspose.Cells Sitefinity Kullanıcıları için Dinamik Form Oluşturucu eklentisini yükleyip yapılandırdıktan sonra, web sitenizde kullanmaya başlamak gerçekten çok basit. Başlamak için lütfen şu basit adımları izleyin:

1. Yönetici düzeyinde bir hesapla Sitefinity'de oturum açtığınızdan emin olun.
1. Eklentiyi eklemek istediğiniz sayfaya gidin. Sayfanın düzenleme modunda açıldığından emin olun.
1.  itibaren**Widget'ları Sürükle** sağdaki menüden Aspose Formu Düzenle/Görüntüle/Dışa Aktar'ı seçin ve konumuna sürükleyin. (**Görmek** **Resmin altında** )

|<p>![yapılacaklar:resim_alternatif_Metin](aspose-cells-forms-for-sitefinity_2)</p><p></p>|
|:- |

Aspose.Cells Sitefinity için Dinamik Form Oluşturucu modülünü sayfanıza başarıyla eklediniz.

#### **Aspose Lisans başvurusu nasıl yapılır?**

 Bu Eklenti, Aspose.Cells'in bir değerlendirme sürümünü kullanır. Değerlendirmenizden memnun kaldığınızda, şu adresten bir lisans satın alabilirsiniz:[Aspose Satın Alma Sitesi](https://purchase.aspose.com/buy).
Değerlendirme mesajını ve özellik sınırlamalarını kaldırmak için ürün lisansı uygulanmalıdır. Ürünü satın aldıktan sonra bir lisans dosyası alacaksınız. Lisansı uygulamak için lütfen aşağıdaki adımları izleyin

-  Lisans dosyasının şu şekilde adlandırıldığından emin olun:**Aspose.Total.lic**
-  Yer**Aspose.Total.lic** dosyasında**Uygulama verisi** Sitefinity web sitenizin klasörü, örneğin "Sitefinity Kök Klasörü/App_Data/Aspose.Total.lic"

#### **Dinamik Form Ayarları**

1.  Giriş yaptığınızdan emin olun Sayfa menüsüne tıklayın ilk satıra tıklayın**görüş** yanındaki seçenek düğmesi**Eylem sütunu.**  
1.  Tıklamak**Düzenlemek** seçenek etiketinin yanında bulunan düğme.
1.  Önceden tanımlanmış birkaç alan vardır, sadece tıklayarak düzenleyebilir/gizleyebilirsiniz.**Düzenlemek** ızgarada.
1. Her türde yeni alan oluşturabilir/silebilir/güncelleyebilirsiniz**(TextBox, MultiLineTextBox, RadioButton, Onay Kutuları, Açılır Liste, Başlık, Başarı Mesajı)**

#### **Dinamik Form Gönderimi**

1. Alanları doldurun.
1.  Tıklamak**Göndermek** verileri kaydetmek için düğme.
1.  Her biri**Göndermek** düğme tıklaması, yeni kaydı excel'e kaydedecektir.

#### **Kayıtlı Verileri Dışa Aktar**

1. Giriş yaptığınızdan emin olun, Sayfalar menüsüne gidin ve eylem sütununun yanındaki ilk satır görüntüleme seçeneği düğmesine tıklayın
1.  Fare Üzerinde**Dışa Aktarma Simgesi** ve tıklayın**üstünde**dışa aktarma sayfası açılacak
1.  Seçme**İhracat Türü**
1.  Tıklamak**Verileri Dışa Aktar**
1. Dışa aktarma türüne göre dışa aktarılan veri dosyası, indirmek/açmak için açılır

Aspose Sitefinity Export Kullanıcılarını Excel'e başarıyla eklediniz.

### **Video Demosu**

 lütfen kontrol edin[video](https://www.youtube.com/watch?v=La5WMCvafR0) modülü çalışırken görmek için aşağıdaki

## **Destekleyin, Genişletin ve Katkıda Bulunun**

### **Destek**

Aspose'in ilk günlerinden itibaren müşterilerimize sadece iyi ürünler vermenin yeterli olmayacağını biliyorduk. Ayrıca iyi hizmet vermemiz gerekiyordu. Biz de geliştiriciyiz ve teknik bir sorun veya yazılımdaki bir tuhaflık, yapmanız gerekeni yapmanızı engellediğinde bunun ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. İster satın almış olsun ister bir değerlendirme yapıyor olsun, ürünümüzü kullanan herkes, tüm dikkatimizi ve saygımızı hak ediyor.
Sitefinity Modülleri için Aspose.Cells .NET ile ilgili her türlü sorun ve önerilerinizi aşağıdaki platformlardan herhangi birini kullanarak günlüğe kaydedebilirsiniz.

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

### **Genişletin ve Katkıda Bulunun**

#### **Kaynak kodu**

En son kaynak kodunu şu adresten indirebilirsiniz:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET)

#### **Kaynak kodu nasıl yapılandırılır**

Kaynak kodunu açıp genişletmek için aşağıdakilerin kurulu olması gerekir.

- Visual Studio 2013 veya üzeri

Başlamak için lütfen bu basit adımları izleyin

1. Kaynak kodunu indirin/Klonlayın.
1. Visual Studio 2013'ü açın ve Seçin**Dosya** > **Açık Proje**
1. İndirdiğiniz en son kaynak koduna göz atın ve**.sln**dosya.
