---
title: Aspose.Cells 8.1.1 におけるパブリックAPIの変更
type: docs
weight: 50
url: /ja/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.1.0 から 8.1.1 への変更点について説明します。これは、モジュール/アプリケーション開発者に興味を持たれる可能性があります。新しいおよび更新された公開メソッドだけでなく、Aspose.Cells の内部動作に関する変更についても説明しています。

{{% /alert %}} 
## **HtmlSaveOptions.PresentationPreference プロパティを追加**
HtmlSaveOptions クラスで PresentationPreference プロパティが公開されており、スプレッドシートを HTML や MHTML にエクスポートする際にレイアウトをよりよくレンダリングするために使用できます。デフォルトの値は false です。true に設定すると、Aspose.Cells API はワークシートの内容をより良いプレゼンテーションでエクスポートします。

{{% alert color="primary" %}} 

[Use PresentationPreference Option for Better Layout](/cells/ja/net/excel-to-html-use-presentationpreference-option-for-better-layout/) の詳細な記事をご確認ください

{{% /alert %}}
## **ワークシートシナリオのサポートの追加**
シナリオは、一つまたは複数の式によってリンクされた可変入力セルからなるモデルのことです。Aspose.Cells API では、ユーザーがワークシートからシナリオを作成、操作、削除するためのクラスとともに Worksheet.Scenarios プロパティが公開されています。 

1. Scenario: 個々のシナリオを表します。
1. ScenarioCollection: シナリオのコレクションを表します。
1. ScenarioInputCellCollection: 特定のシナリオの入力セルのリストを表します。
1. ScenarioInputCell: 特定のシナリオの入力セルのコレクションからの入力セルを表します。

{{% alert color="primary" %}} 

[ワークシートからシナリオを作成、操作、削除する方法](/cells/ja/net/create-manipulate-or-remove-scenarios-from-worksheets/) の詳細な記事をご確認ください

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
