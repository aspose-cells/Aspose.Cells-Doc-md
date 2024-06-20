---
title: GridWeb Kullanılarak Bir Veri Setini Çalış Sayfasına Bağlama
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/bind-worksheet-to-a-dataset-use-designer/
keywords: GridWeb,bind,DataSet,Designer,designer
description: Bu makale, Worksheets Designer ın kullanımını GridWeb de bir Veri Setini Çalış Sayfasına nasıl bağlayacağınızı tanıtır.
---

{{% alert color="primary" %}} 

Bu makale, Aspose.Cells.GridWeb ile birlikte sağlanan özel bir araç olan Worksheets Designer'ı kullanarak GUI moda tabloları veritabanına bağlamanın kolay bir yaklaşımını tartışmaktadır. 

{{% /alert %}} 
## **Worksheets Designer Kullanarak Veritabanı İle Çalış Sayfasının Bağlanması**
	**Adım 1: Örnek Bir Veritabanı Oluşturma**
1. Öncelikle makalede kullanılacak örnek veritabanını oluşturuyoruz. Bu makalede, Products adında bir tablo içeren bir veritabanı oluşturmak için Microsoft Access'i kullanıyoruz. Şeması aşağıda gösterilmiştir.
   **Products tablosunun tasarım bilgileri** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_1.png)




1. Bazı örnek kayıtlar Products tablosuna eklenir.
   **Products tablosundaki kayıtlar** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_2.png)
### **Adım 2: Örnek Uygulamanın Tasarlanması**
Bir ASP.NET web uygulaması oluşturulur ve Visual Studio.NET'te tasarlanır, aşağıda gösterildiği gibi. 
**Tasarlanmış örnek uygulama** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_3.png)
### **Adım 3: Sunucu Gezgini Kullanarak Veritabanına Bağlanma**
Artık veritabanına bağlanma zamanı. Bunun için Visual Studio.NET'te Sunucu Gezgini'ni kullanarak kolayca yapabiliriz. 

1. **Sunucu Gezgini**'nde **Veri Bağlantısı**'nı seçin ve sağ tıklayın.
1. Menüden **Bağlantı Ekle**'yi seçin.
   **Bağlantı Ekle seçeneğini seçme** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_4.png)



Veri Bağlantısı Özellikleri iletişim kutusu görüntülenir. 
**Veri Bağlantısı Özellikleri iletişim kutusu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_5.png)



Bu iletişim kutusunu kullanarak herhangi bir veritabanına bağlanabilirsiniz. Varsayılan olarak, bir SQL Server veritabanına bağlanmanıza izin verir. Bu örnekte bir Microsoft Access veritabanına bağlanmamız gerekiyor. 

1. **Sağlayıcı** sekmesine tıklayın.
1. **OLE DB Sağlayıcılar** listesinden **Microsoft Jet 4.0 OLE DB Sağlayıcısı**'nı seçin.
1. **Sonraki**'ye tıklayın.
   **OLE DB sağlayıcı seçtikten sonra İleri'ye tıklama** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_6.png)


**Bağlantı** sekmesi açılır. 

1. Microsoft Access veritabanı dosyasını (bizim durumumuzda db.mdb) seçin ve **Tamam**'a tıklayın.
   **Veritabanı dosyasını seçtikten sonra Tamam düğmesine tıklama** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_7.png)

{{% alert color="primary" %}} 

**Tamam**'a tıkladıktan sonra Microsoft Access veritabanına bir veritabanı bağlantısı **Sunucu Gezgini**'nde oluşturulur. Tüm tabloları, görünümleri ve depolanan prosedürleri veritabanında görmek için bağlantıya çift tıklayın.

{{% /alert %}} 
### **Adım 4: Veritabanı Bağlantı Nesnelerinin Grafiksel Olarak Oluşturulması**
**Sunucu Gezgini**'nde tabloları göz atın.
   Sadece bir tablo var, Products. 
1. **Web Form**'a **Sunucu Gezgini**'nden Products tablosunu sürükleyip bırakın.
   **Sunucu Gezgini'nden Products tablosunu sürükleyip web formuna bırakma** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_8.png)



Bir iletişim kutusu görünebilir.
**Bağlantı dizesine veritabanı parolasını dahil etmeyi onaylamak için iletişim kutusu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_9.png)



Bağlantı dizesinde bir veritabanı şifresini içermek isteyip istemediğinize karar verin. Bu örnekte **Şifreyi Dahil Etme** seçildi. 
İki veritabanı bağlantı nesnesi (oleDbConnection1 ve oleDbDataAdapter1) oluşturuldu ve eklenmiştir.
**Veritabanı bağlantı nesneleri (oleDbConnection1 & oleDbDataAdapter1) oluşturuldu ve görüntülendi** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_10.png)



### **Adım 5: DataSet Oluşturma**
Şimdiye kadar veritabanı bağlantı nesneleri oluşturduk ancak hala veritabanına bağlandıktan sonra veriyi saklamak için bir yere ihtiyacımız var. Bir DataSet nesnesi veriyi kesinlikle saklayabilir ve VS.NET IDE kullanarak kolayca oluşturabiliriz. 

1. **oleDbDataAdaper1**'i seçin ve sağ tıklayın.
1. Menüden **DataSet Oluştur** seçeneğini seçin.
   **Generate DataSet seçeneğini seçme** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_11.png)



DataSet Oluştur iletişim kutusu görüntülenir. 
Burada, oluşturulacak yeni DataSet nesnesi için bir isim seçmek ve hangi tabloların ona ekleneceğini seçmek mümkündür. 

1. **Bu veri kümesini tasarımcıya ekle** seçeneğini seçin.
1. **Tamam**'a tıklayın.
   **DataSet oluşturmak için Tamam düğmesine tıklama** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_12.png)



Bir dataSet11 nesnesi tasarımcıya eklenir.
**DataSet oluşturuldu ve tasarımcıya eklendi** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_13.png)
### **Adım 6: Çalışsay Tasarımcısı Kullanımı**
Şimdi, sırrı açma zamanı. 

1. **GridWeb** kontrolünü seçin ve sağ tıklayın.
1. Menüden **Çalışsay Tasarımcısı** seçeneğini seçin. 

   **Çalışsay Tasarımcısı seçeneğini seçme** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_14.png)



Çalışsay Koleksiyon Düzenleyicisi (aynı zamanda Çalışsay Tasarımcısı olarak da adlandırılır) görüntülenir. 
**Çalışsay Koleksiyon Düzenleyici iletişim kutusu** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_15.png)



İletişim kutusu, Sheet1'in herhangi bir tabloya bağlanması için yapılandırılabilecek birkaç özelliği içerir.

1. **DataSource** özelliğini seçin.
   Önceki adımda oluşturulan dataSet11 nesnesi menüde listelenir. 
1. dataSet11'i seçin.
1. **DataMember** özelliğine tıklayın.
   Çalışsay Tasarımcısı dataSet11 içindeki tabloların bir listesini otomatik olarak gösterir. Yalnızca bir tablo, Ürünler vardır.
1. Ürünler tablosunu seçin.
   **DataSource ve DataMember özelliklerini ayarlama** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_16.png)




1. **BindColumns** özelliğini kontrol edin.
   **BindColumns özelliğine tıklayın** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_17.png)



**BindColumns** özelliğine tıklamak, BindColumn Koleksiyon Düzenleyicisini açar.
**BindColumn Koleksiyon Düzenleyicisi** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_18.png)



BindColumn Koleksiyon Düzenleyicisi'nde, **Products** tablosunun tüm sütunları otomatik olarak BindColumns koleksiyonuna eklenir. 

1. Herhangi bir sütunu seçin ve özelliklerini özelleştirin.
   Örneğin, her sütun başlığını değiştirebilirsiniz.
   **ProductID sütununun Başlığını Değiştirmek** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_19.png)




1. Değişiklikleri yaptıktan sonra **Tamam**'a tıklayın.
1. **Tamam**'a tıklayarak tüm iletişim kutularını kapatın.
   Son olarak, WebForm1.aspx sayfasına dönersiniz. 
   **Worksheets Tasarımcısı'nı kullandıktan sonra WebForm1.aspx sayfasına geri dönme** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_20.png)


Yukarıda, Products tablosunun sütun adı gösterilmektedir. Bazı sütunların tam adları tamamen görünmez olduğu için sütunların genişliği küçüktür. 
### **Adım 7: Page_Load Olay İşleyicisine Kod Ekleme**
Worksheets Tasarımcısı'nı kullandık ve şimdi sadece dataSet11 nesnesini veritabanından gelen verilerle doldurmak için Page_Load olay işleyicisine kod eklememiz gerekiyor (oleDbDataAdapter1'i kullanarak) ve GridWeb denetimini dataSet11 ile veri bağlamak için DataBind yöntemini çağırmak. 

1. Kodu ekleyin: 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_21.png)
### **Adım 8: Uygulamayı Çalıştırma**
Uygulamayı derleyip çalıştırın: ya **Ctrl+F5** tuşuna basın ya da **Başlat**'a tıklayın. 
**Uygulamayı çalıştırma** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_22.png)



Derlemeden sonra, webForm1.aspx sayfası, veritabanından yüklenmiş tüm verilerle birlikte bir tarayıcı penceresinde açılır.
**GridWeb denetimine veritabanından yüklenmiş veri** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_23.png)
## **GridWeb Denetimi İle Çalışma**
Veri GridWeb denetimine yüklendiğinde, kullanıcılara veri üzerinde kontrol sağlar. GridWeb tarafından bir dizi farklı veri işleme özelliği sunulmaktadır. 
### **Veri Doğrulama**
Aspose.Cells.GridWeb, veritabanında tanımlanan veri tiplerine göre tüm bağlı sütunlar için uygun doğrulama kuralları otomatik olarak oluşturur. Bir hücrenin doğrulama türünü üzerine gelerek imleci kullanarak görebilirsiniz.
**Hücrenin doğrulama türünü kontrol etme** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_24.png)

Here, the selected cell contains the **<INT>** validation, which means that users can only enter integer values into it. If they enter another value, a validation error occurs. Moreover, **<REQUIRED>** shows that the value Product ID must be submitted. 
### **Satırları Silme**
Bir satırı silmek için bir satırı (veya satırdaki herhangi bir hücreyi) seçin, sağ tıklayın ve **Satırı Sil** seçeneğini seçin.
**Menüden Satırı Sil seçeneğini seçmek** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_25.png)


Satır hemen silinir.
**Satır silindikten sonraki ızgara verileri** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_26.png)
### **Satırları Düzenleme**
Hücre veya satırlardaki verileri düzenleyin ve ardından değişiklikleri kaydetmek için **Kaydet** veya **Gönder**i tıklayın. 
### **Satırlar Ekleme**
1. Bir satır eklemek için bir hücreye sağ tıklayın ve **Satır Ekle**'yi seçin.
   **Menüden Satır Ekle seçeneğini seçmek** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_27.png)



Yeni bir satır diğer satırların sonunda sayfaya eklenir.
**Izgara'ya eklenen yeni satır** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_28.png)



At the left of the new row is an asterisk {{< emoticons/cross >}}, indicating that the row is new. 

1. Yeni satıra değerler ekleyin.
1. Değişikliği onaylamak için **Kaydet** veya **Gönder**i tıklayın.
   **Kaydet** düğmesine tıklayarak verilere yapılan değişiklikleri kaydetme 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_29.png)
### **Sayı Biçimini Ayarlama**
Şu anda **Ürün Fiyatı** sütunundaki fiyatlar sayısal değer olarak gösterilmektedir. Bunları para birimi gibi göstermek mümkündür.

1. Visual Studio.NET'e geri dönün.
1. BindColumn Collection Editor'ü açın.
   **Ürün Fiyatı** sütununun **NumberType** özelliği **Genel** olarak ayarlanmıştır.
   **NumberType özelliği Genel olarak ayarlandı** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_30.png)




1. **DropDownList**'e tıklayın ve listeden **Para Birimi4**'ü seçin.
   **NumberType özelliği Para Birimi4 olarak değiştirildi** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_31.png)




1. Uygulamayı tekrar çalıştırın.
   **Ürün Fiyatı** sütunundaki değerler artık para birimidir.
   **Ürün fiyatları para Birimi Numarası Biçiminde** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_32.png)
### **Verileri Düzenleme**
Uygulama şu ana kadar kullanıcılarına yalnızca tablo verilerini görüntüleme olanağı sağlar. Kullanıcılar GridWeb kontrolünde verileri düzenleyebilir ancak tarayıcıyı kapatıp veritabanını açtıklarında hiçbir değişiklik olmaz. Yapılan değişiklikler veritabanında kaydedilmez. 

Aşağıdaki örnek, GridWeb'in veritabanına yapılan değişiklikleri kaydedebilmesi için uygulamaya kod ekler. 

1. **Özellikler** panelini açın ve listeden GridWeb kontrolünün SaveCommand olayını seçin.
   **GridWeb'in SaveCommand olayını seçmek** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_33.png)




1. **SaveCommand** etkinliğine çift tıklayın ve VS.NET GridWeb1_SaveCommand etkinlik işleyicisini oluşturur.
1. Bu etkinlik işleyicisine ekleyeceğiniz kod, oleDbDataAdapter1 ile çalışsayan çalış sayfasına bağlı DataSet'teki değiştirilmiş verileri veritabanı ile güncelleyecektir. 

**C#**

{{< highlight csharp >}}

 //Implementing the event handler for SaveCommand event

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

    try

    {

        //Getting the modified data of worksheet as a DataSet

        DataSet dataset = (DataSet)GridWeb1.WorkSheets[0].DataSource;

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

{{< highlight csharp >}}

 'Implementing the event handler for SaveCommand event

Private Sub GridWeb1_SaveCommand(ByVal sender As Object, ByVal e As System.EventArgs) Handles GridWeb1.SaveCommand

    Try

        'Getting the modified data of worksheet as a DataSet

        Dim dataset As DataSet = CType(GridWeb1.WorkSheets(0).DataSource, DataSet)

        'Updating database according to modified DataSet

        oleDbDataAdapter1.Update(dataset)

    Finally

        'Closing database connection

        oleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}

GridWeb1_SaveCommand etkinlik işleyicisine eklenen kodu da kontrol edebilirsiniz
**GridWeb1_SaveCommand etkinlik işleyicisine eklenen kod** 

![todo:image_alt_text](binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer_34.png)

Şimdi **Kaydet** düğmesini kullanarak veritabanındaki değişiklikleri kesinlikle kaydeder.
## **Sonuç**
{{% alert color="primary" %}} 

Veri bağlama, Aspose.Cells.GridWeb'in önemli bir özelliğidir. Aspose.Cells.GridWeb'in sunduğu Çalış Sayfaları Tasarımcısı aracılığıyla çalış sayfalarını veritabanına kolayca bağlayabilirsiniz. Aspose.Cells.GridWeb güçlü Grid çözümleri oluştururken zaman ve çaba kazandırır. 

{{% /alert %}}
