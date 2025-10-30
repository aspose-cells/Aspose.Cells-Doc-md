---
title: Russianやその他の言語でエラーとブール値をGolang経由のC++で実装する
linktitle: エラーとブール値の実装
type: docs
weight: 40
url: /ja/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aspose.Cellsを使ってC++経由のGolangでロシア語や他の言語でエラーとブール値を実装する方法を学ぶ。
---

## **可能な使用シナリオ**

Microsoft Excelをロシア語ロケールまたは言語やその他のロケール・言語で使用している場合、そのロケールや言語に従ったエラーとブール値が表示されます。Aspose.Cellsの[**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/)プロパティを使うことで、同様の動作を実現できます。これには、[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)クラスの以下のメソッドをオーバーライドする必要があります。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **ロシア語または他の言語でエラーおよび真偽値を実装する**

下記のサンプルコードは、ロシア語または他の言語でのエラーおよび真偽値の実装方法を説明しています。このコードで使用される [サンプルExcelファイル](73990159.xlsx) およびその [出力PDF](73990160.pdf) を確認してください。スクリーンショットは、サンプルExcelファイルと出力PDFの違いを参照用に示しています。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
