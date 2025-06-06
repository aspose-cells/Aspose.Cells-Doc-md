---
title: Regroupement des données
type: docs
weight: 10
url: /fr/net/grouping-data/
---

Dans certains rapports Excel, vous devrez peut-être fractionner les données en groupes pour les rendre plus faciles à lire et à analyser. L'un des principaux objectifs de la division des données en groupes est d'effectuer des calculs (effectuer des opérations de synthèse) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper vos données par champ(s) et de placer des lignes de synthèse entre les ensembles de données ou les groupes de données. Par exemple, si vous regroupez des données par Clients.CustomerID, vous pouvez ajouter un enregistrement de synthèse à chaque changement de groupe.

Les extraits de code exemple suivants montrent comment regrouper des données dans un rapport Excel à l'aide de marqueurs intelligents.
## **Paramètres**
Voici certains des paramètres de marqueurs intelligents utilisés pour le regroupement de données.
**group:normal/merge/repeat**

Nous supportons trois types de regroupement entre lesquels vous pouvez choisir.

- normal - La valeur du champ de regroupement n'est pas répétée pour les enregistrements correspondants dans la colonne; au lieu de cela, elle est imprimée une fois par groupe de données.
- fusionner - Le même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules dans le champ de regroupement pour chaque ensemble de groupes.
- répéter - La valeur du champ de regroupement est répétée pour les enregistrements correspondants.

Si vous avez plusieurs paramètres, séparez-les par des virgules, mais sans espace : paramètreA, paramètreB, paramètreC
### **Exemple**
Cet exemple illustre certains des paramètres de regroupement en action. Il utilise la base de données Microsoft Access Northwind.mdb et extrait des données de la table nommée "Détails de commande". Nous créons un fichier de conception appelé SmartMarker_Designer.xls dans Microsoft Excel et plaçons des marqueurs intelligents dans différentes cellules des feuilles de calcul. Les marqueurs sont traités pour remplir les feuilles de calcul. Les données sont placées et organisées par un champ de regroupement.

Le fichier de conception comporte deux feuilles de calcul. Dans la première, nous plaçons des marqueurs intelligents avec des paramètres de regroupement comme indiqué dans la capture d'écran ci-dessous. Trois marqueurs intelligents (avec des paramètres de regroupement) sont placés :
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(sous-total9:Order Details.OrderID), et
&=Order Details.UnitPrice(sous-total9:Order Details.OrderID) vont dans A5, B5 et C5 respectivement.

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
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
