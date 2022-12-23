---
title: ドキュメント プロパティの管理
linktitle: ドキュメント プロパティ
type: docs
weight: 80
url: /ja/net/managing-document-properties/
description: スプレッドシート ファイルのドキュメント プロパティを管理します。
---
## **序章**

Microsoft Excel には、スプレッドシート ファイルにプロパティを追加する機能があります。これらのドキュメント プロパティは有用な情報を提供し、以下に詳述するように 2 つのカテゴリに分けられます。

- システム定義 (組み込み) プロパティ: 組み込みプロパティには、ドキュメントのタイトル、作成者名、ドキュメントの統計など、ドキュメントに関する一般的な情報が含まれています。
- ユーザー定義 (カスタム) プロパティ: 名前と値のペアの形式でエンド ユーザーによって定義されたカスタム プロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタム プロパティについて知っておくべき最も重要な点は、組み込みプロパティにアクセスして変更することはできますが、作成または削除することはできないということです。ただし、カスタム プロパティは作成および管理できます。

{{% /alert %}}

## **Microsoft Excel を使用したドキュメント プロパティの管理**

 Microsoft Excel では、Excel ファイルのドキュメント プロパティを WYSIWYG 方式で管理できます。以下の手順に従って、**プロパティ** Excel 2016 のダイアログ。

1. から**ファイル**メニュー、選択**情報**.

|**情報メニューの選択**|
|:- |
|![todo:画像_代替_文章](managing-document-properties_1.png)|
1. クリック**プロパティ**見出しを開き、[詳細プロパティ] を選択します。

|**詳細プロパティの選択をクリックする**|
|:- |
|![todo:画像_代替_文章](managing-document-properties_2.png)|
1. ファイルのドキュメント プロパティを管理します。

|**プロパティダイアログ**|
|:- |
|![todo:画像_代替_文章](managing-document-properties_3.png)|
[プロパティ] ダイアログには、[全般]、[概要]、[統計]、[コンテンツ]、[税関] などのさまざまなタブがあります。各タブは、ファイルに関連するさまざまな種類の情報を構成するのに役立ちます。 [カスタム] タブは、カスタム プロパティを管理するために使用されます。

## **Aspose.Cells を使用したドキュメント プロパティの操作**

開発者は、Aspose.Cells API を使用してドキュメント プロパティを動的に管理できます。この機能は、開発者がファイルの受信、処理、タイムスタンプなどの有用な情報をファイルとともに保存するのに役立ちます。

{{% alert color="primary" %}}

 Aspose.Cells for .NET は、出力ドキュメントに API とバージョン番号に関する情報を直接書き込みます。たとえば、Document を PDF にレンダリングすると、Aspose.Cells for .NET が読み込まれます。**応用**値が「Aspose.Cells」のフィールドと**PDF プロデューサー** 'Aspose.Cells v17.9' などの値を持つフィールド。

出力ドキュメントからこの情報を変更または削除するように Aspose.Cells for .NET に指示することはできないことに注意してください。

{{% /alert %}}

### **ドキュメント プロパティへのアクセス**

Aspose.Cells API は、組み込みとカスタムの両方のタイプのドキュメント プロパティをサポートします。 Aspose.Cells'[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスは Excel ファイルを表し、Excel ファイルと同様に、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには複数のワークシートを含めることができ、それぞれが[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されますが、ワークシートのコレクションは[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラス。

使用[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)以下で説明するように、ファイルのドキュメント プロパティにアクセスします。

- 組み込みのドキュメント プロパティにアクセスするには、次を使用します。[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- カスタム ドキュメント プロパティにアクセスするには、次を使用します。[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

両方の[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)と[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)のインスタンスを返します[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection).このコレクションには[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)各オブジェクトは、単一の組み込みまたはカスタム ドキュメント プロパティを表します。

プロパティにアクセスする方法は、アプリケーションの要件次第です。のプロパティのインデックスまたは名前を使用して[**ドキュメント プロパティ コレクション**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)以下の例に示すように。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

の[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスを使用すると、ドキュメント プロパティの名前、値、およびタイプを取得できます。

- プロパティ名を取得するには、次を使用します[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- プロパティ値を取得するには、次を使用します[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)値をオブジェクトとして返します。
- プロパティ タイプを取得するには、次を使用します。[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) .これは、[**プロパティタイプ**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)列挙値。プロパティ タイプを取得したら、次のいずれかを使用します。**DocumentProperty.ToXXX**を使用する代わりに、適切な型の値を取得するメソッド[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value).の**DocumentProperty.ToXXX**メソッドについては、次の表で説明します。

{{% alert color="primary" %}}

の[**ドキュメント プロパティ**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスは、他のデータ型の値を返す一連のメソッドも提供します。

{{% /alert %}}

|**メンバー名**|**説明**|**ToXXX メソッド**|
|:- |:- |:- |
|ブール値|プロパティのデータ型はブール値です|ブール|
|日にち|プロパティのデータ型は DateTime です。 Microsoft Excelストアのみ<br>日付部分。このタイプのカスタム プロパティに時刻を格納することはできません|ToDateTime|
|浮く|プロパティのデータ型は Double です|二重にする|
|番号|プロパティのデータ型は Int32 です|ToInt|
|弦|プロパティのデータ型は文字列です|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **カスタム ドキュメント プロパティの追加または削除**

このトピックの冒頭で説明したように、これらのプロパティはシステム定義であるため、開発者は組み込みプロパティを追加または削除できませんが、カスタム プロパティはユーザー定義であるため、追加または削除することができます。

### **カスタム プロパティの追加**

 Aspose.Cells API が[**追加**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)の方法[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection)コレクションにカスタム プロパティを追加するためのクラス。の[**追加**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)メソッドはプロパティを Excel ファイルに追加し、新しいドキュメント プロパティの参照を[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **「コンテンツへのリンク」カスタム プロパティの構成**

特定の範囲のコンテンツにリンクされたカスタム プロパティを作成するには、[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent)メソッドとパスのプロパティ名とソース。を使用して、プロパティがコンテンツにリンクされているように構成されているかどうかを確認できます。[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent)財産。さらに、以下を使用してソース範囲を取得することもできます。[**ソース**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source)のプロパティ[**ドキュメント プロパティ**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラス。

この例では、単純なテンプレート Microsoft Excel ファイルを使用します。ワークブックには、ラベルが付けられた定義済みの名前付き範囲があります**マイレンジ**これはセル値を参照します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **カスタム プロパティの削除**

Aspose.Cells を使用してカスタム プロパティを削除するには、[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)メソッドを呼び出して、削除するドキュメント プロパティの名前を渡します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **先行トピック**
- [ドキュメント情報パネル内に表示されるカスタム プロパティの追加](/cells/ja/net/adding-custom-properties-visible-inside-document-information-panel/)
- [組み込みドキュメント プロパティの ScaleCrop および LinksUpToDate プロパティの設定](/cells/ja/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [BuiltIn ドキュメント プロパティを使用して Excel ファイルのドキュメント バージョンを指定する](/cells/ja/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [BuiltIn ドキュメント プロパティを使用して Excel ファイルの言語を指定する](/cells/ja/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
