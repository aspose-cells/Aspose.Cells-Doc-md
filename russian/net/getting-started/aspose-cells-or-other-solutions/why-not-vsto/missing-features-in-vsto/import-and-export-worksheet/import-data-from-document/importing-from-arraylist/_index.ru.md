---
title: Импорт из ArrayList
type: docs
weight: 20
url: /ru/net/importing-from-arraylist/
---

Разработчики могут импортировать данные из ArrayList в их листы, вызвав метод **ImportArrayList** коллекции Cells. Метод ImportArray принимает следующие параметры: **ArrayList** , представляет объект ArrayList, чьи содержимое нужно импортировать

- Номер строки , представляет номер строки первой ячейки, куда будут импортированы данные
- Номер столбца , представляет номер столбца первой ячейки, куда будут импортированы данные
- Это вертикальное, логическое значение, которое указывает импортировать данные вертикально или горизонтально

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
