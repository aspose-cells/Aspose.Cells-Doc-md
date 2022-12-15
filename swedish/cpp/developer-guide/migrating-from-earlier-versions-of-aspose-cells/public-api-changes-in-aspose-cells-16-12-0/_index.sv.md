---
title: Offentlig API Ändringar i Aspose.Cells 16.12.0
type: docs
weight: 10
url: /sv/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.11.0 till 16.12.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för pivottabeller**
Den andra versionen av Aspose.Cells for C++ stöder skapande såväl som manipulering av pivottabellerna. Aspose.Cells for C++ tillhandahåller klassen IPivotTable som representerar ett pivottabellobjekt medan IPivotTableCollection representerar en samling pivottabeller. IPivotTableCollection kan nås via IWorksheet-objektet och en ny pivottabell kan läggas till i samlingen när du använder metoden IPivotTableCollection.Add.

 Följande kodavsnitt visar hur enkelt det är att använda Aspose.Cells for C++ API för att[skapa pivottabeller från grunden](/cells/sv/cpp/create-pivot-table/).

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

Förutom att skapa nya pivottabeller stöder Aspose.Cells for C++ API:er även för att manipulera befintliga pivottabeller. API stöder för närvarande att ändra data vid källintervallet för pivottabellen och sedan uppdatera den. När pivottabellen har manipulerats enligt önskemål är det bäst att använda metoderna IPivotTable.RefreshData och IPivotTable.CalculateData för att uppdatera pivottabellen mot den uppdaterade datakällan.

Följande kodavsnitt använder Aspose.Cells for C++ API till[manipulera en befintlig pivottabell](/cells/sv/cpp/manipulate-pivot-table/).

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
### **Stöd för regler för villkorlig formatering**
 Aspose.Cells for C++ ger nu möjligheten att lägga till villkorliga formateringsregler till kalkylbladet genom att exponera klassen IFormatCondition. Ovannämnda klass tillhandahåller vidare följande metoder för att[tillämpa reglerna för villkorlig formatering](/cells/sv/cpp/apply-conditional-formatting-in-worksheet/) enligt applikationskraven.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Följande exempelkod visar hur man lägger till en villkorlig formateringsregel av typen Cell Värde i cellerna A1 och B2.

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
### **Stöd för hyperlänkar**
 Aspose.Cells for C++ stöds nu[lägga till hyperlänkar till kalkylbladets celler](/cells/sv/cpp/add-hyperlinks-to-the-cells/)För att tillhandahålla den här funktionen har Aspose.Cells for C++ 16.12.0 exponerat klassen IHyperlinkCollection som är tillgänglig via IWorksheet-objektet medan en hyperlänk kan läggas till i samlingen med IHyperlinkCollection.Add-metoden som visas nedan.

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
### **Stöd för dokumentegenskaper**
Excel-applikationen stöder 2 typer av dokumentegenskaper enligt listan nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarens namn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper definierade av slutanvändaren i form av namnvärdepar.

 Aspose.Cells for C++ stöder[hantera båda typerna av dokumentegenskaper, inbyggda och anpassade](/cells/sv/cpp/managing-document-properties/)Aspose.Cells' IWorkbook-klassen representerar en Excel-fil. För att komma åt de inbyggda dokumentegenskaperna, använd IWorkbook.GetBuiltInDocumentProperties medan de anpassade dokumentegenskaperna kan nås när du använder metoden IWorkbook.GetCustomDocumentProperties.

Följande exempelkod läser in ett befintligt exempelkalkylblad och läser de inbyggda dokumentegenskaperna som Titel, Ämne och anpassad egenskap med namnet MyCustom1.

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
### **Stöd för ListObjects**
 En Excel-tabell är en matris av celler som innehåller valfritt antal rader och kolumner medan samma tabell hänvisas till som ett listobjekt i Aspose.Cells for C++ API:er. Namnutrymmet Aspose::Cells::Tables innehåller alla nödvändiga klasser som hanterar operationerna relaterade till listobjekten. Mest värda att nämna klasser är IListObject och IListObjectCollection som tillåter det[skapa och formatera listobjekt](/cells/sv/cpp/create-and-format-table/) och så vidare.

Följande exempelkod läser in exempelkalkylarksfilen och skapar sedan ett listobjekt (tabell) i intervallet A1:H10, och använd sedan dess olika metoder för att visa delsumman.

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
### **Stöd för rad- och kolumngruppering**
 Aspose.Cells for C++ API kan användas för att gruppera rader och kolumner samtidigt som klassen ICells används som i princip är samlingen av alla celler i ett givet kalkylblad. Klassen ICells erbjuder metoderna GroupRows och GroupColumns för att[gruppera rader och kolumner](/cells/sv/cpp/group-rows-and-columns-of-worksheet/) respektive.

Följande kodavsnitt visar det enkla användningsscenariot för båda ovannämnda metoder.

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
### **Stöd för teman**
Aspose.Cells for C++ API:er stödjer nu att använda och manipulera teman som erbjuds av Excel-applikationen.
#### **Möjlighet att applicera de anpassade temafärgerna**
 Följande utdrag försöker[skapa ett nytt tema med anpassade färger](/cells/sv/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) för arbetsboken.

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
#### **Stöd för manipulering av temafärger**
 Följande exempelkod visar hur man gör[läsa och ändra temafärgerna i arbetsboken](/cells/sv/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Exempelkoden laddar ett befintligt kalkylblad, läser dess temafärger, dvs. Accent1-Accent6, och ändrar färgerna innan kalkylarket sparas.

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
#### **Möjlighet att kopiera teman över arbetsböcker**
 Följande exempelkod visar hur man gör[kopiera tema från en arbetsbok till en annan](/cells/sv/cpp/copy-theme-from-one-workbook-to-another/), vilket kan vara användbart för att tillämpa inbyggda eller anpassade teman på flera kalkylblad.

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
## **Omdöpta API:er**
Med lanseringen av Aspose.Cells for C++ 16.12.0 har vi bytt namn på några metoder för att hålla gränssnitten enhetliga. Listan över alla omdöpta API:er är följande.
#### **Döpte om ICell::SetStyle-metoden till ICell::SetIStyle**
#### **Döpte om ICell::SetCharacters-metoden till ICell::SetIFontSettings**
#### **Omdöpt ICellsColor::SetThemeColor-metoden till ICellsColor::SetIThemeColor**
#### **Omdöpt ICells::SetStyle-metoden till ICells::SetIStyle**
#### **Döpte om ICellsHelper::GetDPI_i-metoden till ICellsHelper::GetDPI**
#### **Döpte om ICellsHelper::SetDPI_i-metoden till ICellsHelper::SetDPI**
#### **Döpte om ICellsHelper::GetVersion_i-metoden till ICellsHelper::GetVersion**
#### **Döpte om ICellsHelper::IsProtectedByRMS_i-metoden till ICellsHelper::IsProtectedByRMS**
#### **Döpte om ICellsHelper::IsProtectedByRMS_i-metoden till ICellsHelper::IsProtectedByRMS**
#### **Döpte om ICellsHelper::CellNameToIndex_i-metoden till ICellsHelper::CellNameToIndex**
#### **Döpte om ICellsHelper::CellIndexToName_i-metoden till ICellsHelper::CellIndexToName**
#### **Döpte om ICellsHelper::ColumnIndexToName_i-metoden till ICellsHelper::ColumnIndexToName**
#### **Döpte om ICellsHelper::ColumnNameToIndex_i-metoden till ICellsHelper::ColumnNameToIndex**
#### **Döpte om ICellsHelper::RowIndexToName_i-metoden till ICellsHelper::RowIndexToName**
#### **Döpte om ICellsHelper::RowNameToIndex_i-metoden till ICellsHelper::RowNameToIndex**
#### **Döpte om ICellsHelper::ConvertR1C1FormulaToA1_i-metoden till ICellsHelper::ConvertR1C1FormulaToA1**
#### **Döpte om ICellsHelper::ConvertA1FormulaToR1C1_i-metoden till ICellsHelper::ConvertA1FormulaToR1C1**
#### **Döpte om ICellsHelper::GetDateTimeFromDouble_i-metoden till ICellsHelper::GetDateTimeFromDouble**
#### **Döpte om ICellsHelper::GetDoubleFromDateTime_i-metoden till ICellsHelper::GetDoubleFromDateTime**
#### **Döpte om ICellsHelper::DetectLoadFormat_i-metoden till ICellsHelper::DetectLoadFormat**
#### **Döpte om ICellsHelper::DetectFileFormat_i-metoden till ICellsHelper::DetectFileFormat**
#### **Döpte om ICellsHelper::GetFontDir_i-metoden till ICellsHelper::GetFontDir**
#### **Döpte om ICellsHelper::SetFontDir_i-metoden till ICellsHelper::SetFontDir**
#### **Döpte om ICellsHelper::GetFontDirs_i-metoden till ICellsHelper::GetFontDirs**
#### **Döpte om ICellsHelper::SetFontDirs_i-metoden till ICellsHelper::SetFontDirs**
#### **Döpte om ICellsHelper::GetFontFiles_i-metoden till ICellsHelper::GetFontFiles**
#### **Döpte om ICellsHelper::SetFontFiles_i-metoden till ICellsHelper::SetFontFiles**
#### **Döpte om ICellsHelper::GetStartupPath_i-metoden till ICellsHelper::GetStartupPath**
#### **Döpte om ICellsHelper::SetStartupPath_i-metoden till ICellsHelper::SetStartupPath**
#### **Döpte om ICellsHelper::GetAltStartPath_i-metoden till ICellsHelper::GetAltStartPath**
#### **Döpte om ICellsHelper::SetAltStartPath_i-metoden till ICellsHelper::SetAltStartPath**
#### **Döpte om ICellsHelper::GetLibraryPath_i-metoden till ICellsHelper::GetLibraryPath**
#### **Döpte om ICellsHelper::SetLibraryPath_i-metoden till ICellsHelper::SetLibraryPath**
#### **Döpte om ICellsHelper::GetUsedColors_i-metoden till ICellsHelper::GetUsedColors**
#### **Omdöpt ICellsHelper::AddAddInFunction_i-metoden till ICellsHelper::AddAddInFunction**
#### **Döpte om ICellsHelper::MergeFiles_i-metoden till ICellsHelper::MergeFiles**
#### **Omdöpt IColumnCollection::GetByIndex_i-metoden till IColumnCollection::GetIColumn**
#### **Döpte om metoden IFileFormatUtil::DetectFileFormat_i till IFileFormatUtil::DetectFileFormat**
#### **Döpte om metoden IFileFormatUtil::ExtensionToSaveFormat_i till IFileFormatUtil::ExtensionToSaveFormat**
#### **Döpte om metoden IFileFormatUtil::IsTemplateFormat_i till IFileFormatUtil::IsTemplateFormat**
#### **Döpte om metoden IFileFormatUtil::LoadFormatToExtension_i till IFileFormatUtil::LoadFormatToExtension**
#### **Döpte om metoden IFileFormatUtil::LoadFormatToSaveFormat_i till IFileFormatUtil::LoadFormatToSaveFormat**
#### **Döpte om metoden IFileFormatUtil::SaveFormatToExtension_i till IFileFormatUtil::SaveFormatToExtension**
#### **Döpte om metoden IFileFormatUtil::SaveFormatToLoadFormat_i till IFileFormatUtil::SaveFormatToLoadFormat**
#### **Döpte om IRange::SetStyle-metoden till IRange::SetIStyle**
#### **Döpte om IFindOptions::SetRange-metoden till IFindOptions::SetIRange**
#### **Omdöpt ILoadOptions::SetLoadDataOptions-metoden till ILoadOptions::SetILoadDataOptions**
#### **Döpte om IWorkbook::SetSettings-metoden till IWorkbook::SetISettings**
#### **Döpte om IWorkbook::SetDefaultStyle-metoden till IWorkbook::SetDefaultIStyle**
