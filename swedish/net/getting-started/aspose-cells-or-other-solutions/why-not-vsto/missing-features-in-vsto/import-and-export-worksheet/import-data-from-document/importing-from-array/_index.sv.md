---
title: Importerar från Array
type: docs
weight: 10
url: /sv/net/importing-from-array/
---
 Utvecklare kan importera data från en array till sina kalkylblad genom att anropa**ImportArray** metoden för samlingen Cells. Det finns många överbelastade versioner av ImportArray-metoden men en typisk överbelastning kräver följande parametrar:

- Array, representerar arrayobjektet vars innehåll måste importeras
- Radnummer, representerar radnumret för den första cellen där data kommer att importeras
- Kolumnnummer, representerar kolumnnumret för den första cellen där data kommer att importeras
- Is Vertical, ett booleskt värde som anger att data ska importeras vertikalt eller horisontellt

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

workbook.Save("DataImport from Array.xls");

{{< /highlight >}}
