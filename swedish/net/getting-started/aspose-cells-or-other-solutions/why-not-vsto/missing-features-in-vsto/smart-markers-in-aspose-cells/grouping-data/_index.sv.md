---
title: Gruppera data
type: docs
weight: 10
url: /sv/net/grouping-data/
---
I vissa Excel-rapporter kan du behöva dela upp data i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att dela upp data i grupper är att köra beräkningar (utföra sammanfattningar) på varje grupp av poster.

Aspose.Cells smarta markörer låter dig gruppera dina data efter fält och placera sammanfattningsrader mellan datamängder eller datagrupper. Om du till exempel grupperar data efter Customers.CustomerID, kan du lägga till en sammanfattningspost varje gång gruppen ändras.

Exempelkodavsnitten som följer visar hur man grupperar data i en Excel-rapport med hjälp av smarta markörer.
## **Parametrar**
Nedan följer några av de smarta markörparametrarna som används för att gruppera data.
**grupp:normal/sammanfoga/upprepa**

Vi stödjer tre typer av grupper som du kan välja mellan.

- normal - Värdet för grupp efter fält upprepas inte för motsvarande poster i kolumnen; istället skrivs de ut en gång per datagrupp.
- merge - Samma beteende som för den normala parametern, förutom att den slår samman cellerna i gruppen efter fält för varje gruppuppsättning.
- repeat - Värdet för grupp efter fält upprepas för motsvarande poster.

Om du har flera parametrar, separera dem med ett kommatecken, men inget mellanslag: parameterA,parameterB,parameterC
### **Exempel**
Det här exemplet visar några av grupperingsparametrarna i funktion. Den använder Northwind.mdb Microsoft Access-databasen och extraherar data från tabellen med namnet "Order Details". Vi skapar en designerfil som heter SmartMarker_Designer.xls i Microsoft Excel och lägger in smarta markörer i olika celler i kalkylblad. Markörerna bearbetas för att fylla kalkylbladen. Data placeras och organiseras av ett gruppfält.

Designerfilen har två kalkylblad. I den första lägger vi smarta markörer med grupperingsparametrar som visas i skärmdumpen nedan. Tre smarta markörer (med grupperingsparametrar) placeras:
&=Beställningsinformation.OrderID(grupp:sammanfoga,hoppa över:1),
&=Orderdetaljer.Quantity(delsumma9:Orderdetaljer.OrderID), och
&=Orderdetaljer.Enhetspris(delsumma9:Orderdetaljer.OrderID) går in i A5, B5 respektive C5.

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
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
