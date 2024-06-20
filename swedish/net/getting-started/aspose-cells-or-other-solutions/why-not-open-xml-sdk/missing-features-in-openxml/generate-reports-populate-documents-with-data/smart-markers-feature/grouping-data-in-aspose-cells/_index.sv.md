---
title: Gruppering av data i Aspose.Cells
type: docs
weight: 10
url: /sv/net/grouping-data-in-aspose-cells/
---

I vissa Excel-rapporter kan du behöva bryta upp datan i grupper för att göra det lättare att läsa och analysera. Ett av de primära syftena med att bryta upp data i grupper är att köra beräkningar (utföra sammanfattande operationer) på varje grupp av poster.

Aspose.Cells smarta markörer tillåter dig att gruppera dina data efter fält och placera sammanfattande rader mellan datauppsättningar eller datagrupper. Till exempel, om du grupperar data efter Kunder.CustomerID, kan du lägga till en sammanfattande post varje gång gruppen ändras.

De exempelkodsnuttar som följer visar hur man grupperar data i en Excel-rapport med smarta markörer.
## **Parametrar**
Här är några av de smarta markörsparametrar som används för att gruppera data.
**group:normal/merge/repeat**

Vi stödjer tre typer av grupper som du kan välja mellan.

- normal - Grupperingen efter fältens värde upprepas inte för de motsvarande posterna i kolumnen; istället skrivs de ut en gång per datagrupp.
- sammanfoga - Samma beteende som för det normala parametern, förutom att den sammanfogar cellerna i fälten för varje gruppsats.
- repeat - Fältet/gruppfältet värdet är upprepat för de motsvarande posterna.

Om du har flera parametrar, separera dem med kommatecken, men inget mellanrum: parameterA, parameterB, parameterC
### **Exempel**
Det här exemplet visar några av gruppfunktionerna i aktion. Det använder Microsoft Access-databasen Northwind.mdb och extraherar data från tabellen som heter "Order Details". Vi skapar en designerfil som heter SmartMarker_Designer.xls i Microsoft Excel och placerar smarta markörer i olika celler i kalkylbladen. Markörerna bearbetas för att fylla i kalkylbladen. Data placeras och organiseras efter ett gruppfält.

Designfilen har två kalkylblad. På första kalkylbladet placerar vi smarta markörer med gruppindata som visas i skärmbilden nedan. Tre smarta markörer (med gruppfunktioner) placeras:
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID), och
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) placeras i A5, B5 och C5 respektive.

{{< highlight csharp >}}

 //Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

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

wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save("outSmartMarker_Designer.xls");

{{< /highlight >}}
## **Ladda ned provkoden**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
