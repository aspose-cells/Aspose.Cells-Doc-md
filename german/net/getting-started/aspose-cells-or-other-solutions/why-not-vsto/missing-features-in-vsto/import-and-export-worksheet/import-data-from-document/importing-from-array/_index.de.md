---
title: Importieren aus Array
type: docs
weight: 10
url: /de/net/importing-from-array/
---

Entwickler können Daten aus einem Array in ihre Tabellenblätter importieren, indem sie die Methode **ImportArray** der Cells-Sammlung aufrufen. Es gibt viele überladene Versionen der ImportArray Methode, aber eine typische Überladung nimmt die folgenden Parameter an:

- Array, repräsentiert das Array-Objekt, dessen Inhalt importiert werden muss
- Zeilennummer, repräsentiert die Zeilennummer der ersten Zelle, in die die Daten importiert werden
- Spaltennummer, repräsentiert die Spaltennummer der ersten Zelle, in die die Daten importiert werden
- Ist vertikal, ein boolescher Wert, der angibt, ob die Daten vertikal oder horizontal importiert werden sollen

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
