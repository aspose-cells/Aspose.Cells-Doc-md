---
title: Importazione da Array
type: docs
weight: 10
url: /it/net/importing-from-array/
---

Gli sviluppatori possono importare dati da un array nei loro fogli di lavoro chiamando il metodo **ImportArray** della raccolta Cells. Ci sono molte versioni sovraccaricate del metodo ImportArray ma un sovraccarico tipico richiede i seguenti parametri:

- Array, rappresenta l'oggetto array i cui contenuti devono essere importati
- Numero di riga, rappresenta il numero di riga della prima cella dove i dati saranno importati
- Numero di colonna, rappresenta il numero di colonna della prima cella dove i dati saranno importati
- È Verticale, un valore booleano che specifica di importare i dati verticalmente o orizzontalmente

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
