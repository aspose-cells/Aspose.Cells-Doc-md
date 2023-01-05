---
title: Implementieren Sie Fehler und boolesche Werte in Russisch oder einer anderen Sprache
type: docs
weight: 40
url: /de/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie Microsoft Excel in russischem Gebietsschema oder Sprache oder einem anderen Gebietsschema oder einer anderen Sprache verwenden, werden Fehler und boolesche Werte entsprechend diesem Gebietsschema oder dieser Sprache angezeigt. Sie können ein ähnliches Verhalten mit Aspose.Cells erreichen, indem Sie die verwenden**[Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)-Eigenschaft. Sie müssen die folgenden Methoden von überschreiben[**Globalisierungseinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)Klasse.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Implementieren Sie Fehler und boolesche Werte in Russisch oder einer anderen Sprache**

 Der folgende Beispielcode veranschaulicht, wie Fehler und boolesche Werte in Russisch oder einer anderen Sprache implementiert werden. Bitte überprüfen Sie die[Beispiel-Excel-Datei](73990159.xlsx) in diesem Code und seinen verwendet[Ausgabe PDF](73990160.pdf)Der Screenshot zeigt den Unterschied zwischen der Beispiel-Excel-Datei und der Ausgabe PDF als Referenz.

![todo: Bild_alt_Text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
