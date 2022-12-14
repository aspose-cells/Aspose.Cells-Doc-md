---
title: Импорт из ArrayList
type: docs
weight: 20
url: /ru/net/importing-from-arraylist/
---
 Разработчики могут импортировать данные из списка ArrayList в свои рабочие листы, вызвав метод**Импортмассивлист** метод коллекции Cells. Метод ImportArray принимает следующие параметры:**ArrayList** , представляет объект ArrayList, содержимое которого необходимо импортировать

- Номер строки представляет собой номер строки первой ячейки, в которую будут импортированы данные.
- Номер столбца представляет номер столбца первой ячейки, в которую будут импортированы данные.
- Является Вертикальным логическим значением, указывающим на импорт данных по вертикали или по горизонтали.

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
