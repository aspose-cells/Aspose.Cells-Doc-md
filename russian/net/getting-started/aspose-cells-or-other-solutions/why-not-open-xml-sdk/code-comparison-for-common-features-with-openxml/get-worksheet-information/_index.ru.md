---
title: Получить информацию о рабочем листе
type: docs
weight: 50
url: /ru/net/get-worksheet-information/
---
## **Опенксмл Excel**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Получить информацию о рабочем листе.xlsx";

ПолучитьИнформациюЛиста(ИмяФайла);

Консоль.ReadKey();

}

public static void GetSheetInfo(string fileName)

{  // Открыть файл только для чтения.  using (SpreadsheetDocument mySpreadsheetDocument = SpreadsheetDocument.Open(fileName, false))  {  S Sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets; _// For лист, отобразить информацию о листе.  foreach (лист E в листах)  {  foreach (атрибут в листе.GetAttributes())  {  Console.WriteLine("{0}: {1}" , attr.localname, attr.value); _ x000d_ }  }  }   {{< /highlight >}} ## ** Aspose.Cells ** _56103481 ## ** Aspose.Cells ** _07103481 # ** Aspose.Cells ** Files\";  string FileName = FilePath + "Получить информацию о рабочем листе.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

private static void GetSheetInfo(string fileName)

{  // Создание экземпляра рабочей книги object  Workbook workbook = new Workbook(fileName);  // Перебор всех листов в workbook  foreach (Worksheet Sheet in workbook.Worksheets) _00 //Get Name and _ {_ Индекс Sheet  Console.WriteLine("Имя листа: {0}", Sheet.Name);  Console.WriteLine("Индекс листа: {0}", Sheet.Index);  //Повторить все пользовательские Properties  Foreach (свойство CustomProperty в листе .CustomProperties)   {  console.writeline ("{0}: {1}", свойство. **Загрузить пример кода** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)