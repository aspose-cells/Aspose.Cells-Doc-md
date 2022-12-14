---
title: Nummerneinstellungen
type: docs
weight: 10
url: /de/java/cells-number-settings/
---
## **Anzeigeformate für Zahlen und Daten einstellen**

Ein sehr starkes Merkmal von Microsoft Excel ist, dass Benutzer die Anzeigeformate von numerischen Werten und Datumsangaben festlegen können. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, darunter Dezimal-, Währungs-, Prozent-, Bruch- oder Buchhaltungswerte usw. Alle diese numerischen Werte werden in unterschiedlichen Formaten angezeigt, je nach Art der Informationen, die sie darstellen. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells unterstützt diese Funktionalität und ermöglicht es Entwicklern, ein beliebiges Anzeigeformat für eine Zahl oder ein Datum festzulegen.

## **Festlegen von Anzeigeformaten in Microsoft Excel**

Anzeigeformate in Microsoft Excel einstellen:

1. Klicken Sie mit der rechten Maustaste auf eine beliebige Zelle.
1.  Auswählen**Cells formatieren**. Es erscheint ein Dialog, der verwendet wird, um die Anzeigeformate beliebiger Werte einzustellen.

 Auf der linken Seite des Dialogs gibt es viele Kategorien von Werten wie z**Allgemein**, **Nummer**, **Währung**, **Buchhaltung**, **Datum**, **Zeit**, **Prozentsatz,**usw. Aspose.Cells unterstützt alle diese Anzeigeformate.

## **Verwenden von integrierten Zahlenformaten**

 Aspose.Cells bietet einige eingebaute Zahlenformate, um die Anzeigeformate der Zahlen und Daten zu konfigurieren. Allen integrierten Zahlenformaten werden eindeutige numerische Werte zugewiesen. Entwickler können dem einen beliebigen numerischen Wert zuweisen[**Nummer**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) Methode der[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style) Objekt, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten integrierten Zahlenformate sind unten aufgeführt.

|**Wert**|**Typ**|**Zeichenkette formatieren**|
|:- |:- |:- |
|0|Allgemein|Allgemein|
|1|Dezimal|0|
|2|Dezimal|0.00|
|3|Dezimal|# ,##0
|
|4|Dezimal|# ,##0.00
|
|5|Währung|$#,##0;$-#,##0|
|6|Währung|$#,##0;[Rot]$-#,##0|
|7|Währung|$#,##0.00;$-#,##0.00|
|8|Währung|$#,##0.00;[Rot]$-#,##0.00|
|9|Prozentsatz|0%|
|10|Prozentsatz|0.00%|
|11|Wissenschaftlich|0.00E+00|
|12|Fraktion|# ?/?
|
|13|Fraktion|# */*
|
|14|Datum|M/T/JJ|
|15|Datum|t-mm-jj|
|16|Datum|d-mm|
|17|Datum|mmm-jj|
|18|Zeit|h:mm AM/PM|
|19|Zeit|h:mm:ss AM/PM|
|20|Zeit|hmm|
|21|Zeit|h:mm:ss|
|22|Zeit|m/d/jj h:mm|
|37|Währung|# ,##0;-#,##0
|
|38|Währung|# ,##0;[Rot]-#,##0
|
|39|Währung|# ,##0.00;-#,##0.00
|
|40|Währung|# ,##0.00;[Rot]-#,##0.00
|
|41|Buchhaltung|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Buchhaltung|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Buchhaltung|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Buchhaltung|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Zeit|mm:ss|
|46|Zeit|h :mm:ss|
|47|Zeit|mm:ss.0|
|48|Wissenschaftlich|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Verwenden von benutzerdefinierten Zahlenformaten**

Um Ihre eigene benutzerdefinierte Formatzeichenfolge zum Festlegen des Anzeigeformats zu definieren, verwenden Sie die[**Brauch**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Dieser Ansatz ist nicht so schnell wie die Verwendung voreingestellter Formate, aber flexibler.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Wenn Sie die verwenden[**Brauch**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) um das Zahlenformat einzustellen, jedes vorherige Format, das mit eingestellt wurde[**Nummer**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Geben Sie benutzerdefinierte Dezimalzahlen und Gruppentrennzeichen für die Arbeitsmappe an](/cells/de/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Festlegen der benutzerdefinierten DBNum-Musterformatierung](/cells/de/java/specifying-dbnum-custom-pattern-formatting/)
