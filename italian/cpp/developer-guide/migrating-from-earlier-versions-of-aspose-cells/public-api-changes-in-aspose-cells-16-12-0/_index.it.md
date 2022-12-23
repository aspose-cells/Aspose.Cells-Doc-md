---
title: Pubblico API Modifiche Aspose.Cells 16.12.0
type: docs
weight: 10
url: /it/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 16.11.0 alla 16.12.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per tabelle pivot**
La seconda versione di Aspose.Cells for C++ supporta la creazione e la manipolazione delle tabelle pivot. Aspose.Cells for C++ fornisce la classe IPivotTable che rappresenta un oggetto tabella pivot mentre IPivotTableCollection rappresenta una raccolta di tabelle pivot. È possibile accedere a IPivotTableCollection tramite l'oggetto IWorksheet e aggiungere una nuova tabella pivot alla raccolta durante l'utilizzo del metodo IPivotTableCollection.Add.

 Il seguente frammento di codice dimostra quanto sia semplice utilizzare Aspose.Cells for C++ API per[creare tabelle pivot da zero](/cells/it/cpp/create-pivot-table/).

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

Oltre a creare nuove tabelle pivot, le API Aspose.Cells for C++ supportano anche la manipolazione delle tabelle pivot esistenti. Lo API attualmente supporta la modifica dei dati nell'intervallo di origine della tabella pivot e quindi l'aggiornamento. Una volta che la tabella pivot è stata manipolata come desiderato, è consigliabile utilizzare i metodi IPivotTable.RefreshData e IPivotTable.CalculateData per aggiornare la tabella pivot rispetto all'origine dati aggiornata.

Il seguente frammento di codice utilizza Aspose.Cells for C++ API per[manipolare una tabella pivot esistente](/cells/it/cpp/manipulate-pivot-table/).

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
### **Supporto per le regole di formattazione condizionale**
 Aspose.Cells for C++ offre ora la possibilità di aggiungere regole di formattazione condizionale al foglio di lavoro esponendo la classe IFormatCondition. La suddetta classe fornisce inoltre i seguenti metodi per[applicare le regole di formattazione condizionale](/cells/it/cpp/apply-conditional-formatting-in-worksheet/) secondo i requisiti dell'applicazione.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Il codice di esempio seguente mostra come aggiungere una regola di formattazione condizionale di tipo Valore Cell nelle celle A1 e B2.

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
### **Supporto per collegamenti ipertestuali**
 Aspose.Cells for C++ ora supporta[aggiungendo collegamenti ipertestuali alle celle del foglio di lavoro](/cells/it/cpp/add-hyperlinks-to-the-cells/)Per fornire questa funzionalità, Aspose.Cells for C++ 16.12.0 ha esposto la classe IHyperlinkCollection che è accessibile tramite l'oggetto IWorksheet mentre un collegamento ipertestuale può essere aggiunto alla raccolta utilizzando il metodo IHyperlinkCollection.Add come illustrato di seguito.

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
### **Supporto per le proprietà del documento**
L'applicazione Excel supporta 2 tipi di proprietà del documento come elencato di seguito.

- Proprietà (integrate) definite dal sistema: le proprietà integrate contengono informazioni generali sul documento come titolo del documento, nome dell'autore, statistiche del documento e così via.
- Proprietà (personalizzate) definite dall'utente: proprietà personalizzate definite dall'utente finale sotto forma di coppia nome valore.

 Aspose.Cells for C++ supporti[gestendo entrambi i tipi di proprietà del documento, integrate e personalizzate](/cells/it/cpp/managing-document-properties/)Aspose.Cells' La classe IWorkbook rappresenta un file Excel. Per accedere alle proprietà predefinite del documento, utilizzare IWorkbook.GetBuiltInDocumentProperties mentre è possibile accedere alle proprietà personalizzate del documento utilizzando il metodo IWorkbook.GetCustomDocumentProperties.

Il seguente codice di esempio carica un foglio di calcolo di esempio esistente e legge le proprietà predefinite del documento, ad esempio Titolo, Oggetto e proprietà personalizzata con il nome MyCustom1.

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
### **Supporto per ListObject**
 Una tabella di Excel è una matrice di celle contenente un numero qualsiasi di righe e colonne, mentre la stessa tabella viene definita oggetto elenco nelle API Aspose.Cells for C++. Il namespace Aspose::Cells::Tables contiene tutte le classi necessarie che si occupano delle operazioni relative agli oggetti List. Le classi più degne di nota sono IListObject e IListObjectCollection che lo consentono[creare e formattare List Objects](/cells/it/cpp/create-and-format-table/) e così via.

Il seguente codice di esempio carica il file del foglio di calcolo di esempio e quindi crea un oggetto elenco (tabella) in un intervallo A1:H10, quindi utilizza i suoi vari metodi per mostrare il totale parziale.

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
### **Supporto per il raggruppamento di righe e colonne**
 Aspose.Cells for C++ API può essere utilizzato per raggruppare righe e colonne mentre si utilizza la classe ICells che è fondamentalmente la raccolta di tutte le celle in un determinato foglio di lavoro. La classe ICells offre i metodi GroupRows e GroupColumns per[raggruppare righe e colonne](/cells/it/cpp/group-rows-and-columns-of-worksheet/) rispettivamente.

Il frammento di codice seguente illustra il semplice scenario di utilizzo di entrambi i metodi sopra menzionati.

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
### **Supporto per i temi**
Aspose.Cells for C++ Le API ora supportano l'utilizzo e la manipolazione dei temi offerti dall'applicazione Excel.
#### **Possibilità di applicare i colori del tema personalizzato**
 Il seguente frammento tenta di[creare un nuovo tema con colori personalizzati](/cells/it/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) per la cartella di lavoro.

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
#### **Supporto per la manipolazione dei colori del tema**
 Il codice di esempio seguente mostra come[leggere e modificare i colori del tema della cartella di lavoro](/cells/it/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Il codice di esempio carica un foglio di calcolo esistente, ne legge i colori del tema, ad esempio Accent1-Accent6, e modifica i colori prima di salvare il foglio di calcolo.

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
#### **Possibilità di copiare temi tra cartelle di lavoro**
 Il codice di esempio seguente mostra come[copiare il tema da una cartella di lavoro a un'altra](/cells/it/cpp/copy-theme-from-one-workbook-to-another/), che potrebbe essere utile per applicare temi incorporati o personalizzati su più fogli di lavoro.

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
## **API rinominate**
Con il rilascio di Aspose.Cells for C++ 16.12.0, abbiamo rinominato alcuni metodi per mantenere unificate le interfacce. L'elenco di tutte le API rinominate è il seguente.
#### **Metodo ICell::SetStyle rinominato in ICell::SetIStyle**
#### **Metodo ICell::SetCharacters rinominato in ICell::SetIFontSettings**
#### **Metodo ICellsColor::SetThemeColor rinominato in ICellsColor::SetIThemeColor**
#### **Metodo ICells::SetStyle rinominato in ICells::SetIStyle**
#### **Metodo ICellsHelper::GetDPI_i rinominato in ICellsHelper::GetDPI**
#### **Metodo ICellsHelper::SetDPI_i rinominato in ICellsHelper::SetDPI**
#### **Metodo ICellsHelper::GetVersion_i rinominato in ICellsHelper::GetVersion**
#### **Metodo ICellsHelper::IsProtectedByRMS_i rinominato in ICellsHelper::IsProtectedByRMS**
#### **Metodo ICellsHelper::IsProtectedByRMS_i rinominato in ICellsHelper::IsProtectedByRMS**
#### **Metodo ICellsHelper::CellNameToIndex_i rinominato in ICellsHelper::CellNameToIndex**
#### **Metodo ICellsHelper::CellIndexToName_i rinominato in ICellsHelper::CellIndexToName**
#### **Metodo ICellsHelper::ColumnIndexToName_i rinominato in ICellsHelper::ColumnIndexToName**
#### **Metodo ICellsHelper::ColumnNameToIndex_i rinominato in ICellsHelper::ColumnNameToIndex**
#### **Metodo ICellsHelper::RowIndexToName_i rinominato in ICellsHelper::RowIndexToName**
#### **Metodo ICellsHelper::RowNameToIndex_i rinominato in ICellsHelper::RowNameToIndex**
#### **Metodo ICellsHelper::ConvertR1C1FormulaToA1_i rinominato in ICellsHelper::ConvertR1C1FormulaToA1**
#### **Metodo ICellsHelper::ConvertA1FormulaToR1C1_i rinominato in ICellsHelper::ConvertA1FormulaToR1C1**
#### **Metodo ICellsHelper::GetDateTimeFromDouble_i rinominato in ICellsHelper::GetDateTimeFromDouble**
#### **Metodo ICellsHelper::GetDoubleFromDateTime_i rinominato in ICellsHelper::GetDoubleFromDateTime**
#### **Metodo ICellsHelper::DetectLoadFormat_i rinominato in ICellsHelper::DetectLoadFormat**
#### **Metodo ICellsHelper::DetectFileFormat_i rinominato in ICellsHelper::DetectFileFormat**
#### **Metodo ICellsHelper::GetFontDir_i rinominato in ICellsHelper::GetFontDir**
#### **Metodo ICellsHelper::SetFontDir_i rinominato in ICellsHelper::SetFontDir**
#### **Metodo ICellsHelper::GetFontDirs_i rinominato in ICellsHelper::GetFontDirs**
#### **Metodo ICellsHelper::SetFontDirs_i rinominato in ICellsHelper::SetFontDirs**
#### **Metodo ICellsHelper::GetFontFiles_i rinominato in ICellsHelper::GetFontFiles**
#### **Metodo ICellsHelper::SetFontFiles_i rinominato in ICellsHelper::SetFontFiles**
#### **Metodo ICellsHelper::GetStartupPath_i rinominato in ICellsHelper::GetStartupPath**
#### **Metodo ICellsHelper::SetStartupPath_i rinominato in ICellsHelper::SetStartupPath**
#### **Metodo ICellsHelper::GetAltStartPath_i rinominato in ICellsHelper::GetAltStartPath**
#### **Metodo ICellsHelper::SetAltStartPath_i rinominato in ICellsHelper::SetAltStartPath**
#### **Metodo ICellsHelper::GetLibraryPath_i rinominato in ICellsHelper::GetLibraryPath**
#### **Metodo ICellsHelper::SetLibraryPath_i rinominato in ICellsHelper::SetLibraryPath**
#### **Metodo ICellsHelper::GetUsedColors_i rinominato in ICellsHelper::GetUsedColors**
#### **Metodo ICellsHelper::AddAddInFunction_i rinominato in ICellsHelper::AddAddInFunction**
#### **Metodo ICellsHelper::MergeFiles_i rinominato in ICellsHelper::MergeFiles**
#### **Metodo IColumnCollection::GetByIndex_i rinominato in IColumnCollection::GetIColumn**
#### **Metodo IFileFormatUtil::DetectFileFormat_i rinominato in IFileFormatUtil::DetectFileFormat**
#### **Metodo IFileFormatUtil::ExtensionToSaveFormat_i rinominato in IFileFormatUtil::ExtensionToSaveFormat**
#### **Metodo IFileFormatUtil::IsTemplateFormat_i rinominato in IFileFormatUtil::IsTemplateFormat**
#### **Metodo IFileFormatUtil::LoadFormatToExtension_i rinominato in IFileFormatUtil::LoadFormatToExtension**
#### **Metodo IFileFormatUtil::LoadFormatToSaveFormat_i rinominato in IFileFormatUtil::LoadFormatToSaveFormat**
#### **Metodo IFileFormatUtil::SaveFormatToExtension_i rinominato in IFileFormatUtil::SaveFormatToExtension**
#### **Metodo IFileFormatUtil::SaveFormatToLoadFormat_i rinominato in IFileFormatUtil::SaveFormatToLoadFormat**
#### **Metodo IRange::SetStyle rinominato in IRange::SetIStyle**
#### **Metodo IFindOptions::SetRange rinominato in IFindOptions::SetIRange**
#### **Metodo ILoadOptions::SetLoadDataOptions rinominato in ILoadOptions::SetILoadDataOptions**
#### **Metodo IWorkbook::SetSettings rinominato in IWorkbook::SetISettings**
#### **Metodo IWorkbook::SetDefaultStyle rinominato in IWorkbook::SetDefaultIStyle**
