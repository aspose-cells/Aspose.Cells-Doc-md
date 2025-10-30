---
title: Aspose.Cells 16.12.0でのパブリックAPIの変更
type: docs
weight: 10
url: /ja/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、バージョン16.11.0から16.12.0へのAspose.Cells APIの変更について説明します。これは、モジュール/アプリケーション開発者にとって興味深い変更だけでなく、新しいメソッドや更新された公開メソッド、追加および削除されたクラスなどを含むものです。

{{% /alert %}} 
## **APIの追加**
### **ピボットテーブルのサポート**
Aspose.Cells for C++の2番目のリリースでは、ピボットテーブルの作成および操作がサポートされています。Aspose.Cells for C++はPivot Tableオブジェクトを表すIPivotTableクラスを提供し、Pivot Tableのコレクションを表すIPivotTableCollectionも提供します。IPivotTableCollectionはIWorksheetオブジェクトを介してアクセスでき、IPivotTableCollection.Addメソッドを使用してコレクションに新しいピボットテーブルを追加できます。

以下のコードスニペットは、Aspose.Cells for C++ APIを使用して[ゼロからピボットテーブルを作成する](/cells/ja/cpp/create-pivot-table/)方法を示しています。

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

新しいピボットテーブルを作成するだけでなく、Aspose.Cells for C++ APIは既存のピボットテーブルを操作することもサポートしています。APIは現在、ピボットテーブルのソース範囲のデータを変更してからリフレッシュする機能をサポートしています。ピボットテーブルを望む通りに操作した後は、更新されたデータソースに対してピボットテーブルをリフレッシュするためにIPivotTable.RefreshDataおよびIPivotTable.CalculateDataメソッドを使用することが最適です。

以下のコードスニペットは、Aspose.Cells for C++ APIを使用して[既存のピボットテーブルを操作する](/cells/ja/cpp/manipulate-pivot-table/)方法を示しています。

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
### **条件付き書式ルールのサポート**
Aspose.Cells for C++は、IFormatConditionクラスを公開することでワークシートに条件付き書式ルールを追加する機能を提供します。前述のクラスは、アプリケーションの要件に応じて条件付き書式ルールを[適用](/cells/ja/cpp/apply-conditional-formatting-in-worksheet/)するための以下のメソッドをさらに提供します。

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

以下のサンプルコードは、セルA1およびB2のセル値タイプの条件付き書式ルールを追加する方法を示しています。

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
### **ハイパーリンクのサポート**
Aspose.Cells for C++は、ワークシートセルにハイパーリンクを[追加](/cells/ja/cpp/add-hyperlinks-to-the-cells/)する機能をサポートしています。この機能を提供するために、Aspose.Cells for C++ 16.12.0ではIHyperlinkCollectionクラスを公開し、これはIWorksheetオブジェクトを介してアクセスできます。ハイパーリンクはIHyperlinkCollection.Addメソッドを使用してコレクションに追加できます。

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
### **ドキュメントプロパティのサポート**
Excelアプリケーションは以下の2種類のドキュメントプロパティをサポートしています。

- システム定義（組み込み）プロパティ： 組み込みプロパティにはドキュメントのタイトル、著者名、ドキュメントの統計情報など、ドキュメントに関する一般情報が含まれています。
- ユーザー定義（カスタム）プロパティ： エンドユーザーが名前と値のペアの形式で定義するカスタムプロパティです。

Aspose.Cells for C++は[ドキュメントのプロパティ（組み込みおよびカスタム）の管理](/cells/ja/cpp/managing-document-properties/)をサポートしています。Aspose.CellsのIWorkbookクラスはExcelファイルを表します。組み込みのドキュメントのプロパティにアクセスするには、IWorkbook.GetBuiltInDocumentPropertiesを使用し、カスタムのドキュメントのプロパティにアクセスするには、IWorkbook.GetCustomDocumentPropertiesメソッドを使用します。

以下のサンプルコードは既存のサンプルスプレッドシートをロードし、タイトル、サブジェクトなどの組み込みのドキュメントのプロパティとMyCustom1という名前のカスタムプロパティを読み取ります。

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
### **ListObjectsのサポート**
Excelテーブルは行と列の数が任意のセルの行列であり、同じテーブルはAspose.Cells for C++ APIではList Objectとして参照されます。Aspose::Cells::Tables名前空間には、List Objectsに関連する操作を扱うためのすべての必要なクラスが含まれています。最も注目すべきクラスはIListObjectおよびIListObjectCollectionであり、[List Objectを作成および書式設定](/cells/ja/cpp/create-and-format-table/)することができます。

以下のサンプルコードはサンプルのスプレッドシートファイルをロードし、その後、範囲A1:H10にList Object（テーブル）を作成し、そのさまざまなメソッドを使用して小計を表示します。

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
### **行および列のグループ化のサポート**
ICellsクラスを使用して行と列をグループ化するために、Aspose.Cells for C++ APIを使用できます。ICellsクラスは、指定されたワークシート内のすべてのセルのコレクションであり、GroupRowsおよびGroupColumnsメソッドを提供しています。

カスタムテーマカラーを[ワークブックに適用](/cells/ja/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/)するための簡単な使用シナリオを示す以下のスニペット。

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
### **テーマのサポート**
Aspose.Cells for C++ APIは現在、Excelアプリケーションが提供するテーマを使用して操作できるようになりました。
#### **カスタムテーマカラーを適用する能力**
[カスタムカラーを使用して新しいテーマを作成](/cells/ja/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/)するスニペットは以下の通りです。

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
#### **テーマカラーの操作のサポート**
次のサンプルコードは、スプレッドシートをロードし、そのテーマの色（Accent1-Accent6）を読み取り、変更してからスプレッドシートを保存します。

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
#### **ワークブック間でテーマをコピーする能力を示す以下のサンプルコード。**
[ワークブックから別のワークブックにテーマをコピーする](/cells/ja/cpp/copy-theme-from-one-workbook-to-another/)方法を示す以下のサンプルコード。複数のスプレッドシートに組み込みまたはカスタムのテーマを適用する際に役立ちます。

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
## **改名されたAPI**
Aspose.Cells for C++ 16.12.0で、インターフェースを統一するためにいくつかのメソッド名を変更しました。変更されたすべてのAPIのリストは以下のとおりです。
#### **ICell::SetStyleメソッドをICell::SetIStyleに改名**
#### **ICell::SetCharactersメソッドをICell::SetIFontSettingsに改名**
#### **ICellsColor::SetThemeColorメソッドをICellsColor::SetIThemeColorに改名**
#### **ICells::SetStyleメソッドをICells::SetIStyleに改名**
#### **ICellsHelper::GetDPI_iメソッドをICellsHelper::GetDPIに改名**
#### **ICellsHelper::SetDPI_iメソッドをICellsHelper::SetDPIに改名**
#### **ICellsHelper::GetVersion_iメソッドをICellsHelper::GetVersionに改名**
#### **ICellsHelper::IsProtectedByRMS_iメソッドをICellsHelper::IsProtectedByRMSに改名**
#### **ICellsHelper::IsProtectedByRMS_iメソッドをICellsHelper::IsProtectedByRMSに改名**
#### **ICellsHelper::CellNameToIndex_iメソッドをICellsHelper::CellNameToIndexに改名**
#### **ICellsHelper::CellIndexToName_iメソッドをICellsHelper::CellIndexToNameに改名**
#### **ICellsHelper::ColumnIndexToName_iメソッドをICellsHelper::ColumnIndexToNameに改名**
#### **ICellsHelper::ColumnNameToIndex_i メソッドを ICellsHelper::ColumnNameToIndex に名前を変更しました**
#### **ICellsHelper::RowIndexToName_i メソッドを ICellsHelper::RowIndexToName に名前を変更しました**
#### **ICellsHelper::RowNameToIndex_i メソッドを ICellsHelper::RowNameToIndex に名前を変更しました**
#### **ICellsHelper::ConvertR1C1FormulaToA1_i メソッドを ICellsHelper::ConvertR1C1FormulaToA1 に名前を変更しました**
#### **ICellsHelper::ConvertA1FormulaToR1C1_i メソッドを ICellsHelper::ConvertA1FormulaToR1C1 に名前を変更しました**
#### **ICellsHelper::GetDateTimeFromDouble_i メソッドを ICellsHelper::GetDateTimeFromDouble に名前を変更しました**
#### **ICellsHelper::GetDoubleFromDateTime_i メソッドを ICellsHelper::GetDoubleFromDateTime に名前を変更しました**
#### **ICellsHelper::DetectLoadFormat_i メソッドを ICellsHelper::DetectLoadFormat に名前を変更しました**
#### **ICellsHelper::DetectFileFormat_i メソッドを ICellsHelper::DetectFileFormat に名前を変更しました**
#### **ICellsHelper::GetFontDir_i メソッドを ICellsHelper::GetFontDir に名前を変更しました**
#### **ICellsHelper::SetFontDir_i メソッドを ICellsHelper::SetFontDir に名前を変更しました**
#### **ICellsHelper::GetFontDirs_i メソッドを ICellsHelper::GetFontDirs に名前を変更しました**
#### **ICellsHelper::SetFontDirs_i メソッドを ICellsHelper::SetFontDirs に名前を変更しました**
#### **ICellsHelper::GetFontFiles_i メソッドを ICellsHelper::GetFontFiles に名前を変更しました**
#### **ICellsHelper::SetFontFiles_i メソッドを ICellsHelper::SetFontFiles に名前を変更しました**
#### **ICellsHelper::GetStartupPath_i メソッドを ICellsHelper::GetStartupPath に名前を変更しました**
#### **ICellsHelper::SetStartupPath_i メソッドを ICellsHelper::SetStartupPath に名前を変更しました**
#### **ICellsHelper::GetAltStartPath_i メソッドを ICellsHelper::GetAltStartPath に名前を変更しました**
#### **ICellsHelper::SetAltStartPath_i メソッドを ICellsHelper::SetAltStartPath に名前を変更しました**
#### **ICellsHelper::GetLibraryPath_i メソッドを ICellsHelper::GetLibraryPath に名前を変更しました**
#### **ICellsHelper::SetLibraryPath_i メソッドを ICellsHelper::SetLibraryPath に名前を変更しました**
#### **ICellsHelper::GetUsedColors_i メソッドを ICellsHelper::GetUsedColors に名前を変更しました**
#### **ICellsHelper::AddAddInFunction_i メソッドを ICellsHelper::AddAddInFunction に名前を変更しました**
#### **ICellsHelper::MergeFiles_i メソッドを ICellsHelper::MergeFiles に名前を変更しました**
#### **IColumnCollection::GetByIndex_i メソッドを IColumnCollection::GetIColumn に名前を変更しました**
#### **IFileFormatUtil::DetectFileFormat_i メソッドを IFileFormatUtil::DetectFileFormat に名前を変更しました**
#### **IFileFormatUtil::ExtensionToSaveFormat_i メソッドを IFileFormatUtil::ExtensionToSaveFormat に名前を変更しました**
#### **IFileFormatUtil::IsTemplateFormat_i メソッドを IFileFormatUtil::IsTemplateFormat に名前を変更しました**
#### **IFileFormatUtil::LoadFormatToExtension_i メソッドを IFileFormatUtil::LoadFormatToExtension に名前を変更しました**
#### **IFileFormatUtil::LoadFormatToSaveFormat_i メソッドを IFileFormatUtil::LoadFormatToSaveFormat に名前を変更しました**
#### **IFileFormatUtil::SaveFormatToExtension_i メソッドの名前を IFileFormatUtil::SaveFormatToExtension に変更**
#### **IFileFormatUtil::SaveFormatToLoadFormat_i メソッドの名前を IFileFormatUtil::SaveFormatToLoadFormat に変更**
#### **IRange::SetStyle メソッドの名前を IRange::SetIStyle に変更**
#### **IFindOptions::SetRange メソッドの名前を IFindOptions::SetIRange に変更**
#### **ILoadOptions::SetLoadDataOptions メソッドの名前を ILoadOptions::SetILoadDataOptions に変更**
#### **IWorkbook::SetSettings メソッドの名前を IWorkbook::SetISettings に変更**
#### **IWorkbook::SetDefaultStyle メソッドの名前を IWorkbook::SetDefaultIStyle に変更**
{{< app/cells/assistant language="cpp" >}}
