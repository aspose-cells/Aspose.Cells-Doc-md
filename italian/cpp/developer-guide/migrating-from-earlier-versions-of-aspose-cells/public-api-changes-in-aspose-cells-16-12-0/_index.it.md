---
title: Cambiamenti dell API pubblica in Aspose.Cells 16.12.0
type: docs
weight: 10
url: /it/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 16.11.0 alla 16.12.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per le Tabelle Pivot**
La seconda versione di Aspose.Cells for C++ supporta la creazione e la manipolazione delle tabelle pivot. Aspose.Cells for C++ fornisce la classe IPivotTable che rappresenta un oggetto Tabella Pivot mentre IPivotTableCollection rappresenta una raccolta di Tabelle Pivot. L'IPivotTableCollection può essere accesso tramite l'oggetto IWorksheet e una nuova Tabella Pivot può essere aggiunta alla raccolta utilizzando il metodo IPivotTableCollection.Add.

Il seguente frammento di codice dimostra quanto sia semplice utilizzare l'API Aspose.Cells for C++ per [creare Tabelle Pivot da zero](/cells/it/cpp/create-pivot-table/).

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

Oltre a creare nuove tabelle pivot, le API Aspose.Cells for C++ supportano anche la manipolazione delle tabelle pivot esistenti. Attualmente l'API supporta la modifica dei dati nell'intervallo di origine della tabella pivot e quindi l'aggiornamento. Una volta che la tabella pivot è stata manipolata come desiderato, è meglio utilizzare i metodi IPivotTable.RefreshData e IPivotTable.CalculateData per aggiornare la tabella pivot rispetto alla fonte dati aggiornata.

Il seguente frammento di codice utilizza l'API Aspose.Cells for C++ per [manipolare una tabella pivot esistente](/cells/it/cpp/manipulate-pivot-table/).

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
### **Supporto per le regole di formattazione condizionale**
Aspose.Cells for C++ ora fornisce la possibilità di aggiungere regole di formattazione condizionale al foglio di lavoro esponendo la classe IFormatCondition. La suddetta classe fornisce inoltre i seguenti metodi per [applicare le regole di formattazione condizionale](/cells/it/cpp/apply-conditional-formatting-in-worksheet/) in base alle esigenze dell'applicazione.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Il seguente codice di esempio mostra come aggiungere una regola di formattazione condizionale di tipo Valore cella sulle celle A1 e B2.

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
### **Supporto per collegamenti ipertestuali**
Aspose.Cells for C++ supporta ora [aggiunta di collegamenti ipertestuali alle celle del foglio di lavoro](/cells/it/cpp/add-hyperlinks-to-the-cells/). Per fornire questa funzionalità, la versione 16.12.0 di Aspose.Cells for C++ ha esposto la classe IHyperlinkCollection accessibile tramite l'oggetto IWorksheet mentre un collegamento ipertestuale può essere aggiunto alla collezione utilizzando il metodo IHyperlinkCollection.Add come dimostrato di seguito.

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
### **Supporto per le proprietà del documento**
L'applicazione Excel supporta 2 tipi di proprietà del documento come elencato di seguito.

- Proprietà predefinite di sistema (built-in): Le proprietà predefinite contengono informazioni generali sul documento come titolo del documento, nome dell'autore, statistiche del documento e così via.
- Proprietà definite dall'utente (personalizzate): Proprietà personalizzate definite dall'utente sotto forma di coppia nome-valore.

Aspose.Cells for C++ supporta [la gestione di entrambi i tipi di proprietà del documento, built-in e personalizzate](/cells/it/cpp/managing-document-properties/). La classe IWorkbook di Aspose.Cells rappresenta un file Excel. Per accedere alle proprietà del documento incorporate, utilizzare IWorkbook.GetBuiltInDocumentProperties mentre le proprietà del documento personalizzate possono essere accessibili utilizzando il metodo IWorkbook.GetCustomDocumentProperties.

Il codice di esempio seguente carica un foglio di calcolo di esempio esistente e legge le proprietà del documento incorporate come Titolo, Soggetto e la proprietà personalizzata denominata MyCustom1.

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
### **Supporto per gli oggetti elenco**
Una tabella Excel è una matrice di celle contenente un qualsiasi numero di righe e colonne mentre la stessa tabella viene indicata come un oggetto Lista in Aspose.Cells for C++ API. Il namespace Aspose::Cells::Tables contiene tutte le classi necessarie che trattano le operazioni relative agli oggetti Lista. Le classi più importanti da menzionare sono IListObject e IListObjectCollection che consentono di [creare e formattare gli oggetti Lista](/cells/it/cpp/create-and-format-table/) e così via.

Il seguente codice di esempio carica il file di foglio di calcolo di esempio e poi crea un Oggetto Lista (tabella) in un intervallo A1:H10, quindi fa uso dei suoi vari metodi per mostrare il subtotale.

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
### **Supporto per il Raggruppamento di Righe e Colonne**
La Aspose.Cells for C++ API può essere utilizzata per raggruppare righe e colonne utilizzando la classe ICells che è sostanzialmente la collezione di tutte le celle in un dato foglio di lavoro. La classe ICells offre i metodi GroupRows e GroupColumns per [raggruppare righe e colonne](/cells/it/cpp/group-rows-and-columns-of-worksheet/) rispettivamente.

Il seguente frammento di codice dimostra lo scenario di utilizzo semplice di entrambi i metodi sopra menzionati.

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
### **Supporto per Temi**
Le API Aspose.Cells for C++ ora supportano l'uso e la manipolazione dei temi offerti dall'applicazione Excel.
#### **Possibilità di Applicare i Colori del Tema Personalizzati**
Il seguente frammento cerca di [creare un nuovo tema con colori personalizzati](/cells/it/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) per il workbook.

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
#### **Supporto per la Manipolazione dei Colori del Tema**
Il seguente codice di esempio mostra come [leggere e modificare i colori del tema del workbook](/cells/it/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Il codice di esempio carica un foglio di calcolo esistente, legge i suoi colori del tema cioè Accent1-Accent6, e modifica i colori prima di salvare il foglio di calcolo.

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
#### **Possibilità di Copiare Temi tra Workbook**
Il seguente codice di esempio mostra come [copiare un tema da un workbook a un altro](/cells/it/cpp/copy-theme-from-one-workbook-to-another/), il che potrebbe essere utile per applicare temi incorporati o personalizzati su più fogli di calcolo.

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
## **API Rinominate**
Con il rilascio di Aspose.Cells for C++ 16.12.0, abbiamo rinominato alcuni metodi per mantenere uniformi le interfacce. L'elenco di tutte le API rinominate è il seguente.
#### **Rinominato il metodo ICell::SetStyle in ICell::SetIStyle**
#### **Rinominato il metodo ICell::SetCharacters in ICell::SetIFontSettings**
#### **Rinominato il metodo ICellsColor::SetThemeColor in ICellsColor::SetIThemeColor**
#### **Rinominato il metodo ICells::SetStyle in ICells::SetIStyle**
#### **Rinominato il metodo ICellsHelper::GetDPI_i in ICellsHelper::GetDPI**
#### **Rinominato il metodo ICellsHelper::SetDPI_i in ICellsHelper::SetDPI**
#### **Rinominato il metodo ICellsHelper::GetVersion_i in ICellsHelper::GetVersion**
#### **Rinominato il metodo ICellsHelper::IsProtectedByRMS_i in ICellsHelper::IsProtectedByRMS**
#### **Rinominato il metodo ICellsHelper::IsProtectedByRMS_i in ICellsHelper::IsProtectedByRMS**
#### **Rinominato il metodo ICellsHelper::CellNameToIndex_i in ICellsHelper::CellNameToIndex**
#### **Rinominato il metodo ICellsHelper::CellIndexToName_i in ICellsHelper::CellIndexToName**
#### **Rinominato il metodo ICellsHelper::ColumnIndexToName_i in ICellsHelper::ColumnIndexToName**
#### **Rinominato il metodo ICellsHelper::ColumnNameToIndex_i in ICellsHelper::ColumnNameToIndex**
#### **Rinominato il metodo ICellsHelper::RowIndexToName_i in ICellsHelper::RowIndexToName**
#### **Rinominato il metodo ICellsHelper::RowNameToIndex_i in ICellsHelper::RowNameToIndex**
#### **Rinominato il metodo ICellsHelper::ConvertR1C1FormulaToA1_i in ICellsHelper::ConvertR1C1FormulaToA1**
#### **Rinominato il metodo ICellsHelper::ConvertA1FormulaToR1C1_i in ICellsHelper::ConvertA1FormulaToR1C1**
#### **Rinominato il metodo ICellsHelper::GetDateTimeFromDouble_i in ICellsHelper::GetDateTimeFromDouble**
#### **Rinominato il metodo ICellsHelper::GetDoubleFromDateTime_i in ICellsHelper::GetDoubleFromDateTime**
#### **Rinominato il metodo ICellsHelper::DetectLoadFormat_i in ICellsHelper::DetectLoadFormat**
#### **Rinominato il metodo ICellsHelper::DetectFileFormat_i in ICellsHelper::DetectFileFormat**
#### **Rinominato il metodo ICellsHelper::GetFontDir_i in ICellsHelper::GetFontDir**
#### **Rinominato il metodo ICellsHelper::SetFontDir_i in ICellsHelper::SetFontDir**
#### **Rinominato il metodo ICellsHelper::GetFontDirs_i in ICellsHelper::GetFontDirs**
#### **Rinominato il metodo ICellsHelper::SetFontDirs_i in ICellsHelper::SetFontDirs**
#### **Rinominato il metodo ICellsHelper::GetFontFiles_i in ICellsHelper::GetFontFiles**
#### **Rinominato il metodo ICellsHelper::SetFontFiles_i in ICellsHelper::SetFontFiles**
#### **Rinominato il metodo ICellsHelper::GetStartupPath_i in ICellsHelper::GetStartupPath**
#### **Rinominato il metodo ICellsHelper::SetStartupPath_i in ICellsHelper::SetStartupPath**
#### **Rinominato il metodo ICellsHelper::GetAltStartPath_i in ICellsHelper::GetAltStartPath**
#### **Rinominato il metodo ICellsHelper::SetAltStartPath_i in ICellsHelper::SetAltStartPath**
#### **Rinominato il metodo ICellsHelper::GetLibraryPath_i in ICellsHelper::GetLibraryPath**
#### **Rinominato il metodo ICellsHelper::SetLibraryPath_i in ICellsHelper::SetLibraryPath**
#### **Rinominato il metodo ICellsHelper::GetUsedColors_i in ICellsHelper::GetUsedColors**
#### **Rinominato il metodo ICellsHelper::AddAddInFunction_i in ICellsHelper::AddAddInFunction**
#### **Rinominato il metodo ICellsHelper::MergeFiles_i in ICellsHelper::MergeFiles**
#### **Rinominato il metodo IColumnCollection::GetByIndex_i in IColumnCollection::GetIColumn**
#### **Rinominato il metodo IFileFormatUtil::DetectFileFormat_i in IFileFormatUtil::DetectFileFormat**
#### **Rinominato il metodo IFileFormatUtil::ExtensionToSaveFormat_i in IFileFormatUtil::ExtensionToSaveFormat**
#### **Rinominato il metodo IFileFormatUtil::IsTemplateFormat_i in IFileFormatUtil::IsTemplateFormat**
#### **Rinominato il metodo IFileFormatUtil::LoadFormatToExtension_i in IFileFormatUtil::LoadFormatToExtension**
#### **Rinominato il metodo IFileFormatUtil::LoadFormatToSaveFormat_i in IFileFormatUtil::LoadFormatToSaveFormat**
#### **Rinominato il metodo IFileFormatUtil::SaveFormatToExtension_i in IFileFormatUtil::SaveFormatToExtension**
#### **Rinominato il metodo IFileFormatUtil::SaveFormatToLoadFormat_i in IFileFormatUtil::SaveFormatToLoadFormat**
#### **Rinominato il metodo IRange::SetStyle in IRange::SetIStyle**
#### **Rinominato il metodo IFindOptions::SetRange in IFindOptions::SetIRange**
#### **Rinominato il metodo ILoadOptions::SetLoadDataOptions in ILoadOptions::SetILoadDataOptions**
#### **Rinominato il metodo IWorkbook::SetSettings in IWorkbook::SetISettings**
#### **Rinominato il metodo IWorkbook::SetDefaultStyle in IWorkbook::SetDefaultIStyle**
