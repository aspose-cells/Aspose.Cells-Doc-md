---
title: パブリック API Aspose.Cells 16.12.0 の変更点
type: docs
weight: 10
url: /ja/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.11.0 から 16.12.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **ピボット テーブルのサポート**
Aspose.Cells for C++ の 2 番目のリリースでは、ピボット テーブルの作成と操作がサポートされています。 Aspose.Cells for C++ は、ピボット テーブル オブジェクトを表す IPivotTable クラスを提供しますが、IPivotTableCollection はピボット テーブルのコレクションを表します。 IPivotTableCollection には IWorksheet オブジェクトを介してアクセスでき、IPivotTableCollection.Add メソッドを使用して新しいピボット テーブルをコレクションに追加できます。

次のコード スニペットは、Aspose.Cells for C++ API を使用して、[ピボットテーブルを最初から作成する](/cells/ja/cpp/create-pivot-table/).

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

新しいピボット テーブルを作成するだけでなく、Aspose.Cells for C++ API は既存のピボット テーブルの操作もサポートします。 API は現在、ピボット テーブルのソース範囲でデータを変更してから更新することをサポートしています。ピボット テーブルが必要に応じて操作されたら、IPivotTable.RefreshData および IPivotTable.CalculateData メソッドを使用して、更新されたデータ ソースに対してピボット テーブルを更新することをお勧めします。

次のコード スニペットでは、Aspose.Cells for C++ API を使用して[既存のピボット テーブルを操作する](/cells/ja/cpp/manipulate-pivot-table/).

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
### **条件付き書式ルールのサポート**
Aspose.Cells for C++ では、IFormatCondition クラスを公開することで、条件付き書式ルールをワークシートに追加できるようになりました。前述のクラスは、次のメソッドをさらに提供します。[条件付き書式ルールを適用する](/cells/ja/cpp/apply-conditional-formatting-in-worksheet/)アプリケーションの要件に従って。

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

次のサンプル コードは、セル A1 と B2 にタイプ Cell 値の条件付き書式ルールを追加する方法を示しています。

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
### **ハイパーリンクのサポート**
Aspose.Cells for C++ に対応しました[ワークシートのセルにハイパーリンクを追加する](/cells/ja/cpp/add-hyperlinks-to-the-cells/).この機能を提供するために、Aspose.Cells for C++ 16.12.0 は IWorksheet オブジェクトを介してアクセスできる IHyperlinkCollection クラスを公開しましたが、以下に示すように、IHyperlinkCollection.Add メソッドを使用してハイパーリンクをコレクションに追加できます。

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
### **ドキュメント プロパティのサポート**
Excel アプリケーションは、次の 2 種類のドキュメント プロパティをサポートしています。

- システム定義 (組み込み) プロパティ: 組み込みプロパティには、ドキュメントのタイトル、作成者名、ドキュメントの統計など、ドキュメントに関する一般的な情報が含まれています。
- ユーザー定義 (カスタム) プロパティ: 名前と値のペアの形式でエンド ユーザーによって定義されたカスタム プロパティ。

 Aspose.Cells for C++ 対応[組み込みとカスタムの両方のタイプのドキュメント プロパティを管理する](/cells/ja/cpp/managing-document-properties/)Aspose.Cells' IWorkbook クラスは Excel ファイルを表します。組み込みのドキュメント プロパティにアクセスするには、IWorkbook.GetBuiltInDocumentProperties を使用しますが、カスタム ドキュメント プロパティには IWorkbook.GetCustomDocumentProperties メソッドを使用してアクセスできます。

次のサンプル コードは、既存のサンプル スプレッドシートを読み込み、タイトル、件名、カスタム プロパティなどの組み込みのドキュメント プロパティを MyCustom1 という名前で読み取ります。

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
### **ListObjects のサポート**
Excel テーブルは任意の数の行と列を含むセルのマトリックスですが、同じテーブルは Aspose.Cells for C++ API ではリスト オブジェクトと呼ばれます。 Aspose::Cells::Tables 名前空間には、リスト オブジェクトに関連する操作を処理するために必要なすべてのクラスが含まれています。最も言及する価値のあるクラスは IListObject と IListObjectCollection です。[リスト オブジェクトの作成とフォーマット](/cells/ja/cpp/create-and-format-table/)等々。

次のサンプル コードは、サンプル スプレッドシート ファイルをロードし、リスト オブジェクト (テーブル) を A1:H10 の範囲に作成し、そのさまざまなメソッドを使用して小計を表示します。

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
### **行と列のグループ化のサポート**
Aspose.Cells for C++ API は、基本的に特定のワークシート内のすべてのセルのコレクションである ICells クラスを使用しながら、行と列をグループ化するために使用できます。 ICells クラスは、次の目的で GroupRows および GroupColumns メソッドを提供します。[行と列をグループ化する](/cells/ja/cpp/group-rows-and-columns-of-worksheet/)それぞれ。

次のコード スニペットは、前述の両方の方法の簡単な使用シナリオを示しています。

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
### **テーマのサポート**
Aspose.Cells for C++ API は、Excel アプリケーションによって提供されるテーマの使用と操作をサポートするようになりました。
#### **カスタム テーマの色を適用する機能**
次のスニペットは、[カスタム カラーで新しいテーマを作成する](/cells/ja/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/)ワークブック用。

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
#### **テーマの色の操作のサポート**
次のサンプル コードは、[ワークブックのテーマ カラーの読み取りと変更](/cells/ja/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/).サンプル コードは、既存のスプレッドシートを読み込み、テーマの色 (Accent1 ～ Accent6) を読み取り、スプレッドシートを保存する前に色を変更します。

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
#### **ワークブック間でテーマをコピーする機能**
次のサンプル コードは、[あるワークブックから別のワークブックにテーマをコピーする](/cells/ja/cpp/copy-theme-from-one-workbook-to-another/)、複数のスプレッドシートに組み込みテーマまたはカスタム テーマを適用する場合に役立ちます。

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
## **名前が変更された API**
Aspose.Cells for C++ 16.12.0 のリリースに伴い、インターフェイスを統一するためにいくつかのメソッドの名前を変更しました。名前が変更されたすべての API のリストは次のとおりです。
#### **ICell::SetStyle メソッドの名前を ICell::SetIStyle に変更しました**
#### **ICell::SetCharacters メソッドの名前を ICell::SetIFontSettings に変更しました**
#### **ICellsColor::SetThemeColor メソッドの名前を ICellsColor::SetIThemeColor に変更しました**
#### **ICells::SetStyle メソッドの名前を ICells::SetIStyle に変更しました**
#### **ICellsHelper::GetDPI_i メソッドの名前を ICellsHelper::GetDPI に変更しました**
#### **ICellsHelper::SetDPI_i メソッドの名前を ICellsHelper::SetDPI に変更しました**
#### **ICellsHelper::GetVersion_i メソッドの名前を ICellsHelper::GetVersion に変更しました**
#### **ICellsHelper::IsProtectedByRMS_i メソッドの名前を ICellsHelper::IsProtectedByRMS に変更しました**
#### **ICellsHelper::IsProtectedByRMS_i メソッドの名前を ICellsHelper::IsProtectedByRMS に変更しました**
#### **ICellsHelper::CellNameToIndex_i メソッドの名前を ICellsHelper::CellNameToIndex に変更しました**
#### **ICellsHelper::CellIndexToName_i メソッドの名前を ICellsHelper::CellIndexToName に変更しました**
#### **ICellsHelper::ColumnIndexToName_i メソッドの名前を ICellsHelper::ColumnIndexToName に変更しました**
#### **ICellsHelper::ColumnNameToIndex_i メソッドの名前を ICellsHelper::ColumnNameToIndex に変更しました**
#### **ICellsHelper::RowIndexToName_i メソッドの名前を ICellsHelper::RowIndexToName に変更しました**
#### **ICellsHelper::RowNameToIndex_i メソッドの名前を ICellsHelper::RowNameToIndex に変更しました**
#### **ICellsHelper::ConvertR1C1FormulaToA1_i メソッドの名前を ICellsHelper::ConvertR1C1FormulaToA1 に変更しました**
#### **ICellsHelper::ConvertA1FormulaToR1C1_i メソッドの名前を ICellsHelper::ConvertA1FormulaToR1C1 に変更しました**
#### **ICellsHelper::GetDateTimeFromDouble_i メソッドの名前を ICellsHelper::GetDateTimeFromDouble に変更しました**
#### **ICellsHelper::GetDoubleFromDateTime_i メソッドの名前を ICellsHelper::GetDoubleFromDateTime に変更しました**
#### **ICellsHelper::DetectLoadFormat_i メソッドの名前を ICellsHelper::DetectLoadFormat に変更しました**
#### **ICellsHelper::DetectFileFormat_i メソッドの名前を ICellsHelper::DetectFileFormat に変更しました**
#### **ICellsHelper::GetFontDir_i メソッドの名前を ICellsHelper::GetFontDir に変更しました**
#### **ICellsHelper::SetFontDir_i メソッドの名前を ICellsHelper::SetFontDir に変更しました**
#### **ICellsHelper::GetFontDirs_i メソッドの名前を ICellsHelper::GetFontDirs に変更しました**
#### **ICellsHelper::SetFontDirs_i メソッドの名前を ICellsHelper::SetFontDirs に変更しました**
#### **ICellsHelper::GetFontFiles_i メソッドの名前を ICellsHelper::GetFontFiles に変更しました**
#### **ICellsHelper::SetFontFiles_i メソッドの名前を ICellsHelper::SetFontFiles に変更しました**
#### **ICellsHelper::GetStartupPath_i メソッドの名前を ICellsHelper::GetStartupPath に変更しました**
#### **ICellsHelper::SetStartupPath_i メソッドの名前を ICellsHelper::SetStartupPath に変更しました**
#### **ICellsHelper::GetAltStartPath_i メソッドの名前を ICellsHelper::GetAltStartPath に変更しました**
#### **ICellsHelper::SetAltStartPath_i メソッドの名前を ICellsHelper::SetAltStartPath に変更しました**
#### **ICellsHelper::GetLibraryPath_i メソッドの名前を ICellsHelper::GetLibraryPath に変更しました**
#### **ICellsHelper::SetLibraryPath_i メソッドの名前を ICellsHelper::SetLibraryPath に変更しました**
#### **ICellsHelper::GetUsedColors_i メソッドの名前を ICellsHelper::GetUsedColors に変更しました**
#### **ICellsHelper::AddAddInFunction_i メソッドの名前を ICellsHelper::AddAddInFunction に変更しました**
#### **ICellsHelper::MergeFiles_i メソッドの名前を ICellsHelper::MergeFiles に変更しました**
#### **IColumnCollection::GetByIndex_i メソッドの名前を IColumnCollection::GetIColumn に変更しました**
#### **IFileFormatUtil::DetectFileFormat_i メソッドの名前を IFileFormatUtil::DetectFileFormat に変更しました**
#### **IFileFormatUtil::ExtensionToSaveFormat_i メソッドの名前を IFileFormatUtil::ExtensionToSaveFormat に変更しました**
#### **IFileFormatUtil::IsTemplateFormat_i メソッドの名前を IFileFormatUtil::IsTemplateFormat に変更しました**
#### **IFileFormatUtil::LoadFormatToExtension_i メソッドの名前を IFileFormatUtil::LoadFormatToExtension に変更しました**
#### **IFileFormatUtil::LoadFormatToSaveFormat_i メソッドの名前を IFileFormatUtil::LoadFormatToSaveFormat に変更しました**
#### **IFileFormatUtil::SaveFormatToExtension_i メソッドの名前を IFileFormatUtil::SaveFormatToExtension に変更しました**
#### **IFileFormatUtil::SaveFormatToLoadFormat_i メソッドの名前を IFileFormatUtil::SaveFormatToLoadFormat に変更しました**
#### **IRange::SetStyle メソッドの名前を IRange::SetIStyle に変更しました**
#### **IFindOptions::SetRange メソッドの名前を IFindOptions::SetIRange に変更しました**
#### **ILoadOptions::SetLoadDataOptions メソッドの名前を ILoadOptions::SetILoadDataOptions に変更しました**
#### **IWorkbook::SetSettings メソッドの名前を IWorkbook::SetISettings に変更しました**
#### **IWorkbook::SetDefaultStyle メソッドの名前を IWorkbook::SetDefaultIStyle に変更しました**
