---
title: GridWeb ile Çalışmak
type: docs
weight: 20
url: /tr/java/working-with-gridweb/
---
## **Microsoft Excel Dosyasını Açma**

Aspose.Cells.GridWeb kontrolü Microsoft Excel dosyalarını açabilir ve yükleyebilir - veriler, biçimlendirme, grafikler, resimler vb.

GridWeb kontrolünü kullanarak bir Excel dosyasını açmak için:

1. Aspose.Cells.GridWeb denetimini bir web formuna veya sayfasına ekleyin.
1. Dosya yolunu belirterek Excel dosyasını içe aktarın.
1. Uygulamayı çalıştırın veya sayfayı açın.

İçeriği bir Excel dosyasından Aspose.Cells.GridWeb denetimine yüklemek için, Excel dosyasının yolunu belirtmek üzere importExcelFile yöntemini çağırmanız gerekir. Bundan sonra, GridWeb kontrolü dosyayı belirtilen yoldan otomatik olarak bulur ve içeriğini burada görüntüler. Bir Excel dosyasının içeriğini yükleyen bir kod parçacığı aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Yukarıdaki kod parçasını istediğiniz gibi kullanabilirsiniz. Örneğin, bir web formu yüklendiğinde Excel dosyasını otomatik olarak yüklemek için, formun kendi belirlediğiniz Page_Load olayına bu kodu ekleyin.

**GridWeb'e bir Excel dosyası yüklenir**

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_1.png)

## **Microsoft Excel Dosyasını Kaydetme**

Aspose.Cells.GridWeb kontrolü kullanılarak GUI modundaki web sitelerinde yeni Microsoft Excel dosyaları oluşturmak veya bunları değiştirmek mümkündür. Dosyalar daha sonra Excel dosyalarına kaydedilebilir. Aspose.Cells.GridWeb, etkin bir çevrimiçi hesap tablosu düzenleyicisi olarak hizmet verir. Bu konuda kılavuz içeriğinin Excel dosyalarına nasıl kaydedileceği açıklanmaktadır.

### **Dosya Olarak Kaydetme**

Aspose.Cells.GridWeb kontrolünün içeriğini bir Excel dosyası olarak kaydetmek için:

1. Aspose.Cells.GridWeb denetimini bir web formuna veya sayfasına ekleyin.
1. Çalışmanızı belirtilen bir yolda bir Excel dosyası olarak kaydedin.
1. Uygulamayı çalıştırın veya sayfayı açın.

Aşağıdaki kod örneği, ızgara içeriğinin bir Excel dosyasına nasıl kaydedileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Yukarıdaki kod parçacığı birkaç şekilde kullanılabilir. Yaygın bir yol, tıklandığında ızgara içeriğini bir Excel dosyasına kaydeden bir düğme eklemektir. Aspose.Cells.GridWeb, görev için daha kolay bir yaklaşım sunar. Aspose.Cells.GridWeb'de SaveCommand adında bir olay var. Yukarıdaki kod parçacığı, SaveCommand olayının olay işleyicisine eklenebilir ve bu, kullanıcıların Aspose.Cells.GridWeb'in yerleşik**Kayıt etmek** buton.

## **Aspose.Cells.GridWeb ve Başlık Çubuğunu Yeniden Boyutlandırma**

Bu makalede, Aspose.Cells.GridWeb API kullanılarak çalışma zamanında GridWeb'in yeniden boyutlandırılmasının nasıl yapılacağı açıklanmaktadır. Ayrıca, verilerinin okunmasını kolaylaştırmak için Aspose.Cells.GridWeb denetiminin başlık çubuklarının nasıl yeniden boyutlandırılacağı da açıklanmaktadır.

### **Aspose.Cells.GridWeb'in Genişlik ve Yüksekliğini Değiştirme**

Aspose.Cells.GridWeb kontrolünün genişliğini ve yüksekliğini değiştirmek basit ama önemli bir özelliktir. Aspose.Cells.GridWeb denetimi, API'deki GridWeb sınıfı tarafından temsil edilir. GridWeb denetiminin genişlik ve yüksekliğini yeniden boyutlandırmak için, genişlik ve yükseklik özelliklerini kullanmanız yeterlidir.

{{% alert color="primary" %}}

Kontrolün genişliği ve yüksekliği piksel veya nokta olarak tanımlanabilir.

{{% /alert %}}

Aşağıdaki kod parçacığının çıktısı aşağıda gösterilmiştir.

**GridWeb kontrolünün genişliği ve yüksekliği değiştirildi**

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Başlık Çubuğunun Genişliğini ve Yüksekliğini Değiştirme**

Aspose.Cells.GridWeb denetimi aşağıdaki gibi iki başlık çubuğu içerir:

- Üst başlık çubuğu, bu başlık çubuğu A, B, C, D vb. sütunları temsil eder.
- Sol başlık çubuğu, bu başlık çubuğu satırları 1, 2, 3, 4 vb. olarak temsil eder.

Bu başlık çubuklarının her ikisi de aşağıda gösterilmiştir.

**Başlık çubukları**

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_3.png)

Sırasıyla GridWeb denetiminin HeaderBarHeight ve HeaderBarWidth özelliklerini kullanarak üst başlık çubuğunun yüksekliğini ve sol başlık çubuğunun genişliğini değiştirin. Aşağıdaki şekil, aşağıdaki kod örneğinin çıktısını göstermektedir.

**Başlık çubuğunun genişliği ve yüksekliği değiştirildi**

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Aspose.Cells.GridWeb Events ile çalışma**

Tüm geliştiriciler olaylara ve amaçlarına aşina olmalıdır. Olaylar, bir kontrolde veya sınıfta meydana gelebilecek değişikliklerin bildirimlerini göndermek için kullanılır. Aspose.Cells.GridWeb, kontrolde belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılabilecek birkaç olaya sahiptir.

Bu konu, Aspose.Cells.GridWeb denetimi tarafından desteklenen tüm olaylara bir giriş ve bu olayların nasıl ele alınacağına ilişkin bazı ayrıntılar sağlar.

### **Izgara Olaylarına Giriş**

Aspose.Cells.GridWeb kontrolü, kontrolde belirli olaylar tetiklendiğinde işlemlerin gerçekleştirilmesi için daha fazla kontrol sağlayan birkaç olayı destekler. Aspose.Cells.GridWeb denetimi tarafından desteklenen olayların tam listesi aşağıda bulunabilir.

|**Olaylar**|**Açıklama**|
|:- |:- |
|Hücre Komutu|Bir hücrenin komut köprüsü tıklandığında gerçekleşir. Bu olay başlatıldığında, e.Argument parametresi komutun adını sağlar.|
|HücreDoubleClick|Hücre çift tıklandığında gerçekleşir.|
|SütunSilindi|Kullanıcı, istemci tarafındaki menüyü kullanarak bir çalışma sayfasından bir sütunu sildiğinde gerçekleşir.|
|Sütun Silme|Bir kullanıcı, istemci tarafındaki menüyü kullanarak bir çalışma sayfasından bir sütunu silmeye çalışırken gerçekleşir.|
|SütunDoubleClick|Sütun başlığı çift tıklandığında gerçekleşir.|
|Sütun Eklendi|Kullanıcı, istemci tarafındaki menüyü kullanarak bir çalışma sayfasına sütun eklediğinde gerçekleşir.|
|Özel Komut|Bir kullanıcı özel bir komut düğmesini tıklattığında gerçekleşir.|
|Özel Verileri Yükle|Denetimin EnableSession özelliği false olarak ayarlandığında ve çalışma sayfası verilerini yüklemesi gerektiğinde gerçekleşir. Çalışma sayfası verilerini bir dosyadan veya veritabanından yüklemek için bu olayı oturumsuz modda işleyebilirsiniz.|
|Sayfa DiziniDeğişti|Denetimin sayfa sayfası dizini değiştirildiğinde gerçekleşir.|
|SatırSilindi|Kullanıcı, istemci tarafındaki menüyü kullanarak çalışma sayfasından bir satırı sildiğinde gerçekleşir.|
|Satır Silme|Bir kullanıcı, istemci tarafındaki menüyü kullanarak bir çalışma sayfasından bir satırı silmeye çalışırken gerçekleşir.|
|SatırDoubleClick|Satır başlığına çift tıklandığında gerçekleşir.|
|Satır Eklendi|Kullanıcı, istemci tarafındaki menüyü kullanarak çalışma sayfasına bir satır eklediğinde gerçekleşir.|
|Komutu Kaydet| Ne zaman oluşur**Kayıt etmek** butonu tıklanır.|
|SheetSekmeClick|Bir sayfa sekmesi tıklandığında gerçekleşir.|
|Komut Gönder| Ne zaman oluşur**Göndermek** butonu tıklanır.|
|Komutu Geri Al| Ne zaman oluşur**Geri alma** butonu tıklanır.|
|AjaxCallBitti|Kontrolün AJAX güncellemesi bittiğinde tetiklenir. (EnableAJAX, true olarak ayarlanacaktır).|
|CellModifiedOnAjax|AJAX çağrısında hücre değiştirildiğinde tetiklenir.|
|Sütun Filtresinden Sonra|Filtre bir sütuna uygulandığında tetiklenir.|

### **Izgara Olaylarını Yönetme**

Belirli bir olayı tetikleme konusunda belirli bir işlem gerçekleştirmek için bir olay işleyici oluşturmamız gerekir. Bir olay işleyici, belirli bir olay tetiklendiğinde istenen görevi gerçekleştirir. Aşağıdaki örnek, basit bir ızgara olayının nasıl işleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Çift Tıklama Olaylarıyla Çalışma**

Aspose.Cells.GridWeb üç tür çift tıklama olayı içerir:

- CellDoubleClick, bir hücre çift tıklandığında tetiklenir.
- ColumnDoubleClick, bir sütun başlığına çift tıklandığında tetiklenir.
- RowDoubleClick, bir satır başlığına çift tıklandığında tetiklenir.

Bu konuda, Aspose.Cells.GridWeb'de çift tıklama olaylarının nasıl etkinleştirileceği anlatılmaktadır. Ayrıca, bu olaylar için olay işleyicileri oluşturmayı da tartışır.

### **Çift Tıklama Olaylarını Etkinleştirme**

GridWeb denetiminin EnableDoubleClickEvent özelliği true olarak ayarlanarak, tüm çift tıklama olayları istemci tarafında etkinleştirilebilir.

{{% alert color="primary" %}}

Varsayılan olarak, EnableDoubleClickEvent özelliği false olarak ayarlanır. Bu, çift tıklama olaylarının varsayılan olarak etkin olmadığı anlamına gelir. Bu tür olayları uygulamak için önce özelliği etkinleştirin.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Çift tıklama olayları etkinleştirildiğinde, herhangi bir çift tıklama olayı için olay işleyicileri oluşturmak mümkündür. Bu olay işleyicileri, belirli bir çift tıklama olayı başlatıldığında belirli görevleri gerçekleştirir.

### **Çift Tıklama Olaylarını Yönetme**

#### **Çift Tık Cell**

CellDoubleClick olayı için olay işleyicisi, çift tıklanan hücrenin tüm bilgilerini sağlayan CellEventArgs türünde bir bağımsız değişken sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Sütun Başlığına Çift Tıklama**

ColumnDoubleClick olayı için olay işleyicisi, çift tıklanan başlık için sütunun dizin numarasını ve diğer bilgileri sağlayan RowColumnEventArgs türünde bir bağımsız değişken sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Satır Başlığına Çift Tıklama**

RowDoubleClick olayı için olay işleyicisi, çift tıklanan başlık için satırın dizin numarasını ve diğer ilgili bilgileri sağlayan RowColumnEventArgs türünde bir bağımsız değişken sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Aspose.Cells.GridWeb'in Stilini veya Görünümünü Ayarlama**

Aspose.Cells.GridWeb'in kendi varsayılan görünümü ve hissi vardır ancak görünümünü değiştirmek mümkündür. Aspose.Cells.GridWeb, geliştiricilerin görünümünü tamamen kontrol etmesine izin veren çeşitli özellikler sağlar. Bu konu, bu özelliklerden bazılarını tartışmaktadır.

### **Aspose.Cells.GridWeb'in Stilini veya Görünümünü Ayarlama**

#### **Hazır Stiller**

Geliştiricilerin çabalarından tasarruf etmek için Aspose.Cells.GridWeb bazı hazır stiller sunar. Stili uygulamak için listeden bir stil seçmeniz yeterlidir.

|**stiller**|**Renk uyumu**|
|:- |:- |
|Standart|Gümüş rengi|
|Renkli1|Gül|
|Renkli2|Mavi|
|Profesyonel1|camgöbeği|
|Profesyonel2|tekrar camgöbeği|
|Geleneksel1|Karanlık|
|Geleneksel2|Gri|
|Gelenek|Özelleştirilmiş|
Belirli bir stil seçildiğinde, GridWeb kontrolünün tüm görünümünü değiştirir. Geliştiriciler, Aspose.Cells.GridWeb'in esnek API'ini kullanarak çalışma zamanında uygulanacak bir Hazır Ayar Stili seçebilir.

GridWeb denetimi, geliştiricilerin istenen herhangi bir hazır ayar stilini atayabileceği PresetStyle özelliğini sağlar.

Aşağıdaki kod parçacığının çıktısı aşağıda gösterilmiştir.

**Üzerine Colorful1 stili uygulanmış GridWeb denetimi**

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Başlık Çubuğu Stili**

GridWeb kontrolüne bakarsanız, iki başlık çubuğu göreceksiniz. Biri sütunlar (yani A, B, C, D vb.) ve diğeri satırlar (yani 1, 2, 3, 4 vb.) içindir. Aspose.Cells.GridWeb, geliştiricilerin bu başlık çubuklarının görünümünü kontrol etmesine olanak tanır. Geliştiriciler, çalışma zamanında başlık çubuklarının stilini ayarlayabilir.

{{% alert color="primary" %}}

GridWeb denetimi, denetimin her iki başlık çubuğuna da bir stil uygulayan HeaderBarStyle özelliğini sağlar.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Sekme Çubuğu Stili**

Sekme çubuğunun stilini de ayarlamak mümkündür. Lütfen aşağıdaki koda bakın

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Stil Dosyası Yükleniyor**

Varolan bir stil dosyasından GridWeb denetimine stil ayarları uygulamak için, geliştiriciler stil dosyasının yolunu kontrolün CustomStyleFileName özelliğine ayarlayabilir. Ancak, bunu yapmadan önce kontrolün PresetStyle özelliğini Özel olarak ayarlamak gerekir. Bunun nedeni, stil dosyasının bir geliştirici tarafından zaten tanımlanmış olan özel stil bilgilerini içermesidir.

Lütfen GridWeb'i kendisine uygulanan özel stille gösteren aşağıdaki resme bakın.

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

ÖNEMLİ: Stil dosyasının GridWeb kontrolüne yüklenmesi, kontrol hücrelerinin biçimlendirme ayarlarını etkilemez.

{{% /alert %}}

#### **Örnek Özel Stil Şablonu**

İşte örnek özel stil şablonu. Gereksinimlerinize göre değiştirebilirsiniz.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Bir Web Formunda Kontrol Oluşturma**

Bu makale, üzerinde GridWeb kontrolü olan basit bir web formu JSP'nin (Java Sunucu Sayfası) nasıl oluşturulacağı konusunda size rehberlik edecektir.

**Adım 1 - Dizin Yapısı Oluşturun**

 Aşağıdaki dizin yapısını oluşturmanız gerekir.**ağ uygulamaları**Tomcat Sunucusunun dizini

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_7.png)

 Bunlar, oluşturmanız gereken dizinler ve dosyalardır. Lütfen yorumları okuyun ve takip edin. En son Aspose.Cells.GridWeb for Java sürüm arşivlerini şu adresten edinebilirsiniz:[bu bağlantı](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Adım 2 - Oluşturulan Dosyalara Kod Ekleme**

Bu bölüm, yukarıdaki dizin yapısında oluşturulan çeşitli dosyaların kodunu gösterir. Lütfen bu kodları alın ve Not Defteri'nde açarak dosyalarınıza ekleyin ve kopyalayın/yapıştırın.

**Web.xml**

{{< highlight "java" >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**kafa.jsp**

{{< highlight "java" >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**3. Adım - Örnek JSP Web Sayfanızı Çalıştırma**

Şimdi her şeyi yaptın. Web sayfasını çalıştırmanın zamanı geldi. Lütfen Tomcat sunucunuzu başlatın ve ardından aşağıdaki URL'yi web tarayıcısına yapıştırın.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Aşağıdaki ekran görüntüsü gibi bir şey göreceksiniz. Tebrikler, JSP sayfanızda GridWeb kontrolünü başarıyla kullandınız.

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_8.png)

## **GridWeb'i Yazdırma**

Geliştiricilerin bir web sayfasından dahil edilen GridWeb içeriğini Microsoft Excel dosyasını kaydetmeden yazdırması gereken zamanlar vardır. Aspose.Cells.GridWeb kontrolü bu özelliği destekler.

### **GridWeb'i Yazdırma**

Ayrı bir dosya kaydetmeden yazdırmak için, ızgarayı yazdırmak üzere GridWeb sınıfının print() yöntemini istemci tarafında çağırın. Siz de uygun bir olay seçebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

İstemci tarafından aradığınız için, önce gridweb istemci kimliğini almanız gerekecek. İstemci kimliğini gridweb.getClientID() yöntemini kullanarak alabilirsiniz.

### **İstemci Tarafı Örnek Kodu**

Lütfen istemci tarafından gridweb.print() yöntemini çağıran aşağıdaki bağlantıya bakın.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Farklı Izgara Modlarına Giriş**

Bu makale Aspose.Cells.GridWeb'in farklı modlarını açıklamaktadır. Bu modlar, farklı özellikleri ve davranışları nedeniyle mantıksal olarak farklılaşır. Farklı mod türlerini şu şekilde tanımladık:

- Düzenleme modu
- Görünüm Modu

Bu modların hepsinin kendine has özellikleri vardır. Geliştiriciler Aspose.Cells.GridWeb ile gereksinimlerine göre her modda çalışabilirler. Aşağıda her bir moda bakacağız.

### **Düzenleme modu**

Aspose.Cells.GridWeb denetimi varsayılan olarak Düzenleme modundadır. Düzenleme modunda, Aspose.Cells.GridWeb kontrolü tarafından sunulan tüm özellikleri kullanarak ızgara içeriğini tamamen düzenleyebilir veya değiştirebilirsiniz. Bu özellikler şunları içerir:

- Izgara içeriği Microsoft Excel dosyalarına kaydediliyor.
- Verileri bir sunucuya gönderme.
- Hesaplama formülleri.
- Önceki eylemleri geri alma veya silme.
- Satırları ve sütunları yönetme.
- Verileri kesme, kopyalama veya yapıştırma.
- Hücreleri biçimlendirme vb.

**Düzenleme Modunda GridWeb kontrolü**

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_9.png)

Geliştiriciler ayrıca GridWeb denetiminin EditMode özelliğini true olarak ayarlayarak program aracılığıyla Düzenleme moduna geçebilirler.

### **Kod Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Görünüm Modu**

GridWeb denetimi Görünüm modundayken, kullanıcılar ızgara içeriğini düzenleyemez veya değiştiremez; bu, kullanıcıların yalnızca ızgara içeriğini görüntüleyebileceği anlamına gelir. Bu yüzden bu moda Görünüm modu denir. Görünüm modunda, birkaç düğme (**Göndermek**, **Kayıt etmek** ve**Geri alma** ) gizlenir ve sağ tıklandığında görünen menü yalnızca**kopyala** ve**Bulmak** seçenek.

**Görüntüleme Modunda GridWeb kontrolü** 

![yapılacaklar:resim_alternatif_metin](working-with-gridweb_10.png)

 Geliştiriciler, kullanıcılarının yalnızca verileri görüntülemesini istiyorsa, GridWeb kontrolünün EditMode özelliğini olarak ayarlayarak programlı olarak Görünüm moduna geçebilirler.**YANLIŞ**.

### **Kod Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Görünüm modunda bile, kullanıcılar satırların ve sütunların yüksekliğini ve genişliğini değiştirebilir.

{{% /alert %}}
