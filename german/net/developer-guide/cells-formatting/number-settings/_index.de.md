---
title: Zahleneinstellungen
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellendateien, die viele verschiedene Zahlenformateinstellungen unterstützt. Dieser Artikel wird zeigen, wie die Aspose.Cells Bibliothek verwendet werden kann, um die Zahlenformate von Zellen zu verwalten, damit Benutzer das Zahlenformat in der Tabelle anpassen können.
keywords: Aspose.Cells, .NET Bibliothek, elektronisches Tabellenblatt, Zahleneinstellungen, Formatierung, Verwaltung, Formate von Zahlen und Datum
type: docs
weight: 10
url: /de/net/cells-number-settings/
---

## **Wie man Anzeigeformate von Zahlen und Daten einstellt**

Eine sehr starke Eigenschaft von Microsoft Excel ist, dass es Benutzern ermöglicht, die Anzeigeformate von numerischen Werten und Datumsangaben festzulegen. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, einschließlich Dezimalstellen, Währung, Prozentsatz, Bruch oder Buchhaltungswerte usw. Alle diese numerischen Werte werden in unterschiedlichen Formaten angezeigt, abhängig von der Art der dargestellten Informationen. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern, jedes Anzeigeformat für eine Zahl oder ein Datum festzulegen.

### **Wie man Anzeigeformate in Microsoft Excel festlegt**

Um Anzeigeformate in Microsoft Excel festzulegen:

1. Klicken Sie mit der rechten Maustaste auf eine Zelle.
1. Wählen Sie **Zellen formatieren** aus. Es erscheint ein Dialogfeld, das verwendet wird, um die Anzeigeformate für alle Arten von Werten festzulegen.

Auf der linken Seite des Dialogfelds gibt es viele Kategorien von Werten wie **Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz**, usw. Aspose.Cells unterstützt alle diese Anzeigeformate.

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells bietet Methoden [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) und [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) für die Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Diese Methoden werden verwendet, um das Format einer Zelle zu erhalten und festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) bietet einige nützliche Eigenschaften zum Umgang mit den Anzeigeformaten von Zahlen und Datumsangaben.

### **Wie man eingebaute Zahlenformate verwendet**

Aspose.Cells bietet einige eingebaute Zahlenformate zur Konfiguration der Anzeigeformate von Zahlen und Datumsangaben. Diese eingebauten Zahlenformate können unter Verwendung der Eigenschaft [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) des Objekts [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) angewendet werden. Alle eingebauten Zahlenformate haben eindeutige numerische Werte. Entwickler können beliebige gewünschte numerische Werte der Eigenschaft [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) des Objekts [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) zuweisen, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten eingebauten Zahlenformate sind unten aufgeführt.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Wie man benutzerdefinierte Zahlenformate verwendet**

Um Ihre eigene benutzerdefinierte Formatzeichenfolge zur Festlegung des Anzeigeformats zu definieren, verwenden Sie die Eigenschaft [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) des Objekts [**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). Dieser Ansatz ist nicht so schnell wie die Verwendung von voreingestellten Formaten, bietet jedoch mehr Flexibilität.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

Wenn Sie die Eigenschaft [**Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) verwenden, um das Zahlformat festzulegen, wird jedes zuvor festgelegte Format, das unter Verwendung der Eigenschaft [**Number**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) festgelegt wurde, überschrieben, und umgekehrt.

{{% /alert %}}

## **Erweiterte Themen**
- [Benutzerdefiniertes Zahlenformat beim Festlegen von Style.Custom-Eigenschaft überprüfen](/cells/de/net/check-custom-number-format-when-setting-style-custom-property/)
- [Liste der unterstützten Zahlenformate](/cells/de/net/list-of-supported-number-formats/)
- [Benutzerdefiniertes Datumsformatmuster g und ge mm dd anzeigen](/cells/de/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Benutzerdefinierte Dezimal- und Gruppentrennzeichen für Arbeitsmappe festlegen](/cells/de/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Benutzerdefiniertes DBNum-Formatmusterformat festlegen](/cells/de/net/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="csharp" >}}
