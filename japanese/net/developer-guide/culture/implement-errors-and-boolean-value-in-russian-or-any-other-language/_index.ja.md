---
title: ロシア語または他の言語でエラーおよび真偽値を実装する
type: docs
weight: 40
url: /ja/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **可能な使用シナリオ**

Microsoft Excel をロシア語のロケールまたは言語、または他のロケールまたは言語で使用している場合、そのロケールまたは言語に従ってエラーおよび真偽値が表示されます。 Aspose.Cells を使用して、[**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)プロパティを使用することで同様の動作を実現できます。[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラスの以下のメソッドをオーバーライドする必要があります。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **ロシア語または他の言語でエラーおよび真偽値を実装する**

下記のサンプルコードは、ロシア語または他の言語でのエラーおよび真偽値の実装方法を説明しています。このコードで使用される [サンプルExcelファイル](73990159.xlsx) およびその [出力PDF](73990160.pdf) を確認してください。スクリーンショットは、サンプルExcelファイルと出力PDFの違いを参照用に示しています。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
