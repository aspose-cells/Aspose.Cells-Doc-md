---
title: Implementieren Sie Fehler und boolesche Werte in Russisch oder einer anderen Sprache
type: docs
weight: 30
url: /de/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Mögliche Nutzungsszenarien**
 Wenn Sie Microsoft Excel in russischem Gebietsschema oder Sprache oder einem anderen Gebietsschema oder einer anderen Sprache verwenden, werden Fehler und boolesche Werte entsprechend diesem Gebietsschema oder dieser Sprache angezeigt. Sie können ein ähnliches Verhalten erreichen, indem Sie Aspose.Cells verwenden[Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) Methode oder Eigenschaft. Sie müssen die folgenden Methoden von überschreiben[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)Klasse.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Implementieren Sie Fehler und boolesche Werte in Russisch oder einer anderen Sprache**
 Der folgende Beispielcode veranschaulicht, wie Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementiert werden. Bitte überprüfen Sie die in diesem Code verwendete Beispiel-Excel-Datei und das Ausgabe-PDF. Der Screenshot zeigt den Unterschied zwischen[Beispiel-Excel-Datei](48496697.xlsx) und die[PDF ausgeben](48496696.pdf) für eine Referenz.

![todo: Bild_alt_Text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
