---
title: Style.Custom プロパティを設定するときにカスタム数値形式を確認する
description: Aspose.Cells は、スプレッドシート ファイルを操作するための .NET ライブラリで、スタイル設定時のカスタム数値形式のチェックをサポートします。この記事では、Aspose.Cells ライブラリを使用してカスタム数値形式をチェックし、スタイルが正しいことを確認する方法を説明します。
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /ja/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **考えられる使用シナリオ**

無効なカスタム数値形式を割り当てた場合[**スタイル.カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)プロパティを指定すると、Aspose.Cells は例外をスローしません。ただし、Aspose.Cells で割り当てられたカスタム番号形式が有効かどうかを確認したい場合は、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)プロパティを *true** に設定します。

##  **Style.Custom プロパティを設定するときにカスタム数値形式をチェックする**

次のサンプル コードは、無効なカスタム数値形式を[**スタイル.カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)財産。すでに設定されているため、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)プロパティを *true** に設定すると、例外がスローされます (例: 無効な数値形式)。詳細については、コード内のコメントをお読みください。

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
