---
title: Импорт из массива
type: docs
weight: 10
url: /ru/net/importing-from-array/
---
 Разработчики могут импортировать данные из массива на свои рабочие листы, вызвав метод**ИмпортМассив** метод коллекции Cells. Существует много перегруженных версий метода ImportArray, но типичная перегрузка принимает следующие параметры:

- Массив представляет объект массива, содержимое которого необходимо импортировать.
- Номер строки представляет собой номер строки первой ячейки, в которую будут импортированы данные.
- Номер столбца, представляет номер столбца первой ячейки, в которую будут импортированы данные.
- Вертикально, логическое значение, указывающее, импортировать ли данные вертикально или горизонтально.

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
