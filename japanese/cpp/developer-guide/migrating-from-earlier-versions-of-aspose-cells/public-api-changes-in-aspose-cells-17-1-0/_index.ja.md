---
title: パブリック API Aspose.Cells 17.1.0 の変更点
type: docs
weight: 20
url: /ja/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 16.12.0 から 17.1.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **名前付き範囲のサポート**
Aspose.Cells for C++ は、名前付き範囲の作成と操作をサポートするようになりました。次のコード スニペットは、Aspose.Cells for C++ API を使用して、[名前付き範囲を作成する](/cells/ja/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

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

新しい名前付き範囲を作成するだけでなく、Aspose.Cells for C++ API は既存の名前付き範囲の操作もサポートします。次のコード スニペットでは、Aspose.Cells for C++ API を使用して[既存の名前付き範囲を操作する](/cells/ja/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

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
XML マップのリンクに役立つ LinkToXmlMap メソッドが ICells クラスに追加されました。
### **ICells::ImportCSV メソッドを追加**
ImportCSV メソッドが ICells クラスに追加されました。これは、CSV ファイルをワークシートのセルにインポートするのに役立ちます。
### **ICells::ImportTwoDimensionArray メソッドを追加**
GetIProtectedRangeCollection メソッドが ICells クラスに追加されました。これは、データの 2 次元配列をワークシートにインポートするのに役立ちます。
### **IWorksheet::GetIProtectedRangeCollection メソッドを追加**
GetIProtectedRangeCollection メソッドが IWorksheet クラスに追加されました。これは、IProtectedRange オブジェクトのコレクションを取得するのに役立ちます。
### **IWorksheet::GetIProtectedRangeCollection メソッドを追加**
GetIProtectedRangeCollection メソッドが IWorksheet クラスに追加されました。これは、ワークシートから編集範囲コレクションを取得するのに役立ちます。
### **IWorkbookSettings::ClearPivottables メソッドを追加**
ClearPivottables メソッドが IWorkbookSettings クラスに追加されました。これは、特定のスプレッドシートからすべてのピボット テーブルをクリアするのに役立ちます。
### **IWorksheetCollection::CreateIRange メソッドを追加**
CreateIRange メソッドが IWorksheetCollection クラスに追加されました。これは、セル参照を文字列形式で渡すことによって IRange のオブジェクトを作成するのに役立ちます。
### **IExternalLink::IsVisible メソッドを追加**
IsVisible メソッドは、Excel アプリケーションでの外部リンクの表示ステータスを取得します。
### **GetScaleCrop および SetScaleCrop メソッドを追加**
Aspose.Cells for C++ 17.1.0 では、GetScaleCrop および SetScaleCrop メソッドが IBuiltInDocumentPropertyCollection クラスに公開されました。これらのメソッドは、ドキュメント サムネイルの表示モードを示す ScaleCrop プロパティを取得または設定するのに役立ちます。
### **GetLinksUpToDate および SetLinksUpToDate メソッドを追加**
Aspose.Cells for C++ 17.1.0 では、GetLinksUpToDate および SetLinksUpToDate メソッドが IBuiltInDocumentPropertyCollection クラスに公開されました。これらのメソッドは、ドキュメント内のハイパーリンクが最新かどうかを示す LinkUpToDate プロパティを取得または設定するのに役立ちます。
### **GetAbsolutePath および SetAbsolutePath メソッドを追加**
Aspose.Cells for C++ 17.1.0 では、GetAbsolutePath および SetAbsolutePath メソッドが IWorkbook クラスに公開されました。これらのメソッドは、外部リンクにのみ使用できるファイルの絶対パスを取得または設定するのに役立ちます。
### **GetFormula および SetFormula メソッドを追加**
Aspose.Cells for C++ のこのリリースでは、IListColumn クラスの GetFormula および SetFormula メソッドが公開されています。これらのメソッドは、リスト列の数式を取得または設定するのに役立ちます。
### **GetCheckCompatibility および SetCheckCompatibility メソッドを追加**
Aspose.Cells for C++ のこのリリースでは、IWorkbookSettings クラスの GetCheckCompatibility メソッドと GetCheckCompatibility メソッドが公開されました。これらのメソッドは、ワークブックを保存するときに API が互換性をチェックする必要があるかどうかを示す互換性チェック プロパティを取得または設定するのに役立ちます。デフォルト値は true で、アプリケーションの要件が互換性をチェックしない場合は false に設定できます。
### **GetILightCellsDataHandler および SetILightCellsDataHandler メソッドを追加**
Aspose.Cells for C++ は、ILoadOptions クラスの GetILightCellsDataHandler および SetILightCellsDataHandler メソッドを公開しました。これらのメソッドは、テンプレート ファイルの読み取り中にセル データを処理するためのデータ ハンドラーを示します。
### **GetCultureInfo および SetCultureInfo メソッドを追加**
Aspose.Cells for C++ は、ILoadOptions クラスの GetCultureInfo および SetCultureInfo メソッドを公開しました。これらのメソッドは、ファイルのロード時にシステム カルチャ情報を取得または設定できます。
## **削除された API**
### **ICells::MaxDataRowInColumn メソッドを削除**
代わりに ICells::GetLastDataRow メソッドを使用することをお勧めします。
### **ICell::GetConditionalIStyle メソッドを削除**
代わりに ICell::GetIConditionalFormattingResult メソッドを使用することをお勧めします。
### **IPageSetup::GetDraft および SetDraft メソッドを削除**
代わりに IPageSetup::GetPrintDraft および IPageSetup::SetPrintDraft メソッドを使用することをお勧めします。

{{% alert color="primary" %}} 

Aspose.Cells for C++ 17.1.0 のリリースに伴い、使用されていないため不要と判断されたいくつかのメソッドを削除しました。これは、そのようなすべてのメソッドのリストです。

- IPaneCollection::GetAcitvePaneType および SetAcitvePaneType メソッド
- IRange::ToString メソッド
- IRow::Equals メソッド
- IWorkbook::SetISettings メソッド
- ICell::ToString() メソッド
- ICell::Equals(ObjectPtr) メソッド
- ICell::GetHashCode メソッド
- IWorksheet::ToString メソッド

{{% /alert %}}
