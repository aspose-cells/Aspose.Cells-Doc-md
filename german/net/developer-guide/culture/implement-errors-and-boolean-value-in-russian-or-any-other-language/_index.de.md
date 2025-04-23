---
title: Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren
type: docs
weight: 40
url: /de/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Microsoft Excel in der russischen Sprachversion oder in einer anderen Sprachversion verwenden, werden Fehler und boolesche Werte entsprechend dieser Sprachversion oder Sprache angezeigt. Sie können ein ähnliches Verhalten mit Aspose.Cells erreichen, indem Sie die Eigenschaft [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) verwenden. Sie müssen die folgenden Methoden der Klasse [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) überschreiben.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementieren**

Der folgende Beispielcode veranschaulicht, wie Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementiert werden. Bitte überprüfen Sie die in diesem Code verwendete [Beispiel Excel-Datei](73990159.xlsx) und deren [Ausgabe-PDF](73990160.pdf). Der Screenshot zeigt den Unterschied zwischen der Beispiel-Excel-Datei und der Ausgabe-PDF zur Referenz.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
{{< app/cells/assistant language="csharp" >}}
