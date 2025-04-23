---
title: Importation à partir d un tableau
type: docs
weight: 10
url: /fr/net/importing-from-array/
---

Les développeurs peuvent importer des données d'un tableau dans leurs feuilles de calcul en appelant la méthode **ImportArray** de la collection Cells. Il existe de nombreuses versions surchargées de la méthode ImportArray, mais une surcharge typique prend les paramètres suivants :

- Array, représente l'objet tableau dont les contenus doivent être importés
- Numéro de ligne, représente le numéro de ligne de la première cellule où les données seront importées
- Numéro de colonne, représente le numéro de colonne de la première cellule où les données seront importées
- Est Vertical, une valeur booléenne qui spécifie l'importation des données verticalement ou horizontalement

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array.xls");

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
