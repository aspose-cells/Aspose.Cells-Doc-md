---
title: Veri Gruplama
type: docs
weight: 10
url: /tr/net/grouping-data/
---

Bazı Excel raporlarında verileri okumayı ve analiz etmeyi kolaylaştırmak için verileri gruplara ayırmanız gerekebilir. Verileri gruplara ayırmak için temel amaçlardan biri, her kayıt grubu üzerinde hesaplamaları (özet operasyonları gerçekleştirmek) çalıştırmaktır.

Aspose.Cells akıllı işaretçiler, verilerinizi alan(lar)ına göre gruplamayı ve veri setleri veya veri grupları arasına özet satırlar yerleştirmeyi sağlar. Örneğin, Müşteriler.CustomerID'ye göre veri gruplama yapıyorsanız, her grup değiştiğinde bir özet kaydı ekleyebilirsiniz.

Aşağıdaki kod örnekleri, akıllı işaretçiler kullanarak bir Excel raporunda veri gruplamasının nasıl yapıldığını göstermektedir.
## **Parametreler**
Veri gruplama için kullanılan bazı akıllı işaretçi parametreleri aşağıda verilmiştir.
**group:normal/merge/repeat**

Seçebileceğiniz üç tür gruplamayı destekliyoruz.

- normal - Gruplama alan(aları) değeri sütundaki ilgili kayıtlar için tekrarlanmaz; bunun yerine her veri grubu için bir kez yazdırılırlar.
- birleştirme - normal parametresi için aynı davranış, ancak her grup seti için gruplama alan(aları) hücrelerini birleştirir.
- tekrar - Gruplama alan(aları) değeri ilgili kayıtlar için tekrarlanır.

Birden fazla parametreniz varsa, bunları virgülle ayırın, ancak boşluk bırakmayın: parametreA,parametreB,parametreC
### **Örnek**
Bu örnek, gruplama parametrelerinin işleyişi hakkında bilgi vermektedir. Microsoft Access veritabanından Northwind.mdb kullanır ve "Order Details" adlı tablodan veri çıkarır. Microsoft Excel'de SmartMarker_Designer.xls adında bir tasarım dosyası oluşturur ve işlem için sayfalara akıllı işaretçiler yerleştirir. İşaretçiler, çalışma sayfalarını doldurmak için işlenir. Veriler gruplandırılır ve düzenlenir.

Tasarım dosyasında iki çalışma sayfası bulunmaktadır. İlk çalışma sayfasına aşağıdaki ekran görüntüsünde gösterildiği gibi gruplama parametreleriyle akıllı işaretçiler yerleştiririz. Üç akıllı işaretçi (gruplama parametreleri ile birlikte) yerleştirilir:
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID), ve
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) A5, B5 ve C5'e sırasıyla girilir.

{{< highlight csharp >}}

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
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
