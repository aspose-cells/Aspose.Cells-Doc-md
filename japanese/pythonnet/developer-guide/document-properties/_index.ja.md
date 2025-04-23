---
title: ドキュメントプロパティを管理する
linktitle: ドキュメントプロパティ
type: docs
weight: 80
url: /ja/python-net/managing-document-properties/
description: Aspose.Cells for Python via .NET APIを通じてドキュメントプロパティを管理する方法について学びましょう。
keywords: C#でのドキュメントプロパティの管理方法、C#を使ったドキュメントプロパティの取得・設定方法、C#でのドキュメントプロパティの追加・削除方法、C#でのドキュメントプロパティへのアクセス方法、Aspose.Cells for Python via .NET APIを使用したドキュメントプロパティへのアクセス。
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

開発者はAspose.Cells for Python via .NET APIを使用して動的にドキュメントプロパティを管理できます。この機能により、ファイルの受領日時や処理日時、タイムスタンプなどの有用な情報をファイルとともに保存できます。

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、APIとバージョン番号の情報を出力ドキュメントに直接書き込みます。例えば、ドキュメントをPDFにレンダリングするとき、Aspose.Cells for Python via .NETは**Application**フィールドに「Aspose.Cells」を、**PDF Producer**フィールドに「Aspose.Cells for Python via .NET v17.9」などの値を設定します。

この情報を出力ドキュメントから変更または削除するようAspose.Cells for Python via .NETに指示することはできません。

{{% /alert %}}


### **カスタムドキュメントプロパティの追加または削除方法**

このトピックの冒頭で既に説明した通り、ビルトインプロパティはシステム定義されたものであり、開発者は追加または削除することはできませんが、ユーザー定義のカスタムプロパティを追加または削除することは可能です。

### **カスタムプロパティの追加方法**

Aspose.Cells for Python via .NET APIは、コレクションにカスタムプロパティを追加するための[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add)メソッドを[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection)クラスに提供しています。[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add)メソッドはプロパティをExcelファイルに追加し、新しいドキュメントプロパティの参照を[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty)オブジェクトとして返します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **高度なトピック**
- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する](/cells/ja/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する](/cells/ja/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する](/cells/ja/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

