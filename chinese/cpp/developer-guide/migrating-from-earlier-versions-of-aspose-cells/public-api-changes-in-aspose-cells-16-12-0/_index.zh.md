---
title: Aspose.Cells 16.12.0中的公共API更改
type: docs
weight: 10
url: /zh/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

本文档描述了从版本16.11.0到16.12.0的Aspose.Cells API的变化，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还描述了Aspose.Cells背后行为的任何更改。

{{% /alert %}} 
## **已添加API**
### **支持数据透视表**
Aspose.Cells for C++的第二个版本支持创建和操作数据透视表。Aspose.Cells for C++提供了表示数据透视表对象的IPivotTable类，而IPivotTableCollection表示数据透视表的集合。可以通过IWorksheet对象访问IPivotTableCollection，并且可以通过IPivotTableCollection.Add方法向集合添加新的数据透视表。

以下代码片段演示了使用Aspose.Cells for C++ API从头开始[创建数据透视表](/cells/zh/cpp/create-pivot-table/)的简便性。

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

除了创建新的数据透视表外，Aspose.Cells for C++ API还支持操作现有数据透视表。目前，该API支持更改数据透视表的源范围数据，然后刷新它。一旦按需操作数据透视表，最好使用IPivotTable.RefreshData和IPivotTable.CalculateData方法刷新根据更新的数据源数据更新数据透视表。

以下代码片段使用Aspose.Cells for C++ API来[操作现有数据透视表](/cells/zh/cpp/manipulate-pivot-table/)。

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
### **支持条件格式规则**
Aspose.Cells for C++现在通过公开IFormatCondition类提供了向工作表添加条件格式规则的功能。前述类还提供以下方法，根据应用程序要求[应用条件格式规则](/cells/zh/cpp/apply-conditional-formatting-in-worksheet/)。

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

以下示例代码演示了如何在单元格A1和B2上添加单元格值类型的条件格式规则。

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
### **支持超链接**
Aspose.Cells for C++ 现在支持[在工作表单元格中添加超链接](/cells/zh/cpp/add-hyperlinks-to-the-cells/)。为了提供此功能，Aspose.Cells for C++ 16.12.0已经暴露了IHyperlinkCollection类，该类可以通过IWorksheet对象访问，而在使用IHyperlinkCollection.Add方法时可以向集合中添加超链接，如下所示。

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
### **支持文档属性**
Excel应用程序支持以下两种类型的文档属性。

- 系统定义的(内置)属性：内置属性包含有关文档的一般信息，如文档标题、作者名称、文档统计信息等。
- 用户自定义(自定义)属性：最终用户以名称值对的形式定义的自定义属性。

Aspose.Cells for C++支持[管理内置和自定义文档属性](/cells/zh/cpp/managing-document-properties/)。Aspose.Cells的IWorkbook类表示一个Excel文件。为了访问内置文档属性，使用IWorkbook.GetBuiltInDocumentProperties，而可以使用IWorkbook.GetCustomDocumentProperties方法来访问自定义文档属性。

以下示例代码加载现有的示例电子表格并读取标题、主题和名为MyCustom1的自定义属性。

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
### **支持ListObjects**
Excel表是包含任意行和列数量的单元格矩阵，而相同表在Aspose.Cells for C++ API中被称为List Object。Aspose::Cells::Tables命名空间包含处理与List Objects相关操作的所有必要类。最值得一提的类包括IListObject和IListObjectCollection，它们允许[创建和格式化List Objects](/cells/zh/cpp/create-and-format-table/)等操作。

以下示例代码加载示例电子表格文件，然后在范围A1:H10内创建一个List Object(表)，然后利用其各种方法显示小计。

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
### **支持行和列分组**
Aspose.Cells for C++ API可用于在ICells类中分组行和列，ICells类基本上是给定工作表中所有单元格的集合。ICells类提供了GroupRows和GroupColumns方法，分别用于[分组行和列](/cells/zh/cpp/group-rows-and-columns-of-worksheet/)。

以下代码片段演示了上述两种方法的简单使用场景。

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
### **支持主题**
Aspose.Cells for C++ APIs现在支持使用和操作Excel应用程序提供的主题。
#### **应用自定义主题颜色的能力**
以下代码片段尝试为工作簿[创建一个具有自定义颜色的新主题](/cells/zh/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/)。

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
#### **支持主题颜色操作**
以下示例代码展示了如何[读取和修改工作簿的主题颜色](/cells/zh/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/)。示例代码加载现有电子表格，读取其主题颜色即Accent1-Accent6，并在保存电子表格之前修改这些颜色。

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
#### **能够在工作簿之间复制主题的能力**
以下示例代码显示了如何[从一个工作簿复制主题到另一个工作簿](/cells/zh/cpp/copy-theme-from-one-workbook-to-another/)，这对于在多个电子表格上应用内置或自定义主题非常有用。

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
## **API已重命名**
随着 Aspose.Cells for C++ 16.12.0 版的发布，为了保持接口统一，我们重命名了一些方法。所有重命名的 API 列表如下。
#### **重命名 ICell::SetStyle 方法为 ICell::SetIStyle**
#### **重命名 ICell::SetCharacters 方法为 ICell::SetIFontSettings**
#### **重命名 ICellsColor::SetThemeColor 方法为 ICellsColor::SetIThemeColor**
#### **重命名 ICells::SetStyle 方法为 ICells::SetIStyle**
#### **重命名 ICellsHelper::GetDPI_i 方法为 ICellsHelper::GetDPI**
#### **重命名 ICellsHelper::SetDPI_i 方法为 ICellsHelper::SetDPI**
#### **重命名 ICellsHelper::GetVersion_i 方法为 ICellsHelper::GetVersion**
#### **重命名 ICellsHelper::IsProtectedByRMS_i 方法为 ICellsHelper::IsProtectedByRMS**
#### **重命名 ICellsHelper::IsProtectedByRMS_i 方法为 ICellsHelper::IsProtectedByRMS**
#### **重命名 ICellsHelper::CellNameToIndex_i 方法为 ICellsHelper::CellNameToIndex**
#### **重命名 ICellsHelper::CellIndexToName_i 方法为 ICellsHelper::CellIndexToName**
#### **重命名 ICellsHelper::ColumnIndexToName_i 方法为 ICellsHelper::ColumnIndexToName**
#### **重命名 ICellsHelper::ColumnNameToIndex_i 方法为 ICellsHelper::ColumnNameToIndex**
#### **重命名 ICellsHelper::RowIndexToName_i 方法为 ICellsHelper::RowIndexToName**
#### **重命名 ICellsHelper::RowNameToIndex_i 方法为 ICellsHelper::RowNameToIndex**
#### **重命名 ICellsHelper::ConvertR1C1FormulaToA1_i 方法为 ICellsHelper::ConvertR1C1FormulaToA1**
#### **重命名 ICellsHelper::ConvertA1FormulaToR1C1_i 方法为 ICellsHelper::ConvertA1FormulaToR1C1**
#### **重命名 ICellsHelper::GetDateTimeFromDouble_i 方法为 ICellsHelper::GetDateTimeFromDouble**
#### **重命名 ICellsHelper::GetDoubleFromDateTime_i 方法为 ICellsHelper::GetDoubleFromDateTime**
#### **重命名 ICellsHelper::DetectLoadFormat_i 方法为 ICellsHelper::DetectLoadFormat**
#### **重命名 ICellsHelper::DetectFileFormat_i 方法为 ICellsHelper::DetectFileFormat**
#### **重命名 ICellsHelper::GetFontDir_i 方法为 ICellsHelper::GetFontDir**
#### **重命名 ICellsHelper::SetFontDir_i 方法为 ICellsHelper::SetFontDir**
#### **重命名 ICellsHelper::GetFontDirs_i 方法为 ICellsHelper::GetFontDirs**
#### **重命名 ICellsHelper::SetFontDirs_i 方法为 ICellsHelper::SetFontDirs**
#### **将ICellsHelper::GetFontFiles_i方法重命名为ICellsHelper::GetFontFiles**
#### **将ICellsHelper::SetFontFiles_i方法重命名为ICellsHelper::SetFontFiles**
#### **将ICellsHelper::GetStartupPath_i方法重命名为ICellsHelper::GetStartupPath**
#### **将ICellsHelper::SetStartupPath_i方法重命名为ICellsHelper::SetStartupPath**
#### **将ICellsHelper::GetAltStartPath_i方法重命名为ICellsHelper::GetAltStartPath**
#### **将ICellsHelper::SetAltStartPath_i方法重命名为ICellsHelper::SetAltStartPath**
#### **将ICellsHelper::GetLibraryPath_i方法重命名为ICellsHelper::GetLibraryPath**
#### **将ICellsHelper::SetLibraryPath_i方法重命名为ICellsHelper::SetLibraryPath**
#### **将ICellsHelper::GetUsedColors_i方法重命名为ICellsHelper::GetUsedColors**
#### **将ICellsHelper::AddAddInFunction_i方法重命名为ICellsHelper::AddAddInFunction**
#### **将ICellsHelper::MergeFiles_i方法重命名为ICellsHelper::MergeFiles**
#### **将IColumnCollection::GetByIndex_i方法重命名为IColumnCollection::GetIColumn**
#### **将IFileFormatUtil::DetectFileFormat_i方法重命名为IFileFormatUtil::DetectFileFormat**
#### **将IFileFormatUtil::ExtensionToSaveFormat_i方法重命名为IFileFormatUtil::ExtensionToSaveFormat**
#### **将IFileFormatUtil::IsTemplateFormat_i方法重命名为IFileFormatUtil::IsTemplateFormat**
#### **将IFileFormatUtil::LoadFormatToExtension_i方法重命名为IFileFormatUtil::LoadFormatToExtension**
#### **将IFileFormatUtil::LoadFormatToSaveFormat_i方法重命名为IFileFormatUtil::LoadFormatToSaveFormat**
#### **将IFileFormatUtil::SaveFormatToExtension_i方法重命名为IFileFormatUtil::SaveFormatToExtension**
#### **将IFileFormatUtil::SaveFormatToLoadFormat_i方法重命名为IFileFormatUtil::SaveFormatToLoadFormat**
#### **将IRange::SetStyle方法重命名为IRange::SetIStyle**
#### **将IFindOptions::SetRange方法重命名为IFindOptions::SetIRange**
#### **将ILoadOptions::SetLoadDataOptions方法重命名为ILoadOptions::SetILoadDataOptions**
#### **将IWorkbook::SetSettings方法重命名为IWorkbook::SetISettings**
#### **将IWorkbook::SetDefaultStyle方法重命名为IWorkbook::SetDefaultIStyle**
