---
title: Hiyerarşik Görünüm Sayfası Oluşturma
type: docs
weight: 30
url: /tr/net/creating-hierarchical-view-sheet/
---
{{% alert color="primary" %}} 

 Veri bağlama, güçlü ve kullanıcı dostu bir GridWeb özelliğidir. Veritabanı tablolarında depolanan veriler bir DataSet'e getirilir ve verilerle doldurulur

 veri tablolarını temsil eder. Veri bağlama özelliğini kullanarak, birbirine bağlı verilerin hiyerarşik bir görünümünü (ana-alt görünüm) oluşturabilirsiniz ve

 daha zarif hale getirmek için kontrolde görüntüleyin.

 Bu konu, hiyerarşik bir görünüm sayfası oluşturmayı tartışır. Sayfadaki bazı satırlar alt görünümlere sahiptir. Kullanıcı satırı tıkladığında**Genişletmek**

 buton{{< emoticons/cross >}} , o satırın alt görünüm tablosu aşağı doğru genişletilir. Bu özellik, hiyerarşik bir görünüm raporu oluşturmak için çok yararlıdır.

**Hiyerarşik görünüme sahip bir tablo** 

![yapılacaklar:resim_alternatif_Metin](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **DataTable'lar için İlişkiler Oluşturma**
Örneğin, ADO.Net API'i kullanır ve veritabanı tablolarından veri çıkarırsınız. Hiyerarşik görünüm sayfası oluşturmak için bir DataSet tasarlamanız gerekir.

 bazı tablolara dayalı nesne ve önce aralarında bir ilişki oluşturun. VS.NET'leri kullanın**Veri Kümesi Tasarımcısı** ilişkiyi oluşturmak için. İçinde

 bu örnekte üç DataTable vardır: Müşteriler, Siparişler, Sipariş Ayrıntıları. Sayfa, tüm müşteri bilgilerini varsayılan olarak gösterir. Ne zaman

 kullanıcı bir müşteriyi genişletir, ızgara müşterinin verdiği tüm siparişleri gösterir. Kullanıcı bir siparişi genişlettiğinde, ızgara ayrıntıları gösterir

bu düzenin. Veriler hiyerarşiktir: sipariş detayları siparişler altında, siparişler ise müşteriler altında listelenir.

Bunun çalışması için, veri tabloları arasında aşağıdaki ilişkilerin kurulması gerekir:

1.  DataTable Siparişlerinde bir yabancı anahtar oluşturun, anahtar alanı CustomerID'dir.

![yapılacaklar:resim_alternatif_Metin](creating-hierarchical-view-sheet_2.png)




1. DataTable Sipariş Ayrıntılarında bir yabancı anahtar oluşturun, anahtar alanı OrderID'dir.

![yapılacaklar:resim_alternatif_Metin](creating-hierarchical-view-sheet_3.png)



 DataSet Tasarımcısı artık şöyle görünür:

![yapılacaklar:resim_alternatif_Metin](creating-hierarchical-view-sheet_4.png)
### **Bağlama Çalışma Sayfası**
 şimdi kullan**Çalışma Sayfaları Tasarımcısı** çalışma sayfası için DataSource ve DataMember'ı ayarlamak ve veri alanı bağlama sütunlarını yapılandırmak için.

 Denetim, bağlama nesnesi (genellikle bir DataRowView nesnesi) olan bir kayda karşılık gelen her satır için otomatik olarak bir + simgesi ekler.

 çocuk görünümleri. + simgesine tıklandığında, kayıt alt görünümü gösterecek şekilde genişler. Aşağıdaki örnek,**Çalışma Sayfaları Tasarımcısı** bağlamak için

 çalışma sayfasını kök üst DataTable Müşterilerine.

![yapılacaklar:resim_alternatif_Metin](creating-hierarchical-view-sheet_5.png)
### **Alt Tabloları Bağlama Sütunlarını Özelleştirme**
 Denetim, geliştiricilerin alt tabloların bağlama sütunlarını özelleştirmek için kullandıkları GridWeb.BindingChildView adlı bir olay sağlar. Bu örnek

 sipariş ayrıntılarını görüntülemesi gerekiyor'**Birim fiyat** para birimi biçiminde alan. Bağlama sütununun sayı biçimini değiştirmek için bir olay işleyici ekleyin.

**C#**

{{< highlight "csharp" >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Veritabanından ve Bağlamadan Veri Yükleme**
Açıklandığı gibi[GridWeb'in Worksheets Designer'ını kullanarak Çalışma Sayfasını bir DataSet'e Bağlama](/cells/tr/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
 bir veritabanından DataSet'e veri yüklemek için Page_Load bloğuna kod eklemeniz ve DataSet'i sayfaya bağlamanız gerekir.

 Sonraki adım.

Asppose.Grid.Web.Data.WebWorksheet Sınıfı bazı faydalı özelliklere sahiptir.

- Örneğin, EnableCreateBindColumnHeader özelliği, sayfadaki ilişkili sütunun başlıklarını veya sayfadaki sütunu oluşturmak için kullanılır.

 headers, ilişkili sütun adlarını görüntüler. Değerleri alır**doğru** veya**yanlış**. 

- BindStartRow ve BindStartColumn özellikleri, kaynağın bağlı olması gereken GridWeb denetimi sayfasındaki konumu belirtir.
- EnableExpandChildView özelliği, çalışma sayfası için genişletilmiş alt görünümü devre dışı bırakmak için kullanılır. Varsayılan olarak true olarak ayarlanmıştır.

 Sınıfın da bazı yararlı yöntemleri var.

- DataBind() yöntemi, bir sayfayı kaynağa bağlar.
- CreateNewBindRow() yeni bir satır ekler ve onu veri kaynağına bağlar.
- DeleteBindRow() ilişkili bir satırı siler.
- SetRowExpand() yöntemi, genişletilmiş satırı ayarlar ve alt görünüm içeriğini veri bağlama modunda gösterir.
- GetRowExpand() yöntemi, satırın genişletilip genişletilmediğini gösteren bir Boole değeri alır.

 Aşağıdaki kodda, "dataSet21" DataSet nesnesi, üç tabloya dayalı verilerle doldurulur. Müşteriler tablosu, bunu yapmak için filtrelenir.

 hiyerarşik görünümdeki ilk tablo. Önce sayfayı temizleyen ve ardından ayarlayan "sayfa" adlı bir WebWorksheet nesnesi oluşturulur.

 veri kaynağına bağlıdır.

**C#**

{{< highlight "csharp" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WebWorksheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight "csharp" >}}

 Özel Alt Sayfa_Yük(System.Object Olarak ByVal gönderen, System.EventArgs Olarak ByVal e) MyBase.Load İşler

 'Sayfayı başlatmak için kullanıcı kodunu buraya girin

 Değilse PostBack O Zaman

 BindWithoutInSheetHeaders()

 Eğer Sonlandır

Aboneliği Sonlandır

Özel Alt BindWithoutInSheetHeaders()

 DemoDatabase2 = Yeni DemoDatabase2() olarak db'yi azaltın

Yolu karart As String = MapPath(".")

 yol = yol.Substring(0, yol.LastIndexOf("\"))

 yol = yol.Substring(0, yol.LastIndexOf("\"))

 db.OleDbConnection1.ConnectionString = "Sağlayıcı=Microsoft.Jet.OLEDB.4.0;Veri Kaynağı=" + yol + "\Database\Northwind.mdb"

 Denemek

 Veritabanına bağlanır ve verileri getirir.

 ' Müşteriler Tablosu.

 db.OleDbDataAdapter1.Fill(DataSet21)

 ' Sipariş Tablosu.

 db.OleDbDataAdapter2.Fill(DataSet21)

 ' OrderDetailTable.

 db.OleDbDataAdapter3.Fill(DataSet21)

 Verileri filtrele

 DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WebWorksheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
