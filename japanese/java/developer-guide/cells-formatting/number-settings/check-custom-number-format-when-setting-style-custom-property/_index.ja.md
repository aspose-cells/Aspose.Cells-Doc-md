---
title: スタイル.Customプロパティを設定する際にカスタム番号書式をチェックする
type: docs
weight: 160
url: /ja/java/check-custom-number-format-when-setting-style-custom-property/
---

## **可能な使用シナリオ**

Aspose.Cellsに無効なカスタム番号書式を割り当てると、Aspose.Cellsは例外をスローしません。ただし、Aspose.Cellsが割り当てられたカスタム番号書式が有効かどうかをチェックする場合は、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)プロパティを**true**に設定してください。

## **Style.Customプロパティを設定する際のカスタム番号書式をチェックする**

次のサンプルコードでは、[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)プロパティを**true**に設定しているため、無効なカスタム番号書式を[**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)プロパティに割り当てます。そのため、APIはCellsException（無効な番号書式）をスローします。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
