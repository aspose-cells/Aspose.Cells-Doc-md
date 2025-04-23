---  
title: Zahleneinstellungen
linktitle: Zahleneinstellungen  
description: Aspose.Cells ist eine Node.js Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die viele verschiedene Zellnummerneinstellungen unterstützt. Dieser Artikel stellt vor, wie man die Aspose.Cells Bibliothek zur Verwaltung der Zellnummerneinstellungen verwendet, um Zahlenformate in Tabellen zu bearbeiten.  
keywords: Aspose.Cells, Node.js Bibliothek, elektronische Tabellenkalkulation, Zellnummerneinstellungen, Formatierung, Verwaltung, Formate für Zahlen und Daten  
type: docs  
weight: 10  
url: /de/nodejs-cpp/cells-number-settings/  
---  

## **Wie man Anzeigeformate von Zahlen und Daten einstellt**  

Eine sehr starke Funktion von Microsoft Excel ist die Möglichkeit, das Anzeigeformat numerischer Werte und Daten festzulegen. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, darunter Dezimalzahlen, Währungen, Prozentsätze, Brüche oder Buchhaltungswerte usw. Alle diese numerischen Werte werden je nach Art der Information, die sie repräsentieren, in unterschiedlichen Formaten angezeigt. Ebenso gibt es viele Formate, in denen Datum oder Uhrzeit dargestellt werden können.  
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern, jedes Anzeigeformat für eine Zahl oder ein Datum festzulegen.  

### **Wie man Anzeigeformate in Microsoft Excel festlegt**  

Um Anzeigeformate in Microsoft Excel festzulegen:  

1. Klicken Sie mit der rechten Maustaste auf eine Zelle.  
2. Wählen Sie **Zellen formatieren**. Es erscheint ein Dialog, mit dem Sie die Anzeigeformate jeglicher Art von Wert festlegen können.  

Auf der linken Seite des Dialogs gibt es viele Kategorien von Werten wie **Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz** usw. Aspose.Cells unterstützt all diese Anzeigeformate.  

Aspose.Cells bietet ein Modul, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), das eine Excel-Datei repräsentiert. Das [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Modul enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch das [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Modul dargestellt. Das [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Modul stellt eine [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung bereit. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung repräsentiert ein Objekt des [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Moduls.  

Aspose.Cells bietet [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) und [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)-Methoden für das [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-Modul. Diese Methoden werden zum Abrufen und Festlegen der Formatierung einer Zelle verwendet. Das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Modul stellt einige nützliche Eigenschaften für die Arbeit mit Anzeigeformaten von Zahlen und Daten bereit.  

### **Wie man eingebaute Zahlenformate verwendet**  

Aspose.Cells bietet einige integrierte Zahlenformate, um die Anzeigeformate von Zahlen und Daten zu konfigurieren. Diese integrierten Zahlenformate können durch Verwendung der [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)-Methode des [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekts angewendet werden. Alle integrierten Zahlenformate sind mit einzigartigen numerischen Werten versehen. Entwickler können jeder beliebigen Zahl einen gewünschten numerischen Wert zuweisen, um das Anzeigeformat anzuwenden. Diese Methode ist schnell. Die von Aspose.Cells unterstützten integrierten Zahlenformate sind unten aufgelistet.  

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
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Wie man benutzerdefinierte Zahlenformate verwendet**  

Um Ihren eigenen angepasstes Formatstring zur Einstellung des Anzeigeformats zu definieren, verwenden Sie die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Methode des [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)-Objekts. Dieser Ansatz ist nicht so schnell wie vordefinierte Formate, bietet aber mehr Flexibilität.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Wenn Sie die [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-)-Methode verwenden, um das Zahlenformat festzulegen, überschreibt dies das vorherige Format, das mit der [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-)-Methode festgelegt wurde, und umgekehrt.  

{{% /alert %}}  

## **Erweiterte Themen**  
- [Benutzerdefiniertes Zahlenformat beim Festlegen von Style.Custom-Eigenschaft überprüfen](/cells/de/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Liste der unterstützten Zahlenformate](/cells/de/nodejs-cpp/list-of-supported-number-formats/)  
- [Benutzerdefiniertes Datumsformatmuster g und ge mm dd anzeigen](/cells/de/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Benutzerdefinierte Dezimal- und Gruppentrennzeichen für Arbeitsmappe festlegen](/cells/de/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Benutzerdefiniertes DBNum-Formatmusterformat festlegen](/cells/de/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
