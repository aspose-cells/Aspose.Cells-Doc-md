---
title: 公共 API Aspose.Cells 16.12.0 的变化
type: docs
weight: 10
url: /zh/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 16.11.0 到 16.12.0 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持数据透视表**
C++ 的第二个版本 Aspose.Cells 支持数据透视表的创建和操作。 Aspose.Cells 为 C++ 提供了表示数据透视表对象的 IPivotTable 类，而 IPivotTableCollection 表示数据透视表的集合。可以通过 IWorksheet 对象访问 IPivotTableCollection，并且可以在使用 IPivotTableCollection.Add 方法时将新的数据透视表添加到集合中。

下面的代码片段演示了使用 Aspose.Cells 为 C++ API 是多么简单[从头开始创建数据透视表](/cells/zh/cpp/create-pivot-table/).

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

除了创建新的数据透视表，Aspose.Cells for C++ API 还支持操作现有的数据透视表。 API目前支持更改数据透视表源范围内的数据，然后刷新。根据需要操作数据透视表后，最好使用 IPivotTable.RefreshData 和 IPivotTable.CalculateData 方法根据更新的数据源刷新数据透视表。

以下代码片段使用 Aspose.Cells 为 C++ API 到[操纵现有的数据透视表](/cells/zh/cpp/manipulate-pivot-table/).

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
### **支持条件格式规则**
Aspose.Cells for C++ 现在提供了通过公开 IFormatCondition 类向工作表添加条件格式设置规则的功能。上述类还提供了以下方法来[应用条件格式规则](/cells/zh/cpp/apply-conditional-formatting-in-worksheet/)根据申请要求。

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

以下示例代码显示如何在单元格 A1 和 B2 上添加类型为 Cell 值的条件格式设置规则。

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
### **支持超链接**
Aspose.Cells 为 C++ 现在支持[向工作表单元格添加超链接](/cells/zh/cpp/add-hyperlinks-to-the-cells/).为了提供此功能，C++ 16.12.0 的 Aspose.Cells 公开了可通过 IWorksheet 对象访问的 IHyperlinkCollection 类，而在使用 IHyperlinkCollection.Add 方法时可以将超链接添加到集合中，如下所示。

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
### **支持文档属性**
Excel 应用程序支持 2 种类型的文档属性，如下所列。

- 系统定义（内置）属性：内置属性包含有关文档的一般信息，如文档标题、作者姓名、文档统计信息等。
- 用户定义（自定义）属性：由最终用户以名称值对的形式定义的自定义属性。

Aspose.Cells 为 C++ 支持[管理两种类型的文档属性，内置和自定义](/cells/zh/cpp/managing-document-properties/)Aspose.Cells' IWorkbook 类表示一个 Excel 文件。要访问内置文档属性，请使用 IWorkbook.GetBuiltInDocumentProperties，而使用 IWorkbook.GetCustomDocumentProperties 方法可以访问自定义文档属性。

以下示例代码加载现有示例电子表格并读取内置文档属性，例如标题、主题和名为 MyCustom1 的自定义属性。

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
### **支持 ListObjects**
 Excel 表格是包含任意数量的行和列的单元格矩阵，而同一个表格在 Aspose.Cells 中被称为 C++ API 的列表对象。 Aspose::Cells::Tables 命名空间包含处理与列表对象相关的操作的所有必要类。最值得一提的类是 IListObject 和 IListObjectCollection，它们允许[创建和格式化列表对象](/cells/zh/cpp/create-and-format-table/)等等。

以下示例代码加载示例电子表格文件，然后在 A1:H10 范围内创建一个列表对象（表），然后使用其各种方法显示小计。

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
### **支持行和列分组**
Aspose.Cells 为 C++ API 可用于在使用 ICells 类时对行和列进行分组，ICells 类基本上是给定工作表中所有单元格的集合。 ICells 类提供了 GroupRows 和 GroupColumns 方法，以便[对行和列进行分组](/cells/zh/cpp/group-rows-and-columns-of-worksheet/)分别。

以下代码片段演示了上述两种方法的简单使用场景。

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
### **支持主题**
Aspose.Cells 用于 C++ API 现在支持使用和操作 Excel 应用程序提供的主题。
#### **能够应用自定义主题颜色**
以下代码段尝试[使用自定义颜色创建新主题](/cells/zh/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/)对于工作簿。

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
#### **支持主题颜色的操作**
以下示例代码显示了如何[读取和修改工作簿的主题颜色](/cells/zh/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/).示例代码加载现有电子表格，读取其主题颜色，即 Accent1-Accent6，并在保存电子表格之前修改颜色。

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
#### **跨工作簿复制主题的能力**
以下示例代码显示了如何[将主题从一个工作簿复制到另一个](/cells/zh/cpp/copy-theme-from-one-workbook-to-another/)，这可能有助于在多个电子表格上应用内置或自定义主题。

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
## **重命名的 API**
随着 C++ 16.12.0 的 Aspose.Cells 的发布，我们对一些方法进行了重命名以保持接口统一。所有重命名的 API 列表如下。
#### **将 ICell::SetStyle 方法重命名为 ICell::SetIStyle**
#### **将 ICell::SetCharacters 方法重命名为 ICell::SetIFontSettings**
#### **将 ICellsColor::SetThemeColor 方法重命名为 ICellsColor::SetIThemeColor**
#### **将 ICells::SetStyle 方法重命名为 ICells::SetIStyle**
#### **将 ICellsHelper::GetDPI_i 方法重命名为 ICellsHelper::GetDPI**
#### **将 ICellsHelper::SetDPI_i 方法重命名为 ICellsHelper::SetDPI**
#### **将 ICellsHelper::GetVersion_i 方法重命名为 ICellsHelper::GetVersion**
#### **将 ICellsHelper::IsProtectedByRMS_i 方法重命名为 ICellsHelper::IsProtectedByRMS**
#### **将 ICellsHelper::IsProtectedByRMS_i 方法重命名为 ICellsHelper::IsProtectedByRMS**
#### **将 ICellsHelper::CellNameToIndex_i 方法重命名为 ICellsHelper::CellNameToIndex**
#### **将 ICellsHelper::CellIndexToName_i 方法重命名为 ICellsHelper::CellIndexToName**
#### **将 ICellsHelper::ColumnIndexToName_i 方法重命名为 ICellsHelper::ColumnIndexToName**
#### **将 ICellsHelper::ColumnNameToIndex_i 方法重命名为 ICellsHelper::ColumnNameToIndex**
#### **将 ICellsHelper::RowIndexToName_i 方法重命名为 ICellsHelper::RowIndexToName**
#### **将 ICellsHelper::RowNameToIndex_i 方法重命名为 ICellsHelper::RowNameToIndex**
#### **将 ICellsHelper::ConvertR1C1FormulaToA1_i 方法重命名为 ICellsHelper::ConvertR1C1FormulaToA1**
#### **将 ICellsHelper::ConvertA1FormulaToR1C1_i 方法重命名为 ICellsHelper::ConvertA1FormulaToR1C1**
#### **将 ICellsHelper::GetDateTimeFromDouble_i 方法重命名为 ICellsHelper::GetDateTimeFromDouble**
#### **将 ICellsHelper::GetDoubleFromDateTime_i 方法重命名为 ICellsHelper::GetDoubleFromDateTime**
#### **将 ICellsHelper::DetectLoadFormat_i 方法重命名为 ICellsHelper::DetectLoadFormat**
#### **将 ICellsHelper::DetectFileFormat_i 方法重命名为 ICellsHelper::DetectFileFormat**
#### **将 ICellsHelper::GetFontDir_i 方法重命名为 ICellsHelper::GetFontDir**
#### **将 ICellsHelper::SetFontDir_i 方法重命名为 ICellsHelper::SetFontDir**
#### **将 ICellsHelper::GetFontDirs_i 方法重命名为 ICellsHelper::GetFontDirs**
#### **将 ICellsHelper::SetFontDirs_i 方法重命名为 ICellsHelper::SetFontDirs**
#### **将 ICellsHelper::GetFontFiles_i 方法重命名为 ICellsHelper::GetFontFiles**
#### **将 ICellsHelper::SetFontFiles_i 方法重命名为 ICellsHelper::SetFontFiles**
#### **将 ICellsHelper::GetStartupPath_i 方法重命名为 ICellsHelper::GetStartupPath**
#### **将 ICellsHelper::SetStartupPath_i 方法重命名为 ICellsHelper::SetStartupPath**
#### **将 ICellsHelper::GetAltStartPath_i 方法重命名为 ICellsHelper::GetAltStartPath**
#### **将 ICellsHelper::SetAltStartPath_i 方法重命名为 ICellsHelper::SetAltStartPath**
#### **将 ICellsHelper::GetLibraryPath_i 方法重命名为 ICellsHelper::GetLibraryPath**
#### **将 ICellsHelper::SetLibraryPath_i 方法重命名为 ICellsHelper::SetLibraryPath**
#### **将 ICellsHelper::GetUsedColors_i 方法重命名为 ICellsHelper::GetUsedColors**
#### **将 ICellsHelper::AddAddInFunction_i 方法重命名为 ICellsHelper::AddAddInFunction**
#### **将 ICellsHelper::MergeFiles_i 方法重命名为 ICellsHelper::MergeFiles**
#### **将 IColumnCollection::GetByIndex_i 方法重命名为 IColumnCollection::GetIColumn**
#### **将 IFileFormatUtil::DetectFileFormat_i 方法重命名为 IFileFormatUtil::DetectFileFormat**
#### **将 IFileFormatUtil::ExtensionToSaveFormat_i 方法重命名为 IFileFormatUtil::ExtensionToSaveFormat**
#### **将 IFileFormatUtil::IsTemplateFormat_i 方法重命名为 IFileFormatUtil::IsTemplateFormat**
#### **将 IFileFormatUtil::LoadFormatToExtension_i 方法重命名为 IFileFormatUtil::LoadFormatToExtension**
#### **将 IFileFormatUtil::LoadFormatToSaveFormat_i 方法重命名为 IFileFormatUtil::LoadFormatToSaveFormat**
#### **将 IFileFormatUtil::SaveFormatToExtension_i 方法重命名为 IFileFormatUtil::SaveFormatToExtension**
#### **将 IFileFormatUtil::SaveFormatToLoadFormat_i 方法重命名为 IFileFormatUtil::SaveFormatToLoadFormat**
#### **将 IRange::SetStyle 方法重命名为 IRange::SetIStyle**
#### **将 IFindOptions::SetRange 方法重命名为 IFindOptions::SetIRange**
#### **将 ILoadOptions::SetLoadDataOptions 方法重命名为 ILoadOptions::SetILoadDataOptions**
#### **将 IWorkbook::SetSettings 方法重命名为 IWorkbook::SetISettings**
#### **将 IWorkbook::SetDefaultStyle 方法重命名为 IWorkbook::SetDefaultIStyle**
