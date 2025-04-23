---
title: Importation à partir de DataTable
type: docs
weight: 40
url: /fr/net/importing-from-datatable/
---

Les développeurs peuvent importer des données à partir d'un **DataTable** dans leurs feuilles de calcul en appelant la méthode **ImportDataTable** de la collection Cells. Il existe de nombreuses versions surchargées de la méthode **ImportDataTable**, mais une surcharge typique prend les paramètres suivants: **DataTable**, qui représente l'objet **DataTable** dont le contenu doit être importé

- **Indiquer le nom du champ**: spécifie si les noms des colonnes du DataTable doivent être importés dans la feuille de calcul en tant que première ligne ou non
- **Cellule de départ**: représente le nom de la cellule de départ (c.-à-d. "A1") à partir de laquelle importer le contenu du DataTable

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save("Import From Data Table.xls");

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Import.to.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
