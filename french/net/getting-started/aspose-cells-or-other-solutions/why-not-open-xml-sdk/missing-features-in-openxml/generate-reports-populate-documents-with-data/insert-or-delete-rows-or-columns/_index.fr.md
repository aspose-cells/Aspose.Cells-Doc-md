---
title: Insérer ou supprimer des lignes ou des colonnes
type: docs
weight: 20
url: /fr/net/insert-or-delete-rows-or-columns/
---
Que nous créions une nouvelle feuille de calcul à partir de zéro ou que nous travaillions sur une feuille de calcul existante, nous devrons peut-être ajouter des lignes ou des colonnes supplémentaires dans la feuille de calcul pour accueillir plus de données ou pour une autre raison. Inversement, il peut également être nécessaire de supprimer des lignes ou des colonnes à partir de positions spécifiées de la feuille de calcul.
## **Gestion des lignes/colonnes**
**Aspose.Cells** fournit une classe Workbook qui représente un fichier Excel. La classe Workbook contient une collection Worksheets qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit une collection Cells qui représente toutes les cellules de la feuille de calcul.

**Cells**collection fournit plusieurs méthodes pour gérer les lignes ou les colonnes dans une feuille de calcul, quelques-unes d'entre elles sont décrites ci-dessous plus en détail.
## **Insertion d'une ligne**
 Les développeurs peuvent insérer une ligne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode InsertRow de la collection Cells.**Insérer une ligne** La méthode prend l'index de la ligne où la nouvelle ligne sera insérée.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Insertion de plusieurs lignes**
Parfois, les développeurs peuvent avoir besoin d'insérer plusieurs lignes dans la feuille de calcul. Cela peut être fait en appelant la méthode InsertRows de la collection Cells. La méthode InsertRows prend deux paramètres :

- **Index de ligne**, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées
- **Nombre de rangées**, nombre total de lignes à insérer

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Suppression d'une ligne**
 Les développeurs peuvent supprimer une ligne de la feuille de calcul à n'importe quel endroit en appelant le**Supprimer la ligne** méthode de la collection Cells.**Supprimer la ligne** prend l'index de la ligne à supprimer.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Suppression de plusieurs lignes**
Si les développeurs doivent supprimer plusieurs lignes de la feuille de calcul, cela peut également être fait en appelant la méthode DeleteRows de la collection Cells. La méthode DeleteRows prend deux paramètres :

- **Index de ligne**, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- **Nombre de rangées**, nombre total de lignes à supprimer.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Insertion d'une colonne**
Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode InsertColumn de la collection Cells. La méthode InsertColumn prend l'index de la colonne dans laquelle la nouvelle colonne sera insérée.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Supprimer une colonne**
Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, les développeurs peuvent appeler la méthode DeleteColumn de la collection Cells. La méthode DeleteColumn prend l'index de la colonne à supprimer.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
