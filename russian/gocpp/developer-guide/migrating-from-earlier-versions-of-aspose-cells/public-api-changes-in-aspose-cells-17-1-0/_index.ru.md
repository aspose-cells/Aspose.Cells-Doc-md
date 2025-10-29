---
title: Изменения в общедоступном API в Aspose.Cells 17.1.0
type: docs
weight: 20
url: /ru/go-cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 16.12.0 до 17.1.0, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка именованных диапазонов**
Aspose.Cells for C++ теперь поддерживает создание и манипулирование Названными диапазонами. Приведенный ниже фрагмент кода демонстрирует, насколько просто использовать Aspose.Cells for C++ API для [создания названных диапазонов](/cells/ru/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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

Помимо создания новых Названных диапазонов, API Aspose.Cells for C++ также поддерживает манипулирование существующими Названными диапазонами. Приведенный ниже фрагмент кода использует API Aspose.Cells for C++ для [манипулирования существующим названным диапазоном](/cells/ru/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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
Классу ICells был добавлен метод LinkToXmlMap, который полезен для создания ссылок на XML-карту.
### **Добавлен метод ICells::ImportCSV**
Классу ICells был добавлен метод ImportCSV, который полезен для импорта CSV-файла в ячейки листа.
### **Добавлен метод ICells::ImportTwoDimensionArray**
Классу ICells был добавлен метод GetIProtectedRangeCollection, который полезен для импорта двумерного массива данных на лист.
### **Добавлен метод IWorksheet::GetIProtectedRangeCollection**
Классу IWorksheet был добавлен метод GetIProtectedRangeCollection, который полезен для получения коллекции объектов IProtectedRange.
### **Добавлен метод IWorksheet::GetIProtectedRangeCollection**
Классу IWorksheet был добавлен метод GetIProtectedRangeCollection, который полезен для получения коллекции диапазонов редактирования на листе.
### **Добавлен метод IWorkbookSettings::ClearPivottables**
Класс IWorkbookSettings теперь содержит метод ClearPivottables, который полезен для очистки всех сводных таблиц в указанной электронной таблице.
### **Добавлен метод IWorksheetCollection::CreateIRange**
Класс IWorksheetCollection теперь содержит метод CreateIRange, который полезен для создания объекта типа IRange с помощью передачи ссылок на ячейки в виде строки.
### **Добавлен метод IExternalLink::IsVisible**
Метод IsVisible получает статус видимости внешней ссылки в приложении Excel.
### **Добавлены методы GetScaleCrop и SetScaleCrop**
Aspose.Cells for C++ 17.1.0 добавил методы GetScaleCrop и SetScaleCrop в класс IBuiltInDocumentPropertyCollection. Эти методы полезны для получения или установки свойства ScaleCrop, которое указывает режим отображения миниатюры документа.
### **Добавлены методы GetLinksUpToDate и SetLinksUpToDate**
Aspose.Cells for C++ 17.1.0 добавил методы GetLinksUpToDate и SetLinksUpToDate в класс IBuiltInDocumentPropertyCollection. Эти методы полезны для получения или установки свойства LinkUpToDate, которое указывает, актуальны ли гиперссылки в документе.
### **Добавлены методы GetAbsolutePath и SetAbsolutePath**
Aspose.Cells for C++ 17.1.0 добавил методы GetAbsolutePath и SetAbsolutePath в класс IWorkbook. Эти методы полезны для получения или установки абсолютного пути к файлу, который может использоваться только для внешних ссылок.
### **Добавлены методы GetFormula и SetFormula**
В этом выпуске Aspose.Cells for C++ были добавлены методы GetFormula и SetFormula для класса IListColumn. Эти методы полезны для получения или установки формулы списка.
### **Добавлены методы GetCheckCompatibility и SetCheckCompatibility**
В этом выпуске Aspose.Cells for C++ были добавлены методы GetCheckCompatibility и GetCheckCompatibility для класса IWorkbookSettings. Эти методы полезны для получения или установки свойства проверки совместимости, указывающего, должно ли API проверять совместимость при сохранении книги. Значение по умолчанию - true, и его можно установить в false, если требуется не проверять совместимость приложения.
### **Добавлены методы GetILightCellsDataHandler и SetILightCellsDataHandler**
Aspose.Cells for C++ теперь предоставляет методы GetILightCellsDataHandler и SetILightCellsDataHandler для класса ILoadOptions. Эти методы обозначают обработчик данных для обработки данных ячеек при чтении файлов шаблонов.
### **Добавлены методы GetCultureInfo и SetCultureInfo**
Aspose.Cells for C++ предоставляет методы GetCultureInfo и SetCultureInfo для класса ILoadOptions. Эти методы могут получать или устанавливать информацию о культуре системы во время загрузки файла.
## **Удалены API**
### **Удален метод ICells::MaxDataRowInColumn**
Рекомендуется вместо этого использовать метод ICells::GetLastDataRow.
### **Удален метод ICell::GetConditionalIStyle**
Рекомендуется вместо этого использовать метод ICell::GetIConditionalFormattingResult.
### **Удалены методы IPageSetup::GetDraft и SetDraft**
Рекомендуется вместо этого использовать методы IPageSetup::GetPrintDraft и IPageSetup::SetPrintDraft.

{{% alert color="primary" %}} 

С выпуском Aspose.Cells for C++ 17.1.0 мы удалили несколько методов, которые не использовались и считались ненужными. Вот список всех таких методов.

- Методы IPaneCollection::GetAcitvePaneType и SetAcitvePaneType
- Метод IRange::ToString
- Метод IRow::Equals
- Метод IWorkbook::SetISettings
- Метод ICell::ToString()
- Метод ICell::Equals(ObjectPtr)
- Метод ICell::GetHashCode
- Метод IWorksheet::ToString

{{% /alert %}}
