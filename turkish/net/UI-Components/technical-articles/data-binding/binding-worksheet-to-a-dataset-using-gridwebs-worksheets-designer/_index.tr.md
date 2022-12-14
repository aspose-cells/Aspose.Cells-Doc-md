---
title: GridWebs Worksheets Designer kullanarak Çalışma Sayfasını bir DataSet'e Bağlama
type: docs
weight: 20
url: /tr/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/
---
{{% alert color="primary" %}} 

 Bu makalede, Çalışma Sayfaları Tasarımcısı olan Aspose.Cells.GridWeb ile sağlanan özel bir araç kullanılarak GUI modunda çalışma sayfalarını veritabanı tablolarına bağlamak için kolay bir yaklaşım anlatılmaktadır.

{{% /alert %}} 
## **Çalışma Sayfası Tasarımcısını Kullanarak Bir Çalışma Sayfasını Veritabanıyla Bağlama**
	**1. Adım: Örnek Veritabanı Oluşturma**
1. Öncelikle bu yazımızda kullanacağımız örnek veritabanını oluşturuyoruz. Ürünler adlı bir tablo içeren bir veritabanı oluşturmak için Microsoft Access kullanıyoruz. Şeması aşağıda gösterilmiştir.
   **Ürünler tablosunun tasarım bilgileri** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Ürünler tablosuna birkaç sahte kayıt eklenir.
   **Ürünler tablosundaki kayıtlar** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Adım 2: Örnek Uygulama Tasarlama**
 Bir ASP.NET web uygulaması aşağıda gösterildiği gibi Visual Studio.NET'de oluşturulur ve tasarlanır.
**Tasarlanan örnek uygulama** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **3. Adım: Server Explorer Kullanarak Veritabanına Bağlanma**
 Veritabanına bağlanma zamanı. Visual Studio.NET'deki Sunucu Gezgini'ni kullanarak kolayca yapabiliriz.

1.  Seçme**Veri bağlantısı** içinde**Sunucu Gezgini** ve sağ tıklayın.
1.  Seçme**Bağlantı Ekle** menüden.
   **Bağlantı Ekle seçeneğini belirleme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



 Veri Bağlantısı Özellikleri iletişim kutusu görüntülenir.
**Veri Bağlantısı Özellikleri iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



 Bu iletişim kutusunu kullanarak herhangi bir veritabanına bağlanabilirsiniz. Varsayılan olarak, bir SQL Server veritabanına bağlanmanıza izin verir. Bu örnek için Microsoft Access veritabanına bağlanmamız gerekiyor.

1.  Tıkla**Sağlayıcı** sekme.
1.  Seçme**Microsoft Jet 4.0 OLE DB Sağlayıcısı** dan**OLE DB Sağlayıcı(lar)ı** liste.
1.  Tıklamak**Sonraki**.
   **Bir OLE DB sağlayıcı seçtikten sonra İleri'ye tıklama** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


 bu**Bağ** sekme sayfası açılır.

1.  Microsoft Access veritabanı dosyasını (bizim durumumuzda db.mdb) seçin ve tıklayın**TAMAM**.
   **Veritabanı dosyası seçildikten sonra Tamam düğmesine tıklanması** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

 tıkladıktan sonra**TAMAM** Microsoft Access veritabanına bir veritabanı bağlantısı oluşturulacaktır.**Sunucu Gezgini**Veritabanındaki tüm tabloları, görünümleri ve saklı yordamları görmek için bağlantıya çift tıklayın.

{{% /alert %}} 
### **Adım 4: Veritabanı Bağlantı Nesnelerini Grafik Olarak Oluşturma**
1.  kullanarak veritabanındaki tablolara göz atın.**Sunucu Gezgini**.
 Yalnızca bir tablo var, Ürünler.
1.  Ürünler tablosunu sürükleyip bırakın.**Sunucu Gezgini** için**İnternet formu**.
   **Ürünler tablosunu Sunucu Gezgini'nden sürükleyip web formuna bırakmak** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Bir iletişim kutusu görünebilir.
**Bağlantı dizesine veritabanı parolasının eklenmesini onaylamak için iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



 Bağlantı dizesine bir veritabanı parolası eklemek isteyip istemediğinize karar verin. Bu örnek için seçtik**şifreyi dahil etme**. 
İki veritabanı bağlantı nesnesi (oleDbConnection1 ve oleDbDataAdapter1) oluşturuldu ve eklendi.
**Oluşturulan ve görüntülenen veritabanı bağlantı nesneleri (oleDbConnection1 & oleDbDataAdapter1)** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **5. Adım: Veri Kümesi Oluşturma**
Şimdiye kadar veritabanı bağlantı nesneleri oluşturduk ancak yine de veritabanına bağlandıktan sonra verileri depolamak için bir yere ihtiyacımız var. Bir DataSet nesnesi, verileri tam olarak depolayabilir ve biz de VS.NET IDE kullanarak kolayca oluşturabiliriz.

1.  Seçme**oleDbDataAdaper1** ve sağ tıklayın.
1.  Seçme**Veri Kümesi Oluştur** menü seçeneği.
   **Generate DataSet seçeneğini belirleme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



 Veri Kümesi Oluştur iletişim kutusu görüntülenir.
 Burada yeni oluşturulacak DataSet nesnesi için bir isim ve ona hangi tabloların eklenmesi gerektiğini seçmek mümkündür.

1.  seçin**Bu veri kümesini tasarımcıya ekle** seçenek.
1.  Tıklamak**TAMAM**.
   **DataSet oluşturmak için Tamam düğmesini tıklatmak** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Tasarımcıya bir dataSet11 nesnesi eklenir.
**DataSet oluşturuldu ve tasarımcıya eklendi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **6. Adım: Çalışma Sayfası Tasarımcısını Kullanma**
 Şimdi sırrı açma zamanı.

1. GridWeb kontrolünü seçin ve sağ tıklayın.
1.  Seçme**Çalışma Sayfaları Tasarımcısı** menü seçeneği.

   **Çalışma Sayfaları Tasarımcısı seçeneğini belirleme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



 Çalışma Sayfası Koleksiyonu Düzenleyicisi (Çalışma Sayfaları Tasarımcısı olarak da bilinir) görüntülenir.
**Çalışma Sayfaları Koleksiyon Düzenleyici iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



İletişim kutusu, Sayfa1'i veritabanındaki herhangi bir tabloya bağlamak için yapılandırılabilen birkaç özellik içerir.

1.  seçin**Veri kaynağı** Emlak.
 Önceki adımda oluşturulan dataSet11 nesnesi menüde listelenir.
1. dataSet11'i seçin.
1.  Tıkla**Veri Üyesi** Emlak.
 Çalışma Sayfaları Tasarımcısı, dataSet11'deki tabloların bir listesini otomatik olarak gösterir. Yalnızca bir tablo var, Ürünler.
1. Ürünler tablosunu seçin.
   **DataSource ve DataMember özelliklerini ayarlama** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1.  kontrol et**BindColumns** Emlak.
   **BindColumns özelliğine tıklama** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



 tıklayarak**BindColumns** özelliği BindColumn Koleksiyon Düzenleyicisini açar.
**BindColumn Koleksiyon Düzenleyicisi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



 BindColumn Collection Editor'da,**Ürün:% s** tablo otomatik olarak BindColumns koleksiyonuna eklenir.

1. Herhangi bir sütunu seçin ve özelliklerini özelleştirin.
 Örneğin, her bir sütun başlığını değiştirebilirsiniz.
   **Ürün Kimliği sütununun Başlığını değiştirme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1.  Değişiklikleri yaptıktan sonra tıklayın.**TAMAM**.
1.  Tıklayarak tüm iletişim kutularını kapatın**TAMAM**.
 Son olarak, WebForm1.aspx sayfasına geri dönersiniz.
   **Worksheets Designer'ı kullandıktan sonra WebForm1.aspx sayfasına dönme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


 Yukarıda, Ürünler tablosu sütun adı gösterilmektedir. Sütunların genişliği küçüktür, bu nedenle bazı sütunların tam adları tam olarak görünmez.
### **7. Adım: Page_Load Olay İşleyicisine Kod Ekleme**
 Worksheets Designer'ı kullandık ve şimdi dataSet11 nesnesini veritabanındaki verilerle doldurmak (oleDbDataAdapter1 kullanarak) ve DataBind yöntemini çağırarak GridWeb kontrolünü dataSet11'e bağlamak için Page_Load olay işleyicisine kod eklememiz gerekiyor.

1.  Kodu ekleyin:

**C#**

{{< highlight "csharp" >}}

 //Implementing Page_Load event handler

private void Page_Load(object sender, System.EventArgs e)

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

Private Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Load

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

1. Page_Load olay işleyicisine eklenen kodu kontrol edin.
   **Page_Load olay işleyicisine eklenen kod** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **8. Adım: Uygulamayı Çalıştırma**
 Uygulamayı derleyin ve çalıştırın:**Ctrl+F5** veya tıklayın**Başlama**. 
**Uygulamayı çalıştırma** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Derlemeden sonra, veritabanından yüklenen tüm verilerle WebForm1.aspx sayfası bir tarayıcı penceresinde açılır.
**Veritabanından GridWeb kontrolüne yüklenen veriler** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **GridWeb Denetimi ile Çalışma**
 Veriler GridWeb kontrolüne yüklendiğinde, kullanıcılara veriler üzerinde kontrol sağlar. GridWeb tarafından bir dizi farklı türde veri işleme özelliği sunulmaktadır.
### **Veri doğrulama**
Aspose.Cells.GridWeb, veritabanında tanımlanan veri türlerine göre tüm ilişkili sütunlar için uygun doğrulama kurallarını otomatik olarak oluşturur. İmleci hücrenin üzerine getirerek hücrenin doğrulama türünü görün.
**Bir hücrenin doğrulama türünü kontrol etme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

 Burada, seçilen hücre şunları içerir:**<INT>** doğrulama, bu da kullanıcıların ona yalnızca tamsayı değerleri girebileceği anlamına gelir. Başka bir değer girerlerse doğrulama hatası oluşur. Dahası,**<GEREKLİ>** Ürün Kimliği değerinin gönderilmesi gerektiğini gösterir.
### **Satırları Silme**
 Bir satırı silmek için bir satırı (veya satırdaki herhangi bir hücreyi) seçin, sağ tıklayın ve seçin**Sırayı sil**.
**Menüden Satır Sil seçeneğinin seçilmesi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Satır anında silinir.
**Izgara verileri (bir satır silindikten sonra)** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Satırları Düzenleme**
Hücrelerdeki veya satırlardaki verileri düzenleyin ve ardından**Kaydetmek** veya**Göndermek** Değişiklikleri kaydetmek için.
### **Satır Ekleme**
1.  Bir satır eklemek için, bir hücreye sağ tıklayın ve seçin.**Satır ekle**.
   **Menüden Satır Ekle seçeneğinin seçilmesi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Sayfaya diğer satırların sonuna yeni bir satır eklenir.
**Izgaraya yeni satır eklendi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



 Yeni satırın solunda bir yıldız var{{< emoticons/cross >}} , satırın yeni olduğunu belirtir.

1. Yeni satıra değerler ekleyin.
1.  Tıklamak**Kaydetmek** veya**Göndermek** değişikliği onaylamak için.
   ***Kaydet'e tıklayarak verilerdeki değişiklikleri kaydetme** buton*

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Ayar Numarası Biçimi**
 Şu anda fiyatlarda**Ürün fiyatı** sütun sayısal değerler olarak gösterilir. Para birimi gibi görünmelerini sağlamak mümkündür.

1. Visual Studio.NET'e dönün.
1. BindColumn Koleksiyon Düzenleyicisini açın.
 bu**SayıTürü** mülkiyeti**Ürün fiyatı** sütun şu şekilde ayarlandı:**Genel**.
   **NumberType özelliği Genel olarak ayarlandı** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1.  Tıklamak**Açılır liste** ve seç**Para birimi4** listeden.
   **NumberType özelliği Currency4 olarak değiştirildi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Uygulamayı tekrar çalıştırın.
 içindeki değerler**Ürün fiyatı** sütun artık para birimidir.
   **Para birimi cinsinden ürün fiyatları Sayı Biçimi** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Verileri Düzenleme**
 Uygulama şu ana kadar kullanıcılarının yalnızca tablo verilerini görüntülemesine izin veriyor. Kullanıcılar, GridWeb kontrolünde verileri düzenleyebilir, ancak tarayıcıyı kapatırken ve veritabanını açarken hiçbir şey değişmedi. Yapılan değişiklikler veri tabanına kaydedilmez.

 Aşağıdaki örnek, GridWeb'in değişiklikleri veritabanına kaydedebilmesi için uygulamaya kod ekler.

1. Aç**Özellikleri** bölmesini açın ve listeden GridWeb denetiminin SaveCommand olayını seçin.
   **GridWeb'in SaveCommand olayını seçme** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1.  çift tıklayın**Komutu Kaydet** olay ve VS.NET, GridWeb1_SaveCommand olay işleyicisini oluşturur.
1.  Bu olay işleyicisine, oleDbDataAdapter1 kullanarak çalışma sayfasına bağlı DataSet'teki değiştirilmiş verilerle veritabanını güncelleyecek kodu ekleyin.

**C#**

{{< highlight "csharp" >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

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

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

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

GridWeb1_SaveCommand olay işleyicisine eklenen kodu da kontrol edebilirsiniz.
**GridWeb1_SaveCommand olay işleyicisine eklenen kod** 

![yapılacaklar:resim_alternatif_Metin](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

 kullanarak değişiklikleri veritabanına kaydedin.**Kaydetmek** düğmesi artık kesinlikle onları kurtarıyor.
## **Çözüm**
{{% alert color="primary" %}} 

Veri bağlama, Aspose.Cells.GridWeb'in önemli bir özelliğidir. Aspose.Cells.GridWeb tarafından sunulan Worksheets Designer yardımcı programını kullanarak çalışma sayfalarını bir veritabanına bağlamak kolaydır. Aspose.Cells.GridWeb, güçlü Grid çözümleri oluştururken zamandan ve emekten tasarruf sağlar.

{{% /alert %}}
