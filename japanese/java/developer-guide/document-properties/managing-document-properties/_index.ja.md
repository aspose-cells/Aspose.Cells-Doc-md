---
title: ドキュメントプロパティの管理
type: docs
weight: 10
url: /ja/java/managing-document-properties/
---

## **紹介**

Microsoft Excelはスプレッドシートファイルにプロパティを追加できる機能を提供します。これらのドキュメントプロパティは有用な情報を提供し、以下のように2つのカテゴリに分かれています。

- システム定義（組み込み）プロパティ: 組み込みプロパティには文書のタイトル、作成者名、文書の統計などの一般的な情報が含まれています。
- ユーザー定義（カスタム）プロパティ: ユーザーが名前-値のペアの形式で定義したカスタムプロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタムドキュメントプロパティに関して最も重要なポイントは、組み込みプロパティはアクセスおよび変更はできますが、作成や削除はできないということですが、カスタムドキュメントプロパティは作成および管理が可能です。

{{% /alert %}}

## **Microsoft Excel を使用したドキュメントプロパティの管理**

Microsoft Excel では、Excel ファイルのドキュメントプロパティを WYSIWYG の方法で管理することができます。Excel 2016 では、以下の手順に従って **プロパティ** ダイアログを開くことができます。

1. **ファイル**メニューから**情報**を選択します。

|**情報メニューを選択**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. **プロパティ**の見出しをクリックし、「詳細プロパティ」を選択します。

|**詳細プロパティの選択をクリック**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. ファイルのドキュメントプロパティを管理します。

|**プロパティダイアログ**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
プロパティダイアログでは、一般、概要、統計、内容、カスタムのような異なるタブがあります。各タブはファイルに関連する異なる種類の情報を設定するのに役立ちます。カスタムタブはカスタムプロパティを管理するために使用されます。

## **Aspose.Cells を使用したドキュメントプロパティの操作**

開発者はAspose.CellsのAPIを使用してドキュメントプロパティを動的に管理できます。この機能により、ファイルが受信された時点、処理された時点、タイムスタンプなどの有用な情報をファイルと一緒に保存できます。

{{% alert color="primary" %}}

Aspose.Cells for Java は、出力ドキュメントに API およびバージョン番号の情報を直接書き込みます。たとえば、ドキュメントを PDF にレンダリングすると、Aspose.Cells for Java は **Application** フィールドに 'Aspose.Cells' という値、**PDF Producer** フィールドには 'Aspose.Cells for Java v17.9' などの値を記入します。

この情報を出力ドキュメントから変更または削除するようにAspose.Cells for Javaに指示することはできません。

{{% /alert %}}

### **ドキュメントプロパティにアクセスする**

Aspose.CellsのAPIは組み込みプロパティとカスタムプロパティの両方をサポートしています。Aspose.Cellsの[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスはExcelファイルを表し、Excelファイルと同様に[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスは複数のワークシートを含むことができ、各ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスによって表されます。ワークシートのコレクションは[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)クラスによって表されます。

以下に示すように、[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)を使用してファイルのドキュメントプロパティにアクセスします。

- 組み込みドキュメントプロパティにアクセスするには、[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)を使用します。
- カスタムドキュメントプロパティにアクセスするには、[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)を使用します。

[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties)と[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties)の両方が[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)のインスタンスを返します。このコレクションには、[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)オブジェクトが含まれており、それぞれが単一の組み込みまたはカスタムドキュメントプロパティを表します。

プロパティへのアクセス方法はアプリケーションの要件によって異なります。つまり、[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)からのプロパティの名前またはインデックスを使用するか、以下の例に示すようにします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)クラスでは、ドキュメントのプロパティの名前、値、および型を取得することができます。

- プロパティ名を取得するには[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name)を使用します。
- プロパティの値を取得するには[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)を使用します。[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)は値をオブジェクトとして返します。
- プロパティのタイプを取得するには、[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type)を使用します。これにより[**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)の列挙値の1つが返されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **カスタムドキュメントプロパティの追加または削除**

このトピックの冒頭で既に説明した通り、ビルトインプロパティはシステム定義されたものであり、開発者は追加または削除することはできませんが、ユーザー定義のカスタムプロパティを追加または削除することは可能です。

### **カスタムプロパティの追加**

Aspose.Cells APIでは、[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection)クラスにカスタムプロパティを追加するための[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean))メソッドが公開されており、[**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean))メソッドはExcelファイルにプロパティを追加し、新しいドキュメントプロパティの参照として[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)オブジェクトを返します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **「コンテンツにリンク」カスタムプロパティの構成**

特定の範囲のコンテンツにリンクされたカスタムプロパティを作成するには、[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String))メソッドを呼び出してプロパティ名とソースを渡します。 プロパティがコンテンツにリンクされているかどうかを確認するには[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent)プロパティを使用できます。 また、[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)クラスの[**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source)プロパティを使用してソース範囲を取得することも可能です。

この例では、シンプルなテンプレートのMicrosoft Excelファイルを使用します。 ワークブックには、**MyRange**と表記された名前付き範囲があり、セルの値を参照しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **カスタムプロパティの削除**

Aspose.Cellsを使用してカスタムプロパティを削除するには、[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String))メソッドを呼び出して削除するドキュメントプロパティの名前を渡します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
