---
title: Общедоступный API Изменения в Aspose.Cells 17.1.0
type: docs
weight: 20
url: /ru/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.12.0 до 17.1.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка именованных диапазонов**
 Aspose.Cells для C++ теперь поддерживает создание и управление именованными диапазонами. Следующий фрагмент кода демонстрирует, как просто использовать Aspose.Cells вместо C++ API для[создавать именованные диапазоны](/cells/ru/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

 Помимо создания новых именованных диапазонов, API-интерфейсы Aspose.Cells для C++ также поддерживают управление существующими именованными диапазонами. Следующий фрагмент кода использует Aspose.Cells вместо C++ API для[управлять существующим именованным диапазоном](/cells/ru/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **Добавлен метод ICells::LinkToXmlMap**
В класс ICells добавлен метод LinkToXmlMap, который полезен при связывании карты XML.
### **Добавлен метод ICells::ImportCSV**
В класс ICells добавлен метод ImportCSV, который полезен при импорте CSV-файла в ячейки рабочего листа.
### **Добавлен метод ICells::ImportTwoDimensionArray.**
В класс ICells добавлен метод GetIProtectedRangeCollection, который полезен при импорте двумерного массива данных на рабочий лист.
### **Добавлен метод IWorksheet::GetIProtectedRangeCollection.**
В класс IWorksheet добавлен метод GetIProtectedRangeCollection, который полезен для получения коллекции объектов IProtectedRange.
### **Добавлен метод IWorksheet::GetIProtectedRangeCollection.**
В класс IWorksheet добавлен метод GetIProtectedRangeCollection, который полезен при извлечении коллекции диапазонов редактирования из рабочего листа.
### **Добавлен метод IWorkbookSettings::ClearPivottables**
В класс IWorkbookSettings добавлен метод ClearPivottables, который полезен для очистки всех сводных таблиц из данной электронной таблицы.
### **Добавлен метод IWorksheetCollection::CreateIRange.**
В класс IWorksheetCollection добавлен метод CreateIRange, который полезен при создании объекта IRange путем передачи ссылок на ячейки в строковом формате.
### **Добавлен метод IExternalLink::IsVisible.**
Метод IsVisible получает статус видимости внешней ссылки в приложении Excel.
### **Добавлены методы GetScaleCrop и SetScaleCrop.**
Aspose.Cells для C++ 17.1.0 предоставил методы GetScaleCrop и SetScaleCrop классу IBuiltInDocumentPropertyCollection. Эти методы полезны для получения или установки свойства ScaleCrop, которое указывает режим отображения миниатюры документа.
### **Добавлены методы GetLinksUpToDate и SetLinksUpToDate.**
Aspose.Cells для C++ 17.1.0 предоставил методы GetLinksUpToDate и SetLinksUpToDate классу IBuiltInDocumentPropertyCollection. Эти методы полезны для получения или установки свойства LinkUpToDate, которое указывает, являются ли гиперссылки в документе актуальными.
### **Добавлены методы GetAbsolutePath и SetAbsolutePath.**
Aspose.Cells для C++ 17.1.0 предоставил методы GetAbsolutePath и SetAbsolutePath для класса IWorkbook. Эти методы полезны для получения или установки абсолютного пути к файлу, который можно использовать только для внешних ссылок.
### **Добавлены методы GetFormula и SetFormula.**
В этом выпуске Aspose.Cells для C++ представлены методы GetFormula и SetFormula для класса IListColumn. Эти методы полезны для получения или установки формулы столбца списка.
### **Добавлены методы GetCheckCompatibility и SetCheckCompatibility.**
В этом выпуске Aspose.Cells для C++ представлены методы GetCheckCompatibility и GetCheckCompatibility для класса IWorkbookSettings. Эти методы полезны для получения или установки свойства проверки совместимости, указывающего, должен ли API проверять совместимость при сохранении книги. Значение по умолчанию — true, и его можно установить на false, если приложение не требует проверки совместимости.
### **Добавлены методы GetILightCellsDataHandler и SetILightCellsDataHandler.**
Aspose.Cells для C++ теперь предоставляет методы GetILightCellsDataHandler и SetILightCellsDataHandler для класса ILoadOptions. Эти методы обозначают обработчик данных для обработки данных ячеек при чтении файла шаблона.
### **Добавлены методы GetCultureInfo и SetCultureInfo.**
Aspose.Cells для C++ предоставил методы GetCultureInfo и SetCultureInfo для класса ILoadOptions. Эти методы могут получить или установить информацию о культуре системы во время загрузки файла.
## **Удаленные API**
### **Удален метод ICells::MaxDataRowInColumn**
Вместо этого рекомендуется использовать метод ICells::GetLastDataRow.
### **Удален метод ICell::GetConditionalIStyle.**
Вместо этого рекомендуется использовать метод ICell::GetIConditionalFormattingResult.
### **Удалены методы IPageSetup::GetDraft и SetDraft.**
Вместо этого рекомендуется использовать методы IPageSetup::GetPrintDraft и IPageSetup::SetPrintDraft.

{{% alert color="primary" %}} 

С выпуском Aspose.Cells для C++ 17.1.0 мы удалили несколько методов, которые не использовались, поэтому считались ненужными. Вот список всех таких методов.

- Методы IPaneCollection::GetAcitvePaneType и SetAcitvePaneType
- IRange:: Метод ToString
- Метод IRow::Equals
- Метод IWorkbook::SetISettings
- Метод ICell::ToString()
- Метод ICell::Equals(ObjectPtr)
- ICell:: Метод GetHashCode
- Метод IWorksheet::ToString

{{% /alert %}}
