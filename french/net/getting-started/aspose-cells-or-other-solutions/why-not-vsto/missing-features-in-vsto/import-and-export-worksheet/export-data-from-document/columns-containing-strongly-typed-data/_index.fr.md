---
title: Colonnes contenant des données fortement typées
type: docs
weight: 20
url: /fr/net/columns-containing-strongly-typed-data/
---
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
