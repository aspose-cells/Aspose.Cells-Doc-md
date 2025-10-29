---
title: Изменения в общедоступном API в Aspose.Cells 16.12.0
type: docs
weight: 10
url: /ru/go-cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 16.11.0 до 16.12.0, которые могут быть интересны разработчикам модулей/приложений. В нем представлены не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка сводных таблиц**
Вторая версия Aspose.Cells for C++ поддерживает создание и манипулирование сводными таблицами. Aspose.Cells for C++ предоставляет класс IPivotTable, который представляет объект сводной таблицы, в то время как IPivotTableCollection представляет коллекцию сводных таблиц. Класс IPivotTableCollection можно получить через объект IWorksheet, и новая сводная таблица может быть добавлена в коллекцию, используя метод IPivotTableCollection.Add.

Ниже приведен фрагмент кода, демонстрирующий простоту использования Aspose.Cells for C++ API для [создания сводных таблиц с нуля](/cells/ru/cpp/create-pivot-table/).

**C++**

{{< highlight csharp >}}

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

Помимо создания новых сводных таблиц, API Aspose.Cells for C++ также поддерживает манипулирование существующими сводными таблицами. В настоящее время API поддерживает изменение данных в исходном диапазоне сводной таблицы, а затем обновление. После того, как сводная таблица была изменена по желанию, лучше всего использовать методы IPivotTable.RefreshData и IPivotTable.CalculateData для обновления сводной таблицы по обновленному источнику данных.

Ниже приведен фрагмент кода, использующий API Aspose.Cells for C++ для [манипулирования существующей сводной таблицей](/cells/ru/cpp/manipulate-pivot-table/).

**C++**

{{< highlight csharp >}}

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
Теперь Aspose.Cells for C++ предоставляет возможность добавлять правила условного форматирования на лист, путем предоставления класса IFormatCondition. Указанный класс также предоставляет следующие методы для [применения правил условного форматирования](/cells/ru/cpp/apply-conditional-formatting-in-worksheet/) в соответствии с требованиями приложения.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Приведенный ниже образец кода показывает, как добавить правило условного форматирования типа Значение ячейки на ячейки A1 и B2.

**C++**

{{< highlight csharp >}}

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
Теперь Aspose.Cells for C++ поддерживает [добавление гиперссылок в ячейки листа](/cells/ru/cpp/add-hyperlinks-to-the-cells/). Чтобы предоставить эту функцию, Aspose.Cells for C++ версии 16.12.0 предоставил класс IHyperlinkCollection, который доступен через объект IWorksheet, в то время как гиперссылка может быть добавлена в коллекцию, используя метод IHyperlinkCollection.Add, как показано ниже.

**C++**

{{< highlight csharp >}}

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
Приложение Excel поддерживает 2 типа документных свойств, перечисленных ниже.

- Oпределенные системой (встроенные) свойства: Встроенные свойства содержат общую информацию о документе, такую как название документа, имя автора, статистику документа и т. д.
- Пользовательские (пользовательские) свойства: Пользовательские свойства, определенные конечным пользователем в виде пары имени и значения.

Aspose.Cells for C++ поддерживает [управление обоими типами документных свойств, встроенными и пользовательскими](/cells/ru/cpp/managing-document-properties/). Класс IWorkbook Aspose.Cells представляет файл Excel. Для доступа к встроенным документным свойствам используйте IWorkbook.GetBuiltInDocumentProperties, в то время как пользовательские документные свойства могут быть получены с использованием метода IWorkbook.GetCustomDocumentProperties.

Следующий образец кода загружает существующую образцовую электронную таблицу и считывает встроенные свойства документа, такие как Название, Тема и пользовательское свойство с именем Мой_пользовательский_1.

**C++**

{{< highlight csharp >}}

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
### **Поддержка объектов ListObjects**
Таблица Excel представляет собой матрицу ячеек, содержащую любое количество строк и столбцов, в то время как та же таблица называется Объектом списка в Aspose.Cells for C++ API. Пространство имен Aspose::Cells::Tables содержит все необходимые классы, которые работают с операциями, связанными с Объектами списка. Самые важные классы - это IListObject и IListObjectCollection, которые позволяют [создавать и форматировать Объекты списка](/cells/ru/cpp/create-and-format-table/) и так далее.

Следующий образец кода загружает файл образца электронной таблицы, затем создает объект списка (таблицу) в диапазоне A1:H10, затем использует различные методы для отображения итоговой суммы.

**C++**

{{< highlight csharp >}}

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
API Aspose.Cells for C++ можно использовать для группировки строк и столбцов при использовании класса ICells, который в основном представляет собой коллекцию всех ячеек в заданном листе. Класс ICells предлагает методы GroupRows и GroupColumns для [группировки строк и столбцов](/cells/ru/cpp/group-rows-and-columns-of-worksheet/) соответственно.

Приведенный ниже фрагмент кода демонстрирует простой сценарий использования обоих упомянутых методов.

**C++**

{{< highlight csharp >}}

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
API Aspose.Cells for C++ теперь поддерживает использование и манипулирование темами, предлагаемыми приложением Excel.
#### **Возможность применения пользовательских цветов темы**
В следующем фрагменте показано, как [создать новую тему с пользовательскими цветами](/cells/ru/cpp/apply-custom-theme-colors-of-the-workbook/) для книги.

**C++**

{{< highlight csharp >}}

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
#### **Поддержка изменения тем цветов**
В следующем образце кода показано, как [читать и изменять цвета темы книги](/cells/ru/cpp/apply-custom-theme-colors-of-the-workbook/). Образец кода загружает существующую электронную таблицу, читает ее цвета темы, т.е. Accent1-Accent6, и изменяет цвета перед сохранением электронной таблицы.

**C++**

{{< highlight csharp >}}

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
#### **Возможность копирования тем между книгами**
В следующем образце кода показано, как [скопировать тему из одной книги в другую](/cells/ru/cpp/copy-theme-from-one-workbook-to-another/), что может быть полезно при применении встроенных или пользовательских тем для нескольких электронных таблиц.

**C++**

{{< highlight csharp >}}

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
С выпуском Aspose.Cells for C++ 16.12.0 мы переименовали несколько методов, чтобы сохранить единообразие интерфейсов. Список всех переименованных API приведен ниже.
#### **Переименован метод ICell::SetStyle в ICell::SetIStyle**
#### **Переименован метод ICell::SetCharacters в ICell::SetIFontSettings**
#### **Переименован метод ICellsColor::SetThemeColor в ICellsColor::SetIThemeColor**
#### **Переименован метод ICells::SetStyle в ICells::SetIStyle**
#### **Переименован метод ICellsHelper::GetDPI_i в ICellsHelper::GetDPI**
#### **Переименован метод ICellsHelper::SetDPI_i в ICellsHelper::SetDPI**
#### **Переименован метод ICellsHelper::GetVersion_i в ICellsHelper::GetVersion**
#### **Переименован метод ICellsHelper::IsProtectedByRMS_i в ICellsHelper::IsProtectedByRMS**
#### **Переименован метод ICellsHelper::IsProtectedByRMS_i в ICellsHelper::IsProtectedByRMS**
#### **Переименован метод ICellsHelper::CellNameToIndex_i в ICellsHelper::CellNameToIndex**
#### **Переименован метод ICellsHelper::CellIndexToName_i в ICellsHelper::CellIndexToName**
#### **Переименован метод ICellsHelper::ColumnIndexToName_i в ICellsHelper::ColumnIndexToName**
#### **Переименован метод ICellsHelper::ColumnNameToIndex_i в ICellsHelper::ColumnNameToIndex**
#### **Переименован метод ICellsHelper::RowIndexToName_i в ICellsHelper::RowIndexToName**
#### **Переименован метод ICellsHelper::RowNameToIndex_i в ICellsHelper::RowNameToIndex**
#### **Переименован метод ICellsHelper::ConvertR1C1FormulaToA1_i в ICellsHelper::ConvertR1C1FormulaToA1**
#### **Переименован метод ICellsHelper::ConvertA1FormulaToR1C1_i в ICellsHelper::ConvertA1FormulaToR1C1**
#### **Переименован метод ICellsHelper::GetDateTimeFromDouble_i в ICellsHelper::GetDateTimeFromDouble**
#### **Переименован метод ICellsHelper::GetDoubleFromDateTime_i в ICellsHelper::GetDoubleFromDateTime**
#### **Переименован метод ICellsHelper::DetectLoadFormat_i в ICellsHelper::DetectLoadFormat**
#### **Переименован метод ICellsHelper::DetectFileFormat_i в ICellsHelper::DetectFileFormat**
#### **Переименован метод ICellsHelper::GetFontDir_i в ICellsHelper::GetFontDir**
#### **Переименован метод ICellsHelper::SetFontDir_i в ICellsHelper::SetFontDir**
#### **Переименован метод ICellsHelper::GetFontDirs_i в ICellsHelper::GetFontDirs**
#### **Переименован метод ICellsHelper::SetFontDirs_i в ICellsHelper::SetFontDirs**
#### **Переименован метод ICellsHelper::GetFontFiles_i в ICellsHelper::GetFontFiles**
#### **Переименован метод ICellsHelper::SetFontFiles_i в ICellsHelper::SetFontFiles**
#### **Переименован метод ICellsHelper::GetStartupPath_i в ICellsHelper::GetStartupPath**
#### **Переименованный метод ICellsHelper::SetStartupPath_i в ICellsHelper::SetStartupPath**
#### **Переименованный метод ICellsHelper::GetAltStartPath_i в ICellsHelper::GetAltStartPath**
#### **Переименованный метод ICellsHelper::SetAltStartPath_i в ICellsHelper::SetAltStartPath**
#### **Переименованный метод ICellsHelper::GetLibraryPath_i в ICellsHelper::GetLibraryPath**
#### **Переименованный метод ICellsHelper::SetLibraryPath_i в ICellsHelper::SetLibraryPath**
#### **Переименованный метод ICellsHelper::GetUsedColors_i в ICellsHelper::GetUsedColors**
#### **Переименованный метод ICellsHelper::AddAddInFunction_i в ICellsHelper::AddAddInFunction**
#### **Переименованный метод ICellsHelper::MergeFiles_i в ICellsHelper::MergeFiles**
#### **Переименованный метод IColumnCollection::GetByIndex_i в IColumnCollection::GetIColumn**
#### **Переименованный метод IFileFormatUtil::DetectFileFormat_i в IFileFormatUtil::DetectFileFormat**
#### **Переименованный метод IFileFormatUtil::ExtensionToSaveFormat_i в IFileFormatUtil::ExtensionToSaveFormat**
#### **Переименованный метод IFileFormatUtil::IsTemplateFormat_i в IFileFormatUtil::IsTemplateFormat**
#### **Переименованный метод IFileFormatUtil::LoadFormatToExtension_i в IFileFormatUtil::LoadFormatToExtension**
#### **Переименованный метод IFileFormatUtil::LoadFormatToSaveFormat_i в IFileFormatUtil::LoadFormatToSaveFormat**
#### **Переименованный метод IFileFormatUtil::SaveFormatToExtension_i в IFileFormatUtil::SaveFormatToExtension**
#### **Переименованный метод IFileFormatUtil::SaveFormatToLoadFormat_i в IFileFormatUtil::SaveFormatToLoadFormat**
#### **Переименованный метод IRange::SetStyle в IRange::SetIStyle**
#### **Переименованный метод IFindOptions::SetRange в IFindOptions::SetIRange**
#### **Переименованный метод ILoadOptions::SetLoadDataOptions в ILoadOptions::SetILoadDataOptions**
#### **Переименованный метод IWorkbook::SetSettings в IWorkbook::SetISettings**
#### **Переименован метод IWorkbook::SetDefaultStyle в IWorkbook::SetDefaultIStyle**
