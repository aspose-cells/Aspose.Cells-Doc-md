---
title: Öffentlich API Änderungen in Aspose.Cells 16.12.0
type: docs
weight: 10
url: /de/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 16.11.0 zu 16.12.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Pivot-Tabellen**
Die zweite Version von Aspose.Cells for C++ unterstützt sowohl die Erstellung als auch die Manipulation der Pivot-Tabellen. Aspose.Cells for C++ stellt die IPivotTable-Klasse bereit, die ein Pivot-Tabellenobjekt darstellt, während IPivotTableCollection eine Sammlung von Pivot-Tabellen darstellt. Auf die IPivotTableCollection kann über das IWorksheet-Objekt zugegriffen werden, und eine neue Pivot-Tabelle kann der Sammlung hinzugefügt werden, während die IPivotTableCollection.Add-Methode verwendet wird.

 Das folgende Code-Snippet zeigt, wie einfach es ist, Aspose.Cells for C++ API zu verwenden[Erstellen Sie Pivot-Tabellen von Grund auf neu](/cells/de/cpp/create-pivot-table/).

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

Neben der Erstellung neuer Pivot-Tabellen unterstützen Aspose.Cells for C++-APIs auch die Bearbeitung vorhandener Pivot-Tabellen. API unterstützt derzeit das Ändern der Daten im Quellbereich der Pivot-Tabelle und das anschließende Aktualisieren. Nachdem die Pivot-Tabelle wie gewünscht bearbeitet wurde, empfiehlt es sich, die Methoden IPivotTable.RefreshData und IPivotTable.CalculateData zu verwenden, um die Pivot-Tabelle anhand der aktualisierten Datenquelle zu aktualisieren.

Das folgende Code-Snippet verwendet die Aspose.Cells for C++ API zu[Bearbeiten einer vorhandenen Pivot-Tabelle](/cells/de/cpp/manipulate-pivot-table/).

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
### **Unterstützung für bedingte Formatierungsregeln**
 Aspose.Cells for C++ bietet jetzt die Möglichkeit, dem Arbeitsblatt bedingte Formatierungsregeln hinzuzufügen, indem die IFormatCondition-Klasse verfügbar gemacht wird. Die zuvor erwähnte Klasse stellt ferner die folgenden Verfahren bereit[Wenden Sie die Regeln für die bedingte Formatierung an](/cells/de/cpp/apply-conditional-formatting-in-worksheet/) gemäß Bewerbungsanforderungen.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Der folgende Beispielcode zeigt, wie eine bedingte Formatierungsregel des Typs Cell Wert zu den Zellen A1 und B2 hinzugefügt wird.

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
### **Unterstützung für Hyperlinks**
 Aspose.Cells for C++ unterstützt jetzt[Hinzufügen von Hyperlinks zu den Arbeitsblattzellen](/cells/de/cpp/add-hyperlinks-to-the-cells/)Um diese Funktion bereitzustellen, hat Aspose.Cells for C++ 16.12.0 die IHyperlinkCollection-Klasse verfügbar gemacht, auf die über das IWorksheet-Objekt zugegriffen werden kann, während ein Hyperlink zur Sammlung hinzugefügt werden kann, während die IHyperlinkCollection.Add-Methode wie unten gezeigt verwendet wird.

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
### **Unterstützung für Dokumenteigenschaften**
Die Excel-Anwendung unterstützt 2 Arten von Dokumenteigenschaften, wie unten aufgeführt.

- Systemdefinierte (eingebaute) Eigenschaften: Eingebaute Eigenschaften enthalten allgemeine Informationen über das Dokument wie Dokumenttitel, Autorname, Dokumentstatistiken und so weiter.
- Benutzerdefinierte (benutzerdefinierte) Eigenschaften: Benutzerdefinierte Eigenschaften, die vom Endbenutzer in Form von Name-Wert-Paaren definiert werden.

 Aspose.Cells for C++ unterstützt[Verwalten beider Arten von Dokumenteigenschaften, integriert und benutzerdefiniert](/cells/de/cpp/managing-document-properties/)Aspose.Cells' Die IWorkbook-Klasse repräsentiert eine Excel-Datei. Um auf die integrierten Dokumenteigenschaften zuzugreifen, verwenden Sie IWorkbook.GetBuiltInDocumentProperties, während auf die benutzerdefinierten Dokumenteigenschaften mit der IWorkbook.GetCustomDocumentProperties-Methode zugegriffen werden kann.

Der folgende Beispielcode lädt eine vorhandene Beispieltabelle und liest die integrierten Dokumenteigenschaften wie Titel, Betreff und benutzerdefinierte Eigenschaft mit dem Namen MyCustom1.

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
### **Unterstützung für ListObjects**
 Eine Excel-Tabelle ist eine Matrix aus Zellen, die eine beliebige Anzahl von Zeilen und Spalten enthält, während dieselbe Tabelle in Aspose.Cells for C++-APIs als Listenobjekt bezeichnet wird. Der Namespace Aspose::Cells::Tables enthält alle notwendigen Klassen, die sich mit den Operationen im Zusammenhang mit den Listenobjekten befassen. Die erwähnenswertesten Klassen sind IListObject und IListObjectCollection, die dies ermöglichen[Listenobjekte erstellen und formatieren](/cells/de/cpp/create-and-format-table/) usw.

Der folgende Beispielcode lädt die Beispieltabellendatei und erstellt dann ein Listenobjekt (Tabelle) in einem Bereich A1:H10 und verwendet dann seine verschiedenen Methoden, um die Zwischensumme anzuzeigen.

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
### **Unterstützung für Zeilen- und Spaltengruppierung**
 Aspose.Cells for C++ API kann verwendet werden, um Zeilen und Spalten zu gruppieren, während die ICells-Klasse verwendet wird, die im Grunde die Sammlung aller Zellen in einem bestimmten Arbeitsblatt ist. Die Klasse ICells bietet dazu die Methoden GroupRows und GroupColumns an[Zeilen und Spalten gruppieren](/cells/de/cpp/group-rows-and-columns-of-worksheet/) beziehungsweise.

Das folgende Code-Snippet demonstriert das einfache Verwendungsszenario der beiden oben genannten Methoden.

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
### **Unterstützung für Themen**
Aspose.Cells for C++ APIs unterstützen jetzt die Verwendung und Bearbeitung der von der Excel-Anwendung angebotenen Themen.
#### **Möglichkeit, die benutzerdefinierten Designfarben anzuwenden**
 Das folgende Snippet versucht es[Erstellen Sie ein neues Design mit benutzerdefinierten Farben](/cells/de/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) für das Arbeitsheft.

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
#### **Unterstützung für die Manipulation von Themenfarben**
 Der folgende Beispielcode zeigt, wie es geht[Designfarben der Arbeitsmappe lesen und ändern](/cells/de/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Der Beispielcode lädt ein vorhandenes Arbeitsblatt, liest seine Designfarben, dh Accent1-Accent6, und ändert die Farben, bevor das Arbeitsblatt gespeichert wird.

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
#### **Möglichkeit, Designs über Arbeitsmappen hinweg zu kopieren**
 Der folgende Beispielcode zeigt, wie es geht[Thema von einer Arbeitsmappe in eine andere kopieren](/cells/de/cpp/copy-theme-from-one-workbook-to-another/), was beim Anwenden integrierter oder benutzerdefinierter Designs auf mehrere Tabellenkalkulationen nützlich sein kann.

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
## **Umbenannte APIs**
Mit der Veröffentlichung von Aspose.Cells for C++ 16.12.0 haben wir einige Methoden umbenannt, um die Schnittstellen einheitlich zu halten. Die Liste aller umbenannten APIs ist wie folgt.
#### **ICell::SetStyle-Methode in ICell::SetIStyle umbenannt**
#### **ICell::SetCharacters-Methode in ICell::SetIFontSettings umbenannt**
#### **ICellsColor::SetThemeColor-Methode in ICellsColor::SetITemeColor umbenannt**
#### **ICells::SetStyle-Methode in ICells::SetIStyle umbenannt**
#### **ICellsHelper::GetDPI_i-Methode in ICellsHelper::GetDPI umbenannt**
#### **ICellsHelper::SetDPI_i-Methode in ICellsHelper::SetDPI umbenannt**
#### **ICellsHelper::GetVersion_i-Methode in ICellsHelper::GetVersion umbenannt**
#### **ICellsHelper::IsProtectedByRMS_i-Methode in ICellsHelper::IsProtectedByRMS umbenannt**
#### **ICellsHelper::IsProtectedByRMS_i-Methode in ICellsHelper::IsProtectedByRMS umbenannt**
#### **Methode ICellsHelper::CellNameToIndex_i in ICellsHelper::CellNameToIndex umbenannt**
#### **Methode ICellsHelper::CellIndexToName_i in ICellsHelper::CellIndexToName umbenannt**
#### **Methode ICellsHelper::ColumnIndexToName_i in ICellsHelper::ColumnIndexToName umbenannt**
#### **Methode ICellsHelper::ColumnNameToIndex_i in ICellsHelper::ColumnNameToIndex umbenannt**
#### **Methode ICellsHelper::RowIndexToName_i in ICellsHelper::RowIndexToName umbenannt**
#### **Methode ICellsHelper::RowNameToIndex_i in ICellsHelper::RowNameToIndex umbenannt**
#### **ICellsHelper::ConvertR1C1FormulaToA1_i-Methode in ICellsHelper::ConvertR1C1FormulaToA1 umbenannt**
#### **ICellsHelper::ConvertA1FormulaToR1C1_i-Methode in ICellsHelper::ConvertA1FormulaToR1C1 umbenannt**
#### **ICellsHelper::GetDateTimeFromDouble_i-Methode in ICellsHelper::GetDateTimeFromDouble umbenannt**
#### **ICellsHelper::GetDoubleFromDateTime_i-Methode in ICellsHelper::GetDoubleFromDateTime umbenannt**
#### **ICellsHelper::DetectLoadFormat_i-Methode in ICellsHelper::DetectLoadFormat umbenannt**
#### **ICellsHelper::DetectFileFormat_i-Methode in ICellsHelper::DetectFileFormat umbenannt**
#### **ICellsHelper::GetFontDir_i-Methode in ICellsHelper::GetFontDir umbenannt**
#### **ICellsHelper::SetFontDir_i-Methode in ICellsHelper::SetFontDir umbenannt**
#### **ICellsHelper::GetFontDirs_i-Methode in ICellsHelper::GetFontDirs umbenannt**
#### **ICellsHelper::SetFontDirs_i-Methode in ICellsHelper::SetFontDirs umbenannt**
#### **ICellsHelper::GetFontFiles_i-Methode in ICellsHelper::GetFontFiles umbenannt**
#### **Methode ICellsHelper::SetFontFiles_i in ICellsHelper::SetFontFiles umbenannt**
#### **ICellsHelper::GetStartupPath_i-Methode in ICellsHelper::GetStartupPath umbenannt**
#### **Methode ICellsHelper::SetStartupPath_i in ICellsHelper::SetStartupPath umbenannt**
#### **ICellsHelper::GetAltStartPath_i-Methode in ICellsHelper::GetAltStartPath umbenannt**
#### **ICellsHelper::SetAltStartPath_i-Methode in ICellsHelper::SetAltStartPath umbenannt**
#### **ICellsHelper::GetLibraryPath_i-Methode in ICellsHelper::GetLibraryPath umbenannt**
#### **ICellsHelper::SetLibraryPath_i-Methode in ICellsHelper::SetLibraryPath umbenannt**
#### **ICellsHelper::GetUsedColors_i-Methode in ICellsHelper::GetUsedColors umbenannt**
#### **ICellsHelper::AddAddInFunction_i-Methode in ICellsHelper::AddAddInFunction umbenannt**
#### **Methode ICellsHelper::MergeFiles_i in ICellsHelper::MergeFiles umbenannt**
#### **Methode IColumnCollection::GetByIndex_i in IColumnCollection::GetIColumn umbenannt**
#### **Die Methode IFileFormatUtil::DetectFileFormat_i wurde in IFileFormatUtil::DetectFileFormat umbenannt**
#### **Methode IFileFormatUtil::ExtensionToSaveFormat_i in IFileFormatUtil::ExtensionToSaveFormat umbenannt**
#### **Methode IFileFormatUtil::IsTemplateFormat_i in IFileFormatUtil::IsTemplateFormat umbenannt**
#### **Methode IFileFormatUtil::LoadFormatToExtension_i in IFileFormatUtil::LoadFormatToExtension umbenannt**
#### **Methode IFileFormatUtil::LoadFormatToSaveFormat_i in IFileFormatUtil::LoadFormatToSaveFormat umbenannt**
#### **Methode IFileFormatUtil::SaveFormatToExtension_i in IFileFormatUtil::SaveFormatToExtension umbenannt**
#### **Methode IFileFormatUtil::SaveFormatToLoadFormat_i in IFileFormatUtil::SaveFormatToLoadFormat umbenannt**
#### **IRange::SetStyle-Methode in IRange::SetIStyle umbenannt**
#### **Umbenannte IFindOptions::SetRange-Methode in IFindOptions::SetIRange**
#### **Umbenannte ILoadOptions::SetLoadDataOptions-Methode in ILoadOptions::SetILoadDataOptions**
#### **Umbenannte IWorkbook::SetSettings-Methode in IWorkbook::SetISettings**
#### **Umbenannte IWorkbook::SetDefaultStyle-Methode in IWorkbook::SetDefaultIStyle**
