---
title: Colonnes contenant des données non fortement typées
type: docs
weight: 10
url: /fr/net/columns-containing-non-strongly-typed-data/
---

Si toutes les valeurs dans les colonnes d'une feuille de calcul ne sont pas fortement typées (ce qui signifie que les valeurs dans une colonne peuvent avoir des types de données différents), alors nous pouvons exporter le contenu de la feuille de calcul en appelant la méthode **ExportDataTableAsString** de la classe Cells. La méthode **ExportDataTableAsString** prend le même ensemble de paramètres que la méthode **ExportDataTable** pour exporter les données de la feuille de calcul en tant qu'objet **DataTable**.

{{< highlight csharp >}}

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

Ci-dessous se trouvent les captures d'écran :

![todo:image_alt_text](picture1.png)

![todo:image_alt_text](picture2.png)

## **Télécharger le code source d'exemple**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Export.from.Worksheet.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
