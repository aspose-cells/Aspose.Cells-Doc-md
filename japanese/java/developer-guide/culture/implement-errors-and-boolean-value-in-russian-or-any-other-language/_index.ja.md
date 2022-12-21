---
title: ロシア語またはその他の言語でエラーとブール値を実装する
type: docs
weight: 30
url: /ja/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **考えられる使用シナリオ**
ロシア語のロケールまたは言語、またはその他のロケールまたは言語で Microsoft Excel を使用している場合、そのロケールまたは言語に従ってエラーとブール値が表示されます。 Aspose.Cells を使用して同様の動作を実現できます[Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)メソッドまたはプロパティ。次のメソッドをオーバーライドする必要があります[グローバリゼーション設定](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)クラス。

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **ロシア語またはその他の言語でエラーとブール値を実装する**
次のサンプル コードは、ロシア語またはその他の言語でエラーとブール値を実装する方法を示しています。このコードで使用されているサンプル Excel ファイルとその出力 PDF を確認してください。スクリーンショットは、[サンプル Excel ファイル](48496697.xlsx)そしてその[PDF出力](48496696.pdf)参考までに。

![todo:画像_代替_文章](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
