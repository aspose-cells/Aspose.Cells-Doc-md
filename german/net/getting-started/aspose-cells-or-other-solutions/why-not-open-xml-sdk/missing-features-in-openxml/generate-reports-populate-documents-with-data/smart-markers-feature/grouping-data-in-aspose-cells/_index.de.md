---
title: Gruppierungsdaten in Aspose.Cells
type: docs
weight: 10
url: /de/net/grouping-data-in-aspose-cells/
---
In einigen Excel-Berichten müssen Sie die Daten möglicherweise in Gruppen aufteilen, um sie leichter lesen und analysieren zu können. Einer der Hauptzwecke für das Aufteilen von Daten in Gruppen ist das Ausführen von Berechnungen (Durchführen von Zusammenfassungsoperationen) für jede Gruppe von Datensätzen.

Aspose.Cells Mit intelligenten Markierungen können Sie Ihre Daten nach Feld(ern) gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen platzieren. Wenn Sie beispielsweise Daten nach Customers.CustomerID gruppieren, können Sie jedes Mal, wenn sich die Gruppe ändert, einen Zusammenfassungsdatensatz hinzufügen.

Die folgenden Beispiel-Codeausschnitte zeigen, wie Daten in einem Excel-Bericht mithilfe von intelligenten Markierungen gruppiert werden.
## **Parameter**
Im Folgenden sind einige der Smart-Marker-Parameter aufgeführt, die zum Gruppieren von Daten verwendet werden.
**Gruppe:normal/zusammenführen/wiederholen**

Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- normal - Der Gruppieren-nach-Feld(er)-Wert wird für die entsprechenden Datensätze in der Spalte nicht wiederholt; stattdessen werden sie einmal pro Datengruppe gedruckt.
- merge - Dasselbe Verhalten wie für den normalen Parameter, außer dass er die Zellen in den Gruppieren-nach-Feldern für jeden Gruppensatz zusammenführt.
- repeat - Der Gruppieren-nach-Feld(er)-Wert wird für die entsprechenden Datensätze wiederholt.

Wenn Sie mehrere Parameter haben, trennen Sie sie mit einem Komma, aber ohne Leerzeichen: ParameterA,ParameterB,ParameterC
### **Beispiel**
Dieses Beispiel zeigt einige der Gruppierungsparameter in Aktion. Es verwendet die Access-Datenbank Northwind.mdb Microsoft und extrahiert Daten aus der Tabelle mit dem Namen "Bestelldetails". Wir erstellen eine Designer-Datei mit dem Namen SmartMarker_Designer.xls in Microsoft Excel und platzieren intelligente Markierungen in verschiedenen Zellen in Arbeitsblättern. Die Markierungen werden verarbeitet, um die Arbeitsblätter zu füllen. Die Daten werden durch ein Gruppenfeld platziert und organisiert.

Die Designerdatei hat zwei Arbeitsblätter. In der ersten setzen wir intelligente Markierungen mit Gruppierungsparametern, wie im folgenden Screenshot gezeigt. Drei Smart-Marker (mit Gruppierungsparametern) werden platziert:
&=Bestelldetails.OrderID(group:merge,skip:1),
&=Bestelldetails.Menge(Zwischensumme9:Bestelldetails.BestellID) und
&=Bestelldetails.Einzelpreis(Zwischensumme9:Bestelldetails.Bestell-ID) gehen jeweils in A5, B5 und C5.

{{< highlight "csharp" >}}

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
## **Beispielcode herunterladen**
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
