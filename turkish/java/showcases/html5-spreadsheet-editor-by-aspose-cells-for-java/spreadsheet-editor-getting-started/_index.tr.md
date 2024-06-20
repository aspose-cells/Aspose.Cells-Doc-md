---
title: Tablo Düzenleyici Başlangıç Kılavuzu
type: docs
weight: 10
url: /tr/java/spreadsheet-editor-getting-started/
---

**İçindekiler**

- [Giriş](#SpreadsheetEditorGettingStarted-Introduction)
- [Sistem Gereksinimleri](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [İndirme ve Kurulum](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Destek](#SpreadsheetEditorGettingStarted-Support)
- [Katkıda bulun](#SpreadsheetEditorGettingStarted-Contribute)
- [Lisans](#SpreadsheetEditorGettingStarted-License)
### **Giriş**
Html5 Tablo Düzenleyici, bir web tarayıcısında elektronik tablo belgelerini görüntüleyebilen ve düzenleyebilen bir web uygulamasıdır. Excel, SpreadsheetML, CVS, OpenDocument ve Microsoft Excel tarafından desteklenen birçok diğer formatı destekler. Hücre düzenleme, biçimlendirme, formül düzenleme, satır ve sütun yönetimi vb. gibi tüm temel olanaklar desteklenmektedir.

![todo:image_alt_text](aowcrc1.png)

HTML5 Tablo Düzenleyici, [Aspose.Cells for Java](https://products.aspose.com/cells/java/) ürününün birçok özelliğini kullanır ve onları Java uygulamanızda elektronik tablo oluşturmak, değiştirmek ve görüntülemek için nasıl kullanılacağını gösterir.

**Özellikler**

- Dosyalarla Çalışma 
  - Desteklenen Formatlar
  - Yerel dosyaları açma
  - Dropbox’tan açma
  - URL’den açma
  - Yeni tablo oluşturma
  - Çeşitli formatlarda dışa aktarma
- Sayfalarla Çalışma 
  - Sayfa ekleme ve kaldırma
  - Sayfa yeniden adlandırma
  - Sayfalar arasında geçiş
- Satır ve Sütunlarla Çalışma 
  - Satır ekleme
  - Sütun ekleme
  - Satır kaldırma
  - Sütun kaldırma
  - Sütun Genişliği ve Satır Yüksekliği
- Hücrelerle Çalışma 
  - Bir hücre seçme
  - Bir hücreyi düzenleme
  - Formül düzenleme
  - Hücre hizalaması
  - Hücreyi temizleme
  - Bir hücre eklemek
  - Bir hücreyi kaldırmak
- Metin biçimlendirmeyle çalışmak 
  - Kalın, italik, altı çizili
  - Yazı tipi ve boyutu
  - Biçimlendirmeyi temizleme
### **Sistem Gereksinimleri**
**Yazılım Gereksinimleri**

- CDI destekli Java uygulama sunucusu
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Donanım Gereksinimleri**

Donanım gereksinimleri, HTML5 Elektronik Tablo Düzenleyicisi'ni dağıtmayı seçtiğimiz Java uygulama sunucusuna ve aynı anda açtığımız elektronik tabloların sayısına bağlı olarak değişir. Aşağıda, ortamı başlangıçta kurmanıza yardımcı olacak bir tahmin bulunmaktadır.

- 2 GHz CPU
- 2 GB RAM
- 500 MB Disk
### **İndirme ve Kurulum**
HTML5 Elektronik Tablo Düzenleyicisi, CDI desteği olan herhangi bir Java uygulama sunucusuna dağıtılabilen bir Java EE uygulamasıdır. [Glassfish](https://javaee.github.io/glassfish/) ile test edilmiştir.

**Kaynak Kodu**

Proje kaynağı [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/) adresinde bulunmaktadır. Ayrıca, aşağıdaki sitelerde Git aynalarını tutuyoruz:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Komut satırı aracılığıyla kaynak kodunu indirmek için aşağıdaki komutlardan birini kullanın:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Maven kullanarak derleme**

Proje derleme işlemi Maven kullanılarak yönetilmektedir. Bu nedenle, herhangi bir IDE olmadan komut satırından bir WAR dosyası hazırlayabilirsiniz. Dağıtım için üretilen WAR'ı ve bağımlılıklarınızı nasıl dağıtacağınız konusundaki uygulama sunucusu belgeleri size yardımcı olacaktır.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**NetBeans Kullanarak**

[NetBeans IDE](https://netbeans.apache.org/) ile projeyi yönetmek çok kolaydır. NetBeans, Java geliştiricileri arasında popüler olan ve Oracle tarafından desteklenen popüler bir IDE'dir.

- Proje kaynak kodunu indirin.
- NetBeans IDE'de projeyi açın.
- Araç çubuğundaki ***Çalıştır*** düğmesine tıklayın.
- Uygulama Sunucusu olarak ***Glassfish*** sunucusunu seçin.

**Eclipse Kullanımı**

[Eclipse IDE](http://www.eclipse.org/ide/) Maven projelerini içe aktarmak için resmi entegrasyon sağlar: [M2Eclipse](http://www.eclipse.org/m2e/) adlı.

1. Eclipse IDE'nize M2Eclipse'i yükleyin. Kurulum prosedürü web sitelerinde açıklanmaktadır.
1. Proje kaynak kodunu indirin.
1. Dosya menüsünden ***İçe Aktar*** iletişim kutusunu açın.
1. İçe aktarma iletişim kutusundan ***Maven Projesi***'ni seçin.
1. ***İleri***'ye tıklayın.
1. Kaynak kodunun konumunu seçmek için ***Göz At***'a tıklayın.
1. Aşağıdaki listeden ***pom.xml***'i seçin.
1. ***Bitir***'e tıklayın.

Eclipse IDE'nin projeyi içe aktarması ve yüklemesi gerekmektedir.
### **Destek**
**Hata Raporu**

Hata raporu göndermek için [Github proje sayfası](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) üzerinde yeni bir konu oluşturun ve ***hata*** etiketini uygulayın.

**Özellik İsteği**

Geri bildiriminizi ve istediğiniz özellikleri büyük bir memnuniyetle karşılıyoruz. Yeni bir özellik veya mevcut bir iyileştirme isteğinde bulunmak için lütfen [Github proje sayfası](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) üzerinde yeni bir konu oluşturun ve ***iyileştirme*** etiketini uygulayın.

**Sorular ve Yardım**

HTML5 Elektronik Tablo Düzenleyicisi ile ilgili her türlü soruyu [Github konusu](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) üzerinden sorabilirsiniz. Sadece yeni bir konu oluşturun ve ***soru*** etiketini uygulayın.

**Aspose.Cells for Java Forumları**

Aspose ürün forumları, hem deneme hem de ödeme yapan müşterilere tam destek sağlar. Uzmanlar, yardım sağlamak ve soruları yanıtlamak üzere 7/24 hazır bekliyor. [Ürün forumlarına buradan](https://forum.aspose.com/c/cells/9) ulaşın.

**Aspose Blogları**

Bizimle iletişime geçin ve ürünlerimiz ve tekliflerimiz hakkında en son haberlerden haberdar olun. [Blogumuza buradan](http://blog.aspose.com) abone olun.
### **Katkıda bulun**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


HTML5 Elektronik Tablo Düzenleyicisi, herkesin projeye katkıda bulunmak için maksimum seçenekler sunan bir açık kaynaklı projedir.

**Kaynak Kodu**

Proje kaynağı [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java) üzerinde mevcuttur. Ayrıca aşağıdaki sitelerde Git yansılarını sürdürüyoruz:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Pull İstekleri**

Proje için kaynak koduna katkıda bulunmak için Github üzerinden bir pull isteği gönderin. Bir pull isteği oluşturma hakkında daha fazla bilgi için Github'ın [Bir pull isteği oluşturmak](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) başlıklı makalesini okuyun.
### **Lisans**
**MIT Lisansı**

Minimum sorumluluklar için en liberal açık kaynak lisanslarından birini kullanıyoruz. HTML5 Elektronik Tablo Düzenleyici [MIT Lisansı](https://opensource.org/licenses/mit-license.php) altında yayınlandı.

**Aspose Lisansı**

Ürün, Aspose lisansı olmadan [kısıtlamalarla çalışabilir](/cells/tr/java/licensing/). Kısıtlamaları kaldırmak için [ücretsiz geçici lisans](https://purchase.aspose.com/temporary-license) alabilir veya [tam lisans satın alabilirsiniz](https://purchase.aspose.com/buy).

Varsayılan olarak, düzenleyici **src/main/resources/com/aspose/spreadsheeteditor** dizininden **Aspose.Total.Java.lic** dosyasını yüklemeye çalışacaktır. Lisans dosyasını bu dizine kopyalayın. Varsayılan davranış, **AsposeLicense** sınıfını düzenleyerek değiştirilebilir.
