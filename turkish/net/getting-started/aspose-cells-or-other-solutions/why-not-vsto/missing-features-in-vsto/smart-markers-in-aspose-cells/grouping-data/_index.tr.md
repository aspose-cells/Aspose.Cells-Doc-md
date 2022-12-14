---
title: Verileri Gruplandırma
type: docs
weight: 10
url: /tr/net/grouping-data/
---
Bazı Excel raporlarında, okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmanın birincil amaçlarından biri, her bir kayıt grubu üzerinde hesaplamalar yapmaktır (özet işlemleri gerçekleştirmek).

Aspose.Cells akıllı işaretleyiciler, verilerinizi alan(lar)a göre gruplandırmanıza ve veri kümeleri veya veri grupları arasına özet satırlar yerleştirmenize olanak tanır. Örneğin, verileri Customers.CustomerID'ye göre gruplandırıyorsanız, grup her değiştiğinde bir özet kayıt ekleyebilirsiniz.

Aşağıdaki örnek kod parçacıkları, akıllı işaretçiler kullanılarak bir Excel raporundaki verilerin nasıl gruplanacağını gösterir.
## **parametreler**
Aşağıda, verileri gruplandırmak için kullanılan akıllı işaretçi parametrelerinden bazıları verilmiştir.
**grup:normal/birleştir/tekrarla**

Aralarından seçim yapabileceğiniz üç tür grubu destekliyoruz.

- normal - Alanlara göre grup değeri, sütundaki karşılık gelen kayıtlar için tekrarlanmaz; bunun yerine veri grubu başına bir kez yazdırılırlar.
- birleştirme - Her grup kümesi için alan(lar)a göre gruptaki hücreleri birleştirme dışında normal parametreyle aynı davranış.
- tekrar - Alanlara göre grup değeri ilgili kayıtlar için tekrarlanır.

Birden fazla parametreniz varsa, bunları virgülle ayırın ancak boşluk kullanmayın: parameterA,parameterB,parameterC
### **Örnek**
Bu örnek, eylem halindeki bazı gruplandırma parametrelerini göstermektedir. Northwind.mdb Microsoft Access veritabanını kullanır ve "Sipariş Ayrıntıları" adlı tablodan veri çıkarır. Microsoft Excel'de SmartMarker_Designer.xls adlı bir tasarımcı dosyası oluşturuyoruz ve çalışma sayfalarında çeşitli hücrelere akıllı işaretleyiciler yerleştiriyoruz. İşaretçiler, çalışma sayfalarını doldurmak için işlenir. Veriler bir grup alanı tarafından yerleştirilir ve düzenlenir.

Tasarımcı dosyasında iki çalışma sayfası vardır. İlkinde, aşağıdaki ekran görüntüsünde gösterildiği gibi gruplama parametrelerine sahip akıllı işaretçiler koyduk. Üç akıllı işaretçi (gruplama parametreleriyle birlikte) yerleştirilir:
&=Sipariş Ayrıntıları.SiparişKimliği(grup:birleştir,atla:1),
&=Sipariş Ayrıntıları.Miktar(ara toplam9:Sipariş Ayrıntıları.SiparişKimliği) ve
&=Sipariş Ayrıntıları.BirimFiyat(alt toplam9:Sipariş Ayrıntıları.SiparişKimliği) sırasıyla A5, B5 ve C5'e gider.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Grouping Data OLE DB.xlsx";

//Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=~\\..\\..\\..\\Data\\Northwind.mdb");

//Open the connection object.

con.Open();

//Create a command object and specify the SQL query.

OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

//Create a data adapter object.

OleDbDataAdapter da = new OleDbDataAdapter();

//Specify the command.

da.SelectCommand = cmd;

//Create a dataset object.

DataSet ds = new DataSet();

//Fill the dataset with the table records.

da.Fill(ds, "Order Details");

//Create a datatable with respect to dataset table.

DataTable dt = ds.Tables["Order Details"];

//Create WorkbookDesigner object.

WorkbookDesigner wd = new WorkbookDesigner();

//Open the template file (which contains smart markers).

wd.Workbook = new Workbook(FileName);

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save(FileName);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
