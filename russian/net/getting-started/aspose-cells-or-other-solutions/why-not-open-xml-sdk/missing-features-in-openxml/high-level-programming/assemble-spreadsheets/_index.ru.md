---
title: Собрать электронные таблицы
type: docs
weight: 10
url: /ru/net/assemble-spreadsheets/
---
В этом разделе описывается, как:

Создайте новый файл Excel с нуля и добавьте в него рабочий лист.

- Добавляйте рабочие листы в электронные таблицы конструктора.
- Доступ к рабочим листам с использованием имени листа.
- Удалите рабочий лист из файла Excel, используя его имя листа.
- Удалите рабочий лист из файла Excel, используя его индекс листа.
- Aspose.Cells предоставляет класс Workbook, представляющий файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет широкий набор свойств и методов для управления рабочими листами.
## **Добавление рабочих листов в новый файл Excel**
Чтобы создать новый файл Excel программно:

- Создайте объект класса Workbook.
- Вызовите метод Add коллекции Worksheets. Пустой лист добавляется в файл Excel * автоматически. На него можно сослаться, передав индекс листа нового рабочего листа в коллекцию Worksheets.
- Получите ссылку на рабочий лист.
- Выполнить работу с рабочими листами.
- Сохраните новый файл Excel с новыми листами, вызвав метод Save класса Workbook.

{{< highlight "csharp" >}}

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
## **Добавление рабочих листов в электронную таблицу конструктора**
Процесс добавления рабочих листов в электронную таблицу конструктора такой же, как и добавление нового рабочего листа, за исключением того, что файл Excel уже существует, поэтому его следует открыть перед добавлением рабочих листов. Таблицу дизайнера можно открыть с помощью класса Workbook.

{{< highlight "csharp" >}}

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
## **Доступ к рабочим листам с использованием имени листа**
Получите доступ или получите любой рабочий лист, указав его имя или индекс.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Удаление рабочих листов с использованием имени листа**
Чтобы удалить рабочие листы из файла, вызовите метод RemoveAt коллекции рабочих листов. Передайте имя листа методу RemoveAt, чтобы удалить определенный рабочий лист.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Удаление рабочих листов с помощью индекса листов**
Удаление рабочих листов по имени хорошо работает, когда известно имя рабочего листа. Если вы не знаете имя листа, используйте перегруженную версию метода RemoveAt, который принимает индекс листа вместо имени листа.

{{< highlight "csharp" >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
