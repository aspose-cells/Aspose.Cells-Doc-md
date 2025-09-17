##Public API Changes in Aspose.Cells 16.12.0
This document describes the changes to the Aspose.Cells API from version 16.11.0 to 16.12.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added APIs**
### **Support for Pivot Tables**
The second release of Aspose.Cells for C++ supports creation as well as the manipulation of the Pivot Tables. Aspose.Cells for C++ provides the IPivotTable class which represents a Pivot Table object whereas IPivotTableCollection represents a collection of Pivot Tables. The IPivotTableCollection can be accessed via the IWorksheet object and a new Pivot Table can be added to the collection while using the IPivotTableCollection.Add method.
The following code snippet demonstrates how simple is to use Aspose.Cells for C++ API to [create Pivot Tables from scratch](https://docs.aspose.com/cells/cpp/create-pivot-table/).
**C++**
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
Besides creating new Pivot Tables, Aspose.Cells for C++ APIs also support to manipulate existing Pivot Tables. The API currently supports to change the data at the source range of the Pivot Table and then refresh it. Once the Pivot Table has been manipulated as desired, it is best to use the IPivotTable.RefreshData and IPivotTable.CalculateData methods to refresh the Pivot Table against the updated data source.
The following code snippet uses the Aspose.Cells for C++ API to [manipulate an existing Pivot Table](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/).
**C++**
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
### **Support for Conditional Formatting Rules**
Aspose.Cells for C++ now provides the ability to add conditional formatting rules to the worksheet by exposing the IFormatCondition class. The aforementioned class further provides the following methods to [apply the conditional formatting rules](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) as per application requirements.
- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10
The following sample code shows how to add a conditional formatting rule of type Cell Value on cells A1 and B2.
**C++**
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
### **Support for Hyperlinks**
Aspose.Cells for C++ now supports [adding hyperlinks to the worksheet cells](https://docs.aspose.com/cells/cpp/add-hyperlinks-to-the-cells/). In order to provide this feature, the Aspose.Cells for C++ 16.12.0 has exposed the IHyperlinkCollection class which is accessible via the IWorksheet object whereas a hyperlink can be added to the collection while using the IHyperlinkCollection.Add method as demonstrated below.
**C++**
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
### **Support for Document Properties**
Excel application supports 2 types of document properties as listed below.
- System defined (built-in) properties: Built-in properties contain general information about the document like document title, author name, document statistics and so on.
- User-defined (custom) properties: Custom properties defined by the end user in the form of name value pair.
Aspose.Cells for C++ supports [managing both types of document properties, built-in and custom](https://docs.aspose.com/cells/cpp/managing-document-properties/). Aspose.Cells’ IWorkbook class represents an Excel file. In order to access the built-in document properties, use IWorkbook.GetBuiltInDocumentProperties whereas the custom document properties can be accessed while using the IWorkbook.GetCustomDocumentProperties method.
The following sample code loads an existing sample spreadsheet and reads the built-in document properties such as Title, Subject and custom property by the name MyCustom1.
**C++**
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
### **Support for ListObjects**
An Excel table is a matrix of cells containing any number of rows and columns whereas the same table is referred to be as a List Object in Aspose.Cells for C++ APIs. The Aspose::Cells::Tables namespace contains all the necessary classes that deals with the operations related to the List Objects. Most worth mentioning classes are IListObject and IListObjectCollection which allow to [create and format List Objects](https://docs.aspose.com/cells/cpp/create-and-format-table/) and so on.
The following sample code loads the sample spreadsheet file and then creates a List Object (table) in a range A1:H10, then make use of its various methods to show the subtotal.
**C++**
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
### **Support for Row & Column Grouping**
Aspose.Cells for C++ API can be used to group rows & columns while using the ICells class which is basically the collection of all cells in a given worksheet. The ICells class offers the GroupRows and GroupColumns methods in order to [group rows and columns](https://docs.aspose.com/cells/cpp/group-rows-and-columns-of-worksheet/) respectively.
The following code snippet demonstrates the simple usage scenario of both aforementioned methods.
**C++**
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
### **Support for Themes**
Aspose.Cells for C++ APIs now support to use and manipulate the themes offered by Excel application.
#### **Ability to Apply the Custom Theme Colors**
The following snippet tries to [create a new theme with custom colors](https://docs.aspose.com/cells/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) for the workbook.
**C++**
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
#### **Support for Manipulation of Theme Colors**
The following sample code shows how to [read and modify theme colors of the workbook](https://docs.aspose.com/cells/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). The sample code loads an existing spreadsheet, read its theme colors i.e. Accent1-Accent6, and modifies the colors before saving the spreadsheet.
**C++**
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
#### **Ability to Copy Themes Across Workbooks**
The following sample code shows how to [copy theme from one workbook to another](https://docs.aspose.com/cells/cpp/copy-theme-from-one-workbook-to-another/), which could be useful in applying built-in or custom themes on multiple spreadsheets.
**C++**
//Read excel file that has Damask theme applied on it
intrusive_ptr<IWorkbook> damask = Factory::CreateIWorkbook(damaskPath);
//Read your sample excel file
intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);
//Copy theme from source file
wb->CopyTheme(damask);
//Save the workbook in xlsx format
wb->Save(outputPath, SaveFormat_Xlsx);
## **Renamed APIs**
With the release of Aspose.Cells for C++ 16.12.0, we have renamed a few method in order to keep the interfaces unified. The list of all renamed APIs is as follow.
#### **Renamed ICell::SetStyle method to ICell::SetIStyle**
#### **Renamed ICell::SetCharacters method to ICell::SetIFontSettings**
#### **Renamed ICellsColor::SetThemeColor method to ICellsColor::SetIThemeColor**
#### **Renamed ICells::SetStyle method to ICells::SetIStyle**
#### **Renamed ICellsHelper::GetDPI_i method to ICellsHelper::GetDPI**
#### **Renamed ICellsHelper::SetDPI_i method to ICellsHelper::SetDPI**
#### **Renamed ICellsHelper::GetVersion_i method to ICellsHelper::GetVersion**
#### **Renamed ICellsHelper::IsProtectedByRMS_i method to ICellsHelper::IsProtectedByRMS**
#### **Renamed ICellsHelper::IsProtectedByRMS_i method to ICellsHelper::IsProtectedByRMS**
#### **Renamed ICellsHelper::CellNameToIndex_i method to ICellsHelper::CellNameToIndex**
#### **Renamed ICellsHelper::CellIndexToName_i method to ICellsHelper::CellIndexToName**
#### **Renamed ICellsHelper::ColumnIndexToName_i method to ICellsHelper::ColumnIndexToName**
#### **Renamed ICellsHelper::ColumnNameToIndex_i method to ICellsHelper::ColumnNameToIndex**
#### **Renamed ICellsHelper::RowIndexToName_i method to ICellsHelper::RowIndexToName**
#### **Renamed ICellsHelper::RowNameToIndex_i method to ICellsHelper::RowNameToIndex**
#### **Renamed ICellsHelper::ConvertR1C1FormulaToA1_i method to ICellsHelper::ConvertR1C1FormulaToA1**
#### **Renamed ICellsHelper::ConvertA1FormulaToR1C1_i method to ICellsHelper::ConvertA1FormulaToR1C1**
#### **Renamed ICellsHelper::GetDateTimeFromDouble_i method to ICellsHelper::GetDateTimeFromDouble**
#### **Renamed ICellsHelper::GetDoubleFromDateTime_i method to ICellsHelper::GetDoubleFromDateTime**
#### **Renamed ICellsHelper::DetectLoadFormat_i method to ICellsHelper::DetectLoadFormat**
#### **Renamed ICellsHelper::DetectFileFormat_i method to ICellsHelper::DetectFileFormat**
#### **Renamed ICellsHelper::GetFontDir_i method to ICellsHelper::GetFontDir**
#### **Renamed ICellsHelper::SetFontDir_i method to ICellsHelper::SetFontDir**
#### **Renamed ICellsHelper::GetFontDirs_i method to ICellsHelper::GetFontDirs**
#### **Renamed ICellsHelper::SetFontDirs_i method to ICellsHelper::SetFontDirs**
#### **Renamed ICellsHelper::GetFontFiles_i method to ICellsHelper::GetFontFiles**
#### **Renamed ICellsHelper::SetFontFiles_i method to ICellsHelper::SetFontFiles**
#### **Renamed ICellsHelper::GetStartupPath_i method to ICellsHelper::GetStartupPath**
#### **Renamed ICellsHelper::SetStartupPath_i method to ICellsHelper::SetStartupPath**
#### **Renamed ICellsHelper::GetAltStartPath_i method to ICellsHelper::GetAltStartPath**
#### **Renamed ICellsHelper::SetAltStartPath_i method to ICellsHelper::SetAltStartPath**
#### **Renamed ICellsHelper::GetLibraryPath_i method to ICellsHelper::GetLibraryPath**
#### **Renamed ICellsHelper::SetLibraryPath_i method to ICellsHelper::SetLibraryPath**
#### **Renamed ICellsHelper::GetUsedColors_i method to ICellsHelper::GetUsedColors**
#### **Renamed ICellsHelper::AddAddInFunction_i method to ICellsHelper::AddAddInFunction**
#### **Renamed ICellsHelper::MergeFiles_i method to ICellsHelper::MergeFiles**
#### **Renamed IColumnCollection::GetByIndex_i method to IColumnCollection::GetIColumn**
#### **Renamed IFileFormatUtil::DetectFileFormat_i method to IFileFormatUtil::DetectFileFormat**
#### **Renamed IFileFormatUtil::ExtensionToSaveFormat_i method to IFileFormatUtil::ExtensionToSaveFormat**
#### **Renamed IFileFormatUtil::IsTemplateFormat_i method to IFileFormatUtil::IsTemplateFormat**
#### **Renamed IFileFormatUtil::LoadFormatToExtension_i method to IFileFormatUtil::LoadFormatToExtension**
#### **Renamed IFileFormatUtil::LoadFormatToSaveFormat_i method to IFileFormatUtil::LoadFormatToSaveFormat**
#### **Renamed IFileFormatUtil::SaveFormatToExtension_i method to IFileFormatUtil::SaveFormatToExtension**
#### **Renamed IFileFormatUtil::SaveFormatToLoadFormat_i method to IFileFormatUtil::SaveFormatToLoadFormat**
#### **Renamed IRange::SetStyle method to IRange::SetIStyle**
#### **Renamed IFindOptions::SetRange method to IFindOptions::SetIRange**
#### **Renamed ILoadOptions::SetLoadDataOptions method to ILoadOptions::SetILoadDataOptions**
#### **Renamed IWorkbook::SetSettings method to IWorkbook::SetISettings**
#### **Renamed IWorkbook::SetDefaultStyle method to IWorkbook::SetDefaultIStyle**
