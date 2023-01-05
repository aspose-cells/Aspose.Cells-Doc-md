---
title: Style.Custom プロパティの設定時にカスタム数値形式を確認する
type: docs
weight: 170
url: /ja/net/check-custom-number-format-when-setting-style-custom-property/
---
## **考えられる使用シナリオ**

に無効なカスタム数値形式を割り当てた場合[**スタイル.カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)プロパティの場合、Aspose.Cells は例外をスローしません。ただし、Aspose.Cells が割り当てられたカスタム数値形式が有効かどうかを確認する必要がある場合は、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)プロパティへ**真実**.

## **Style.Custom プロパティを設定するときは、カスタム数値形式を確認してください**

次のサンプル コードは、無効なカスタム数値形式を[**スタイル.カスタム**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)財産。以来、私たちはすでに設定しています[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat)プロパティへ**真実**、したがって、無効な数値形式などの例外がスローされます。詳細については、コード内のコメントをお読みください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
