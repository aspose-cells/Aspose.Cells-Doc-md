---
title: Elektronik Tablo Düzenleyici Başlarken
type: docs
weight: 10
url: /tr/java/spreadsheet-editor-getting-started/
---
**İçindekiler**

- [Giriş](#SpreadsheetEditorGettingStarted-Introduction)
- [sistem gereksinimleri](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [İndirme ve Kurulum](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Destek olmak](#SpreadsheetEditorGettingStarted-Support)
- [Katkı yapmak](#SpreadsheetEditorGettingStarted-Contribute)
- [Lisans](#SpreadsheetEditorGettingStarted-License)
### **Giriş**
Html5 Elektronik Tablo Düzenleyicisi, elektronik tablo belgelerini bir web tarayıcısında görüntüleyebilen ve düzenleyebilen bir web uygulamasıdır. Excel, SpreadsheetML, CVS, OpenDocument ve Microsoft Excel tarafından desteklenen diğer birçok formatı destekler. Hücre düzenleme, biçimlendirme, formül düzenleme, satır ve sütun yönetimi vb. dahil olmak üzere tüm temel özellikler desteklenir.

![yapılacaklar:resim_alternatif_metin](aowcrc1.png)

 HTML5 Elektronik Tablo Düzenleyicisi'nin birçok özelliğini kullanır.[Aspose.Cells for Java](https://products.aspose.com/cells/java/) ve bunların Java uygulamanızda bir elektronik tablo oluşturmak, işlemek ve işlemek için nasıl kullanılacağını gösterir.

**Özellikleri**

- Dosyalarla Çalışmak
 - Desteklenen Formatlar
 - Yerel dosyaları aç
 - Dropbox'tan aç
 - URL'den aç
 - Yeni bir Elektronik Tablo oluşturun
 - Çeşitli biçimlerde dışa aktarma
-  E-Tablolarla Çalışma
 - Sayfa ekle ve kaldır
 - Sayfaları yeniden adlandırın
 - Sayfalar arasında geçiş yapın
-  Satırlar ve Sütunlarla Çalışmak
 - Satır Ekle
 - Bir Sütun Ekle
 - Bir Satırı Kaldır
 - Bir Sütunu Kaldır
 - Sütun Genişliği ve Sıra Yüksekliği
-  Cells ile çalışmak
 - Hücre seçme
 - Bir hücreyi düzenleme
 - Formül Düzenleme
 - Cell hizalama
 - Temizle Cell
 - Hücre ekle
 - Bir hücreyi kaldır
-  Metin formatlama ile çalışma
 - Kalın, italik, altı çizili
 - Yazı tipi stili ve boyutu
 - Biçimlendirmeyi temizle
### **sistem gereksinimleri**
**yazılım gereksinimleri**

- CDI destekli Java uygulama sunucusu
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [Java Sunucusu Yüzleri 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primeface'ler 5.1](https://www.primefaces.org/)

**Donanım Gereksinimleri**

Donanım gereksinimleri, HTML5 Elektronik Tablo Düzenleyiciyi dağıtmak için seçtiğimiz Java uygulama sunucusuna ve aynı anda açtığımız elektronik tablo sayısına göre değişir. Aşağıda, başlangıçta ortamın kurulmasına yardımcı olacak bir tahmin verilmiştir.

- 2 GHz işlemci
- 2 GB RAM
- 500 MB Disk
### **İndirme ve Kurulum**
 HTML5 Elektronik Tablo Düzenleyicisi bir Java EE uygulamasıdır ve CDI desteğiyle herhangi bir Java uygulama sunucusu web profiline dağıtılabilir. ile test edilmiştir[cam balığı](https://javaee.github.io/glassfish/).

**Kaynak kodu**

 Proje kaynağı şu adreste mevcuttur:[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Ayrıca aşağıdaki sitelerde Git yansılarını koruyoruz:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Kod](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [KaynakForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Kaynak kodunu komut satırı aracılığıyla indirmek için aşağıdaki komutlardan birini kullanın:

**Github**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Kod**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**KaynakForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Maven kullanarak oluşturun**

Proje oluşturma süreci Maven ile yönetilmektedir. Böylece herhangi bir IDE olmadan komut satırından WAR dosyası hazırlayabilirsiniz. Dağıtım için bir SAVAŞ oluşturmak üzere aşağıdaki komutu kullanın. İlgili uygulama sunucusunun belgeleri, oluşturulan WAR'ı ve bağımlılıklarını nasıl konuşlandıracağınız konusunda size yardımcı olacaktır.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**NetBeans'i Kullanma**

 kullanarak projeyi yönetmek çok kolaydır.[NetBeans IDE'si](https://netbeans.apache.org/). NetBeans, Java geliştiricileri arasında popüler IDE'lerden biridir ve Oracle tarafından desteklenmektedir.

- Proje kaynak kodunu indirin.
- Projeyi NetBeans IDE'de açın.
-  Tıklamak***Koşmak*** araç çubuğundaki düğme.
-  Seçme***cam balığı*** Uygulama Sunucusu olarak sunucu.

**Eclipse'i Kullanma**

[Eclipse IDE'si](http://www.eclipse.org/ide/) adlı Maven projelerini içe aktarmak için resmi entegrasyon sağlar[M2Eclipse](http://www.eclipse.org/m2e/):

1. M2Eclipse'i Eclipse IDE'nize kurun. Kurulum prosedürü kendi web sitesinde açıklanmıştır.
1. Proje kaynak kodunu indirin.
1. Aç***İçe aktarmak*** Dosya menüsünden iletişim kutusu.
1.  Seçme***Maven Proje*** içe aktarma iletişim kutusundan.
1.  Tıklamak***Sonraki***.
1.  Tıklamak***Araştır*** kaynak kodunun konumunu seçmek için.
1.  Seçme***pom.xml*** aşağıdaki listeden.
1.  Tıklamak***Bitiş***.

Eclipse IDE, projeyi içe aktarmalı ve yüklemelidir.
### **Destek olmak**
**Hata raporu**

 Bir hata raporu göndermek için adresinde yeni bir sorun oluşturun.[Github proje sayfası](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) ve etiketi uygulayın***böcek***.

**Özellik isteği**

 Geri bildiriminiz ve talep ettiğiniz özellikler için çok teşekkür ederiz. Mevcutta yeni bir özellik veya geliştirme talep etmek için lütfen adresinde yeni bir sayı oluşturun.[Github proje sayfası](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) ve etiketi uygulayın***artırma***.

**Sorular ve Yardım**

 HTML5 Elektronik Tablo Düzenleyici ile ilgili her türlü soruyu kullanarak sorabilirsiniz.[Github sorunu](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Sadece yeni bir sorun oluşturun ve***soru*** etiket.

**Aspose.Cells for Java Forumlar**

 Aspose ürün forumları, hem deneme hem de ücretli müşteriler için tam destek sağlar. Uzmanlar, yardım sağlamak ve soruları yanıtlamak için 7/24 oturuyor. Ziyaret[ürün forumları burada](https://forum.aspose.com/c/cells/9).

**Aspose Bloglar**

 Bizimle iletişime geçin ve ürünlerimiz ve tekliflerimiz hakkında en son haberleri takip edin. Abone olmak[blogumuz burada](http://blog.aspose.com).
### **Katkı yapmak**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_elektronik tablo_Editör_tarafından_Aspose.Cells_için_Java)


HTML5 Elektronik Tablo Düzenleyici, herkesin projeye katkıda bulunması için maksimum seçeneğe izin veren açık kaynaklı bir projedir.

**Kaynak kodu**

 Proje kaynağı şu adreste mevcuttur:[Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Ayrıca aşağıdaki sitelerde Git yansılarını koruyoruz:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [KaynakForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Çekme İstekleri**

 Projeye kaynak koduyla katkıda bulunmak için Github aracılığıyla bir çekme isteği göndermeniz yeterlidir. Github'un makalesinde daha fazla bilgi okuyun:[Bir çekme isteği oluşturun](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Lisans**
**MİT Lisansı**

 Katkıda bulunanlar üzerindeki minimum yükümlülükler için en liberal açık kaynak lisanslarından birini kullanıyoruz. HTML5 Elektronik Tablo Düzenleyicisi altında yayınlandı[MİT Lisansı](https://opensource.org/licenses/mit-license.php).

**Aspose Lisans**

 Ürün Aspose lisansı olmadan çalışmaktadır,[sınırlamalarla](/cells/tr/java/licensing/) . Sınırlamaları kaldırmak için bir[ücretsiz geçici lisans](https://purchase.aspose.com/temporary-license) veya[tam lisans satın al](https://purchase.aspose.com/buy).

 Varsayılan olarak, editör yüklemeyi deneyecektir.**Aspose.Total.Java.lic** gelen dosya**src/main/resources/com/aspose/spreadsheeteditor** dizin. Lisans dosyasını bu dizine kopyalamanız yeterlidir. Varsayılan davranış düzenlenerek değiştirilebilir.**AsposeLisans** sınıf.
