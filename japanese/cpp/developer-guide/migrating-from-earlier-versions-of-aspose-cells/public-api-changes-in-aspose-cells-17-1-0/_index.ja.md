---
title: Aspose.Cells 17.1.0 の公開API変更
type: docs
weight: 20
url: /ja/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

この文書は、バージョン16.12.0から17.1.0へのAspose.Cells APIの変更について、モジュール/アプリケーション開発者に興味を持たれる可能性のあるものを記載しています。新しいメソッドや更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **名前付き範囲のサポート**
Aspose.Cells for C++ は、名前付き範囲の作成および操作をサポートするようになりました。次のコードスニペットは、Aspose.Cells for C++ APIを使用して[名前付き範囲を作成](/cells/ja/cpp/create-named-range-in-a-workbook/)する方法を示しています。

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

新しい名前付き範囲を作成するだけでなく、Aspose.Cells for C++ APIは既存の名前付き範囲を操作することもサポートしています。次のコードスニペットは、Aspose.Cells for C++ APIを使用して[既存の名前付き範囲を操作](/cells/ja/cpp/manipulate-named-range-in-a-workbook/)する方法を示しています。

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **ICells::LinkToXmlMap メソッドを追加**
LinkToXmlMap メソッドがICellsクラスに追加され、XMLマップへのリンク付けに役立ちます。
### **ICells::ImportCSV メソッドを追加**
ImportCSV メソッドがICellsクラスに追加され、ワークシート上にCSVファイルをインポートするのに役立ちます。
### **ICells::ImportTwoDimensionArray メソッドを追加**
GetIProtectedRangeCollection メソッドがICellsクラスに追加され、2次元配列データをワークシートにインポートするのに役立ちます。
### **IWorksheet::GetIProtectedRangeCollection メソッドを追加**
GetIProtectedRangeCollection メソッドがIWorksheetクラスに追加され、IProtectedRangeオブジェクトのコレクションを取得するのに役立ちます。
### **IWorksheet::GetIProtectedRangeCollection メソッドを追加**
GetIProtectedRangeCollection メソッドがIWorksheetクラスに追加され、ワークシートから編集範囲コレクションを取得するのに役立ちます。
### **IWorkbookSettings::ClearPivottables メソッドを追加**
ClearPivottables メソッドがIWorkbookSettingsクラスに追加され、指定されたスプレッドシートからすべてのピボットテーブルを削除するのに役立ちます。
### **IWorksheetCollection::CreateIRange メソッドを追加**
CreateIRange メソッドがIWorksheetCollectionクラスに追加され、セル参照を文字列形式で渡すことで、IRangeのオブジェクトを作成するのに役立ちます。
### **IExternalLink::IsVisible メソッドを追加**
IsVisible メソッドは、Excelアプリケーション内の外部リンクの表示状態を取得します。
### **GetScaleCrop & SetScaleCrop メソッドを追加**
Aspose.Cells for C++ 17.1.0 では、IBuiltInDocumentPropertyCollection クラスに GetScaleCrop および SetScaleCrop メソッドが公開されました。これらのメソッドは、サムネイルの表示モードを示す ScaleCrop プロパティを取得または設定するために役立ちます。
### **GetLinksUpToDate および SetLinksUpToDate メソッドが追加されました**
Aspose.Cells for C++ 17.1.0 では、IBuiltInDocumentPropertyCollection クラスに GetLinksUpToDate および SetLinksUpToDate メソッドが公開されました。これらのメソッドは、ドキュメント内のハイパーリンクが最新かどうかを示す LinkUpToDate プロパティを取得または設定するために役立ちます。
### **GetAbsolutePath および SetAbsolutePath メソッドが追加されました**
Aspose.Cells for C++ 17.1.0 では、IWorkbook クラスに GetAbsolutePath および SetAbsolutePath メソッドが公開されました。これらのメソッドは、ファイルの絶対パスを取得または設定するために役立ちます。これは外部リンク専用のものです。
### **GetFormula および SetFormula メソッドが追加されました**
Aspose.Cells for C++ のこのリリースでは、IListColumn クラスに GetFormula および SetFormula メソッドが公開されました。これらのメソッドは、リスト列の数式を取得または設定するために役立ちます。
### **GetCheckCompatibility および SetCheckCompatibility メソッドが追加されました**
この Aspose.Cells for C++ のリリースでは、IWorkbookSettings クラスに GetCheckCompatibility および GetCheckCompatibility メソッドが公開されました。これらのメソッドは、ワークブックを保存する際に API が互換性をチェックすべきかどうかを示す互換性チェックプロパティを取得または設定するために役立ちます。デフォルト値は true で、アプリケーションの要件が互換性をチェックしない場合は false に設定できます。
### **GetILightCellsDataHandler および SetILightCellsDataHandler メソッドが追加されました**
Aspose.Cells for C++ は、ILoadOptions クラスの GetILightCellsDataHandler および SetILightCellsDataHandler メソッドを公開しています。これらのメソッドは、テンプレートファイルを読み込みながらセルデータの処理を行うデータハンドラを示します。
### **GetCultureInfo および SetCultureInfo メソッドが追加されました**
Aspose.Cells for C++ には、ILoadOptions クラスに GetCultureInfo および SetCultureInfo メソッドが公開されました。これらのメソッドは、ファイルを読み込む際のシステムカルチャ情報を取得または設定できます。
## **API が削除されました**
### **ICells::MaxDataRowInColumn メソッドが削除されました**
かわりに ICells::GetLastDataRow メソッドを使用することをお勧めします。
### **ICell::GetConditionalIStyle メソッドが削除されました**
かわりに ICell::GetIConditionalFormattingResult メソッドを使用することをお勧めします。
### **IPageSetup::GetDraft および SetDraft メソッドが削除されました**
かわりに IPageSetup::GetPrintDraft および IPageSetup::SetPrintDraft メソッドを使用することをお勧めします。

{{% alert color="primary" %}} 

Aspose.Cells for C++ 17.1.0 のリリースにより、使用されていないいくつかのメソッドが削除されました。以下はそのようなメソッドのリストです。

- IPaneCollection::GetAcitvePaneType および SetAcitvePaneType メソッド
- IRange::ToString メソッド
- IRow::Equals メソッド
- IWorkbook::SetISettings メソッド
- ICell::ToString() メソッド
- ICell::Equals(ObjectPtr) メソッド
- ICell::GetHashCode メソッド
- IWorksheet::ToString メソッド

{{% /alert %}}
