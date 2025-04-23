---
title: Сборка электронных таблиц
type: docs
weight: 10
url: /ru/net/assemble-spreadsheets/
---

Этот раздел описывает, как:

Создать новый файл Excel с нуля и добавить в него лист.

- Добавить листы к дизайнерским электронным таблицам.
– Доступ к листам с использованием имени листа.
– Удаление листа из файла Excel с использованием его имени листа.
– Удаление листа из файла Excel с использованием его индекса листа.
– Aspose.Cells предоставляет класс Workbook, который представляет файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому листу в файле Excel.

Лист представляется классом Worksheet. Класс Worksheet предоставляет широкий набор свойств и методов для управления листами.
## **Добавление рабочих листов в новый файл Excel**
Для создания нового файла Excel программно:

– Создайте объект класса Workbook.
– Вызовите метод Add из коллекции Worksheets. Пустой лист добавляется в файл Excel автоматически. Его можно ссылаться, передавая индекс нового листа коллекции Worksheets.
– Получите ссылку на лист.
– Выполните работу на листах.
– Сохраните новый файл Excel с новыми листами, вызвав метод Save класса Workbook.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Добавление листов в дизайнерскую электронную таблицу**
Процесс добавления листов в дизайнерскую электронную таблицу такой же, как добавление нового листа, за исключением того, что файл Excel уже существует, поэтому перед добавлением листов его нужно открыть. Дизайнерскую электронную таблицу можно открыть с помощью класса Workbook.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Доступ к листам с использованием имени листа**
Получение любого листа, указав его имя или индекс.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Удаление листов с использованием имени листа**
Чтобы удалить листы из файла, вызовите метод RemoveAt коллекции Worksheets. Передайте имя листа методу RemoveAt, чтобы удалить конкретный лист.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Удаление рабочих листов с использованием индекса листа.**
Удаление листов по имени работает хорошо, когда известно имя листа. Если не известно имя листа, используйте перегруженную версию метода RemoveAt, которая принимает индекс листа вместо его имени.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
