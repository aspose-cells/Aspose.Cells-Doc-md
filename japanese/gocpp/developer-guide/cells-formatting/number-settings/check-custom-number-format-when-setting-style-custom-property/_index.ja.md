---
title: GolangとC++を使用して、スタイルのカスタムプロパティ設定時にカスタム番号形式を確認
description: Aspose.Cellsは、スプレッドシートファイルに対する操作をサポートするC++ライブラリで、スタイリング時のカスタム番号形式の確認が可能です。この記事では、Aspose.Cellsライブラリを使用してカスタム番号形式を検証し、スタイリングの正確さを確保する方法を説明します。
keywords: Aspose.Cells、C++ライブラリ、スプレッドシート、スタイリング、カスタム番号フォーマット、検証、チェック
type: docs
weight: 170
url: /ja/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

無効なカスタム番号フォーマットを [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) プロパティに割り当てても、Aspose.Cellsは例外をスローしません。ただし、Aspose.Cellsが割り当てられたカスタム番号フォーマットの妥当性を確認すべき場合は、[**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) プロパティを **true**に設定してください。

## **スタイルのカスタムプロパティを設定する際のカスタム番号形式をチェック**

以下のサンプルコードは、無効なカスタム番号フォーマットを [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) プロパティに割り当てた例です。既に [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) プロパティを **true**に設定しているため、例外（例：無効な番号フォーマット）をスローします。詳細はコード内のコメントを参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
