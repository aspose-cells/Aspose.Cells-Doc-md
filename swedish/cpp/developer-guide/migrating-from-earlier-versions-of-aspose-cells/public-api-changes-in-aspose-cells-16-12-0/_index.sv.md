---
title: Offentliga API ändringar i Aspose.Cells 16.12.0
type: docs
weight: 10
url: /sv/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar i Aspose.Cells API från version 16.11.0 till 16.12.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för pivot-tabeller**
Den andra versionen av Aspose.Cells for C++ stöder skapande och manipulation av pivot-tabeller. Aspose.Cells for C++ tillhandahåller klassen IPivotTable som representerar ett pivot-tabellobjekt medan IPivotTableCollection representerar en samling pivot-tabeller. IPivotTableCollection kan nås via IWorksheet-objektet och en ny pivot-tabell kan läggas till i samlingen medan man använder IPivotTableCollection.Add-metoden.

Följande kodsnutt demonstrerar hur enkelt det är att använda Aspose.Cells for C++ API för att [skapa pivot-tabeller från grunden](/cells/sv/cpp/create-pivot-table/).

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

Förutom att skapa nya pivot-tabeller, stöder Aspose.Cells for C++-API:erna också att manipulera befintliga pivot-tabeller. API:et stöder för närvarande att ändra data i källområdet för pivot-tabellen och sedan uppdatera den. När pivot-tabellen har manipulerats enligt önskemål, är det bäst att använda IPivotTable.RefreshData och IPivotTable.CalculateData-metoderna för att uppdatera pivot-tabellen mot uppdaterade datakällan.

Följande kodsnutt använder Aspose.Cells for C++-API:et för att [manipulera en befintlig pivot-tabell](/cells/sv/cpp/manipulate-pivot-table/).

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
### **Stöd för villkors- formateringsregler**
Aspose.Cells for C++ tillhandahåller nu möjligheten att lägga till villkorsformateringsregler på arbetsbladet genom att exponera klassen IFormatCondition. Ovan nämnda klass tillhandahåller vidare följande metoder för att [tillämpa villkorsformateringsregler](/cells/sv/cpp/apply-conditional-formatting-in-worksheet/) enligt programvaru kraven.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Följande exempelkod visar hur man lägger till en villkorsformateringsregel av typen Cellvärde på cellerna A1 och B2.

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
### **Stöd för Hyperlänkar**
Aspose.Cells for C++ stödjer nu [att lägga till hyperlänkar till arbetsbladscellerna](/cells/sv/cpp/add-hyperlinks-to-the-cells/). För att tillhandahålla denna funktion har Aspose.Cells for C++ 16.12.0 exponerat klassen IHyperlinkCollection som är åtkomlig via IWorksheet-objektet medan en hyperlänk kan läggas till i samlingen under användning av IHyperlinkCollection.Add-metoden enligt nedan.

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
### **Stöd för dokumentegenskaper**
Excel-programmet stöder 2 typer av dokumentegenskaper enligt nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarens namn, dokumentstatistik osv.
- Användardefinierade (användardefinierade) egenskaper: Användardefinierade egenskaper definieras av slutanvändaren i form av namn-värdepar.

Aspose.Cells for C++ stöder [hantering av både inbyggda och anpassade dokumentegenskaper](/cells/sv/cpp/managing-document-properties/). Aspose.Cells IWorkbook-klassen representerar en Excel-fil. För att få åtkomst till de inbyggda dokumentegenskaperna, använd IWorkbook.GetBuiltInDocumentProperties medan de anpassade dokumentegenskaperna kan nås med hjälp av metoden IWorkbook.GetCustomDocumentProperties.

Följande kodexempel laddar en befintlig exempelkalkyl och läser de inbyggda dokumentegenskaperna som Titel, Ämne och anpassad egenskap med namnet MyCustom1.

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
### **Stöd för ListObjects**
En Excel-tabell är en matris av celler som innehåller ett valfritt antal rader och kolumner, medan samma tabell kallas en List Object i Aspose.Cells for C++-API:er. Namnrymden Aspose::Cells::Tables innehåller alla nödvändiga klasser som hanterar operationer relaterade till List Objects. De mest noterbara klasserna är IListObject och IListObjectCollection som möjliggör [skapande och formatering av List Objects](/cells/sv/cpp/create-and-format-table/) och så vidare.

Följande kodexempel laddar exempelkalkylfilen och skapar sedan en List Object (tabell) i en omfattning A1:H10, och använder sedan olika metoder för att visa delsumman.

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
### **Stöd för gruppering av rader och kolumner**
Aspose.Cells for C++-API:er kan användas för att gruppera rader och kolumner med hjälp av ICells-klassen som i grund och botten är samlingen av alla celler i en given arbetsblad. ICells-klassen erbjuder metoderna GroupRows och GroupColumns för att [gruppera rader och kolumner](/cells/sv/cpp/group-rows-and-columns-of-worksheet/) respektive.

Följande kodsnutt visar det enkla användningsscenario för båda ovan nämnda metoderna.

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
### **Stöd för teman**
Aspose.Cells for C++-API:er stöder nu användning och manipulering av teman som erbjuds av Excel-applikationen.
#### **Möjlighet att tillämpa anpassade temafärger**
Följande kodsnutt försöker [skapa ett nytt tema med anpassade färger](/cells/sv/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) för arbetsboken.

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
#### **Stöd för manipulation av temafärger**
Följande kodexempel visar hur man [läser och ändrar temafärger i arbetsboken](/cells/sv/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Kodexemplet laddar en befintlig kalkyl, läser dess temafärger, dvs Accent1-Accent6, och ändrar färgerna innan kalkylen sparas.

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
#### **Möjlighet att kopiera teman mellan arbetsböcker**
Följande kodexempel visar hur man [kopierar tema från en arbetsbok till en annan](/cells/sv/cpp/copy-theme-from-one-workbook-to-another/), vilket kan vara användbart för att tillämpa inbyggda eller anpassade teman på flera kalkyler.

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
## **Namnändrade API:er**
Med släppet av Aspose.Cells for C++ 16.12.0 har vi namnändrat några metoder för att hålla gränssnitten enhetliga. Listan över alla namnändrade API:er är följande.
#### **Namnändrade ICell::SetStyle-metod till ICell::SetIStyle**
#### **Namnändrade ICell::SetCharacters-metod till ICell::SetIFontSettings**
#### **Namnändrade ICellsColor::SetThemeColor-metod till ICellsColor::SetIThemeColor**
#### **Namnändrade ICells::SetStyle-metod till ICells::SetIStyle**
#### **Namnändrade ICellsHelper::GetDPI_i-metod till ICellsHelper::GetDPI**
#### **Namnändrade ICellsHelper::SetDPI_i-metod till ICellsHelper::SetDPI**
#### **Namnändrade ICellsHelper::GetVersion_i-metod till ICellsHelper::GetVersion**
#### **Namnändrade ICellsHelper::IsProtectedByRMS_i-metod till ICellsHelper::IsProtectedByRMS**
#### **Namnändrade ICellsHelper::IsProtectedByRMS_i-metod till ICellsHelper::IsProtectedByRMS**
#### **Namnändrade ICellsHelper::CellNameToIndex_i-metod till ICellsHelper::CellNameToIndex**
#### **Namnändrade ICellsHelper::CellIndexToName_i-metod till ICellsHelper::CellIndexToName**
#### **Namnändrade ICellsHelper::ColumnIndexToName_i-metod till ICellsHelper::ColumnIndexToName**
#### **Omdöptes ICellsHelper::ColumnNameToIndex_i-metoden till ICellsHelper::ColumnNameToIndex**
#### **Omdöptes ICellsHelper::RowIndexToName_i-metoden till ICellsHelper::RowIndexToName**
#### **Omdöptes ICellsHelper::RowNameToIndex_i-metoden till ICellsHelper::RowNameToIndex**
#### **Omdöptes ICellsHelper::ConvertR1C1FormulaToA1_i-metoden till ICellsHelper::ConvertR1C1FormulaToA1**
#### **Omdöptes ICellsHelper::ConvertA1FormulaToR1C1_i-metoden till ICellsHelper::ConvertA1FormulaToR1C1**
#### **Omdöptes ICellsHelper::GetDateTimeFromDouble_i-metoden till ICellsHelper::GetDateTimeFromDouble**
#### **Omdöptes ICellsHelper::GetDoubleFromDateTime_i-metoden till ICellsHelper::GetDoubleFromDateTime**
#### **Omdöptes ICellsHelper::DetectLoadFormat_i-metoden till ICellsHelper::DetectLoadFormat**
#### **Omdöptes ICellsHelper::DetectFileFormat_i-metoden till ICellsHelper::DetectFileFormat**
#### **Omdöptes ICellsHelper::GetFontDir_i-metoden till ICellsHelper::GetFontDir**
#### **Omdöptes ICellsHelper::SetFontDir_i-metoden till ICellsHelper::SetFontDir**
#### **Omdöptes ICellsHelper::GetFontDirs_i-metoden till ICellsHelper::GetFontDirs**
#### **Omdöptes ICellsHelper::SetFontDirs_i-metoden till ICellsHelper::SetFontDirs**
#### **Omdöptes ICellsHelper::GetFontFiles_i-metoden till ICellsHelper::GetFontFiles**
#### **Omdöptes ICellsHelper::SetFontFiles_i-metoden till ICellsHelper::SetFontFiles**
#### **Omdöptes ICellsHelper::GetStartupPath_i-metoden till ICellsHelper::GetStartupPath**
#### **Omdöptes ICellsHelper::SetStartupPath_i-metoden till ICellsHelper::SetStartupPath**
#### **Omdöptes ICellsHelper::GetAltStartPath_i-metoden till ICellsHelper::GetAltStartPath**
#### **Omdöptes ICellsHelper::SetAltStartPath_i-metoden till ICellsHelper::SetAltStartPath**
#### **Omdöptes ICellsHelper::GetLibraryPath_i-metoden till ICellsHelper::GetLibraryPath**
#### **Omdöptes ICellsHelper::SetLibraryPath_i-metoden till ICellsHelper::SetLibraryPath**
#### **Omdöptes ICellsHelper::GetUsedColors_i-metoden till ICellsHelper::GetUsedColors**
#### **Omdöptes ICellsHelper::AddAddInFunction_i-metoden till ICellsHelper::AddAddInFunction**
#### **Omdöptes ICellsHelper::MergeFiles_i-metoden till ICellsHelper::MergeFiles**
#### **Omdöptes IColumnCollection::GetByIndex_i-metoden till IColumnCollection::GetIColumn**
#### **Omdöptes IFileFormatUtil::DetectFileFormat_i-metoden till IFileFormatUtil::DetectFileFormat**
#### **Omdöptes IFileFormatUtil::ExtensionToSaveFormat_i-metoden till IFileFormatUtil::ExtensionToSaveFormat**
#### **Omdöptes IFileFormatUtil::IsTemplateFormat_i-metoden till IFileFormatUtil::IsTemplateFormat**
#### **Omdöptes IFileFormatUtil::LoadFormatToExtension_i-metoden till IFileFormatUtil::LoadFormatToExtension**
#### **Omdöptes IFileFormatUtil::LoadFormatToSaveFormat_i-metoden till IFileFormatUtil::LoadFormatToSaveFormat**
#### **Bytte namn på metoden IFileFormatUtil::SaveFormatToExtension_i till IFileFormatUtil::SaveFormatToExtension**
#### **Bytte namn på metoden IFileFormatUtil::SaveFormatToLoadFormat_i till IFileFormatUtil::SaveFormatToLoadFormat**
#### **Bytte namn på metoden IRange::SetStyle till IRange::SetIStyle**
#### **Bytte namn på metoden IFindOptions::SetRange till IFindOptions::SetIRange**
#### **Bytte namn på metoden ILoadOptions::SetLoadDataOptions till ILoadOptions::SetILoadDataOptions**
#### **Bytte namn på metoden IWorkbook::SetSettings till IWorkbook::SetISettings**
#### **Bytte namn på metoden IWorkbook::SetDefaultStyle till IWorkbook::SetDefaultIStyle**
