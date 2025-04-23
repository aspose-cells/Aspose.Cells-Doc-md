---
title: Importazione da ArrayList
type: docs
weight: 20
url: /it/net/importing-from-arraylist/
---

Gli sviluppatori possono importare dati da un ArrayList nei loro fogli di lavoro chiamando il metodo **ImportArrayList** della raccolta Cells. Il metodo ImportArray richiede i seguenti parametri: **ArrayList** , rappresenta l'oggetto ArrayList i cui contenuti devono essere importati

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
