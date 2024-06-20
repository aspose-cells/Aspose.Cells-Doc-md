---
title: GridWeb ile Çalışmak
type: docs
weight: 20
url: /tr/java/working-with-gridweb/
---

## **Bir Microsoft Excel Dosyasını Açma**

Aspose.Cells.GridWeb denetimi, Microsoft Excel dosyalarını - veri, biçimlendirme, grafikler, resimler vb. ile birlikte - açabilir ve yükleyebilir. Bu konu nasıl açıklar.

GridWeb denetimini kullanarak bir Excel dosyasını açmak için:

1. Aspose.Cells.GridWeb denetimini bir web formuna veya sayfaya ekleyin.
1. Dosya yolunu belirterek Excel dosyasını içe aktarın.
1. Uygulamayı çalıştırın veya sayfayı açın.

Bir Excel dosyasından içeriği Aspose.Cells.GridWeb denetimine yüklemek için, belirtilen Excel dosyasının yolunu belirtmek için importExcelFile yöntemini çağırmanız gerekir. Bundan sonra, GridWeb denetimi otomatik olarak belirtilen dosya'yı bulacak ve içeriğini içinde gösterecektir. Bir Excel dosyasının içeriğini yükleyen bir kod parçası aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Yukarıdaki kod parçası istediğiniz gibi kullanılabilir. Örneğin, bir web formu yüklendiğinde otomatik olarak bir Excel dosyasını yüklemek için bu kodu kendiniz tarafından belirtilen formun Page_Load olayına ekleyin.

**Bir Excel dosyası GridWeb'e yüklenir**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Bir Microsoft Excel Dosyasını Kaydetme**

Aspose.Cells.GridWeb denetimini kullanarak web sitelerinde GUI modunda yeni oluşturulabilir veya mevcut Microsoft Excel dosyalarını değiştirebilir ve bunları Excel dosyalarına kaydedebilirsiniz. Aspose.Cells.GridWeb etkili bir çevrimiçi elektronik tablo düzenleyici olarak hizmet verir. Bu konu, grid içeriğini Excel dosyalarına kaydetmeyi nasıl açıklar.

### **Dosya Olarak Kaydetme**

Aspose.Cells.GridWeb denetiminin içeriğini Excel dosyası olarak kaydetmek için:

1. Aspose.Cells.GridWeb denetimini bir web formuna veya sayfaya ekleyin.
1. Çalışmanızı belirtilen bir yola Excel dosyası olarak kaydedin.
1. Uygulamayı çalıştırın veya sayfayı açın.

Aşağıdaki kod örneği, grid içeriğini bir Excel dosyasına kaydetmenin nasıl yapıldığını açıklar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

Yukarıdaki kod parçası çeşitli şekillerde kullanılabilir. Bir düğmeye tıklandığında grid içeriğini bir Excel dosyasına kaydeden bir düğme eklemek yaygın bir yoldur. Aspose.Cells.GridWeb, görev için daha kolay bir yaklaşım sunar. Aspose.Cells.GridWeb'in **Kaydet** düğmesine tıklayarak kullanıcıların çalışmalarını kaydetmelerine izin veren SaveCommand adlı bir olayı vardır. Yukarıdaki kod parçası, bu olayın olay işleyicisine eklenebilir.

## **Aspose.Cells.GridWeb ve Başlık Çubuğunu Yeniden Boyutlandırma**

Bu makale, Aspose.Cells.GridWeb API'sını kullanarak GridWeb'i çalışma zamanında nasıl yeniden boyutlandıracağını açıklar. Ayrıca Aspose.Cells.GridWeb denetiminin başlık çubuklarını yeniden boyutlandırarak verilerini okumayı daha kolay hale getirmeyi açıklar.

### **Aspose.Cells.GridWeb'in Genişliği ve Yüksekliği Değiştirme**

Aspose.Cells.GridWeb kontrolünün genişliğini ve yüksekliğini değiştirmek basit ancak önemli bir özelliktir. Aspose.Cells.GridWeb kontrolü, API'de GridWeb sınıfı tarafından temsil edilir. GridWeb kontrolünün genişliğini ve yüksekliğini yeniden boyutlandırmak için sadece genişlik ve yükseklik özelliklerini kullanın.

{{% alert color="primary" %}}

Denetimin genişliği ve yüksekliği piksel veya noktalarda tanımlanabilir.

{{% /alert %}}

Aşağıdaki kod parçasının çıktısı aşağıda gösterilmiştir.

**GridWeb kontrolünün genişliği ve yüksekliği değiştirildi**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Başlık Çubuğunun Genişliği ve Yüksekliğini Değiştirme**

Aspose.Cells.GridWeb kontrolü şu şekilde iki başlık çubuğu içerir:

- Üst başlık çubuğu, bu başlık çubuğu sütunları A, B, C, D, vb. olarak temsil eder.
- Sol başlık çubuğu, bu başlık çubuğu satırları 1, 2, 3, 4, vb. olarak temsil eder.

Bu başlık çubukları aşağıda gösterilmiştir.

**Başlık çubukları**

![todo:image_alt_text](working-with-gridweb_3.png)

GridWeb kontrolünün HeaderBarHeight ve HeaderBarWidth özelliklerini kullanarak üst başlık çubuğunun yüksekliğini ve sol başlık çubuğunun genişliğini değiştirin. Aşağıdaki şekil, aşağıdaki kod örneğinin çıktısını göstermektedir.

**Değiştirilmiş başlık çubuğu genişliği ve yüksekliği**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Aspose.Cells.GridWeb Olaylarıyla Çalışma**

Tüm geliştiriciler olayları ve amaçlarını bilmesi gerekir. Olaylar, bir kontrol veya sınıfta meydana gelebilecek değişiklikler hakkında bildirim göndermek için kullanılır. Aspose.Cells.GridWeb'in, kontrolde belirli değişiklikler meydana geldiğinde belirli görevleri gerçekleştirmek için kullanılabilecek birkaç olayı bulunmaktadır.

Bu konu, Aspose.Cells.GridWeb kontrolü tarafından desteklenen tüm olaylara giriş yapar ve bu olayları nasıl ele alacağınıza dair bazı detaylar içerir.

### **Olaylara Giriş**

Aspose.Cells.GridWeb kontrolü, kontrolde belirli olaylar tetiklendiğinde belirli işlemleri gerçekleştirmek için daha fazla kontrol sağlayan birkaç olayı destekler. Aspose.Cells.GridWeb kontrolü tarafından desteklenen olayların tam listesi aşağıda bulunabilir.

|**Olaylar**|**Açıklama**|
| :- | :- |
|CellCommand|Hücrenin komut linkine tıklandığında oluşur. Bu olay tetiklendiğinde, parametre e.Argument komutun adını verir.|
|CellDoubleClick|Hücre çift tıklandığında oluşur.|
|ColumnDeleted|Kullanıcı bir sütunu istemci tarafı menüsünü kullanarak sildiğinde oluşur.|
|ColumnDeleting|Kullanıcı, istemci tarafı menüsünü kullanarak bir sütunu silmeye çalıştığında oluşur.|
|ColumnDoubleClick|Sütun başlığı çift tıklandığında oluşur.|
|ColumnInserted|Kullanıcı bir sütun eklemeye çalıştığında istemci tarafı menüsünde oluşur.|
|CustomCommand|Kullanıcı özel komut düğmesine tıkladığında oluşur.|
|LoadCustomData|Kontrolün EnableSession özelliği false olarak ayarlandığında ve çalışma sayfası verilerini yüklemesi gerektiğinde oluşur. Bu olayı oturumsuz modda çalışma sayfası verilerini bir dosyadan veya veritabanından yüklemek için kullanabilirsiniz.|
|PageIndexChanged|Kontrolün sayfa dizini değiştiğinde oluşur.|
|RowDeleted|Kullanıcı, istemci tarafı menüsünü kullanarak bir satırı sildiğinde oluşur.|
|RowDeleting|Kullanıcı, istemci tarafı menüsünü kullanarak bir satırı silmeye çalıştığında oluşur.|
|RowDoubleClick|Satır başlığı çift tıklandığında oluşur.|
|RowInserted|Kullanıcı, istemci tarafı menüsünü kullanarak çalışma sayfasına bir satır eklediğinde meydana gelir.
|SaveCommand|**Kaydet** düğmesine tıklandığında meydana gelir.
|SheetTabClick|Bir sayfa sekmesine tıklandığında meydana gelir.
|SubmitCommand|**Gönder** düğmesine tıklandığında meydana gelir.
|UndoCommand|**Geri Al** düğmesine tıklandığında meydana gelir.
|AjaxCallFinished|Kontrolün AJAX güncellemesi tamamlandığında meydana gelir. (EnableAJAX özelliği true olarak ayarlanmalıdır).
|CellModifiedOnAjax|Hücre AJAX çağrısı sırasında değiştirildiğinde meydana gelir.
|AfterColumnFilter|Bir sütuna filtre uygulandığında meydana gelir.

### **Grid Olaylarını İşleme**

Belirli bir olayın tetiklenmesi durumunda belirli bir işlemi gerçekleştirmek için bir olay işleyici oluşturmalıyız. Bir olay işleyicisi, belirli bir olay tetiklendiğinde istenen görevi gerçekleştirir. Aşağıdaki örnek, basit bir kılavuz olayının nasıl işleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Çift Tıklama Olaylarıyla Çalışmak**

Aspose.Cells.GridWeb, üç tür çift tıklama olayı içerir:

- CellDoubleClick, bir hücre çift tıklandığında tetiklenir.
- ColumnDoubleClick, bir sütun başlığı çift tıklandığında tetiklenir.
- RowDoubleClick, bir satır başlığı çift tıklandığında tetiklenir.

Bu konu, Aspose.Cells.GridWeb'de çift tıklama olaylarını etkinleştirmeyi ve bu olaylar için olay işleyicileri oluşturmayı tartışmaktadır.

### **Çift Tıklama Olaylarını Etkinleştirme**

Tüm çift tıklama olayları, GridWeb kontrolünün EnableDoubleClickEvent özelliğinin true olarak ayarlanmasıyla istemci tarafında etkinleştirilebilir.

{{% alert color="primary" %}}

EnableDoubleClickEvent özelliği varsayılan olarak false olarak ayarlanmıştır. Bu, çift tıklama olaylarının varsayılan olarak etkin olmadığı anlamına gelir. Bu tür olayları uygulamak için önce özelliği etkinleştirmeniz gerekir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Çift tıklama olayları etkinleştirildiğinde, herhangi bir çift tıklama olayı için olay işleyicileri oluşturmak mümkündür. Bu olay işleyicileri, belirli bir çift tıklama olayı tetiklendiğinde belirli görevleri gerçekleştirir.

### **Çift Tıklama Olaylarını Ele Almak**

#### **Hücreyi Çift Tıklama**

CellDoubleClick olay işleyicisi, çift tıklanan hücre ile ilgili tam bilgiyi sağlayan CellEventArgs türünden bir argüman sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Sütun Başlığını Çift Tıklama**

ColumnDoubleClick olay işleyicisi, çift tıklanan başlık için sütunun indeks numarasını ve diğer bilgileri sağlayan RowColumnEventArgs türünden bir argüman sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Satır Başlığını Çift Tıklama**

RowDoubleClick olay işleyicisi, çift tıklanan başlık için satırın indeks numarasını ve diğer ilgili bilgileri sağlayan RowColumnEventArgs türünden bir argüman sağlar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Aspose.Cells.GridWeb Stilini veya Görünümünü Ayarlama**

Aspose.Cells.GridWeb'ın kendi varsayılan görünümü vardır, ancak görünümünü değiştirme imkanı vardır. Aspose.Cells.GridWeb, geliştiricilerin tam kontrolü sağlamak için çeşitli özellikler sunar. Bu konu, bu özelliklerden bazılarını tartışmaktadır.

### **Aspose.Cells.GridWeb Stilini veya Görünümünü Ayarlama**

#### **Hazır Stiller**

Geliştiricilerin çabalarını kaydetmek için, Aspose.Cells.GridWeb bazı hazır stiller sunar. Basitçe bir stil seçin ve uygulamak için listeden bir stil seçin.

|**Stilller**|**Renk Düzeni**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Belirli bir stil seçildiğinde, GridWeb denetiminin tüm görünümünü değiştirir. Geliştiriciler, Aspose.Cells.GridWeb'in esnek API'sini kullanarak çalışma zamanında bir Önceden Tanımlanmış Stil seçebilir.

GridWeb denetimi geliştiricilerin istedikleri önceden belirlenmiş stili atayabileceği PresetStyle özelliğini sağlar.

Aşağıdaki kod parçasının çıktısı aşağıda gösterilmiştir.

**Renkli1 stili uygulanmış GridWeb denetimi**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Başlık Çubuğu Stili**

GridWeb denetimine bakarsanız, iki başlık çubuğu fark edeceksiniz. Birisi sütunlar için (yani A, B, C, D, vs.) ve diğeri satırlar için (yani 1, 2, 3, 4, vs.). Aspose.Cells.GridWeb, geliştiricilere bu başlık çubuklarının görünümünü kontrol etme olanağı sağlar. Geliştiriciler, başlık çubuklarının stilini çalışma zamanında ayarlayabilirler.

{{% alert color="primary" %}}

GridWeb denetimi, kontrolün her iki başlık çubuğuna da bir stil uygulayan HeaderBarStyle özelliğini sağlar.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Sekme Çubuğu Stili**

Sekme çubuğunun stili de ayarlanabilir. Lütfen aşağıdaki kodu görün.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Stil Dosyası Yükleme**

Geliştiriciler, GridWeb denetimine mevcut bir stil dosyasından stil ayarlarını uygulamak için kontrolün CustomStyleFileName özelliğine stil dosyasının yolunu belirleyebilir. Ancak bunu yapmadan önce kontrolün PresetStyle özelliğini Custom olarak ayarlamak zorunludur. Bu, stil dosyasının zaten bir geliştirici tarafından tanımlanan özel stil bilgilerini içerdiği içindir.

Lütfen aşağıdaki resme bakınız, bu resim GridWeb'e özel olarak uygulanan stilin GridWeb'i göstermektedir.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

ÖNEMLİ: Stil dosyasını GridWeb denetine yüklemek, denetimin hücrelerinin biçimlendirme ayarlarını etkilemez.

{{% /alert %}}

#### **Örnek Özel Stil Şablonu**

İşte örnek özel stil şablonu. Gereksinimlerinize göre değiştirebilirsiniz.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Web Formu Üzerinde Kontrol Oluşturma**

Bu makale, üzerinde GridWeb denetimi bulunan bir JSP (Java Sunucusu Sayfası) içeren basit bir web formu oluşturmanıza rehberlik edecektir.

**Adım 1 - Dizin Yapısı Oluşturma**

Tomcat Sunucusunun **webapps** dizininde aşağıdaki dizin yapısını oluşturmanız gerekmektedir.

![todo:image_alt_text](working-with-gridweb_7.png)

Oluşturmanız gereken dizinler ve dosyalar bunlardır. Lütfen yorumları okuyun ve onları takip edin. En son Aspose.Cells.GridWeb for Java sürüm arşivlerini [bu bağlantıdan](https://downloads.aspose.com/cells/java) alabilirsiniz.

{{< highlight java >}}

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

**Adım 2 - Oluşturulan Dosyalara Kod Eklemek**

Bu bölüm, yukarıdaki dizin yapısında oluşturulan çeşitli dosyalar için kodları gösterir. Lütfen bu kodları alın ve Notepad'de açarak dosyalarınıza kopyalayıp yapıştırın.

**Web.xml**

{{< highlight java >}}

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

{{< highlight java >}}

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

Artık her şeyi yaptınız. Web sayfasını çalıştırma zamanı geldi. Lütfen Tomcat sunucunuzu başlatın ve ardından aşağıdaki URL'yi web tarayıcınıza yapıştırın.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Aşağıdaki ekran görüntüsüne benzer bir şey göreceksiniz. Tebrikler, JSP sayfanızda GridWeb denetimini başarıyla kullandınız.

![todo:image_alt_text](working-with-gridweb_8.png)

## **GridWeb Yazdırma**

Geliştiricilerin, Microsoft Excel dosyasını kaydetmeden bir web sayfasına dahil edilen GridWeb içeriğini yazdırmasına ihtiyaç duyduğu zamanlar olur. Aspose.Cells.GridWeb denetimi bu özelliği destekler.

### **GridWeb Yazdırma**

Ayrı bir dosyaya kaydetmeden yazdırmak için, client tarafında GridWeb sınıfının print() metodunu çağırın. Ayrıca uygun bir olay seçebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Client tarafından çağırıldığından, öncelikle gridweb client id almanız gerekecek. Gridweb.getClientID() metodu kullanılarak client id alınabilir.

### **Client Tarafı Örnek Kod**

Lütfen aşağıdaki bağlantıya bakın, bu bağlantı client tarafından gridweb.print() metodunu çağırır.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Farklı Grid Modlarına Giriş**

Bu makale Aspose.Cells.GridWeb'ın farklı modlarını açıklar. Bu modlar, farklı özelliklere ve davranışlara sahip olduklarından mantıksal olarak ayrılmıştır. Modları şu şekilde tanımladık:

- Edit Modu
- Görünüm Modu

Bu modların hepsinin kendi özellikleri vardır. Geliştiriciler, gereksinimlerine göre Aspose.Cells.GridWeb'i herhangi bir modda kullanabilir. Aşağıda her bir moda bakacağız.

### **Edit Modu**

Varsayılan olarak, Aspose.Cells.GridWeb kontrolü Edit modundadır. Edit modunda, Aspose.Cells.GridWeb kontrolünün sunduğu tüm özellikleri kullanarak ızgara içeriğini tamamen düzenleyebilir veya değiştirebilirsiniz. Bu özellikler şunları içerir:

- İçeriğin Microsoft Excel dosyalarına kaydedilmesi.
- Verileri sunucuya gönderme.
- Formüllerin hesaplanması.
- Önceki işlemlerin geri alınması veya atılması.
- Satır ve sütunları yönetme.
- Veri kesme, kopyalama veya yapıştırma.
- Hücreleri biçimlendirme vb.

**GridWeb denetimi Düzenleme Modunda**

![todo:image_alt_text](working-with-gridweb_9.png)

Geliştiriciler GridWeb denetiminin EditMode özelliğini true olarak ayarlayarak programlı olarak Düzenleme moduna da geçebilirler.

### **Kod Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Görünüm Modu**

GridWeb kontrolü Görüntüleme modundayken, kullanıcılar grid içeriğini düzenleyemez veya değiştiremez, bu da kullanıcıların yalnızca grid içeriğini görüntüleyebileceği anlamına gelir. Bu nedenle bu moda Görüntüleme modu denir. Görüntüleme modunda, birkaç düğme (**Gönder**, **Kaydet** ve **Geri Al**) gizlenir ve sağ tıkladığınızda çıkan menü yalnızca **Kopyala** ve **Bul** seçeneğini içerir.

**GridWeb denetimi Görünüm Modunda** 

![todo:image_alt_text](working-with-gridweb_10.png)

Geliştiriciler, kullanıcılarının yalnızca veri görüntülemesini isterlerse GridWeb kontrolünün EditMode özelliğini **false** olarak ayarlayarak programlı olarak Görüntüleme moduna geçebilirler.

### **Kod Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Görünüm modunda bile, kullanıcılar satır ve sütunların yüksekliğini ve genişliğini değiştirebilirler.

{{% /alert %}}
