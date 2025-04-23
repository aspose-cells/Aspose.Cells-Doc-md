---
title: ロシア語または他の言語でエラーおよび真偽値を実装する
type: docs
weight: 30
url: /ja/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **可能な使用シナリオ**
Microsoft Excelをロシア語のロケールまたは言語、または他のロケールまたは言語で使用している場合、そのロケールまたは言語に応じてエラーと真偽値が表示されます。同様の動作を実現するには、Aspose.Cellsの[Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)メソッドまたはプロパティを使用する必要があります。[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)クラスの以下のメソッドをオーバーライドする必要があります。

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString-java.lang.String-)
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString-boolean-)
## **ロシア語または他の言語でエラーおよび真偽値を実装する**
以下のサンプルコードは、ロシア語または他の言語でエラーと真偽値を実装する方法を示しています。このコードで使用されているサンプルExcelファイルと出力されたPDFを確認してください。スクリーンショットは、[サンプルExcelファイル](48496697.xlsx) と [出力PDF](48496696.pdf) の違いを示しています。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
{{< app/cells/assistant language="java" >}}
