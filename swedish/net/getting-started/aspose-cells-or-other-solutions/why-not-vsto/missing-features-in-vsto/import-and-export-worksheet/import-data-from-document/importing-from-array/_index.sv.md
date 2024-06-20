---
title: Importera från Array
type: docs
weight: 10
url: /sv/net/importing-from-array/
---

Utvecklare kan importera data från en array till sina kalkylblad genom att anropa metoden **ImportArray** i Cells-samlingen. Det finns många överbelastade versioner av metoden ImportArray men en typisk överbelastning tar följande parametrar:

- Array, representerar arrayobjektet vars innehåll behöver importeras
- Radnummer, representerar radnumret för den första cellen där datan kommer att importeras
- Kolumnnummer, representerar kolumnnumret för den första cellen där datan kommer att importeras
- Är Vertikal, ett booleskt värde som specificerar att importera data vertikalt eller horisontellt

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
