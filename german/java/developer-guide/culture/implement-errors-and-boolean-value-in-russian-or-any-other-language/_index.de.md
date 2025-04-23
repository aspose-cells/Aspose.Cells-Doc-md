---
title: Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren
type: docs
weight: 30
url: /de/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie Microsoft Excel in russischer oder einer anderen Sprache verwenden, werden Fehler- und boolesche Werte gemäß dieser Spracheinstellung angezeigt. Dieses Verhalten können Sie mit der Methode oder Eigenschaft [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) von Aspose.Cells nachahmen. Sie müssen die folgenden Methoden der Klasse [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) überschreiben.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString-java.lang.String-)
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString-boolean-)
## **Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren**
Der folgende Beispielcode veranschaulicht, wie Fehler und boolescher Wert in Russisch oder in einer anderen Sprache implementiert werden. Überprüfen Sie bitte die im Code verwendete [Beispiel-Excel-Datei](48496697.xlsx) und das generierte [Output-PDF](48496696.pdf). Der Screenshot zeigt den Unterschied zwischen der [Beispiel-Excel-Datei](48496697.xlsx) und dem [Output-PDF](48496696.pdf) für Referenzzwecke.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
{{< app/cells/assistant language="java" >}}
