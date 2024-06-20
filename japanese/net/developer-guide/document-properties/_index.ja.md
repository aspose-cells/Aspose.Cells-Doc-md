---
title: ドキュメントプロパティを管理する
linktitle: ドキュメントプロパティ
type: docs
weight: 80
url: /ja/net/managing-document-properties/
description: Aspose.Cells for NETのAPIを使用してドキュメントプロパティの管理方法を学ぶ。
keywords: C#でドキュメントプロパティの管理方法、Aspose.Cells for NETのAPIを使用してドキュメントプロパティの取得または設定、C#を使用してドキュメントプロパティの追加または削除、C#を使用してドキュメントプロパティの挿入または削除、Aspose.Cells for NETのAPIを使用してドキュメントプロパティにアクセスする方法。
---


## **紹介**

Microsoft Excelはスプレッドシートファイルにプロパティを追加できる機能を提供します。これらのドキュメントプロパティは有用な情報を提供し、以下のように2つのカテゴリに分かれています。

- システム定義（組み込み）プロパティ: 組み込みプロパティには文書のタイトル、作成者名、文書の統計などの一般的な情報が含まれています。
- ユーザー定義（カスタム）プロパティ: ユーザーが名前-値のペアの形式で定義したカスタムプロパティ。

{{% alert color="primary" %}}

組み込みプロパティとカスタムプロパティについて知っておくべき最も重要な点は、組み込みプロパティはアクセスおよび変更が可能ですが、作成または削除はできないということです。一方、カスタムプロパティは作成および管理が可能です。

{{% /alert %}}

## **Microsoft Excelを使用してドキュメントプロパティを管理する方法**

Microsoft Excelを使用してExcelファイルのドキュメントプロパティをWYSIWYG形式で管理できます。以下の手順に従ってExcel 2016で**プロパティ**ダイアログを開いてください。

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

## **Aspose.Cellsを使用してドキュメントプロパティを操作する方法**

開発者はAspose.CellsのAPIを使用してドキュメントプロパティを動的に管理できます。この機能により、ファイルが受信された時点、処理された時点、タイムスタンプなどの有用な情報をファイルと一緒に保存できます。

{{% alert color="primary" %}}

Aspose.Cells for .NETは、出力ドキュメントにAPIおよびバージョン番号に関する情報を直接書き込みます。たとえば、ドキュメントをPDFにレンダリングすると、「アプリケーション」フィールドに'Aspose.Cells'という値、また「PDFプロデューサー」フィールドに'Aspose.Cells v17.9'などの値が設定されます。

ただし、Aspose.Cells for .NETに対してこの情報を出力ドキュメントから変更または削除するよう指示することはできません。

{{% /alert %}}

### **ドキュメントプロパティにアクセスする方法**

Aspose.CellsのAPIは組み込みプロパティとカスタムプロパティの両方をサポートしています。Aspose.Cellsの[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスはExcelファイルを表し、Excelファイルと同様に[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスは複数のワークシートを含むことができ、各ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスによって表されます。ワークシートのコレクションは[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)クラスによって表されます。

以下に示すように、[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)を使用してファイルのドキュメントプロパティにアクセスします。

- 組み込みドキュメントプロパティにアクセスするには、[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)を使用します。
- カスタムドキュメントのプロパティにアクセスするには[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)を使用します。

[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties)と[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties)の両方が[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)のインスタンスを返します。 このコレクションには[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)を含むオブジェクトが含まれており、それぞれが単一のビルトインまたはカスタムドキュメントプロパティを表します。

プロパティへのアクセス方法はアプリケーションの要件によって異なります。つまり、[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)からのプロパティの名前またはインデックスを使用するか、以下の例に示すようにします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスでは、ドキュメントのプロパティの名前、値、および型を取得することができます。

- プロパティ名を取得するには[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name)を使用します。
- プロパティの値を取得するには[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)を使用します。[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)は値をオブジェクトとして返します。
- プロパティの型を取得するには[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type)を使用します。 これにより、[**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)の列挙型の値のいずれかが返されます。 プロパティの型を取得した後は、[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)を使用せずに適切な型の値を取得するために**DocumentProperty.ToXXX**メソッドのいずれかを使用します。 **DocumentProperty.ToXXX**メソッドについては、以下の表に説明があります。

{{% alert color="primary" %}}

[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスは、他のデータ型の値を返す一連のメソッドも提供しています。

{{% /alert %}}

|**メンバー名**|**説明**|**ToXXXメソッド**|
| :- | :- | :- |
|Boolean|プロパティのデータ型はブールです|ToBool|
|Date|プロパティのデータ型は日時です。Microsoft Excelでは日付部分のみが保存され、時刻は保存されません。|ToDateTime|
|Float|プロパティのデータ型はダブルです|ToDouble|
|Number|プロパティのデータ型はInt32です|ToInt|
|String|プロパティのデータ型は文字列です|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **カスタムドキュメントプロパティの追加または削除方法**

このトピックの冒頭で既に説明した通り、ビルトインプロパティはシステム定義されたものであり、開発者は追加または削除することはできませんが、ユーザー定義のカスタムプロパティを追加または削除することは可能です。

### **カスタムプロパティの追加方法**

Aspose.Cells APIでは、カスタムプロパティをコレクションに追加するために、[**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)クラスの[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection)メソッドが公開されています。[**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)メソッドは、プロパティをExcelファイルに追加して新しいドキュメントプロパティの参照を[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)オブジェクトとして返します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **「コンテンツにリンク」カスタムプロパティの構成方法**

特定の範囲のコンテンツにリンクされたカスタムプロパティを作成するには、[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent)メソッドを呼び出してプロパティ名とソースを渡します。 プロパティがコンテンツにリンクされているかどうかを確認するには[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent)プロパティを使用できます。 また、[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)クラスの[**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source)プロパティを使用してソース範囲を取得することも可能です。

この例では、シンプルなテンプレートのMicrosoft Excelファイルを使用します。 ワークブックには、**MyRange**と表記された名前付き範囲があり、セルの値を参照しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **カスタムプロパティを削除する方法**

Aspose.Cellsを使用してカスタムプロパティを削除するには、[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)メソッドを呼び出して削除するドキュメントプロパティの名前を渡します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **高度なトピック**
- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/net/adding-custom-properties-visible-inside-document-information-panel/)
- [ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する](/cells/ja/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する](/cells/ja/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する](/cells/ja/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
