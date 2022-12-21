---
title: Style.Custom プロパティの設定時にカスタム数値形式を確認する
type: docs
weight: 160
url: /ja/java/check-custom-number-format-when-setting-style-custom-property/
---
## **考えられる使用シナリオ**

に無効なカスタム数値形式を割り当てた場合[**スタイル.カスタム**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)プロパティの場合、Aspose.Cells は例外をスローしません。ただし、Aspose.Cells が割り当てられたカスタム数値形式が有効かどうかを確認する必要がある場合は、次のように設定してください。[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)プロパティへ**真実**.

## **Style.Custom プロパティを設定するときは、カスタム数値形式を確認してください**

次のサンプル コードは、無効なカスタム数値形式を[**スタイル.カスタム**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)財産。すでに設定していますので、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)プロパティへ**真実**したがって、API は CellsException をスローします。*数値形式が無効です*.

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
