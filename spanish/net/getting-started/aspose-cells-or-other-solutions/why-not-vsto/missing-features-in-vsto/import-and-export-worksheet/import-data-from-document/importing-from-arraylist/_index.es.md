---
title: Importando desde ArrayList
type: docs
weight: 20
url: /es/net/importing-from-arraylist/
---
 Los desarrolladores pueden importar datos de un ArrayList a sus hojas de trabajo llamando al**Importar ArrayList** método de la colección Cells. El método ImportArray toma los siguientes parámetros:**Lista de arreglo** , representa el objeto ArrayList cuyo contenido necesita importar

- Número de fila, representa el número de fila de la primera celda donde se importarán los datos
- Número de columna, representa el número de columna de la primera celda donde se importarán los datos
- Es Vertical , un valor booleano que especifica importar datos vertical u horizontalmente

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
