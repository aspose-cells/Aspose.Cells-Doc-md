---
title: Importation à partir d un ArrayList
type: docs
weight: 20
url: /fr/net/importing-from-arraylist/
---

Les développeurs peuvent importer des données à partir d'un ArrayList dans leurs feuilles de calcul en appelant la méthode **ImportArrayList** de la collection Cells. La méthode ImportArray prend les paramètres suivants : **ArrayList** , représente l'objet ArrayList dont les contenus doivent être importés

- Numéro de ligne , représente le numéro de ligne de la première cellule où les données seront importées
- Numéro de colonne , représente le numéro de colonne de la première cellule où les données seront importées
- Est Vertical , une valeur booléenne qui spécifie l'importation des données verticalement ou horizontalement

{{< highlight csharp >}}

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

workbook.Save("DataImport from Array List.xls");


{{< /highlight >}}
