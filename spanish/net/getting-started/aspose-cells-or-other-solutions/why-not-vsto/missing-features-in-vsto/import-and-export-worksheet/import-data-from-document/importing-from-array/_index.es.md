---
title: Importación desde matriz
type: docs
weight: 10
url: /es/net/importing-from-array/
---
 Los desarrolladores pueden importar datos de una matriz a sus hojas de trabajo llamando al**Importar matriz** método de la colección Cells. Hay muchas versiones sobrecargadas del método ImportArray pero una sobrecarga típica toma los siguientes parámetros:

- Array, representa el objeto de matriz cuyo contenido necesita importar
- Número de fila, representa el número de fila de la primera celda donde se importarán los datos
- Número de columna, representa el número de columna de la primera celda donde se importarán los datos
- Es Vertical, un valor booleano que especifica importar datos vertical u horizontalmente

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
