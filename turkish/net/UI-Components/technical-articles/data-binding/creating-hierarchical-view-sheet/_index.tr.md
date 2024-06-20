---
title: Hiyerarşik Görünüm Sayfası Oluşturma
type: docs
weight: 30
url: /tr/net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb,hiyerarşik
description: Bu makale, GridWeb de hiyerarşik görünüm oluşturmayı tanıtıyor.
---

{{% alert color="primary" %}} 

Veri bağlama güçlü ve kullanıcı dostu bir GridWeb özelliğidir. Veritabanı tablolarında depolanan veriler bir DataSet'e getirilir ve verilerle doldurulur 

veri tablolarını temsil eder. Veri bağlama özelliği kullanılarak, ilişkilendirilmiş verilerin hiyerarşik bir görünümünü (ana-çocuk görünümü) oluşturabilir ve 

onları daha zarif hale getirmek için kontrolde görüntüleyebilirsiniz. 

Bu konu hiyerarşik görünüm sayfası oluşturmayı tartışmaktadır. Sayfanın bazı satırlarının alt özelliği vardır. Bir kullanıcı satırın **Genişlet**

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**Hiyerarşik görünümü olan tablo** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **DataTable'lar İçin İlişkiler Oluşturma**
Örneğin, ADO.Net API'sını kullanarak veritabanı tablolarından veri çekersiniz. Hiyerarşik görünüm sayfası oluşturmak için öncelikle bir DataSet

nesnesi tasarlamalısınız ve önce bunlar arasında bir ilişki oluşturmalısınız. İlişkiyi oluşturmak için VS.NET'in **DataSet Tasarımcısı**'nı kullanın. Bu 

örnekte üç DataTable bulunmaktadır: Customers, Orders, Order Details. Sayfa varsayılan olarak tüm müşteri bilgilerini gösterir. Kullanıcı bir müşteriyi genişlettiğinde, 

çalış sayfası o müşterinin verdiği tüm siparişleri gösterir. Kullanıcı bir siparişi genişlettiğinde, çalış sayfası siparişin detaylarını gösterir. Veri hiyerarşiktir: 

sipariş detayları siparişlerin altında listelenir ve siparişler müşterilerin altında listelenir.

Bu çalışabilmesi için veri tabloları arasında aşağıdaki ilişkilerin oluşturulması gerekmektedir:

1. Orders DataTable'e bir dış anahtar oluşturun, anahtar alanı CustomerID'dir 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Order Details DataTable'e bir dış anahtar oluşturun, anahtar alanı OrderID'dir. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



DataSet Tasarımcısı şimdi şu şekilde görünüyor: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Çalış Sayfası Bağlama**
Şimdi **Çalış Sayfaları Tasarımcısı**'nı kullanarak çalış sayfası için DataSource ve DataMember'ı ayarlayın ve veri alanı bağlama sütunlarını yapılandırın. 

Kontrol, genellikle bir DataRowView nesnesi olan bağlama nesnesine ait her kayıt için bir + simgesi ekler. + simgesine tıklandığında, kayıt çocuk görünümünü göstermek üzere genişler. Aşağıdaki örnek, **Çalış Sayfaları Tasarımcısı**'nı kullanarak bağlama 

alt görünümler. + simgesine tıklandığında, kayıt genişleyerek alt görünümü gösterir. Aşağıdaki örnek, **Çalışsayılar Tasarımcısı**'nı bağlamak için kullanılır 

Kök üst ebeveyn DataTable Müşterilerine çalışma sayfası. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Çocuk Tabloları Bağlama Sütunlarını Özelleştirmek**
Kontrol, geliştiricilerin çocuk tabloların bağlama sütunlarını özelleştirmek için kullandığı GridWeb.BindingChildView adında bir etkinlik sağlar. Bu örnek 

gereksinimi, bağlama sütununun numara formatını değiştirmek için bir olay işleyici eklemektir ve sipariş ayrıntıları **UnitPrice** alanını bir para birimi formatında görüntülemektir. 

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Verileri Veritabanından Yükleme ve Bağlama**
Aşağıdaki [GridWeb'in Çalışsayfası Tasarımcısı kullanarak Dataset'e Çalışsayfası Bağlama](/cells/tr/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/)'nda açıklandığı gibi,
bir sonraki adımda, veritabanından veri yüklemek ve Dataset'i çalışma sayfasına bağlamak için Page_Load bloğuna kod eklemeniz gerekmektedir. 

Asppose.Grid.Web.Data.WebWorksheet Sınıfı bazı kullanışlı özelliklere sahiptir. 

- Örneğin, **EnableCreateBindColumnHeader** özelliği, tablo içindeki bağlı sütun başlıklarını oluşturmak için kullanılır veya sütun başlıkları bağlı sütun

- Örneğin, EnableCreateBindColumnHeader özelliği, çalışma sayfası içinde bağlı sütunun başlıklarını oluşturmak için kullanılır veya sütun

adlarını gösterir. Bu **true** veya **false** değerlerini alır. 

- **BindStartRow** ve **BindStartColumn** özellikleri, kaynağın GridWeb kontrol sayfasındaki konumunu belirtir.
- **EnableExpandChildView** özelliği, çalışsayfa için genişletilmiş çocuk görünümünü devre dışı bırakmak için kullanılır. Varsayılan olarak **true** olarak ayarlıdır.

Sınıfın bazı kullanışlı yöntemleri de vardır. 

- **DataBind()** yöntemi bir sayfayı kaynağa bağlar.
- **CreateNewBindRow()** yeni bir satır ekler ve onu veri kaynağına bağlar.
- **DeleteBindRow()** bağlı bir satırı siler.
- **SetRowExpand()** yöntemi genişletilmiş satırı ayarlar ve veri bağlama modunda çocuk görünüm içeriğini gösterir.
- **GetRowExpand()** yöntemi satırın genişletilip genişletilmediğini belirten bir Boolean değeri alır.

Aşağıdaki kodda, "dataSet21" adlı DataSet nesnesi üç tabloya dayalı verilerle doldurulur. Müşteriler tablosu, hiyerarşik görüntüde ilk tablo olacak şekilde filtrelenir. Ardından, "sheet" adında bir WebWorksheet nesnesi oluşturulup, sayfayı temizler ve ardından veri kaynağına bağlar. 

**VB.NET** 

GridDesktop Veri Bağlama Özelliğini Uygulama 

**C#**

{{< highlight csharp >}}

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

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

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

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

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
