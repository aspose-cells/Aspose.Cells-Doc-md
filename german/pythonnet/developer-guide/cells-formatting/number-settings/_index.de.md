---
title: Zahleneinstellungen
description: Aspose.Cells ist eine Python Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien, die viele verschiedene Zellnummerneinstellungen unterstützt. Dieser Artikel führt ein, wie man die Aspose.Cells Bibliothek nutzt, um die Number Formatierung der Zellen zu verwalten, damit Benutzer das Zahlenformat bei Bedarf anpassen können.
keywords: Aspose.Cells, Python Bibliothek, elektronische Tabellenkalkulation, Zellen Nummerneinstellungen, Formatierung, Verwaltung, Formate von Zahlen und Daten
type: docs
weight: 10
url: /de/python-net/cells-number-settings/
---

## **Wie man Anzeigeformate von Zahlen und Daten einstellt**

Eine sehr starke Eigenschaft von Microsoft Excel ist, dass es Benutzern ermöglicht, die Anzeigeformate von numerischen Werten und Datumsangaben festzulegen. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, einschließlich Dezimalstellen, Währung, Prozentsatz, Bruch oder Buchhaltungswerte usw. Alle diese numerischen Werte werden in unterschiedlichen Formaten angezeigt, abhängig von der Art der dargestellten Informationen. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells für Python via .NET unterstützt diese Funktionalität und ermöglicht Entwicklern, beliebiges Anzeigeformat für eine Zahl oder ein Datum festzulegen.

### **Wie man Anzeigeformate in Microsoft Excel festlegt**

Um Anzeigeformate in Microsoft Excel festzulegen:

1. Klicken Sie mit der rechten Maustaste auf eine Zelle.
1. Wählen Sie **Zellen formatieren** aus. Es erscheint ein Dialogfeld, das verwendet wird, um die Anzeigeformate für alle Arten von Werten festzulegen.

Auf der linken Seite des Dialogfelds gibt es viele Kategorien von Werten wie **Allgemein**, **Nummer**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz**, usw. Aspose.Cells für Python via .NET unterstützt all diese Anzeigeformate.

Aspose.Cells für Python via .NET stellt eine Klasse bereit, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung stellt ein Objekt der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse dar.

Aspose.Cells für Python via .NET bietet [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) und [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)-Methoden für die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse. Diese Methoden werden verwendet, um die Formatierung einer Zelle zu lesen und festzulegen. Die [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Klasse stellt nützliche Eigenschaften für die Behandlung der Anzeigeformate von Zahlen und Daten bereit.

### **Wie man eingebaute Zahlenformate verwendet**

Aspose.Cells für Python via .NET bietet einige eingebaute Zahlenformate, um die Anzeigeformate von Zahlen und Daten zu konfigurieren. Diese eingebauten Zahlenformate können durch die Verwendung der Eigenschaft [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) des Objekts [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) angewendet werden. Alle eingebauten Zahlenformate haben eindeutige numerische Werte. Entwickler können jedem gewünschten numerischen Wert die Eigenschaft [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) des [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-Objekts zuweisen, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten eingebauten Zahlenformate sind unten aufgeführt.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Wie man benutzerdefinierte Zahlenformate verwendet**

Um Ihre eigene benutzerdefinierte Formatzeichenfolge zur Festlegung des Anzeigeformats zu definieren, verwenden Sie die Eigenschaft [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) des Objekts [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Dieser Ansatz ist nicht so schnell wie die Verwendung von voreingestellten Formaten, bietet jedoch mehr Flexibilität.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

Wenn Sie die Eigenschaft [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) verwenden, um das Zahlformat festzulegen, wird jedes zuvor festgelegte Format, das unter Verwendung der Eigenschaft [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) festgelegt wurde, überschrieben, und umgekehrt.

{{% /alert %}}

## **Erweiterte Themen**
- [Benutzerdefiniertes Zahlenformat beim Festlegen von Style.Custom-Eigenschaft überprüfen](/cells/de/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Liste der unterstützten Zahlenformate](/cells/de/python-net/list-of-supported-number-formats/)
- [Benutzerdefiniertes Datumsformatmuster g und ge mm dd anzeigen](/cells/de/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Benutzerdefinierte Dezimal- und Gruppentrennzeichen für Arbeitsmappe festlegen](/cells/de/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Benutzerdefiniertes DBNum-Formatmusterformat festlegen](/cells/de/python-net/specifying-dbnum-custom-pattern-formatting/)

{{< app/cells/assistant language="python-net" >}}
