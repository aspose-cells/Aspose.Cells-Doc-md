---
title: VS.Net 2005'te Worksheets Designer Kullanarak Bir Çalışma Sayfasını Veritabanıyla Bağlama
type: docs
weight: 40
url: /tr/net/binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005/
---
{{% alert color="primary" %}}

 Bu makalede, çalışma sayfalarını veritabanı tablolarıyla bağlamak için en kolay yaklaşım anlatılmaktadır.**Visual Studio.Net 2005** Aspose.Cells.GridWeb ile sağlanan özel bir araç kullanılarak**Çalışma Sayfaları Tasarımcısı** . Bu makale kesinlikle Aspose.Cells.GridWeb'de veri bağlama özelliğini kullanmanın ne kadar kolay olduğunu size hissettirecektir.**Çalışma Sayfaları Tasarımcısı** .

{{% /alert %}}

## **VS.Net 2005'te Worksheets Designer Kullanarak Bir Çalışma Sayfasını Veritabanıyla Bağlama**

 Bu makalenin amacı, tüm geliştiricilerin bir veri bağlama uygulamasını nasıl oluşturabileceğinizi öğrenmelerini sağlamaktır.**VS.Net 2005** ve kullanımını ve rolünü anlayın**Çalışma Sayfaları Tasarımcısı** editör. Bir şeyi öğrenmenin ve anlamanın en iyi yolu örneklerdir. Bu nedenle, bu yazıda, kullanımını göstermek için örnek bir uygulama oluşturmak da bizim için en iyisi olacaktır.**Çalışma Sayfaları Tasarımcısı**çalışma sayfalarını veritabanıyla bağlamada. Adım adım bir uygulama oluşturalım.

### **1. Adım: Örnek Veritabanı Oluşturma**

 Öncelikle bu yazımızda kullanılacak örnek bir veritabanı oluşturacağız. Aşağıdakileri içeren örnek bir veritabanı oluşturmak için MS Access'i kullandık:**Ürün:% s** Şeması aşağıda gösterilen tablo:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_1.png)

**Figür:** Tasarım bilgisi**Ürün:% s** masa

 Birkaç boş kayıt eklendi**Ürün:% s** aşağıdaki şekilde gösterildiği gibi tablo:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_2.png)

**Figür:** Kayıtlar**Ürün:% s** masa

### **Adım 2: Örnek Uygulama Tasarlama**

 Bir**ASP.NET Web Uygulaması** aşağıdaki şekillerde gösterildiği gibi Visual Studio.NET 2005'te oluşturulmuş ve tasarlanmıştır. Bu ekran görüntüleri, Visual Studio.Net 2005'te Aspose.Cells.GridWeb kullanımına pek aşina olmayan geliştiriciler için kullanışlıdır.

İlk önce VS.Net 2005'i başlatın.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_3.png)

**Figür:** VS.Net 2005'i Başlatma

Dosya|Yeni|Web Sitesi... Menüsünden yeni bir Web Sitesi oluşturun.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_4.png)

**Figür:** Yeni bir Web Sitesi Oluşturma

 Dosya|Yeni|Web Sitesi... menü seçeneğine tıkladıktan sonra,**Yeni web sitesi** diyalog gösterilir. Tıkla**Araştır** içindeki düğme.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_5.png)

**Figür:**Yeni Web Sitesi İletişim Kutusu

 tıkladıktan sonra**Araştır** düğmesine basın, yerel IIS'de konum klasörünü seçin. Yeni bir klasör oluşturup şekilde görüldüğü gibi sanal klasör haline getirebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_6.png)

**Figür:** Yeni bir Klasör oluşturma


 tıkladıktan sonra**Açık** düğmesindeki**Konum seç** diyalog,**Yeni web sitesi** diyalog gibi görünecektir.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_7.png)

**Figür:** Proje Konumunu Ayarlama

Şimdi proje oluşturuldu

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_8.png)

**Figür:** Oluşturulan Proje

### **XHTML ve HTML Modları**

**Aspose.Cells.GridWeb** beri VS.Net 2005'te varsayılan olarak uygulanan XHTML Modunu tamamen destekler.**Xhtml Modu** mülkiyeti**GridWeb** kontrol ayarlandı**Doğru** kontrolü web sayfasına yerleştirdiğinizde varsayılan olarak. Ancak VS.Net 2005'te kontrol için HTML Modunu uygulamak istiyorsanız, bunu oldukça kolay bir şekilde yapabilirsiniz. değiştirmek zorundasın**<!BELGE TÜRÜ>** web sayfasının kaynak kodunda biraz etiketleyin ve**Xhtml Modu** mülkiyeti**GridWeb** kontrol etmek**Yanlış** .

#### **Bu konuda kontrol için HTML Modunu kullanacağız. Öyleyse aşağıdaki adımları izleyin**

##### **1. Web sayfasının Kaynak görünümüne geçin ve kaynak kodunda aşağıdaki <!DOCTYPE> etiketini bulun.**

**xml**

{{< highlight "csharp" >}}

 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

{{< /highlight >}}

Bu etiketi bulduğunuzda, aşağıda gösterildiği gibi kaynak kodundaki tam etiketi seçin.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_9.png)

**Figür:** seçme**<!DOCTYPE> etiketi**

 değiştirin**<!BELGE TÜRÜ>** kaynak kodunuzdan aşağıdaki ile etiketleyin.

**xml**

{{< highlight "csharp" >}}

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> 

{{< /highlight >}}

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_10.png)

**Figür:** Değiştirme**<!DOCTYPE> etiketi**

##### **2. Ardından GridWeb kontrolünü web formuna ekleyeceksiniz. Denetimi seçmeli ve Özellikler penceresinden XhtmlMode özelliğini Yanlış olarak ayarlamak için seçmelisiniz.**

**GridWeb'i WebForm'a Ekleme** 

 Sağ tıklayın**Araç Kutusu** ve seç**Öğeleri Seç...** menüden.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_11.png)

**Figür:** Öğeleri Seçmek

 şimdi seç**GridWeb** bileşen ve tıklayın**TAMAM**

{{% alert color="primary" %}}

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_12.png)

**Figür:** seçme**GridWeb** bileşen iletişim kutusundaki bileşen

 Şimdi**GridWeb** aşağıdaki şekilde gösterildiği gibi eklenir.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_13.png)

**Figür:** **GridWeb** araç kutusuna eklenir

 yerleştirin**GridWeb** aşağıda gösterildiği gibi web formunda.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_14.png)

**Figür:** yerleştirme**GridWeb** web sayfasında

{{% /alert %}} {{% alert color="primary" %}}

**prosedür** : Kontrolü seçin, Şimdi,**Xhtml Modu** gelen mülk**Özellikleri** penceresini açın ve ayarlayın**Yanlış** değer.

{{% /alert %}}

##### **Adım 3: Server Explorer Kullanarak Veritabanına Bağlanma ve Bağlantı Nesnesini Ayarlama**

 Daha önce oluşturduğumuz projeye ilk olarak MS Access veritabanını ekliyoruz.**Aşama 1** . bunu görebilirsin**db.mdb** dosya projeye eklenir.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_15.png)

**Figür:** Proje klasörüne veritabanı eklendi

 Şimdi, gidiyoruz**Bileşen Tasarımcısı** web sayfasının sağ tıklama menü seçeneğini kullanarak web formunun penceresi.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_16.png)

**Figür:** seçme**Bileşen Tasarımcısını Görüntüle** seçenek

Bileşen Tasarımcısı penceresi aşağıdaki gibidir.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_17.png)

**Figür:** Bileşen Tasarımcısı Penceresi

 çift tıklayın**OleDbConnection** oleDbConnection1 nesnesini pencereye yerleştirmek için Veri panelinden bileşen.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_18.png)

**Figür:** oleDbConnection1 nesnesi

 Şimdi veritabanı ile bağlantı kurma zamanı. kullanarak kolayca yapabiliriz.**Sunucu Gezgini** Visual Studio.NET 2005'te. Sadece seçin**Veri bağlantısı** içinde**Sunucu Gezgini** ve sağ tıklayın. Önünüzde görünen bir bağlam menüsü göreceksiniz. Seçme**Bağlantı Ekle...**menüden aşağıdaki şekilde gösterildiği gibi bir seçenek:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_19.png)

**Figür:** seçme**Bağlantı Ekle...** menüden seçenek


 seçtikten sonra**Bağlantı Ekle...** menü seçeneği,**Bağlantı Ekle** iletişim kutusu açılacak ve**Araştır** aşağıda gösterildiği gibi veritabanı dosyasını seçmek için.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_20.png)

**Figür:** Veritabanı dosyasının seçilmesi

Bağlantıyı test edebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_21.png)

**Figür:** Bağlantıyı test etme

Tabloyu ve alanlarını kontrol etmek için bağlantıya göz atabilirsiniz.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_22.png)

**Figür:** Tabloyu ve bağlantı alanlarını kontrol etme

 Şimdi seçerseniz**oleDbConnection1** içindeki nesne**Bileşen Tasarımcısı** penceresinde, yeni oluşturulan mevcut bağlantıyla ilgili bağlantı dizesini seçebilirsiniz, bu, "ConnectionString" özelliğinde oradadır.**oleDbConnection1** Özellikler penceresindeki nesne.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_23.png)

**Figür:** Nesne için bağlantı dizesini seçme

 Son olarak, nesnenin değiştiricisi şu şekilde değiştirilir:**Korumalı** daha iyi erişilebilirlik için.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_24.png)

**Figür:** Nesnenin değiştiricisini ayarlama

##### **4. Adım: Veri Bağdaştırıcısı Nesnesini Yapılandırma**

 Şimdi, bir ekleyin**OleDbDataAdapter** yapılandırmak için araç kutusundaki Veri panelinden bileşeni seçin. çift tıklayın**OleDbDataAdapter** araç kutusunun Veri panelinde, yapılandırma sihirbazını başlatacak ve şekilde gösterildiği gibi mevcut bağlantıyı seçecektir:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_25.png)

**Figür:** Veri Bağdaştırıcısı Yapılandırma Sihirbazı

 tıkladıktan sonra**Sonraki** düğmesini tıklayın**Sorgu oluşturucu** eklemek için**Ürün:% s** tablo, Tüm Sütunlar'ı seçin ve tıklayın**TAMAM** buton.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_26.png)

**Figür:** Ürün tablosu ekleme

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_27.png)

**Figür:** Sorgu oluşturucu

 Şimdi tıklayın**Bitiş** Sihirbazı bitirmek için düğmesine basın.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_28.png)

**Figür:** Sihirbazı Bitirme

 Sihirbazı yapılandırdıktan sonra, oleDbDataAdapter1 aşağıda gösterildiği gibi otomatik olarak pencereye eklenir. Ayrıca, değiştiricisini şu şekilde ayarlayabilirsiniz:**Korumalı**.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_29.png)

**Figür:** Tasarımcı penceresinde OleDbDataAdapter nesnesini alma

##### **5. Adım: Veri Kümesi Oluşturma**

 Veritabanı bağlantısı ve veri adaptörü nesneleri oluşturduğumuz için, ancak yine de veritabanına bağlandıktan sonra verileri depolayabileceğimiz bir şeye ihtiyacımız var. A**Veri Kümesi**nesne verileri tam olarak depolayabilir ve biz de VS.NET 2005 IDE kullanarak kolayca üretebiliriz. Bunu yapmak için seçin**oleDbDataAdaper1** ve sağ tıklayın. Bazı seçeneklerle birlikte bir bağlam menüsü açılır. Seçme**oluştur** **Veri Kümesi...** menüden aşağıdaki şekilde gösterildiği gibi seçeneği seçin.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_30.png)

**Figür:** seçme**oluştur** **Veri Kümesi...** menüden seçenek

 seçtikten sonra**oluştur** **Veri Kümesi...** menü seçeneği, bir**Veri Kümesi Oluştur** diyalog açılacaktı. Bu iletişim kutusunu kullanarak, yeni dosyanın adının ne olacağını seçebiliriz.**Veri Kümesi** oluşturulacak nesne ve hangi tabloların eklenmesi gerektiği**Veri Kümesi** . Kontrol**Bu veri kümesini tasarımcıya ekle** seçeneği ve tıklayın**TAMAM** aşağıdaki şekilde gösterildiği gibi düğme.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_31.png)

**Figür:** tıklama**TAMAM** oluşturmak için düğme**Veri Kümesi**

 Şimdi, bir görebilirsiniz**veri Kümesi11** aşağıdaki şekilde gösterildiği gibi tasarımcıya nesne eklendi. Nesne değiştiriciyi şu şekilde ayarlayın:**Korumalı**.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_32.png)

**Figür:** **Veri Kümesi** oluşturuldu ve tasarımcı penceresine eklendi

.cs dosyasıyla ilgili bağlantı, veri bağdaştırıcısı, veri kümesi nesnesinde belirli kodlar otomatik olarak oluşturulur.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_33.png)

**Figür:** Üretilen Kod

##### **6. Adım: Çalışma Sayfası Tasarımcısını Kullanma**

 Şimdi sırrı açma zamanı. Kontrolü seçin ve sağ tıklayın. Bir bağlam menüsü açılacaktı. Aşağıdaki şekilde gösterildiği gibi menüden Worksheets Designer... seçeneğini seçin.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_34.png)

**Figür:** seçme**Çalışma Sayfaları Tasarımcısı...** menüden seçenek

 Daha sonra**Çalışma Sayfası Koleksiyonu Düzenleyicisi** diyalog (aynı zamanda**Çalışma Sayfaları Tasarımcısı** ) açılacaktır, bağlamak için yapılandırılabilecek birkaç özellik görebilirsiniz.**Sayfa1** veritabanındaki herhangi bir tablo ile. hadi seçelim**Veri kaynağı** Emlak. Yazmak**veri Kümesi11** içinde (önceki adımda oluşturup tasarımcı penceresine eklediğimiz). Sonra üzerine tıklayın**Veri Üyesi** Emlak. Yazmak**Ürün:% s** Şekilde aşağıda gösterildiği gibi burada bir tablo adı olarak:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_35.png)

**Figür:** Ayar**Veri kaynağı** ve**Veri Üyesi** özellikleri

 Şimdi yapılandırabilirsiniz**BindColumns** Emlak. Tıkladıktan sonra, Şimdi bağlama sütunlarını ekleyebilir ve**Altyazı** , **Veri alanı** (Şununla aynı olmalıdır:**Ürün:% s** tablo alanları) ve diğer özellikler. ayarlayabilirsiniz**AutoCreated mı** ile**doğru** ve uygula**Doğrulama** ve ayarla**SayıTürü**Gereksinimleriniz için farklı alanlar.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_36.png)

**Figür:** tıklama**BindColumns** Emlak

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_37.png)

**Figür:** **BindColumn Toplama Düzenleyicisi** diyalog

##### **7. Adım: Web Sayfası İçin Bazı Kod Satırları Ekleme**

 Kullandık**Çalışma Sayfaları Tasarımcısı** kolayca ve şimdi sadece birkaç kod satırı eklememiz gerekiyor

 ilk biz ekleyeceğiz**OnInit'te** başlatılacak olayla ilgili kod**Bileşeni Başlatma** bağlantı, komut, veri bağdaştırıcısı ve veri kümesi nesnelerini başlatma ve oluşturma yöntemi. Bu kod satırları, otomatik olarak oluşturulan kodla birlikte eklenmez, bu nedenle bunları manuel olarak eklemeliyiz.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_38.png)

**Figür:** Biraz kod ekleme1

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_39.png)

**Figür:** Bazı code2 ekleme

 Şimdi bazı kodlar ekliyoruz**Sayfa_Yük** doldurma için olay işleyicisi**veri Kümesi11** veritabanından veri içeren nesne (kullanarak**oleDbDataAdapter1** ) ve bağlama**GridWeb** ile kontrol**veri Kümesi11** onu arayarak**veri bağı** yöntem.

{{% alert color="primary" %}}   {{% /alert %}}

##### **Örnek:**

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

protected void Page_Load(object sender, EventArgs e)

{

    //Checking if there is not any PostBack

    if (!IsPostBack)

    {

        try

        {

            //Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11);

            //Binding GridWeb with DataSet

            GridWeb1.DataBind();

        }

        finally

        {

            //Finally, closing database connection

            oleDbConnection1.Close();

        }

    }

}

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing Page_Load event handler

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

    'Checking if there is not any PostBack

    If Not IsPostBack Then

        Try

            'Filling DataSet with data 

            oleDbDataAdapter1.Fill(dataSet11)

            'Binding GridWeb with DataSet

            GridWeb1.DataBind()

        Finally

            'Finally, closing database connection

            oleDbConnection1.Close()

        End Try

    End If

End Sub

{{< /highlight >}}

 Eklenen kodu da kontrol edebilirsiniz.**Sayfa_Yük** aşağıdaki şekilde gösterildiği gibi olay işleyicisi:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_40.png)

**Figür:** Kod eklendi**Sayfa_Yük** olay işleyicisi

Şimdiye kadar çok kullanışlı bir veritabanı uygulaması oluşturduk. Ancak bu uygulama sadece tablonun verilerini görmenizi sağlar. Verileri düzenleyebilmenize rağmen**GridWeb** kontrol edin, ancak ne zaman tarayıcı pencerenizi kapatacaksınız ve veritabanınızı açacaksınız. Hiçbir şeyin değişmediğini göreceksiniz. Yani yaptığınız değişiklikler veri tabanına kaydedilmez. Yani, yapmanız gereken bir şey var.

 Şimdi uygulamamıza bazı kodlar ekleyeceğiz, böylece**GridWeb** değişikliklerini gerçek veritabanına kaydedebilir. Hadi açalım**Özellikleri** bölmesi ve seçin**Komutu Kaydet** olayı**GridWeb** olayları listesinden kontrol edin. üzerine çift tıklarsanız**Komutu Kaydet** olay sonra VS.NET 2005 IDE oluşturacak**GridWeb1_SaveCommand** sizin için olay işleyicisi. Veritabanını içinde yer alan değiştirilmiş verilerle güncellemek için bu olay işleyicisine bazı kodlar ekleyin.**Veri Kümesi** (çalışma sayfasına bağlı) kullanarak**oleDbDataAdapter1**.

##### **Örnek:**

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

protected void GridWeb1_SaveCommand(object sender, EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WebWorksheets[0].DataSource;

        //Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset);

    }

    finally

    {

        //Closing database connection

        oleDbConnection1.Close();

    }

}

{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Implementing the event handler for SaveCommand event

Protected Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs)

  Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WebWorksheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub

{{< /highlight >}}

 Eklenen kodu da kontrol edebilirsiniz.**GridWeb1_SaveCommand** aşağıdaki şekilde gösterildiği gibi olay işleyicisi:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_41.png)

**Figür:** Kod eklendi**GridWeb1_SaveCommand** olay işleyicisi

 Şimdi, değişikliklerinizi kullanarak veritabanına kaydedecekseniz**Kaydetmek** düğmesi**GridWeb** , kesinlikle kurtulacaklardı.

##### **8. Adım: Uygulamanızı Çalıştırma**

 Son olarak, ya basarak uygulamamızı derleyebilir ve çalıştırabiliriz.**Ctrl+F5** veya tıklama**Başlama** buton. Hata ayıklama iletişim kutusunda, uygun hata ayıklama seçeneğini belirtebilir ve**TAMAM** aşağıdaki şekilde gösterildiği gibi düğme.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_42.png)

**Figür:** Çalışan uygulama

 Derlemeden sonra,**varsayılan.aspx** web uygulamamızın sayfası, aşağıda gösterildiği gibi veritabanından yüklenen tüm verileri görebileceğimiz yeni bir tarayıcı penceresinde açılacaktır:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_43.png)

**Figür:** Veriler yüklendi**GridWeb** veri tabanından kontrol

 Veriler yüklendiğinde**GridWeb** kontrol ederseniz, Aspose.Cells.GridWeb'in kullanıcılarına üstü kapalı bir veri kontrolü sağladığını hissedersiniz. tarafından ne tür veri işleme özelliklerinin sunulduğunu kontrol edelim.**GridWeb** kullanıcılarına.

##### **Veri doğrulama**

Aspose.Cells.GridWeb, veritabanında tanımlanan veri türlerine göre tüm ilişkili sütunlar için uygun doğrulama kurallarını otomatik olarak oluşturur. Aşağıdaki şekilde gösterildiği gibi, fare işaretçinizi hücrenin üzerine getirerek bir hücrenin doğrulama türünü görebilirsiniz:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_44.png)

**Figür:**Bir hücrenin doğrulama türünü kontrol etme

 Yukarıdaki şekilde, seçili hücrenin içerdiğini görebiliriz.**\<INT>** Bu, kullanıcıların ona yalnızca tamsayı değeri girebileceği anlamına gelir, aksi takdirde bir doğrulama hatası oluşur. Dahası,**\<GEREKLİ>** değerinin olduğunu gösterir.**ürün kimliği** kullanıcı tarafından sunulması zorunludur.

##### **Satırları Silme**

 Bir satırı silmek için önce bir satırı (veya satırın herhangi bir hücresini) seçip**Sırayı sil** Aşağıda gösterildiği gibi sağ tıklama menüsünden seçenek:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_45.png)

**Figür:** seçme**Sırayı sil** menüden seçenek

 seçtikten sonra**Sırayı sil** menüden satır silinir**GridWeb** . Şimdi tıklayın**kaydetmek** düğmesi**GridWeb** orijinal veritabanı tablosundaki bu kaydı silmek için.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_46.png)

**Figür:** Izgara verileri (bir satır silindikten sonra)

##### **Satırları Düzenleme**

 Ayrıca hücrelerdeki veya satırlardaki verileri düzenleyebilir ve ardından**Kaydetmek** Değişikliklerinizi kaydetmek için düğmesine basın.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_47.png)

**Figür:** Kılavuz verileri (Kayıt1 Düzenleme)

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_48.png)

**Figür:** Izgara verileri (Kayıt2'yi Düzenleme)

##### **Satır Ekleme**

 Satır eklemek için seçin**Satır ekle** Aşağıda gösterildiği gibi sağ tıklama menüsünden seçenek:

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_49.png)

**Figür:** seçme**Satır ekle** menüden seçenek

Seçildikten sonra satırların sonunda sayfaya yeni bir satır eklenecektir.**Satır ekle** menü seçeneği. Yeni eklenen satırın solunda bir**yıldız işareti** satırın yeni eklendiğini gösteren işaret.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_50.png)

**Figür:** Izgaraya yeni satır eklendi

 Yeni satırdaki değerleri girdikten sonra, tıklayın**Kaydetmek** Aşağıda gösterildiği gibi orijinal veritabanı tablosundaki değişiklikleri onaylamak için düğmesine basın.

![yapılacaklar:resim_alternatif_Metin](binding-a-worksheet-with-database-using-worksheets-designer-in-vs-net-2005_51.png)

**Figür:** Değişiklikleri tıklayarak veritabanı tablosuna kaydetme**Kaydetmek** buton

{{% alert color="primary" %}}   {{% /alert %}}

##### **Çözüm**

{{% alert color="primary" %}}

**Bağlanma verileri** Aspose.Cells.GridWeb'in önemli bir özelliğidir. Geliştiricilerin çalışma sayfalarını kullanarak veri tabanına bağlaması gerçekten zahmetsizdir.**Çalışma Sayfaları Tasarımcısı** Aspose.Cells.GridWeb tarafından sunulan yardımcı program. Aspose.Cells.GridWeb, geliştiricilerin güçlü Grid çözümleri oluşturmada zamandan ve emekten tasarruf etmeleri için çok faydalıdır.

{{% /alert %}}
