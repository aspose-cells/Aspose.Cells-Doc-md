---
title: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
description: Aspose.Cellsはスプレッドシートファイルを操作するための.NETライブラリであり、スタイリング時にカスタム番号形式をチェックすることをサポートしています。この記事では、Aspose.Cellsライブラリを使用してカスタム番号形式をチェックする方法を説明します。
keywords: Aspose.Cells, .NETライブラリ, スプレッドシート, スタイリング, カスタム番号形式, チェック, 検証
type: docs
weight: 170
url: /ja/net/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)プロパティに無効なカスタム番号形式を割り当てた場合、Aspose.Cellsは例外をスローしません。ただし、Aspose.Cellsに割り当てたカスタム番号形式が有効かどうかをチェックする場合は、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)プロパティを**true**に設定してください。

## **スタイルのカスタムプロパティを設定する際のカスタム番号形式をチェック**

次のサンプルコードは、[**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)プロパティに無効なカスタム番号形式を割り当てます。すでに[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)プロパティを**true**に設定しているため、例外（無効な番号形式など）がスローされます。詳細についてはコード内のコメントをお読みください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
