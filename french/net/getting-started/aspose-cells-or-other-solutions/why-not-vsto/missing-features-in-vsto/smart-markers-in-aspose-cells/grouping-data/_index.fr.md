---
title: Regroupement de données
type: docs
weight: 10
url: /fr/net/grouping-data/
---
Dans certains rapports Excel, vous devrez peut-être diviser les données en groupes pour en faciliter la lecture et l'analyse. L'un des principaux objectifs de la répartition des données en groupes est d'exécuter des calculs (effectuer des opérations récapitulatives) sur chaque groupe d'enregistrements.

Les marqueurs intelligents Aspose.Cells vous permettent de regrouper vos données par champ(s) et de placer des lignes récapitulatives entre les ensembles de données ou les groupes de données. Par exemple, si vous regroupez des données par Customers.CustomerID, vous pouvez ajouter un enregistrement récapitulatif chaque fois que le groupe change.

Les exemples d'extraits de code qui suivent montrent comment regrouper des données dans un rapport Excel à l'aide de marqueurs intelligents.
## **Paramètres**
Voici quelques-uns des paramètres de marqueur intelligent utilisés pour regrouper les données.
**groupe : normal/fusionner/répéter**

Nous prenons en charge trois types de groupes parmi lesquels vous pouvez choisir.

- normal - La valeur de regroupement par champ(s) n'est pas répétée pour les enregistrements correspondants dans la colonne ; au lieu de cela, ils sont imprimés une fois par groupe de données.
- merge - Le même comportement que pour le paramètre normal, sauf qu'il fusionne les cellules dans le(s) champ(s) group by pour chaque ensemble de groupe.
- répéter - La valeur de regroupement par champ(s) est répétée pour les enregistrements correspondants.

Si vous avez plusieurs paramètres, séparez-les par des virgules, mais sans espace : paramètreA, paramètreB, paramètreC
### **Exemple**
Cet exemple montre certains des paramètres de regroupement en action. Il utilise la base de données Access Northwind.mdb Microsoft et extrait les données de la table nommée "Détails de la commande". Nous créons un fichier de concepteur appelé SmartMarker_Designer.xls dans Microsoft Excel et plaçons des marqueurs intelligents dans diverses cellules des feuilles de calcul. Les marqueurs sont traités pour remplir les feuilles de travail. Les données sont placées et organisées par un champ de groupe.

Le fichier de concepteur comporte deux feuilles de calcul. Dans le premier, nous mettons des marqueurs intelligents avec des paramètres de regroupement, comme indiqué dans la capture d'écran ci-dessous. Trois marqueurs intelligents (avec des paramètres de regroupement) sont placés :
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID), et
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) vont respectivement dans A5, B5 et C5.

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
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
