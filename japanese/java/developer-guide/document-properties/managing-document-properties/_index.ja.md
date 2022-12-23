---
title: ドキュメント プロパティの管理
type: docs
weight: 10
url: /ja/java/managing-document-properties/
---
## **序章**

Microsoft Excel には、スプレッドシート ファイルにプロパティを追加する機能があります。これらのドキュメント プロパティは有用な情報を提供し、以下に詳述するように 2 つのカテゴリに分けられます。

- システム定義 (組み込み) プロパティ: 組み込みプロパティには、ドキュメントのタイトル、作成者名、ドキュメントの統計など、ドキュメントに関する一般的な情報が含まれています。
- ユーザー定義 (カスタム) プロパティ: 名前と値のペアの形式でエンド ユーザーによって定義されたカスタム プロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタム プロパティについて知っておくべき最も重要な点は、組み込みプロパティにアクセスして変更することはできますが、作成または削除することはできませんが、カスタム ドキュメント プロパティは作成および管理できるということです。

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

 Aspose.Cells for Java は、出力ドキュメントに API とバージョン番号に関する情報を直接書き込みます。たとえば、Document を PDF にレンダリングすると、Aspose.Cells for Java が読み込まれます。**応用**値が「Aspose.Cells」のフィールドと**PDF プロデューサー** 'Aspose.Cells for Java v17.9' などの値を持つフィールド。

出力ドキュメントからこの情報を変更または削除するように Aspose.Cells for Java に指示することはできないことに注意してください。

{{% /alert %}}

### **ドキュメント プロパティへのアクセス**

Aspose.Cells API は、組み込みとカスタムの両方のタイプのドキュメント プロパティをサポートします。 Aspose.Cells'[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスは Excel ファイルを表し、Excel ファイルと同様に、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには複数のワークシートを含めることができ、それぞれが[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスで表されますが、ワークシートのコレクションは[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)クラス。

使用[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)以下で説明するように、ファイルのドキュメント プロパティにアクセスします。

- 組み込みのドキュメント プロパティにアクセスするには、次を使用します。[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- カスタム ドキュメント プロパティにアクセスするには、[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

両方の[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)と[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)のインスタンスを返す[**ドキュメント プロパティ コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection).このコレクションには[**ドキュメント プロパティ**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)各オブジェクトは、単一の組み込みまたはカスタム ドキュメント プロパティを表します。

プロパティにアクセスする方法は、アプリケーションの要件次第です。のプロパティのインデックスまたは名前を使用して[**ドキュメント プロパティ コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)以下の例に示すように。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

の[**ドキュメント プロパティ**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)クラスを使用すると、ドキュメント プロパティの名前、値、およびタイプを取得できます。

- プロパティ名を取得するには、次を使用します[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- プロパティ値を取得するには、次を使用します[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)値をオブジェクトとして返します。
- プロパティ タイプを取得するには、次を使用します。[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) .これは、[**プロパティタイプ**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)列挙値。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **カスタム ドキュメント プロパティの追加または削除**

このトピックの冒頭で説明したように、これらのプロパティはシステム定義であるため、開発者は組み込みプロパティを追加または削除できませんが、カスタム プロパティはユーザー定義であるため、追加または削除することができます。

### **カスタム プロパティの追加**

 Aspose.Cells API が[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) メソッド[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection)コレクションにカスタム プロパティを追加するためのクラス。の[**追加**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) メソッドはプロパティを Excel ファイルに追加し、新しいドキュメント プロパティの参照を[**ドキュメント プロパティ**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)物体。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **「コンテンツへのリンク」カスタム プロパティの構成**

特定の範囲のコンテンツにリンクされたカスタム プロパティを作成するには、[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) ) メソッドと、プロパティ名とソースを渡します。を使用して、プロパティがコンテンツにリンクされているように構成されているかどうかを確認できます。[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent)財産。さらに、以下を使用してソース範囲を取得することもできます。[**ソース**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source)のプロパティ[**ドキュメント プロパティ**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)クラス。

この例では、単純なテンプレート Microsoft Excel ファイルを使用します。ワークブックには、ラベルが付けられた定義済みの名前付き範囲があります**マイレンジ**これはセル値を参照します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **カスタム プロパティの削除**

Aspose.Cells を使用してカスタム プロパティを削除するには、[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) メソッドを呼び出して、削除するドキュメント プロパティの名前を渡します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
