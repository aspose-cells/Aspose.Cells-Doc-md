---
title: Importieren aus ArrayList
type: docs
weight: 20
url: /de/net/importing-from-arraylist/
---

Entwickler können Daten aus einem ArrayList in ihre Tabellenblätter importieren, indem sie die **ImportArrayList**-Methode der Cells-Sammlung aufrufen. Die ImportArray Methode nimmt die folgenden Parameter an: **ArrayList** , repräsentiert das ArrayList-Objekt, dessen Inhalt importiert werden muss

- Zeilennummer , repräsentiert die Zeilennummer der ersten Zelle, in die die Daten importiert werden
- Spaltennummer , repräsentiert die Spaltennummer der ersten Zelle, in die die Daten importiert werden
- Ist vertikal , ein boolescher Wert, der angibt, ob die Daten vertikal oder horizontal importiert werden sollen

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
