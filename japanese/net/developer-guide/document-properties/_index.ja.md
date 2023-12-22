---
title: ドキュメントのプロパティの管理
linktitle: ドキュメントのプロパティ
type: docs
weight: 80
url: /ja/net/managing-document-properties/
description: NET API の Aspose.Cells を使用してドキュメント プロパティを管理する方法を学習します。
keywords: How to Manage Document Properties in C#, Get or Set Document Properties using C#, Add or Delete Document Properties via C#, Insert or Remove Document Properties with C#, How to Access Document Properties using Aspose.Cells for NET APIs.
---
##  **導入**

Microsoft Excel には、スプレッドシート ファイルにプロパティを追加する機能が用意されています。これらのドキュメント プロパティは有用な情報を提供し、以下で詳しく説明するように 2 つのカテゴリに分類されます。

- システム定義 (組み込み) プロパティ: 組み込みプロパティには、文書タイトル、作成者名、文書統計などの文書に関する一般情報が含まれています。
- ユーザー定義 (カスタム) プロパティ: エンド ユーザーによって名前と値のペアの形式で定義されたカスタム プロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタム プロパティについて知っておくべき最も重要な点は、組み込みプロパティはアクセスして変更することはできますが、作成したり削除したりすることはできないということです。ただし、カスタム プロパティを作成および管理することはできます。

{{% /alert %}}

##  **Microsoft Excel を使用してドキュメントのプロパティを管理する方法**

Microsoft Excel では、Excel ファイルのドキュメント プロパティを WYSIWYG 方式で管理できます。以下の手順に従って開いてください。**プロパティ**Excel 2016 のダイアログ。

1. から**ファイル**メニューで、*情報**を選択します。

|**情報メニューの選択**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. クリック**プロパティ**見出しをクリックして「詳細プロパティ」を選択します。

|**「詳細プロパティの選択」をクリックする**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. ファイルのドキュメント プロパティを管理します。

|**プロパティダイアログ**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
「プロパティ」ダイアログには、「一般」、「概要」、「統計」、「コンテンツ」、「カスタム」などのさまざまなタブがあります。各タブは、ファイルに関連するさまざまな種類の情報を構成するのに役立ちます。 [カスタム] タブは、カスタム プロパティを管理するために使用されます。

##  **Aspose.Cells を使用してドキュメントのプロパティを操作する方法**

開発者は、Aspose.Cells API を使用してドキュメントのプロパティを動的に管理できます。この機能は、開発者がファイルの受信、処理、タイムスタンプの日付などの有用な情報をファイルとともに保存するのに役立ちます。

{{% alert color="primary" %}}

 Aspose.Cells for .NET は、API とバージョン番号に関する情報を出力ドキュメントに直接書き込みます。たとえば、Document を PDF にレンダリングすると、Aspose.Cells for .NET が設定されます。**応用**値「Aspose.Cells」を持つフィールドと**PDF プロデューサー**フィールドに値を入力します（例：「Aspose.Cells v17.9」）。

Aspose.Cells for .NET に対して、出力ドキュメントからこの情報を変更または削除するように指示することはできないことに注意してください。

{{% /alert %}}

###  **ドキュメントのプロパティにアクセスする方法**

Aspose.Cells API は、組み込みとカスタムの両方のタイプのドキュメント プロパティをサポートします。 Aspose.Cells'[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスは Excel ファイルを表し、Excel ファイルと同様に、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには複数のワークシートを含めることができ、それぞれのワークシートは[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表現されるのに対し、ワークシートのコレクションは[**ワークシートコレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラス。

使用[**ワークシートコレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)以下で説明するように、ファイルのドキュメント プロパティにアクセスします。

- 組み込みのドキュメント プロパティにアクセスするには、次を使用します。[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- カスタム ドキュメント プロパティにアクセスするには、次を使用します。[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

どちらも[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)そして[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)のインスタンスを返します[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)。このコレクションには以下が含まれます[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)オブジェクト。それぞれが単一の組み込みまたはカスタムのドキュメント プロパティを表します。

プロパティにアクセスする方法はアプリケーションの要件次第です。のプロパティのインデックスまたは名前を使用して、[**ドキュメントプロパティコレクション**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)以下の例で示すように。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

の[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスを使用すると、ドキュメント プロパティの名前、値、タイプを取得できます。

- プロパティ名を取得するには、次を使用します。[**ドキュメントプロパティ名**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- プロパティ値を取得するには、次を使用します。[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)値をオブジェクトとして返します。
- プロパティのタイプを取得するには、次を使用します。[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) 。これは、次のいずれかを返します。[**プロパティタイプ**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)列挙値。プロパティ タイプを取得したら、次のいずれかを使用します。**DocumentProperty.ToXXX**を使用する代わりに適切な型の値を取得するメソッド[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)。の**DocumentProperty.ToXXX**方法については、以下の表で説明します。

{{% alert color="primary" %}}

の[**ドキュメントプロパティ**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスは、他のデータ型の値を返す一連のメソッドも提供します。

{{% /alert %}}

|**メンバー名**|**説明**|**ToXXXメソッド**|
| :- | :- | :- |
|ブール値|プロパティのデータ型はブール型です|トブール|
|日付|プロパティのデータ型は DateTime です。 Microsoft Excel ストアのみに注意してください<br>日付部分、このタイプのカスタム プロパティには時間を保存できません|終了日時|
|浮く|プロパティのデータ型は Double です|ダブルに|
|番号|プロパティのデータ型は Int32 です|ToInt|
|String|プロパティのデータ型は文字列です|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

###  **カスタムドキュメントプロパティを追加または削除する方法**

このトピックの冒頭で説明したように、組み込みプロパティはシステム定義であるため開発者は追加または削除できませんが、カスタム プロパティはユーザー定義であるため追加または削除できます。

###  **カスタム プロパティを追加する方法**

 Aspose.Cells API により、[**追加**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)の方法[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection)クラスを使用してカスタム プロパティをコレクションに追加します。の[**追加**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)メソッドはプロパティを Excel ファイルに追加し、新しいドキュメント プロパティの参照を[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

###  **「コンテンツへのリンク」カスタムプロパティを設定する方法**

特定の範囲のコンテンツにリンクされたカスタム プロパティを作成するには、[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent)メソッドを作成し、プロパティ名とソースを渡します。プロパティがコンテンツにリンクされるように構成されているかどうかを確認するには、[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent)財産。さらに、次を使用してソース範囲を取得することもできます。[**ソース**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source)の財産[**ドキュメントプロパティ**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラス。

この例では、単純なテンプレート Microsoft Excel ファイルを使用します。ワークブックには、ラベル付きの名前付き範囲が定義されています。**マイレンジ**これはセル値を参照します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

###  **カスタム プロパティを削除する方法**

Aspose.Cells を使用してカスタム プロパティを削除するには、[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)メソッドを使用して、削除するドキュメント プロパティの名前を渡します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

##  **アドバンストトピック**
- [ドキュメント情報パネル内に表示されるカスタム プロパティの追加](/cells/ja/net/adding-custom-properties-visible-inside-document-information-panel/)
- [組み込みドキュメント プロパティの ScaleCrop プロパティと LinksUpToDate プロパティの設定](/cells/ja/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [組み込みドキュメント プロパティを使用して Excel ファイルのドキュメント バージョンを指定する](/cells/ja/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [組み込みドキュメント プロパティを使用して Excel ファイルの言語を指定する](/cells/ja/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
