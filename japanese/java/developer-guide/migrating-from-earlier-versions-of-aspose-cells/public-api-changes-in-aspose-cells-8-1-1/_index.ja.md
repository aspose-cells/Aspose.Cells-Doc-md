---
title: パブリック API Aspose.Cells 8.1.1 の変更点
type: docs
weight: 60
url: /ja/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.1.0 から 8.1.1 への Aspose.Cells API の変更点について説明します。これは、モジュールおよびアプリケーションの開発者にとって興味深いものです。だけでなく、[新規および更新されたパブリック メソッド](/cells/ja/java/public-api-changes-in-aspose-cells-8-1-1/)だけでなく、任意の説明[行動の変化](/cells/ja/java/public-api-changes-in-aspose-cells-8-1-1/)Aspose.Cellsの舞台裏。

{{% /alert %}} 
## **追加されたプロパティと機能**
### **HtmlSaveOptions.PresentationPreference プロパティを追加しました**
HtmlSaveOptions クラスには、スプレッドシートを HTML または MHTML にエクスポートするときに、より良いレイアウトで結果をレンダリングするために使用できる PresentationPreference プロパティの getter/setter が公開されています。デフォルト値は false です。一方、true に設定すると、Aspose.Cells API はワークシートの内容をより適切なプレゼンテーションでエクスポートします。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[レイアウトを改善するために PresentationPreference オプションを使用する](/cells/ja/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **ワークシート シナリオの追加サポート**
シナリオとは、1 つ以上の数式でリンクされた変数入力セルを含む what-if モデルです。 Aspose.Cells は、Worksheet.Scenarios プロパティの getter と setter を次のクラスと共に公開して、開発者がシナリオを作成、操作、および削除できるようにしました。

1. シナリオ: 個々のシナリオを表します。
1. ScenarioCollection: シナリオのコレクションを表します。
1. ScenarioInputCellCollection: 特定のシナリオの入力セルのリストを表します。
1. ScenarioInputCell: 特定のシナリオの入力セルのコレクションからの入力セルを表します。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[ワークシートからシナリオを作成、操作、または削除する方法](/cells/ja/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **CellsException の動作の変更**
Aspose.Cells for Java API の以前のリリースでは、破損している可能性のあるスプレッドシートが Workbook のインスタンスに読み込まれると、API は、問題がどこにあるかを言及せずに一般的なメッセージをスローする傾向がありました。 8.1.1 ではこの動作を変更して、API が例外をスローし、テンプレート ファイルの読み取り時にどこ (どのセル) と何が (数式) が例外を引き起こすかを示す意味のあるメッセージをスローするようにしました。
