---
title: Importera från ArrayList
type: docs
weight: 20
url: /sv/net/importing-from-arraylist/
---

Utvecklare kan importera data från en ArrayList till sina kalkylblad genom att anropa metoden **ImportArrayList** i Cells-samlingen. ImportArray metoden tar följande parametrar: **ArrayList** , representerar ArrayList-objektet vars innehåll behöver importeras

- Radnummer , representerar radnumret för den första cellen där datan kommer att importeras
- Kolumnnummer , representerar kolumnnumret för den första cellen där datan kommer att importeras
- Är Vertikal , ett booleskt värde som specificerar att importera data vertikalt eller horisontellt

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
{{< app/cells/assistant language="csharp" >}}
