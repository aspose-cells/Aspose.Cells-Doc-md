---
title: Importer Exporter les données du document
type: docs
weight: 10
url: /fr/net/import-export-data-from-document/
---
## **Importer des données à partir d'un document**

Les données sont la collecte de faits bruts et nous créons des feuilles de calcul ou des rapports pour présenter ces faits bruts de manière plus significative. Normalement, nous ajoutons nous-mêmes des données aux feuilles de calcul, mais parfois, nous devons réutiliser les ressources de données existantes et voici le besoin d'importer des données dans des feuilles de calcul à partir de différentes sources de données. Dans cette rubrique, nous aborderons certaines techniques permettant d'importer des données dans des feuilles de calcul à partir de différentes sources de données.

## **Importation de données à l'aide de Aspose.Cells**

 Lorsque vous utilisez**Aspose.Cells** pour ouvrir un fichier Excel, toutes les données du fichier sont automatiquement importées mais Aspose.Cells prend également en charge l'importation de données à partir de différentes sources de données. Quelques-unes de ces sources de données sont répertoriées ci-dessous :

- **Déployer**
- **Liste des tableaux**
- **Tableau de données**
- **ColonneDonnées**
- **Affichage des données**
- **Grille de données**
- **Lecteur de données**
- **GridView**

 Aspose.Cells fournit une classe,**Cahier** qui représente un fichier Excel. La classe Workbook contient une collection Worksheets qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit une collection Cells.

La collection Cells fournit des méthodes très utiles pour importer des données à partir de différentes sources de données.

### **Importation à partir d'un tableau**

 Les développeurs peuvent importer des données d'un tableau dans leurs feuilles de calcul en appelant le**ImporterTableau** méthode de la collection Cells. Il existe de nombreuses versions surchargées de la méthode ImportArray, mais une surcharge typique prend les paramètres suivants :

- Array, représente l'objet tableau dont le contenu doit être importé
- Numéro de ligne, représente le numéro de ligne de la première cellule où les données seront importées
- Numéro de colonne, représente le numéro de colonne de la première cellule où les données seront importées
- Est vertical, une valeur booléenne qui spécifie d'importer des données verticalement ou horizontalement

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **Importation depuis ArrayList**

 Les développeurs peuvent importer des données d'une ArrayList dans leurs feuilles de calcul en appelant le**ImportArrayListImportArrayListImportArrayList** méthode de la collection Cells. La méthode ImportArray prend les paramètres suivants :**Liste des tableaux** , représente l'objet ArrayList dont le contenu doit être importé

- Numéro de ligne , représente le numéro de ligne de la première cellule où les données seront importées
- Numéro de colonne , représente le numéro de colonne de la première cellule où les données seront importées
- Est Vertical , une valeur booléenne qui spécifie d'importer des données verticalement ou horizontalement

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **Importation à partir d'objets personnalisés**

 Les développeurs peuvent importer des données d'une collection d'objets vers une feuille de calcul à l'aide de**ImportCustomObjects**. Vous pouvez fournir une liste de colonnes/propriétés à la méthode pour afficher la liste d'objets souhaitée.

{{< highlight "csharp" >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **Importation depuis DataTable**

 Les développeurs peuvent importer des données à partir d'un**Tableau de données** à leurs feuilles de travail en appelant le**ImportDataTable** méthode de la collection Cells. Il existe de nombreuses versions surchargées du**ImportDataTable** mais une surcharge typique prend les paramètres suivants :**Tableau de données** , représente le**Tableau de données** objet dont le contenu doit être importé

- **Le nom du champ est-il affiché**, spécifie si les noms des colonnes de DataTable doivent être importés dans la feuille de calcul en tant que première ligne ou non
- **Début Cell** représente le nom de la cellule de départ (c'est-à-dire "A1") à partir de laquelle importer le contenu du DataTable

{{< highlight "csharp" >}}

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

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **Télécharger l'exemple de code**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Exporter les données du document**

 Aspose.Cells permet non seulement à ses utilisateurs d'importer des données dans des feuilles de calcul à partir de sources de données externes, mais leur permet également d'exporter leurs données de feuille de calcul vers un**Tableau de données** . Comme nous savons que**Tableau de données** fait partie de ADO.NET et est utilisé pour stocker des données. Une fois les données stockées dans un**Tableau de données**, il peut être utilisé de n'importe quelle manière selon les exigences des utilisateurs.

## **Exportation de données vers DataTable (.NET) à l'aide de Aspose.Cells**

Les développeurs peuvent facilement exporter leurs données de feuille de calcul vers un objet DataTable en appelant la méthode ExportDataTable ou ExportDataTableAsString de la classe Cells. Les deux méthodes sont utilisées dans différents scénarios, qui sont discutés ci-dessous plus en détail.

### **Colonnes contenant des données fortement typées**

Nous savons qu'une feuille de calcul stocke les données sous la forme d'une séquence de lignes et de colonnes. Si toutes les valeurs des colonnes d'une feuille de calcul sont fortement typées (cela signifie que toutes les valeurs d'une colonne doivent avoir le même type de données), nous pouvons exporter le contenu de la feuille de calcul en appelant le**ExporterTableDeDonnées** méthode de la classe Cells.**ExporterTableDeDonnées** prend les paramètres suivants pour exporter les données de la feuille de calcul en tant que**Tableau de données** objet:**Numéro de ligne** , représente le numéro de ligne de la première cellule à partir de laquelle les données seront exportées

- **Numéro de colonne** , représente le numéro de colonne de la première cellule à partir de laquelle les données seront exportées
- **Nombre de rangées** , représente le nombre de lignes à exporter
- **Le nombre de colonnes** représente le nombre de colonnes à exporter
- **Exporter les noms de colonne** , une propriété booléenne qui indique si les données de la première ligne de la feuille de calcul doivent être exportées en tant que noms de colonne du DataTable ou non

{{< highlight "csharp" >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

### **Colonnes contenant des données non fortement typées**

 Si toutes les valeurs des colonnes d'une feuille de calcul ne sont pas fortement typées (cela signifie que les valeurs d'une colonne peuvent avoir des types de données différents), nous pouvons exporter le contenu de la feuille de calcul en appelant le**ExportDataTableAsString** méthode de la classe Cells.**ExportDataTableAsString** prend le même ensemble de paramètres que celui de**ExporterTableDeDonnées** méthode pour exporter des données de feuille de calcul en tant que**Tableau de données** objet.

{{< highlight "csharp" >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Télécharger l'exemple de code**

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
