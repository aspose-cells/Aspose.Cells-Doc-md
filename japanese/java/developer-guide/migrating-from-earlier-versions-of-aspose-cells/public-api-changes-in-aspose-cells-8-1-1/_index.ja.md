---
title: Aspose.Cells 8.1.1 におけるパブリックAPIの変更
type: docs
weight: 60
url: /ja/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.1.0から8.1.1へのAPIの変更について、モジュールおよびアプリケーション開発者に関心がある可能性のあるものについて説明しています。[新しいおよび更新されたパブリックメソッド](/cells/ja/java/public-api-changes-in-aspose-cells-8-1-1/)だけでなく、Aspose.Cellsの仕様の変更についての説明も含まれています。

{{% /alert %}} 
## **プロパティと機能の追加**
### **HtmlSaveOptions.PresentationPreferenceプロパティの追加**
HtmlSaveOptionsクラスはPresentationPreferenceプロパティのgetter/setterを公開しており、スプレッドシートをHTMLやMHTML形式にエクスポートする際にレイアウトを改善して結果をレンダリングするために使用できます。デフォルト値はfalseです。trueに設定すると、Aspose.Cells APIはワークシートの内容をより良いプレゼンテーションでエクスポートします。

{{% alert color="primary" %}} 

[レイアウトを改善するためにPresentationPreferenceオプションを使用](/cells/ja/java/excel-to-html-use-presentationpreference-option-for-better-layout/)の詳細記事をご覧ください

{{% /alert %}} 
### **ワークシートシナリオのサポートの追加**
シナリオは、1つ以上の数式でリンクされた変数入力セルを含む仮想モデルです。Aspose.CellsはWorksheet.Scenariosプロパティのgetterとsetterを公開し、開発者がシナリオを作成、操作、および削除するのを助けるために次のクラスを提供しています。

1. Scenario: 個々のシナリオを表します。
1. ScenarioCollection: シナリオのコレクションを表します。
1. ScenarioInputCellCollection: 特定のシナリオに対する入力セルのリストを表します。
1. ScenarioInputCell: 特定のシナリオの入力セルを表します。

{{% alert color="primary" %}} 

[ワークシートからシナリオを作成、操作、または削除する方法](/cells/ja/java/create-manipulate-or-remove-scenarios-from-worksheets/)の詳細記事をご覧ください。

{{% /alert %}}
## **CellsExceptionの動作の変更**
以前のリリースのAspose.Cells for Java APIでは、破損している可能性のあるスプレッドシートをWorkbookのインスタンスにロードすると、APIは問題がどこにあるかを指摘せずに一般的なメッセージをスローしていました。8.1.1では、テンプレートファイルの読み込み時にどこ（どのセル）で何（式の式）が例外を引き起こすかを指摘する意味のあるメッセージとともに例外をスローするようにこの動作を変更しました。
