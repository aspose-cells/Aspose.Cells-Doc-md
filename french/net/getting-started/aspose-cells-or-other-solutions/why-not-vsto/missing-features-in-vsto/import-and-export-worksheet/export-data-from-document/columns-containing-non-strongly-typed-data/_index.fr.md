---
title: Colonnes contenant des données non fortement typées
type: docs
weight: 10
url: /fr/net/columns-containing-non-strongly-typed-data/
---
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

Ci-dessous les captures d'écran :

![tâche : image_autre_texte](picture1.png)

![tâche : image_autre_texte](picture2.png)

## **Télécharger l'exemple de code**

- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
