---
title: Changements d API publics dans Aspose.Cells 16.12.0
type: docs
weight: 10
url: /fr/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 16.11.0 à la version 16.12.0 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement de nouvelles méthodes publiques et mises à jour, des classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge des tableaux croisés dynamiques**
La deuxième version de Aspose.Cells for C++ prend en charge la création ainsi que la manipulation des tableaux croisés dynamiques. Aspose.Cells for C++ fournit la classe IPivotTable qui représente un objet Tableau croisé dynamique, tandis que IPivotTableCollection représente une collection de tableaux croisés dynamiques. La IPivotTableCollection peut être accédée via l'objet IWorksheet et un nouveau tableau croisé dynamique peut être ajouté à la collection en utilisant la méthode IPivotTableCollection.Add.

Le code suivant illustre à quel point il est simple d'utiliser l'API Aspose.Cells for C++ pour [créer des tableaux croisés dynamiques à partir de zéro](/cells/fr/cpp/create-pivot-table/).

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

Outre la création de nouveaux tableaux croisés dynamiques, les API Aspose.Cells for C++ prennent également en charge la manipulation des tableaux croisés dynamiques existants. L'API prend actuellement en charge la modification des données dans la plage source du tableau croisé dynamique, suivi de son actualisation. Une fois le tableau croisé dynamique manipulé comme souhaité, il est préférable d'utiliser les méthodes IPivotTable.RefreshData et IPivotTable.CalculateData pour actualiser le tableau croisé dynamique par rapport à la source de données mise à jour.

Le code suivant utilise l'API Aspose.Cells for C++ pour [manipuler un tableau croisé dynamique existant](/cells/fr/cpp/manipulate-pivot-table/).

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
### **Prise en charge des règles de mise en forme conditionnelle**
Aspose.Cells for C++ permet désormais d'ajouter des règles de mise en forme conditionnelle à la feuille de calcul en exposant la classe IFormatCondition. La classe susmentionnée fournit en outre les méthodes suivantes pour [appliquer les règles de mise en forme conditionnelle](/cells/fr/cpp/apply-conditional-formatting-in-worksheet/) selon les besoins de l'application.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

Le code d'exemple suivant montre comment ajouter une règle de mise en forme conditionnelle de type Valeur de cellule sur les cellules A1 et B2.

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
### **Support des hyperliens**
Aspose.Cells for C++ prend désormais en charge [l'ajout de hyperliens aux cellules de la feuille de calcul](/cells/fr/cpp/add-hyperlinks-to-the-cells/). Pour offrir cette fonctionnalité, la version 16.12.0 de Aspose.Cells for C++ a exposé la classe IHyperlinkCollection qui est accessible via l'objet IWorksheet. Un hyperlien peut être ajouté à la collection en utilisant la méthode IHyperlinkCollection.Add comme démontré ci-dessous.

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
### **Support des propriétés du document**
L'application Excel prend en charge 2 types de propriétés de document comme indiqué ci-dessous.

- Propriétés définies par le système (intégrées) : Les propriétés intégrées contiennent des informations générales sur le document telles que le titre du document, le nom de l'auteur, les statistiques du document, etc.
- Propriétés définies par l'utilisateur (personnalisées) : Les propriétés personnalisées définies par l'utilisateur sous forme de paire nom-valeur.

Aspose.Cells for C++ prend en charge [la gestion des deux types de propriétés du document, intégrées et personnalisées](/cells/fr/cpp/managing-document-properties/). La classe IWorkbook d'Aspose.Cells représente un fichier Excel. Pour accéder aux propriétés de document intégrées, utilisez IWorkbook.GetBuiltInDocumentProperties tandis que les propriétés de document personnalisées peuvent être consultées en utilisant la méthode IWorkbook.GetCustomDocumentProperties.

Le code d'exemple suivant charge une feuille de calcul existante et lit les propriétés de document intégrées telles que le titre, le sujet et la propriété personnalisée nommée MyCustom1.

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
### **Support des ListObjects**
Une table Excel est une matrice de cellules contenant un nombre quelconque de lignes et de colonnes tandis que la même table est désignée comme un objet List dans les API Aspose.Cells for C++. L'espace de noms Aspose::Cells::Tables contient toutes les classes nécessaires pour les opérations liées aux objets List. Les classes les plus importantes sont IListObject et IListObjectCollection qui permettent de [créer et formater des objets List](/cells/fr/cpp/create-and-format-table/) et ainsi de suite.

Le code d'exemple suivant charge le fichier de feuille de calcul d'exemple, crée ensuite un objet List (table) dans une plage A1:H10, puis utilise ses différentes méthodes pour afficher le sous-total.

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
### **Support du regroupement de lignes et de colonnes**
L'API Aspose.Cells for C++ peut être utilisée pour regrouper des lignes et des colonnes en utilisant la classe ICells qui est essentiellement la collection de toutes les cellules dans une feuille de calcul donnée. La classe ICells offre les méthodes GroupRows et GroupColumns pour [regrouper les lignes et les colonnes](/cells/fr/cpp/group-rows-and-columns-of-worksheet/) respectivement.

Le passage de code suivant démontre le scénario d'utilisation simple des deux méthodes susmentionnées.

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
### **Support des thèmes**
Les APIs de Aspose.Cells for C++ permettent désormais d'utiliser et de manipuler les thèmes offerts par l'application Excel.
#### **Capacité à Appliquer les Couleurs de Thème Personnalisé**
Le snippet suivant tente de [créer un nouveau thème avec des couleurs personnalisées](/cells/fr/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) pour le classeur.

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
#### **Support de la Manipulation des Couleurs de Thème**
Le code d'exemple suivant montre comment [lire et modifier les couleurs de thème du classeur](/cells/fr/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). Le code d'exemple charge une feuille de calcul existante, lit ses couleurs de thème, c’est-à-dire Accent1-Accent6, et modifie les couleurs avant de sauvegarder la feuille de calcul.

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
#### **Capacité de Copier les Thèmes Entre les Classeurs**
Le code d'exemple suivant montre comment [copier un thème d'un classeur à un autre](/cells/fr/cpp/copy-theme-from-one-workbook-to-another/), ce qui pourrait être utile pour appliquer des thèmes intégrés ou personnalisés sur plusieurs feuilles de calcul.

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
## **API renommées**
Avec la sortie de Aspose.Cells for C++ 16.12.0, nous avons renommé quelques méthodes afin de maintenir l'uniformité des interfaces. La liste de toutes les APIs renommées est la suivante:
#### **La méthode ICell::SetStyle a été renommée en ICell::SetIStyle**
#### **La méthode ICell::SetCharacters a été renommée en ICell::SetIFontSettings**
#### **La méthode ICellsColor::SetThemeColor a été renommée en ICellsColor::SetIThemeColor**
#### **La méthode ICells::SetStyle a été renommée en ICells::SetIStyle**
#### **La méthode ICellsHelper::GetDPI_i a été renommée en ICellsHelper::GetDPI**
#### **La méthode ICellsHelper::SetDPI_i a été renommée en ICellsHelper::SetDPI**
#### **La méthode ICellsHelper::GetVersion_i a été renommée en ICellsHelper::GetVersion**
#### **La méthode ICellsHelper::IsProtectedByRMS_i a été renommée en ICellsHelper::IsProtectedByRMS**
#### **La méthode ICellsHelper::IsProtectedByRMS_i a été renommée en ICellsHelper::IsProtectedByRMS**
#### **La méthode ICellsHelper::CellNameToIndex_i a été renommée en ICellsHelper::CellNameToIndex**
#### **La méthode ICellsHelper::CellIndexToName_i a été renommée en ICellsHelper::CellIndexToName**
#### **La méthode ICellsHelper::ColumnIndexToName_i a été renommée en ICellsHelper::ColumnIndexToName**
#### **La méthode ICellsHelper::ColumnNameToIndex_i a été renommée en ICellsHelper::ColumnNameToIndex**
#### **La méthode ICellsHelper::RowIndexToName_i a été renommée en ICellsHelper::RowIndexToName**
#### **La méthode ICellsHelper::RowNameToIndex_i a été renommée en ICellsHelper::RowNameToIndex**
#### **La méthode ICellsHelper::ConvertR1C1FormulaToA1_i a été renommée en ICellsHelper::ConvertR1C1FormulaToA1**
#### **La méthode ICellsHelper::ConvertA1FormulaToR1C1_i a été renommée en ICellsHelper::ConvertA1FormulaToR1C1**
#### **La méthode ICellsHelper::GetDateTimeFromDouble_i a été renommée en ICellsHelper::GetDateTimeFromDouble**
#### **La méthode ICellsHelper::GetDoubleFromDateTime_i a été renommée en ICellsHelper::GetDoubleFromDateTime**
#### **La méthode ICellsHelper::DetectLoadFormat_i a été renommée en ICellsHelper::DetectLoadFormat**
#### **La méthode ICellsHelper::DetectFileFormat_i a été renommée en ICellsHelper::DetectFileFormat**
#### **La méthode ICellsHelper::GetFontDir_i a été renommée en ICellsHelper::GetFontDir**
#### **La méthode ICellsHelper::SetFontDir_i a été renommée en ICellsHelper::SetFontDir**
#### **La méthode ICellsHelper::GetFontDirs_i a été renommée en ICellsHelper::GetFontDirs**
#### **La méthode ICellsHelper::SetFontDirs_i a été renommée en ICellsHelper::SetFontDirs**
#### **La méthode ICellsHelper::GetFontFiles_i a été renommée en ICellsHelper::GetFontFiles**
#### **La méthode ICellsHelper::SetFontFiles_i a été renommée en ICellsHelper::SetFontFiles**
#### **La méthode ICellsHelper::GetStartupPath_i a été renommée en ICellsHelper::GetStartupPath**
#### **La méthode ICellsHelper::SetStartupPath_i a été renommée en ICellsHelper::SetStartupPath**
#### **La méthode ICellsHelper::GetAltStartPath_i a été renommée en ICellsHelper::GetAltStartPath**
#### **La méthode ICellsHelper::SetAltStartPath_i a été renommée en ICellsHelper::SetAltStartPath**
#### **La méthode ICellsHelper::GetLibraryPath_i a été renommée en ICellsHelper::GetLibraryPath**
#### **La méthode ICellsHelper::SetLibraryPath_i a été renommée en ICellsHelper::SetLibraryPath**
#### **La méthode ICellsHelper::GetUsedColors_i a été renommée en ICellsHelper::GetUsedColors**
#### **La méthode ICellsHelper::AddAddInFunction_i a été renommée en ICellsHelper::AddAddInFunction**
#### **La méthode ICellsHelper::MergeFiles_i a été renommée en ICellsHelper::MergeFiles**
#### **La méthode IColumnCollection::GetByIndex_i a été renommée en IColumnCollection::GetIColumn**
#### **La méthode IFileFormatUtil::DetectFileFormat_i a été renommée en IFileFormatUtil::DetectFileFormat**
#### **La méthode IFileFormatUtil::ExtensionToSaveFormat_i a été renommée en IFileFormatUtil::ExtensionToSaveFormat**
#### **La méthode IFileFormatUtil::IsTemplateFormat_i a été renommée en IFileFormatUtil::IsTemplateFormat**
#### **La méthode IFileFormatUtil::LoadFormatToExtension_i a été renommée en IFileFormatUtil::LoadFormatToExtension**
#### **La méthode IFileFormatUtil::LoadFormatToSaveFormat_i a été renommée en IFileFormatUtil::LoadFormatToSaveFormat**
#### **La méthode IFileFormatUtil::SaveFormatToExtension_i a été renommée en IFileFormatUtil::SaveFormatToExtension**
#### **La méthode IFileFormatUtil::SaveFormatToLoadFormat_i a été renommée en IFileFormatUtil::SaveFormatToLoadFormat**
#### **La méthode IRange::SetStyle a été renommée en IRange::SetIStyle**
#### **La méthode IFindOptions::SetRange a été renommée en IFindOptions::SetIRange**
#### **La méthode ILoadOptions::SetLoadDataOptions a été renommée en ILoadOptions::SetILoadDataOptions**
#### **La méthode IWorkbook::SetSettings a été renommée en IWorkbook::SetISettings**
#### **La méthode IWorkbook::SetDefaultStyle a été renommée en IWorkbook::SetDefaultIStyle**
{{< app/cells/assistant language="cpp" >}}
