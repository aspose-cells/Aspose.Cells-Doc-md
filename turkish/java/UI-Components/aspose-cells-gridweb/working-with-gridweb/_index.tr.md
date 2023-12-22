---
title: GridWeb'le Çalışmak
type: docs
weight: 20
url: /tr/java/working-with-gridweb/
---
##  **Microsoft Excel Dosyasını Açma**

Aspose.Cells.GridWeb kontrolü Microsoft Excel dosyalarını açabilir ve yükleyebilir - veriler, biçimlendirme, grafikler, resimler vb. ile birlikte. Bu konu bunun nasıl yapılacağını açıklamaktadır.

GridWeb kontrolünü kullanarak bir Excel dosyasını açmak için:

1. Aspose.Cells.GridWeb denetimini bir web formuna veya sayfasına ekleyin.
1. Dosya yolunu belirterek Excel dosyasını içe aktarın.
1. Uygulamayı çalıştırın veya sayfayı açın.

İçeriği bir Excel dosyasından Aspose.Cells.GridWeb kontrolüne yüklemek için, Excel dosyasının yolunu belirtmek üzere importExcelFile yöntemini çağırmanız gerekir. Bundan sonra, GridWeb kontrolü belirtilen yoldan dosyayı otomatik olarak bulacak ve içeriğini içinde gösterecektir. Aşağıda bir Excel dosyasının içeriğini yükleyen bir kod pasajı verilmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Yukarıdaki kod parçasını istediğiniz şekilde kullanabilirsiniz. Örneğin bir web formu yüklendiğinde Excel dosyasının otomatik olarak yüklenmesi için bu kodu formun kendi belirlediğiniz Page_Load olayına ekleyin.

**GridWeb'e bir Excel dosyası yüklenir**

![yapılacak şey:image_alt_text](working-with-gridweb_1.png)

##  **Microsoft Excel Dosyasını Kaydetme**

Aspose.Cells.GridWeb kontrolünü kullanarak GUI modundaki web sitelerinde yeni Microsoft Excel dosyaları oluşturmak veya mevcut Microsoft Excel dosyalarını değiştirmek mümkündür. Dosyalar daha sonra Excel dosyalarına kaydedilebilir. Aspose.Cells.GridWeb etkili bir çevrimiçi elektronik tablo düzenleyicisi olarak hizmet eder. Bu konu, ızgara içeriğinin Excel dosyalarına nasıl kaydedileceğini açıklamaktadır.

###  **Dosya Olarak Kaydetme**

Aspose.Cells.GridWeb kontrolünün içeriğini Excel dosyası olarak kaydetmek için:

1. Aspose.Cells.GridWeb denetimini bir web formuna veya sayfasına ekleyin.
1. Çalışmanızı belirtilen yola Excel dosyası olarak kaydedin.
1. Uygulamayı çalıştırın veya sayfayı açın.

Aşağıdaki kod örneği, ızgara içeriğinin bir Excel dosyasına nasıl kaydedileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Yukarıdaki kod parçacığı çeşitli şekillerde kullanılabilir. Yaygın bir yol, tıklandığında ızgara içeriğini bir Excel dosyasına kaydeden bir düğme eklemektir. Aspose.Cells.GridWeb bu görev için daha kolay bir yaklaşım sunuyor. Aspose.Cells.GridWeb'in SaveCommand adında bir etkinliği var. Yukarıdaki kod parçacığı, SaveCommand olayının olay işleyicisine eklenebilir; bu, kullanıcıların Aspose.Cells.GridWeb'in yerleşik kodunu tıklatarak çalışmalarını kaydetmelerine olanak tanır.**Kaydetmek** düğme.

##  **Aspose.Cells.GridWeb ve Başlık Çubuğunun yeniden boyutlandırılması**

Bu makalede, Aspose.Cells.GridWeb API kullanılarak çalışma zamanında GridWeb'in yeniden boyutlandırılmasının nasıl yapılacağı açıklanmaktadır. Ayrıca, verilerinin okunmasını kolaylaştırmak için Aspose.Cells.GridWeb denetiminin başlık çubuklarının nasıl yeniden boyutlandırılacağı da açıklanmaktadır.

###  **Aspose.Cells.GridWeb'in Genişliğini ve Yüksekliğini Değiştirme**

Aspose.Cells.GridWeb kontrolünün genişliğini ve yüksekliğini değiştirmek basit ama önemli bir özelliktir. Aspose.Cells.GridWeb denetimi, API içindeki GridWeb sınıfı tarafından temsil edilir. GridWeb denetiminin genişliğini ve yüksekliğini yeniden boyutlandırmak için genişlik ve yükseklik özelliklerini kullanmanız yeterlidir.

{{% alert color="primary" %}}

Kontrolün genişliği ve yüksekliği piksel veya nokta cinsinden tanımlanabilir.

{{% /alert %}}

Aşağıdaki kod parçacığının çıktısı aşağıda gösterilmiştir.

**GridWeb kontrolünün genişliği ve yüksekliği değiştirildi**

![yapılacak şey:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

###  **Başlık Çubuğunun Genişliğini ve Yüksekliğini Değiştirme**

Aspose.Cells.GridWeb denetimi aşağıdaki gibi iki başlık çubuğu içerir:

- Üst başlık çubuğu, bu başlık çubuğu A, B, C, D vb. sütunları temsil eder.
- Sol başlık çubuğu, bu başlık çubuğu 1, 2, 3, 4 vb. satırları temsil eder.

Bu başlık çubuklarının her ikisi de aşağıda gösterilmiştir.

**Başlık çubukları**

![yapılacak şey:image_alt_text](working-with-gridweb_3.png)

GridWeb denetiminin HeaderBarHeight ve HeaderBarWidth özelliklerini sırasıyla kullanarak üst başlık çubuğunun yüksekliğini ve sol başlık çubuğunun genişliğini değiştirin. Aşağıdaki şekil aşağıdaki kod örneğinin çıktısını göstermektedir.

**Başlık çubuğu genişliği ve yüksekliği değiştirildi**

![yapılacak şey:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

##  **Aspose.Cells.GridWeb Events ile çalışma**

Tüm geliştiricilerin olaylara ve amaçlarına aşina olması gerekir. Olaylar, bir kontrolde veya sınıfta meydana gelebilecek değişikliklerin bildirimlerini göndermek için kullanılır. Aspose.Cells.GridWeb, denetimde belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılabilecek çeşitli olaylara sahiptir.

Bu konu, Aspose.Cells.GridWeb denetimi tarafından desteklenen tüm olaylara bir giriş ve bu olayların nasıl ele alınacağına ilişkin bazı ayrıntılar sağlar.

###  **Grid Olaylarına Giriş**

Aspose.Cells.GridWeb kontrolü, kontrolde belirli olaylar tetiklendiğinde işlemleri gerçekleştirmek için daha fazla kontrol sağlayan çeşitli olayları destekler. Aspose.Cells.GridWeb kontrolü tarafından desteklenen olayların tam listesini aşağıda bulabilirsiniz.

|**Olaylar**|**Tanım**|
| :- | :- |
|Hücre Komutu|Bir hücrenin komut köprüsüne tıklandığında gerçekleşir. Bu olay başlatıldığında, e.Argument parametresi komutun adını sağlar.|
|HücreDoubleClick|Hücreye çift tıklandığında gerçekleşir.|
|SütunSilindi|Kullanıcı, istemci tarafı menüsünü kullanarak çalışma sayfasındaki bir sütunu sildiğinde gerçekleşir.|
|SütunSilme|Kullanıcı, istemci tarafı menüsünü kullanarak çalışma sayfasından bir sütunu silmeye çalıştığında gerçekleşir.|
|SütunÇift Tıklama|Sütun başlığına çift tıklandığında gerçekleşir.|
|Sütun Eklendi|Kullanıcı, istemci tarafı menüsünü kullanarak çalışma sayfasına bir sütun eklediğinde gerçekleşir.|
|Özel Komut|Kullanıcı özel bir komut düğmesini tıklattığında gerçekleşir.|
|ÖzelVerileri Yükle|Denetimin EnableSession özelliği false olarak ayarlandığında ve çalışma sayfası verilerinin yüklenmesi gerektiğinde gerçekleşir. Bir dosyadan veya veritabanından çalışma sayfası verilerini yüklemek için bu olayı oturumsuz modda işleyebilirsiniz.|
|PageIndexDeğiştirildi|Denetimin sayfa sayfası dizini değiştirildiğinde gerçekleşir.|
|Satır Silindi|Kullanıcı, istemci tarafındaki menüyü kullanarak çalışma sayfasından bir satırı sildiğinde gerçekleşir.|
|Satır Silme|Kullanıcı, istemci tarafı menüsünü kullanarak çalışma sayfasındaki bir satırı silmeye çalıştığında gerçekleşir.|
|SatırDoubleClick|Satır başlığına çift tıklandığında gerçekleşir.|
|Satır Eklendi|Kullanıcı, istemci tarafındaki menüyü kullanarak çalışma sayfasına bir satır eklediğinde gerçekleşir.|
|KaydetKomut| Ne zaman oluşur**Kaydetmek** butonuna tıklanır.|
|SheetTabClick|Bir sayfa sekmesi tıklatıldığında gerçekleşir.|
|Komutu Gönder| Ne zaman oluşur**Göndermek** butonuna tıklanır.|
|Komutu Geri Al| Ne zaman oluşur**Geri alma** butonuna tıklanır.|
|AjaxÇağrıBitti|Denetimin AJAX güncellemesi tamamlandığında tetiklenir. (EnableAJAX true olarak ayarlanacaktır).|
|CellModifiedOnAjax|AJAX çağrısında hücre değiştirildiğinde tetiklenir.|
|Sütun Sonrası Filtresi|Filtre bir sütuna uygulandığında tetiklenir.|

###  **Izgara Olaylarını Yönetme**

Belirli bir olayı tetikleyerek belirli bir işlemi gerçekleştirmek için bir olay işleyicisi oluşturmamız gerekir. Bir olay işleyicisi, belirli bir olay tetiklendiğinde istenen görevi gerçekleştirir. Aşağıdaki örnekte basit bir grid olayının nasıl ele alınacağı gösterilmektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

##  **Çift Tıklama Olaylarıyla Çalışmak**

Aspose.Cells.GridWeb üç tür çift tıklama olayı içerir:

- CellDoubleClick, bir hücreye çift tıklandığında tetiklenir.
- ColumnDoubleClick, bir sütun başlığı çift tıklandığında tetiklenir.
- RowDoubleClick, bir satır başlığına çift tıklandığında tetiklenir.

Bu konu, Aspose.Cells.GridWeb'de çift tıklama olaylarının nasıl etkinleştirileceğini açıklamaktadır. Ayrıca bu olaylar için olay işleyicilerinin oluşturulması da tartışılmaktadır.

###  **Çift Tıklama Olaylarını Etkinleştirme**

Tüm çift tıklama olayı türleri, GridWeb denetiminin EnableDoubleClickEvent özelliği true olarak ayarlanarak istemci tarafında etkinleştirilebilir.

{{% alert color="primary" %}}

Varsayılan olarak EnableDoubleClickEvent özelliği false olarak ayarlanmıştır. Bu, çift tıklama olaylarının varsayılan olarak etkin olmadığı anlamına gelir. Bu tür etkinlikleri uygulamak için öncelikle özelliği etkinleştirin.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Çift tıklama olayları etkinleştirildiğinde, herhangi bir çift tıklama olayı için olay işleyicileri oluşturmak mümkündür. Bu olay işleyicileri, belirli bir çift tıklama olayı başlatıldığında belirli görevleri gerçekleştirir.

###  **Çift Tıklama Olaylarını Yönetme**

####  **Çift Tıklayın Cell**

CellDoubleClick olayının olay işleyicisi, çift tıklanan hücrenin tüm bilgilerini sağlayan CellEventArgs türünde bir bağımsız değişken sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

####  **Sütun Başlığına Çift Tıklayın**

ColumnDoubleClick olayının olay işleyicisi, çift tıklanan başlığa ilişkin sütunun dizin numarasını ve diğer bilgileri sağlayan RowColumnEventArgs türünde bir bağımsız değişken sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

####  **Satır Başlığına Çift Tıklayın**

RowDoubleClick olayının olay işleyicisi, çift tıklanan başlığa ilişkin satırın dizin numarasını ve diğer ilgili bilgileri sağlayan RowColumnEventArgs türünde bir bağımsız değişken sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

##  **Aspose.Cells.GridWeb'in Stilini veya Görünümünü Ayarlama**

Aspose.Cells.GridWeb'in kendi varsayılan görünümü ve hissi vardır ancak görünümünü değiştirmek mümkündür. Aspose.Cells.GridWeb, geliştiricilerin görünümünü tamamen kontrol etmesine olanak tanıyan çeşitli özellikler sağlar. Bu konuda bu özelliklerden bazıları anlatılmaktadır.

###  **Aspose.Cells.GridWeb'in Stilini veya Görünümünü Ayarlama**

####  **Önceden Ayarlanmış Stiller**

Geliştiricilerin çabalarından tasarruf etmek için Aspose.Cells.GridWeb bazı önceden ayarlanmış stiller sunar. Stili uygulamak için listeden bir stil seçmeniz yeterlidir.

|**Stiller**|**Renk uyumu**|
| :- | :- |
|Standart|Gümüş|
|Renkli1|Gül|
|Renkli2|Mavi|
|Profesyonel1|Camgöbeği|
|Profesyonel2|Yine camgöbeği|
|Geleneksel1|Karanlık|
|Geleneksel2|Gri|
|Gelenek|Özelleştirilmiş|
Belirli bir stil seçildiğinde GridWeb denetiminin tüm görünümü değişir. Geliştiriciler, Aspose.Cells.GridWeb'in esnek API'ini kullanarak çalışma zamanında uygulanacak bir Ön Ayar Stili seçebilir.

GridWeb kontrolü, geliştiricilerin istenen herhangi bir ön ayar stilini atayabilecekleri PresetStyle özelliğini sağlar.

Aşağıdaki kod parçacığının çıktısı aşağıda gösterilmiştir.

**Üzerinde Renkli1 stilinin uygulandığı GridWeb kontrolü**

![yapılacak şey:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **Başlık Çubuğu Stili**

GridWeb kontrolüne bakarsanız iki başlık çubuğu göreceksiniz. Biri sütunlar için (yani A, B, C, D vb.) ve diğeri satırlar için (yani 1, 2, 3, 4 vb.). Aspose.Cells.GridWeb, geliştiricilerin bu başlık çubuklarının görünümünü kontrol etmesine olanak tanır. Geliştiriciler çalışma zamanında başlık çubuklarının stilini ayarlayabilir.

{{% alert color="primary" %}}

GridWeb denetimi, denetimin her iki başlık çubuğuna da stil uygulayan HeaderBarStyle özelliğini sağlar.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

####  **Sekme Çubuğu Stili**

Sekme çubuğunun stilini de ayarlamak mümkündür. Lütfen aşağıdaki koda bakın

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

####  **Stil Dosyası Yükleniyor**

Stil ayarlarını mevcut bir stil dosyasından GridWeb kontrolüne uygulamak için geliştiriciler, stil dosyasının yolunu kontrolün CustomStyleFileName özelliğine ayarlayabilir. Ancak bunu yapmadan önce kontrolün PresetStyle özelliğini Custom olarak ayarlamak gerekir. Bunun nedeni, stil dosyasının geliştirici tarafından önceden tanımlanmış özel stil bilgilerini içermesidir.

Lütfen GridWeb'i kendisine uygulanan özel stille gösteren aşağıdaki resme bakın.

![yapılacak şey:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

ÖNEMLİ: Stil dosyasının GridWeb kontrolüne yüklenmesi, kontrol hücrelerinin formatlama ayarlarını etkilemez.

{{% /alert %}}

####  **Örnek Özel Stil Şablonu**

Örnek özel stil şablonunu burada bulabilirsiniz. Gereksinimlerinize göre değiştirebilirsiniz.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

##  **Web Formunda Denetim Oluşturma**

Bu makale, GridWeb kontrolüne sahip basit bir web formu JSP'nin (Java Sunucu Sayfası) nasıl oluşturulacağı konusunda size rehberlik edecektir.

**Adım 1 - Dizin Yapısı Oluşturun**

 Aşağıdaki dizin yapısını oluşturmanız gerekir.**ağ uygulamaları**Tomcat Sunucusunun dizini

![yapılacak şey:image_alt_text](working-with-gridweb_7.png)

 Bunlar oluşturmanız gereken dizinler ve dosyalardır. Lütfen yorumları okuyun ve takip edin. En son Aspose.Cells.GridWeb for Java sürüm arşivlerini şu adresten alabilirsiniz:[bu bağlantı](https://downloads.aspose.com/cells/java).

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

Bu bölüm yukarıdaki dizin yapısında oluşturulan çeşitli dosyaların kodunu gösterir. Lütfen bu kodları alın ve Not Defteri'nde açarak dosyalarınıza ekleyin ve kopyalayıp yapıştırın.

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

**head.jsp**

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

**Adım 3 - Örnek JSP Web Sayfanızı Çalıştırma**

Artık her şeyi yaptınız. Web sayfasını çalıştırmanın zamanı geldi. Lütfen Tomcat sunucunuzu başlatın ve ardından aşağıdaki URL'yi web tarayıcınıza yapıştırın.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Aşağıdaki ekran görüntüsüne benzer bir şey göreceksiniz. Tebrikler, JSP sayfanızda GridWeb kontrolünü başarıyla kullandınız.

![yapılacak şey:image_alt_text](working-with-gridweb_8.png)

##  **GridWeb'i Yazdırma**

Geliştiricilerin bir web sayfasındaki GridWeb içeriğini Microsoft Excel dosyasını kaydetmeden yazdırmaları gerektiği zamanlar vardır. Aspose.Cells.GridWeb denetimi bu özelliği destekler.

###  **GridWeb'i Yazdırma**

Ayrı bir dosyayı kaydetmeden yazdırmak için, ızgarayı yazdırmak üzere istemci tarafında GridWeb sınıfının print() yöntemini çağırın. Siz de uygun bir etkinlik seçebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

İstemci tarafından aradığınız için öncelikle gridweb istemci kimliğini almanız gerekecektir. Gridweb.getClientID() yöntemini kullanarak istemci kimliğini alabilirsiniz.

###  **İstemci Tarafı Örnek Kodu**

Lütfen istemci tarafından gridweb.print() yöntemini çağıran aşağıdaki bağlantıya bakın.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

##  **Farklı Izgara Modlarına Giriş**

Bu makalede Aspose.Cells.GridWeb'in farklı modları açıklanmaktadır. Bu modlar, farklı özellikleri ve davranışları nedeniyle mantıksal olarak farklılaşmaktadır. Farklı mod türlerini şu şekilde tanımladık:

- Düzenleme modu
- Görünüm Modu

Bu modların hepsinin kendine has özellikleri vardır. Geliştiriciler Aspose.Cells.GridWeb ile ihtiyaçları doğrultusunda diledikleri modda çalışabilirler. Aşağıda her moda bakacağız.

###  **Düzenleme modu**

Varsayılan olarak Aspose.Cells.GridWeb denetimi Düzenleme modundadır. Düzenleme modunda, Aspose.Cells.GridWeb denetiminin sunduğu tüm özellikleri kullanarak ızgara içeriğini tamamen düzenleyebilir veya değiştirebilirsiniz. Bu özellikler şunları içerir:

- Izgara içeriğini Microsoft Excel dosyalarına kaydetme.
- Verilerin bir sunucuya gönderilmesi.
- Formüllerin hesaplanması.
- Önceki eylemleri geri alma veya atma.
- Satırları ve sütunları yönetme.
- Verileri kesme, kopyalama veya yapıştırma.
- Hücreleri biçimlendirme vb.

**Düzenleme Modunda GridWeb kontrolü**

![yapılacak şey:image_alt_text](working-with-gridweb_9.png)

Geliştiriciler ayrıca GridWeb denetiminin EditMode özelliğini true olarak ayarlayarak program aracılığıyla Düzenleme moduna geçebilirler.

###  **Kod Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

###  **Görünüm Modu**

GridWeb kontrolü Görünüm modundayken kullanıcılar ızgara içeriğini düzenleyemez veya değiştiremez; bu, kullanıcıların yalnızca ızgara içeriğini görüntüleyebileceği anlamına gelir. Bu nedenle bu moda Görünüm modu adı verilir. Görünüm modunda birkaç düğme (**Gönder**,**Kaydetmek** Ve**Geri al**) gizlidir ve sağ tıklandığında görünen menü yalnızca **Kopyala seçeneğini içerir.** Ve**Bulmak** seçenek.

**Görünüm Modunda GridWeb kontrolü** 

![yapılacak şey:image_alt_text](working-with-gridweb_10.png)

Geliştiriciler kullanıcılarının yalnızca verileri görüntülemesini isterse, GridWeb denetiminin EditMode özelliğini *false** olarak ayarlayarak programlı olarak Görünüm moduna geçebilirler.

###  **Kod Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Görünüm modunda bile kullanıcılar satır ve sütunların yüksekliğini ve genişliğini değiştirebilir.

{{% /alert %}}
