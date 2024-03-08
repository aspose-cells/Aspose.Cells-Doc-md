---
title: Nummerneinstellungen
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die viele verschiedene Zellennummerneinstellungen unterstützt. In diesem Artikel wird erläutert, wie Sie mithilfe der Bibliothek Aspose.Cells die Zahleneinstellungen von Zellen verwalten, sodass Benutzer das Zahlenformat in der Tabelle nach Bedarf anpassen können.
keywords: Aspose.Cells, .NET library, electronic spreadsheet, cell number settings, formatting, management, Formats of Numbers and Dates
type: docs
weight: 10
url: /de/net/cells-number-settings/
---
##  **So legen Sie die Anzeigeformate Numbers und Datumsangaben fest**

Eine sehr starke Funktion von Microsoft Excel besteht darin, dass Benutzer die Anzeigeformate für numerische Werte und Datumsangaben festlegen können. Wir wissen, dass numerische Daten zur Darstellung verschiedener Werte verwendet werden können, einschließlich Dezimal-, Währungs-, Prozent-, Bruch- oder Buchhaltungswerten usw. Alle diese numerischen Werte werden je nach Art der dargestellten Informationen in unterschiedlichen Formaten angezeigt. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern die Festlegung eines beliebigen Anzeigeformats für eine Zahl oder ein Datum.

###  **So legen Sie Anzeigeformate in Microsoft Excel fest**

So legen Sie Anzeigeformate in Microsoft Excel fest:

1. Klicken Sie mit der rechten Maustaste auf eine beliebige Zelle.
1. Wählen Sie *Format Cells**. Es erscheint ein Dialog, in dem Sie die Anzeigeformate für beliebige Werte festlegen können.

 Auf der linken Seite des Dialogs gibt es viele Kategorien von Werten wie z**Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz,**usw. Aspose.Cells unterstützt alle diese Anzeigeformate.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden für die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse. Diese Methoden werden verwendet, um die Formatierung einer Zelle abzurufen und festzulegen. Der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Die Klasse stellt einige nützliche Eigenschaften für den Umgang mit den Anzeigeformaten von Zahlen und Datumsangaben bereit.

###  **So verwenden Sie integrierte Zahlenformate**

 Aspose.Cells bietet einige integrierte Zahlenformate zum Konfigurieren der Anzeigeformate der Zahlen und Datumsangaben. Diese integrierten Zahlenformate können mithilfe von angewendet werden[**Nummer**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) Eigentum der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt. Alle integrierten Zahlenformate erhalten eindeutige numerische Werte. Entwickler können dem einen beliebigen numerischen Wert zuweisen[**Nummer**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) Eigentum der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Objekt, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten integrierten Zahlenformate sind unten aufgeführt.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

###  **So verwenden Sie benutzerdefinierte Zahlenformate**

 Um Ihre eigene benutzerdefinierte Formatzeichenfolge zum Festlegen des Anzeigeformats zu definieren, verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Brauch**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)Eigentum. Dieser Ansatz ist nicht so schnell wie die Verwendung voreingestellter Formate, aber flexibler.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Wenn Sie die verwenden[**Brauch**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Eigenschaft zum Festlegen des Zahlenformats, jedes vorherige Format, das mit der festgelegt wurde[**Nummer**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)Die Eigenschaft wird überschrieben und umgekehrt.

{{% /alert %}}

##  **Vorabthemen**
- [Überprüfen Sie das benutzerdefinierte Zahlenformat, wenn Sie die Style.Custom-Eigenschaft festlegen](/cells/de/net/check-custom-number-format-when-setting-style-custom-property/)
- [Liste der unterstützten Zahlenformate](/cells/de/net/list-of-supported-number-formats/)
- [Rendern Sie das benutzerdefinierte Datumsformatmuster g und ge mm dd](/cells/de/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Geben Sie benutzerdefinierte Dezimalzahlen und Gruppentrennzeichen für die Arbeitsmappe an](/cells/de/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Angeben der benutzerdefinierten DBNum-Musterformatierung](/cells/de/net/specifying-dbnum-custom-pattern-formatting/)
