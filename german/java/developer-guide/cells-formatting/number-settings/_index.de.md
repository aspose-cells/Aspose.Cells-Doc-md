---
title: Zahleneinstellungen
type: docs
weight: 10
url: /de/java/cells-number-settings/
---

## **Einrichten von Anzeigeformaten für Zahlen und Daten**

Eine sehr starke Eigenschaft von Microsoft Excel ist, dass es Benutzern ermöglicht, die Anzeigeformate von numerischen Werten und Datumsangaben festzulegen. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, einschließlich Dezimalstellen, Währung, Prozentsatz, Bruch oder Buchhaltungswerte usw. Alle diese numerischen Werte werden in unterschiedlichen Formaten angezeigt, abhängig von der Art der dargestellten Informationen. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern, jedes Anzeigeformat für eine Zahl oder ein Datum festzulegen.

## **Einrichten von Anzeigeformaten in Microsoft Excel**

Um Anzeigeformate in Microsoft Excel festzulegen:

1. Klicken Sie mit der rechten Maustaste auf eine Zelle.
1. Wählen Sie **Zellen formatieren** aus. Es erscheint ein Dialogfeld, das verwendet wird, um die Anzeigeformate für alle Arten von Werten festzulegen.

Auf der linken Seite des Dialogfelds gibt es viele Kategorien von Werten wie **Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz**, usw. Aspose.Cells unterstützt alle diese Anzeigeformate.

## **Verwendung von integrierten Zahlenformaten**

Aspose.Cells bietet einige eingebaute Nummernformate, um die Anzeigeformate von Zahlen und Datum zu konfigurieren. Alle eingebauten Nummernformate erhalten eindeutige numerische Werte. Entwickler können jeder gewünschten numerischen Wert der [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number)-Methode des [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts zuweisen, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten eingebauten Nummernformate sind nachstehend aufgeführt.

|**Wert**|**Typ**|**Formatzeichenfolge**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Verwendung von benutzerdefinierten Nummernformaten**

Um Ihre eigene benutzerdefinierte Formatzeichenkette zur Festlegung des Anzeigeformats festzulegen, verwenden Sie die [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Dieser Ansatz ist nicht so schnell wie die Verwendung von voreingestellten Formaten, aber er ist flexibler.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

Wenn Sie die [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) verwenden, um das Nummernformat festzulegen, wird jedes zuvor festgelegte Format, das mit dem [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number）eingerichtet wurde, überschrieben und umgekehrt.

{{% /alert %}}

## **Erweiterte Themen**
- [Benutzerdefiniertes Zahlenformat beim Festlegen von Style.Custom-Eigenschaft überprüfen](/cells/de/java/check-custom-number-format-when-setting-style-custom-property/)
- [Benutzerdefinierte Dezimal- und Gruppentrennzeichen für Arbeitsmappe festlegen](/cells/de/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Benutzerdefiniertes DBNum-Formatmusterformat festlegen](/cells/de/java/specifying-dbnum-custom-pattern-formatting/)
