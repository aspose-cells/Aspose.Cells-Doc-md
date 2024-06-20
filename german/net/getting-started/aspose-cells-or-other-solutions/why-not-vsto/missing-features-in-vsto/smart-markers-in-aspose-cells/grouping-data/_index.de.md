---
title: Daten gruppieren
type: docs
weight: 10
url: /de/net/grouping-data/
---

In einigen Excel-Berichten ist es möglicherweise erforderlich, die Daten in Gruppen aufzuteilen, um sie einfacher zu lesen und zu analysieren. Ein Hauptzweck, Daten in Gruppen aufzuteilen, besteht darin, Berechnungen (Zusammenfassungsoperationen) für jede Gruppe von Datensätzen auszuführen.

Mit Aspose.Cells Smart Markers können Sie Ihre Daten nach Feldern gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Daten-Gruppen platzieren. Wenn beispielsweise Daten nach Kunden.CustomerID gruppiert werden, können Sie bei jeder Änderung der Gruppe einen Zusammenfassungsdatensatz hinzufügen.

Die nachfolgenden Beispielcodes zeigen, wie Daten in einem Excel-Bericht mithilfe von Smart Markers gruppiert werden.
## **Parameter**
Im Folgenden sind einige der Smart-Marker-Parameter aufgeführt, die für die Gruppierung von Daten verwendet werden.
**group:normal/merge/repeat**

Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- normal - Der Gruppenwert wird nicht für die entsprechenden Datensätze in der Spalte wiederholt, sondern einmal pro Daten-Gruppe gedruckt.
- merge - Das gleiche Verhalten wie beim normal-Parameter, außer dass die Zellen in den Gruppenfeldern für jede Gruppe zusammengeführt werden.
- repeat - Der Gruppenwert wird für die entsprechenden Datensätze wiederholt.

Wenn Sie mehrere Parameter haben, trennen Sie diese mit Kommas, aber ohne Leerzeichen: parameterA,parameterB,parameterC.
### **Beispiel**
Dieses Beispiel zeigt einige der Gruppierungsparameter in Aktion. Es verwendet die Microsoft Access-Datenbank Northwind.mdb und extrahiert Daten aus der Tabelle "Order Details". Wir erstellen eine Designer-Datei namens SmartMarker_Designer.xls in Microsoft Excel und fügen Smart Marker in verschiedene Zellen in Arbeitsblättern ein. Die Marker werden verarbeitet, um die Arbeitsblätter auszufüllen. Die Daten werden anhand eines Gruppenfelds platziert und organisiert.

Die Designer-Datei hat zwei Arbeitsblätter. Im ersten Arbeitsblatt fügen wir Smart Marker mit Gruppierungsparametern gemäß dem untenstehenden Screenshot ein. Drei Smart Marker (mit Gruppierungsparametern) werden platziert:
&=Order Details.OrderID(group:merge,skip:1),
&=Bestelldetails.Menge(subtotal9:Bestelldetails.BestellID) und
&=Bestelldetails.Einzelpreis(subtotal9:Bestelldetails.BestellID) werden in A5, B5 und C5 entsprechend eingefügt.

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
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
