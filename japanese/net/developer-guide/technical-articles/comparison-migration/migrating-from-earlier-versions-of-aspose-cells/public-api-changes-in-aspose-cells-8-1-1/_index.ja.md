---
title: パブリック API Aspose.Cells 8.1.1 の変更点
type: docs
weight: 50
url: /ja/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.1.0 から 8.1.1 への Aspose.Cells API の変更点について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **HtmlSaveOptions.PresentationPreference プロパティを追加**
HtmlSaveOptions クラスには、スプレッドシートを HTML または MHTML にエクスポートするときに、より良いレイアウトで結果をレンダリングするために使用できる PresentationPreference プロパティが公開されています。デフォルト値は false です。一方、true に設定すると、Aspose.Cells API はワークシートの内容をより適切なプレゼンテーションでエクスポートします。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[レイアウトを改善するために PresentationPreference オプションを使用する](/cells/ja/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **ワークシート シナリオの追加サポート**
シナリオは、1 つ以上の式によって相互にリンクされた可変入力セルを含む what-if モデルと呼ばれます。 Aspose.Cells API は、ユーザーがワークシートからシナリオを作成、操作、および削除するのを容易にするために、次のクラスとともに Worksheet.Scenarios プロパティを公開しました。

1. シナリオ: 個々のシナリオを表します。
1. ScenarioCollection: シナリオのコレクションを表します。
1. ScenarioInputCellCollection: 特定のシナリオの入力セルのリストを表します。
1. ScenarioInputCell: 特定のシナリオの入力セルのコレクションからの入力セルを表します。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[ワークシートからシナリオを作成、操作、または削除する方法](/cells/ja/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
