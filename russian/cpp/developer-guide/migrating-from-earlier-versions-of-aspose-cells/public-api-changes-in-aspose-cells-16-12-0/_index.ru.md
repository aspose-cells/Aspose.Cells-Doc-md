---
title: Общедоступный API Изменения в Aspose.Cells 16.12.0
type: docs
weight: 10
url: /ru/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.11.0 до 16.12.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка сводных таблиц**
Второй выпуск Aspose.Cells для C++ поддерживает создание и управление сводными таблицами. Aspose.Cells для C++ предоставляет класс IPivotTable, который представляет объект сводной таблицы, тогда как IPivotTableCollection представляет коллекцию сводных таблиц. Доступ к IPivotTableCollection можно получить через объект IWorksheet, а новую сводную таблицу можно добавить в коллекцию с помощью метода IPivotTableCollection.Add.

 В следующем фрагменте кода показано, как просто использовать Aspose.Cells вместо C++ API для[создавать сводные таблицы с нуля](/cells/ru/cpp/create-pivot-table/).

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Add source data for pivot table

intrusive_ptr<String> str = new String("Fruit");

ws->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(str);

str = new String("Quantity");

ws->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(str);

str = new String("Price");

ws->GetICells()->GetObjectByIndex(new String("C1"))->PutValue(str);

str = new String("Apple");

ws->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(str);

str = new String("Orange");

ws->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(str);

ws->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(3);

ws->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(4);

ws->GetICells()->GetObjectByIndex(new String("C2"))->PutValue(2);

ws->GetICells()->GetObjectByIndex(new String("C3"))->PutValue(1);

//Add pivot table

int idx = ws->GetIPivotTables()->Add(new String("A1:C3"), new String("E5"), new String("MyPivotTable"));

//Access created pivot table

intrusive_ptr<IPivotTable> pt = ws->GetIPivotTables()->GetObjectByIndex(idx);

//Manipulate pivot table rows, columns and data fields

pt->AddFieldToArea(PivotFieldType_Row, pt->GetIBaseFields()->GetObjectByIndex(0));

pt->AddFieldToArea(PivotFieldType_Data, pt->GetIBaseFields()->GetObjectByIndex(1));

pt->AddFieldToArea(PivotFieldType_Data, pt->GetIBaseFields()->GetObjectByIndex(2));

pt->AddFieldToArea(PivotFieldType_Column, pt->GetIDataField());

//Set pivot table style

pt->SetPivotTableStyleType(PivotTableStyleType_PivotTableStyleMedium9);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}

Помимо создания новых сводных таблиц, API-интерфейсы Aspose.Cells для C++ также поддерживают управление существующими сводными таблицами. В настоящее время API поддерживает изменение данных в исходном диапазоне сводной таблицы, а затем их обновление. После того как сводная таблица будет обработана по желанию, лучше всего использовать методы IPivotTable.RefreshData и IPivotTable.CalculateData для обновления сводной таблицы в соответствии с обновленным источником данных.

 Следующий фрагмент кода использует Aspose.Cells вместо C++ API для[управлять существующей сводной таблицей](/cells/ru/cpp/manipulate-pivot-table/).

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr wb = Factory::CreateIWorkbook(samplePath);

//Access first worksheet

intrusive_ptr ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Change value of cell B3 which is inside the source data of pivot table

intrusive_ptr str = new String("Cup");

ws->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(str);

//Get the value of cell H8 before refreshing pivot table

intrusive_ptr val = ws->GetICells()->GetObjectByIndex(new String("H8"))->GetStringValue();

printf("Before refreshing Pivot Table value of cell H8: %s\r\n%", val->charValue());

//Access pivot table, refresh and calculate it

intrusive_ptr pt = ws->GetIPivotTables()->GetObjectByIndex(0);

pt->RefreshData();

pt->CalculateData();

//Get the value of cell H8 after refreshing pivot table

val = ws->GetICells()->GetObjectByIndex(new String("H8"))->GetStringValue();

printf("After refreshing Pivot Table value of cell H8: %s\r\n%", val->charValue());

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Поддержка правил условного форматирования**
 Aspose.Cells для C++ теперь предоставляет возможность добавлять правила условного форматирования на лист, предоставляя класс IFormatCondition. Вышеупомянутый класс дополнительно предоставляет следующие методы для[применять правила условного форматирования](/cells/ru/cpp/apply-conditional-formatting-in-worksheet/) в соответствии с требованиями приложения.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

В следующем примере кода показано, как добавить правило условного форматирования типа Cell Значение в ячейки A1 и B2.

**C++**

{{< highlight "csharp" >}}

 //Create an empty workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Adds an empty conditional formatting

int idx = ws->GetIConditionalFormattings()->Add();

intrusive_ptr fcs = ws->GetIConditionalFormattings()->GetObjectByIndex(idx);

//Set the conditional format range

intrusive_ptr ca = ICellArea::CreateICellArea(new String("A1"), new String("A1"));

fcs->AddArea(ca);

ca = ICellArea::CreateICellArea(new String("B2"), new String("B2"));

fcs->AddArea(ca);

//Add condition and set the background color

idx = fcs->AddCondition(FormatConditionType_CellValue, OperatorType_Between, new String("=A2"), new String("100"));

intrusive_ptr fc = fcs->GetObjectByIndex(idx);

fc->GetIStyle()->SetBackgroundColor(Color::GetRed());

//User friendly message to test the output excel file.

StringPtr msgStr = new String("Red color in cells A1 and B2 is because of Conditional Formatting.");

ws->GetICells()->GetObjectByIndex(new String("A10"))->PutValue(msgStr);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Поддержка гиперссылок**
 Aspose.Cells для C++ теперь поддерживает[добавление гиперссылок в ячейки рабочего листа](/cells/ru/cpp/add-hyperlinks-to-the-cells/). Чтобы обеспечить эту функцию, Aspose.Cells для C++ 16.12.0 предоставил класс IHyperlinkCollection, который доступен через объект IWorksheet, тогда как гиперссылку можно добавить в коллекцию при использовании метода IHyperlinkCollection.Add, как показано ниже.

**C++**

{{< highlight "csharp" >}}

 //Create a new workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Get the first worksheet

intrusive_ptr wsc = wb->GetIWorksheets();

intrusive_ptr ws = wsc->GetObjectByIndex(0);

//Add hyperlink in cell C7 and make use of its various methods

intrusive_ptr hypLnks = ws->GetIHyperlinks();

int idx = hypLnks->Add(new String("C7"), 1, 1, new String("http://www.aspose.com/"));

intrusive_ptr lnk = hypLnks->GetObjectByIndex(idx);

lnk->SetTextToDisplay(new String("Aspose"));

lnk->SetScreenTip(new String("Link to Aspose Website"));

//Save the workbook in xlsx format

wb->Save(dirPath->Append(new String("output.xlsx")), SaveFormat_Xlsx);

{{< /highlight >}}
### **Поддержка свойств документа**
Приложение Excel поддерживает 2 типа свойств документа, перечисленных ниже.

- Системные (встроенные) свойства. Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (настраиваемые) свойства: настраиваемые свойства, определенные конечным пользователем в виде пары "имя-значение".

Aspose.Cells для опор C++[управление обоими типами свойств документа, встроенными и пользовательскими](/cells/ru/cpp/managing-document-properties/). Aspose.Cells' Класс IWorkbook представляет файл Excel. Чтобы получить доступ к встроенным свойствам документа, используйте IWorkbook.GetBuiltInDocumentProperties, тогда как доступ к пользовательским свойствам документа можно получить с помощью метода IWorkbook.GetCustomDocumentProperties.

Следующий пример кода загружает существующий образец электронной таблицы и считывает встроенные свойства документа, такие как заголовок, тема и настраиваемое свойство, по имени MyCustom1.

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr wb = Factory::CreateIWorkbook(samplePath);

//Read built-in title and subject properties

StringPtr strTitle = wb->GetIBuiltInDocumentProperties()->GetTitle();

StringPtr strSubject = wb->GetIBuiltInDocumentProperties()->GetSubject();

printf("Title: %s\r\n", strTitle->charValue());

printf("Subject: %s\r\n", strSubject->charValue());

printf("\r\n");

//Modify built-in title and subject properties

strTitle = new String("Aspose.Cells New Title");

strSubject = new String("Aspose.Cells New Subject");

wb->GetIBuiltInDocumentProperties()->SetTitle(strTitle);

wb->GetIBuiltInDocumentProperties()->SetSubject(strSubject);

//Read the custom property

StringPtr strCustomPropName = new String("MyCustom1");

StringPtr strCustomPropValue = wb->GetICustomDocumentProperties()->GetObjectByIndex(strCustomPropName)->ToString();

printf("MyCustom1: %s\r\n", strCustomPropValue->charValue());

//Add a new custom property

strCustomPropName = new String("MyCustom5");

strCustomPropValue = new String("This is my custom five.");

wb->GetICustomDocumentProperties()->AddIDocumentProperty(strCustomPropName, strCustomPropValue);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Поддержка объектов списка.**
 Таблица Excel представляет собой матрицу ячеек, содержащую любое количество строк и столбцов, тогда как та же самая таблица называется объектом списка в Aspose.Cells для C++ API. Пространство имен Aspose::Cells::Tables содержит все необходимые классы, которые имеют дело с операциями, связанными с объектами списка. Наиболее заслуживают упоминания классы IListObject и IListObjectCollection, которые позволяют[создавать и форматировать объекты списка](/cells/ru/cpp/create-and-format-table/) и так далее.

Следующий пример кода загружает образец файла электронной таблицы, а затем создает объект списка (таблицу) в диапазоне A1:H10, а затем использует его различные методы для отображения промежуточного итога.

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Add table i.e. list object

int idx = ws->GetIListObjects()->Add(new String("A1"), new String("H10"), true);

//Access the newly added list object

intrusive_ptr<IListObject> lo = ws->GetIListObjects()->GetObjectByIndex(idx);

//Make use of its display methods

lo->SetShowHeaderRow(true);

lo->SetShowTableStyleColumnStripes(true);

lo->SetShowTotals(true);

//Set its style

lo->SetTableStyleType(TableStyleType_TableStyleLight12);

//Set total functions of 3rd, 4th and 5th columns

lo->GetIListColumns()->GetObjectByIndex(2)->SetTotalsCalculation(TotalsCalculation_Min);

lo->GetIListColumns()->GetObjectByIndex(3)->SetTotalsCalculation(TotalsCalculation_Max);

lo->GetIListColumns()->GetObjectByIndex(4)->SetTotalsCalculation(TotalsCalculation_Count);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Поддержка группировки строк и столбцов**
 Aspose.Cells для C++ API можно использовать для группировки строк и столбцов при использовании класса ICells, который в основном представляет собой набор всех ячеек на данном листе. Класс ICells предлагает методы GroupRows и GroupColumns для[группировать строки и столбцы](/cells/ru/cpp/group-rows-and-columns-of-worksheet/) соответственно.

Следующий фрагмент кода демонстрирует простой сценарий использования обоих вышеупомянутых методов.

**C++**

{{< highlight "csharp" >}}

 //Create an empty workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Add worksheet for grouping rows

intrusive_ptr grpRows = wb->GetIWorksheets()->GetObjectByIndex(0);

grpRows->SetName(new String("GroupRows"));

//Add worksheet for grouping columns

int idx = wb->GetIWorksheets()->Add();

intrusive_ptr grpCols = wb->GetIWorksheets()->GetObjectByIndex(idx);

grpCols->SetName(new String("GroupColumns"));

//Add sample values in both worksheets

for (int i = 0; i<50; i++)

{

	intrusive_ptr str = new String("Text");

	grpRows->GetICells()->GetObjectByIndex(i, 0)->PutValue(str);

	grpCols->GetICells()->GetObjectByIndex(0, i)->PutValue(str);

}

//Grouping rows at first level

grpRows->GetICells()->GroupRows(0, 10);

grpRows->GetICells()->GroupRows(12, 22);

grpRows->GetICells()->GroupRows(24, 34);

//Grouping rows at second level

grpRows->GetICells()->GroupRows(2, 8);

grpRows->GetICells()->GroupRows(14, 20);

grpRows->GetICells()->GroupRows(28, 30);

//Grouping rows at third level

grpRows->GetICells()->GroupRows(5, 7);

//Grouping columns at first level

grpCols->GetICells()->GroupColumns(0, 10);

grpCols->GetICells()->GroupColumns(12, 22);

grpCols->GetICells()->GroupColumns(24, 34);

//Grouping columns at second level

grpCols->GetICells()->GroupColumns(2, 8);

grpCols->GetICells()->GroupColumns(14, 20);

grpCols->GetICells()->GroupColumns(28, 30);

//Grouping columns at third level

grpCols->GetICells()->GroupColumns(5, 7);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Поддержка тем**
Aspose.Cells для C++ API-интерфейсы теперь поддерживают использование и управление темами, предлагаемыми приложением Excel.
#### **Возможность применения пользовательских цветов темы**
 Следующий фрагмент пытается[создать новую тему с пользовательскими цветами](/cells/ru/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) для трудовой книжки.

**C++**

{{< highlight "csharp" >}}

 //Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Create array of custom theme colors

intrusive_ptr<Array1D<Color*>> clrs = new Array1D<Color*>(12);

//Background1

clrs->SetValue(Color::GetRed(), 0);

//Text1

clrs->SetValue(Color::GetRed(), 1);

//Background2

clrs->SetValue(Color::GetRed(), 2);

//Text2

clrs->SetValue(Color::GetRed(), 3);

//Accent1

clrs->SetValue(Color::GetRed(), 4);

//Accent2

clrs->SetValue(Color::GetGreen(), 5);

//Accent3

clrs->SetValue(Color::GetGreen(), 6);

//Accent4

clrs->SetValue(Color::GetGreen(), 7);

//Accent5

clrs->SetValue(Color::GetGreen(), 8);

//Accent6

clrs->SetValue(Color::GetBlue(), 9);

//Hyperlink

clrs->SetValue(Color::GetBlue(), 10);

//Followed Hyperlink

clrs->SetValue(Color::GetBlue(), 11);

//Apply custom theme colors on workbook

wb->CustomTheme(new String("AnyTheme"), clrs);

//Save the workbook

wb->Save(outputPath);

{{< /highlight >}}
#### **Поддержка управления цветами темы**
В следующем примере кода показано, как[читать и изменять цвета темы книги](/cells/ru/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Пример кода загружает существующую электронную таблицу, считывает цвета ее темы, т. е. Accent1-Accent6, и изменяет цвета перед сохранением электронной таблицы.

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Read these theme colors i.e. Accent1 till Accent6

intrusive_ptr<Color> clr_Accent1 = wb->GetThemeColor(ThemeColorType_Accent1);

intrusive_ptr<Color> clr_Accent2 = wb->GetThemeColor(ThemeColorType_Accent2);

intrusive_ptr<Color> clr_Accent3 = wb->GetThemeColor(ThemeColorType_Accent3);

intrusive_ptr<Color> clr_Accent4 = wb->GetThemeColor(ThemeColorType_Accent4);

intrusive_ptr<Color> clr_Accent5 = wb->GetThemeColor(ThemeColorType_Accent5);

intrusive_ptr<Color> clr_Accent6 = wb->GetThemeColor(ThemeColorType_Accent6);

//Print all of them. ffff00 means Yellow

printf("Accent1: %x\r\n", clr_Accent1->ToArgb());

printf("Accent2: %x\r\n", clr_Accent2->ToArgb());

printf("Accent3: %x\r\n", clr_Accent3->ToArgb());

printf("Accent4: %x\r\n", clr_Accent4->ToArgb());

printf("Accent5: %x\r\n", clr_Accent5->ToArgb());

printf("Accent6: %x\r\n", clr_Accent6->ToArgb());

//Set all of them to Red

wb->SetThemeColor(ThemeColorType_Accent1, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent2, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent3, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent4, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent5, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent6, Color::GetRed());

//Reading one of them after modifying, it will be ff0000 which means Red

printf("\r\nReading one of them after modifying, it will be ff0000 which means Red\r\n\r\n");

clr_Accent6 = wb->GetThemeColor(ThemeColorType_Accent6);

printf("Accent6: %x\r\n", (clr_Accent6->ToArgb())&0xffffff);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
#### **Возможность копировать темы между книгами**
В следующем примере кода показано, как[скопировать тему из одной книги в другую](/cells/ru/cpp/copy-theme-from-one-workbook-to-another/), что может быть полезно при применении встроенных или пользовательских тем к нескольким электронным таблицам.

**C++**

{{< highlight "csharp" >}}

 //Read excel file that has Damask theme applied on it

intrusive_ptr<IWorkbook> damask = Factory::CreateIWorkbook(damaskPath);

//Read your sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Copy theme from source file

wb->CopyTheme(damask);

//Save the workbook in xlsx format

wb->Save(outputPath, SaveFormat_Xlsx);

{{< /highlight >}}
## **Переименованные API**
С выпуском Aspose.Cells для C++ 16.12.0 мы переименовали несколько методов, чтобы сохранить унифицированные интерфейсы. Список всех переименованных API выглядит следующим образом.
#### **Метод ICell::SetStyle переименован в ICell::SetIStyle.**
#### **Метод ICell::SetCharacters переименован в ICell::SetIFontSettings.**
#### **Метод ICellsColor::SetThemeColor переименован в ICellsColor::SetIThemeColor.**
#### **Метод ICells::SetStyle переименован в ICells::SetIStyle.**
#### **Метод ICellsHelper::GetDPI_i переименован в ICellsHelper::GetDPI.**
#### **Метод ICellsHelper::SetDPI_i переименован в ICellsHelper::SetDPI.**
#### **Метод ICellsHelper::GetVersion_i переименован в ICellsHelper::GetVersion.**
#### **Метод ICellsHelper::IsProtectedByRMS_i переименован в ICellsHelper::IsProtectedByRMS.**
#### **Метод ICellsHelper::IsProtectedByRMS_i переименован в ICellsHelper::IsProtectedByRMS.**
#### **Метод ICellsHelper::CellNameToIndex_i переименован в ICellsHelper::CellNameToIndex.**
#### **Метод ICellsHelper::CellIndexToName_i переименован в ICellsHelper::CellIndexToName.**
#### **Метод ICellsHelper::ColumnIndexToName_i переименован в ICellsHelper::ColumnIndexToName.**
#### **Метод ICellsHelper::ColumnNameToIndex_i переименован в ICellsHelper::ColumnNameToIndex.**
#### **Метод ICellsHelper::RowIndexToName_i переименован в ICellsHelper::RowIndexToName.**
#### **Метод ICellsHelper::RowNameToIndex_i переименован в ICellsHelper::RowNameToIndex.**
#### **Метод ICellsHelper::ConvertR1C1FormulaToA1_i переименован в ICellsHelper::ConvertR1C1FormulaToA1.**
#### **Метод ICellsHelper::ConvertA1FormulaToR1C1_i переименован в ICellsHelper::ConvertA1FormulaToR1C1.**
#### **Метод ICellsHelper::GetDateTimeFromDouble_i переименован в ICellsHelper::GetDateTimeFromDouble.**
#### **Метод ICellsHelper::GetDoubleFromDateTime_i переименован в ICellsHelper::GetDoubleFromDateTime.**
#### **Метод ICellsHelper::DetectLoadFormat_i переименован в ICellsHelper::DetectLoadFormat.**
#### **Метод ICellsHelper::DetectFileFormat_i переименован в ICellsHelper::DetectFileFormat.**
#### **Метод ICellsHelper::GetFontDir_i переименован в ICellsHelper::GetFontDir.**
#### **Метод ICellsHelper::SetFontDir_i переименован в ICellsHelper::SetFontDir.**
#### **Метод ICellsHelper::GetFontDirs_i переименован в ICellsHelper::GetFontDirs.**
#### **Метод ICellsHelper::SetFontDirs_i переименован в ICellsHelper::SetFontDirs.**
#### **Метод ICellsHelper::GetFontFiles_i переименован в ICellsHelper::GetFontFiles.**
#### **Метод ICellsHelper::SetFontFiles_i переименован в ICellsHelper::SetFontFiles.**
#### **Метод ICellsHelper::GetStartupPath_i переименован в ICellsHelper::GetStartupPath.**
#### **Метод ICellsHelper::SetStartupPath_i переименован в ICellsHelper::SetStartupPath.**
#### **Метод ICellsHelper::GetAltStartPath_i переименован в ICellsHelper::GetAltStartPath.**
#### **Метод ICellsHelper::SetAltStartPath_i переименован в ICellsHelper::SetAltStartPath.**
#### **Метод ICellsHelper::GetLibraryPath_i переименован в ICellsHelper::GetLibraryPath.**
#### **Метод ICellsHelper::SetLibraryPath_i переименован в ICellsHelper::SetLibraryPath.**
#### **Метод ICellsHelper::GetUsedColors_i переименован в ICellsHelper::GetUsedColors.**
#### **Метод ICellsHelper::AddAddInFunction_i переименован в ICellsHelper::AddAddInFunction.**
#### **Метод ICellsHelper::MergeFiles_i переименован в ICellsHelper::MergeFiles.**
#### **Метод IColumnCollection::GetByIndex_i переименован в IColumnCollection::GetIColumn.**
#### **Метод IFileFormatUtil::DetectFileFormat_i переименован в IFileFormatUtil::DetectFileFormat.**
#### **Метод IFileFormatUtil::ExtensionToSaveFormat_i переименован в IFileFormatUtil::ExtensionToSaveFormat.**
#### **Метод IFileFormatUtil::IsTemplateFormat_i переименован в IFileFormatUtil::IsTemplateFormat.**
#### **Метод IFileFormatUtil::LoadFormatToExtension_i переименован в IFileFormatUtil::LoadFormatToExtension.**
#### **Метод IFileFormatUtil::LoadFormatToSaveFormat_i переименован в IFileFormatUtil::LoadFormatToSaveFormat.**
#### **Метод IFileFormatUtil::SaveFormatToExtension_i переименован в IFileFormatUtil::SaveFormatToExtension.**
#### **Метод IFileFormatUtil::SaveFormatToLoadFormat_i переименован в IFileFormatUtil::SaveFormatToLoadFormat.**
#### **Метод IRange::SetStyle переименован в IRange::SetIStyle.**
#### **Метод IFindOptions::SetRange переименован в IFindOptions::SetIRange.**
#### **Метод ILoadOptions::SetLoadDataOptions переименован в ILoadOptions::SetLoadDataOptions.**
#### **Метод IWorkbook::SetSettings переименован в IWorkbook::SetISettings.**
#### **Метод IWorkbook::SetDefaultStyle переименован в IWorkbook::SetDefaultIStyle.**
