---
title: Importieren aus ArrayList
type: docs
weight: 20
url: /de/net/importing-from-arraylist/
---
 Entwickler können Daten aus einer ArrayList in ihre Arbeitsblätter importieren, indem sie die aufrufen**ArrayListe importieren** Methode der Sammlung Cells. Die ImportArray-Methode akzeptiert die folgenden Parameter:**Anordnungsliste** , stellt das ArrayList-Objekt dar, dessen Inhalt importiert werden muss

- Zeilennummer stellt die Zeilennummer der ersten Zelle dar, in die die Daten importiert werden
- Spaltennummer stellt die Spaltennummer der ersten Zelle dar, in die die Daten importiert werden
- Is Vertical , ein boolescher Wert, der angibt, dass Daten vertikal oder horizontal importiert werden

{{< highlight "csharp" >}}

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
