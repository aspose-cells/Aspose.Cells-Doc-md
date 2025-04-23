---
title: Assembler les feuilles de calcul
type: docs
weight: 10
url: /fr/net/assemble-spreadsheets/
---

Cette section décrit comment :

Créer un nouveau fichier Excel à partir de zéro et ajouter une feuille de calcul.

- Ajouter des feuilles de travail à des feuilles de calcul.
- Accéder aux feuilles de calcul en utilisant le nom de la feuille.
- Supprimer une feuille de calcul d'un fichier Excel en utilisant son nom de feuille.
- Supprimer une feuille de calcul d'un fichier Excel en utilisant son indice de feuille.
- Aspose.Cells fournit une classe, Workbook qui représente un fichier Excel. La classe Workbook contient une collection Worksheets qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul.
## **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour créer un nouveau fichier Excel de manière programmatique:

- Créer un objet de la classe Workbook.
- Appeler la méthode Ajouter de la collection Worksheets. Une feuille de calcul vide est ajoutée au fichier Excel * automatiquement. Elle peut être référencée en passant l'index de feuille de la nouvelle feuille de calcul à la collection Worksheets.
- Obtenir une référence de feuille de calcul.
- Effectuer des tâches sur les feuilles de calcul.
- Enregistrer le nouveau fichier Excel avec de nouvelles feuilles de calcul en appelant la méthode Enregistrer de la classe Workbook.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Ajout de feuilles de calcul à une feuille de calcul Designer**
Le processus d'ajout de feuilles de calcul à une feuille de calcul prédéfinie est le même que celui d'ajout d'une nouvelle feuille de calcul, sauf que le fichier Excel existe déjà et doit être ouvert avant l'ajout des feuilles de calcul. Une feuille de calcul prédéfinie peut être ouverte avec la classe Workbook.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Accéder aux feuilles de calcul en utilisant le nom de la feuille**
Accéder ou obtenir n'importe quelle feuille de calcul en spécifiant son nom ou son indice.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Suppression des feuilles de calcul en utilisant le nom de la feuille**
Pour supprimer des feuilles de calcul d'un fichier, appelez la méthode RemoveAt de la collection Worksheets. Passez le nom de la feuille à la méthode RemoveAt pour supprimer une feuille spécifique.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**
La suppression des feuilles de calcul par leur nom fonctionne bien lorsque le nom de la feuille est connu. Si vous ne connaissez pas le nom de la feuille, utilisez une version surchargée de la méthode RemoveAt qui prend l'index de la feuille de calcul au lieu de son nom de feuille.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
