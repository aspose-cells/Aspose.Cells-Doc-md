---
title: Nummerneinstellungen
type: docs
weight: 10
url: /de/java/cells-number-settings/
---
##  **Festlegen der Anzeigeformate Numbers und Datumsangaben**

Eine sehr starke Funktion von Microsoft Excel besteht darin, dass Benutzer die Anzeigeformate für numerische Werte und Datumsangaben festlegen können. Wir wissen, dass numerische Daten zur Darstellung verschiedener Werte verwendet werden können, einschließlich Dezimal-, Währungs-, Prozent-, Bruch- oder Buchhaltungswerten usw. Alle diese numerischen Werte werden je nach Art der dargestellten Informationen in unterschiedlichen Formaten angezeigt. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern die Festlegung eines beliebigen Anzeigeformats für eine Zahl oder ein Datum.

##  **Festlegen von Anzeigeformaten in Microsoft Excel**

So legen Sie Anzeigeformate in Microsoft Excel fest:

1. Klicken Sie mit der rechten Maustaste auf eine beliebige Zelle.
1. Wählen Sie *Format Cells**. Es erscheint ein Dialog, in dem Sie die Anzeigeformate für beliebige Werte festlegen können.

 Auf der linken Seite des Dialogs gibt es viele Kategorien von Werten wie z**Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz,**usw. Aspose.Cells unterstützt alle diese Anzeigeformate.

##  **Verwenden integrierter Zahlenformate**

 Aspose.Cells bietet einige integrierte Zahlenformate zum Konfigurieren der Anzeigeformate der Zahlen und Datumsangaben. Alle integrierten Zahlenformate erhalten eindeutige numerische Werte. Entwickler können dem einen beliebigen numerischen Wert zuweisen[**Nummer**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) Methode der[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style) Objekt, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten integrierten Zahlenformate sind unten aufgeführt.

|**Wert**|**Typ**|**Zeichenfolge formatieren**|
| :- | :- | :- |
|0|General|Allgemein|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Rot]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Rot]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0,00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|m/t/jjjj|
|15|Date|d-mmm-jj|
|16|Date|d-mmm|
|17|Date|mmm-jj|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|Hmm|
|21|Time|h:mm:ss|
|22|Time|m/t/jj h:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Rot]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[Rot]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0,0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **Verwenden benutzerdefinierter Zahlenformate**

 Um Ihre eigene benutzerdefinierte Formatzeichenfolge zum Festlegen des Anzeigeformats zu definieren, verwenden Sie die[**Brauch**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Dieser Ansatz ist nicht so schnell wie die Verwendung voreingestellter Formate, aber flexibler.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Wenn Sie die verwenden[**Brauch**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) Um das Zahlenformat festzulegen, kann jedes zuvor mithilfe von festgelegte Format verwendet werden[**Nummer**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Geben Sie benutzerdefinierte Dezimalzahlen und Gruppentrennzeichen für die Arbeitsmappe an](/cells/de/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Angeben der benutzerdefinierten DBNum-Musterformatierung](/cells/de/java/specifying-dbnum-custom-pattern-formatting/)
