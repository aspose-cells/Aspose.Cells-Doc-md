---
title: ロシア語またはその他の言語でエラーとブール値を実装する
type: docs
weight: 40
url: /ja/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **考えられる使用シナリオ**

ロシア語のロケールまたは言語、またはその他のロケールまたは言語で Microsoft Excel を使用している場合、そのロケールまたは言語に従ってエラーとブール値が表示されます。を使用して、Aspose.Cells を使用して同様の動作を実現できます。**[Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) プロパティ。次のメソッドをオーバーライドする必要があります[**グローバリゼーション設定**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)クラス。

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **ロシア語またはその他の言語でエラーとブール値を実装する**

次のサンプル コードは、ロシア語またはその他の言語でエラーとブール値を実装する方法を示しています。を確認してください[サンプル Excel ファイル](73990159.xlsx)このコードとその[出力 PDF](73990160.pdf).スクリーンショットは、参照用にサンプル Excel ファイルと出力 PDF の違いを示しています。

![todo:画像_代替_文章](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
