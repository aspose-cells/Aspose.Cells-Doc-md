---
title: Nummer Einstellungen mit C++
linktitle: Zahleneinstellungen
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die viele verschiedene Zellen Nummerneinstellungen unterstützt. Dieser Artikel führt ein, wie man die Aspose.Cells Bibliothek nutzt, um die Nummerneinstellungen der Zellen zu verwalten, sodass Benutzer das Zahlenformat nach Bedarf im Tabellenblatt anpassen können.
keywords: Aspose.Cells, C++ Bibliothek, elektronische Tabelle, Zellen Nummerneinstellungen, Formatierung, Verwaltung, Formate von Zahlen und Daten
type: docs
weight: 10
url: /de/cpp/cells-number-settings/
---

## **Wie man Anzeigeformate von Zahlen und Daten einstellt**

Eine sehr starke Eigenschaft von Microsoft Excel ist, dass es Benutzern ermöglicht, die Anzeigeformate von numerischen Werten und Datumsangaben festzulegen. Wir wissen, dass numerische Daten verwendet werden können, um verschiedene Werte darzustellen, einschließlich Dezimalstellen, Währung, Prozentsatz, Bruch oder Buchhaltungswerte usw. Alle diese numerischen Werte werden in unterschiedlichen Formaten angezeigt, abhängig von der Art der dargestellten Informationen. Ebenso gibt es viele Formate, in denen ein Datum oder eine Uhrzeit angezeigt werden kann.
Aspose.Cells unterstützt diese Funktionalität und ermöglicht Entwicklern, jedes Anzeigeformat für eine Zahl oder ein Datum festzulegen.

### **Wie man Anzeigeformate in Microsoft Excel festlegt**

Um Anzeigeformate in Microsoft Excel festzulegen:

1. Klicken Sie mit der rechten Maustaste auf eine Zelle.
1. Wählen Sie **Zellen formatieren** aus. Es erscheint ein Dialogfeld, das verwendet wird, um die Anzeigeformate für alle Arten von Werten festzulegen.

Auf der linken Seite des Dialogfelds gibt es viele Kategorien von Werten wie **Allgemein**, **Zahl**, **Währung**, **Buchhaltung**, **Datum**, **Uhrzeit**, **Prozentsatz**, usw. Aspose.Cells unterstützt alle diese Anzeigeformate.

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells bietet Methoden [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) und [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) für die Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Diese Methoden werden verwendet, um das Format einer Zelle zu erhalten und festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) bietet einige nützliche Eigenschaften zum Umgang mit den Anzeigeformaten von Zahlen und Datumsangaben.

### **Wie man eingebaute Zahlenformate verwendet**

Aspose.Cells bietet einige eingebaute Zahlenformate zur Konfiguration der Anzeigeformate von Zahlen und Datumsangaben. Diese eingebauten Zahlenformate können unter Verwendung der Eigenschaft [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) angewendet werden. Alle eingebauten Zahlenformate haben eindeutige numerische Werte. Entwickler können beliebige gewünschte numerische Werte der Eigenschaft [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) des Objekts [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) zuweisen, um das Anzeigeformat anzuwenden. Dieser Ansatz ist schnell. Die von Aspose.Cells unterstützten eingebauten Zahlenformate sind unten aufgeführt.

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

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::time_t now = std::time(nullptr);
    double excelDate = static_cast<double>(now) / 86400.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetNumber(15);
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetNumber(9);
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetNumber(6);
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Wie man benutzerdefinierte Zahlenformate verwendet**

Um Ihre eigene benutzerdefinierte Formatzeichenfolge zur Festlegung des Anzeigeformats zu definieren, verwenden Sie die Eigenschaft [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) des Objekts [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Dieser Ansatz ist nicht so schnell wie die Verwendung von voreingestellten Formaten, bietet jedoch mehr Flexibilität.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    auto now = std::chrono::system_clock::now();
    auto duration = now.time_since_epoch();
    auto hours = std::chrono::duration_cast<std::chrono::hours>(duration).count();
    double excelDate = hours / 24.0 + 25569.0;
    worksheet.GetCells().Get(u"A1").PutValue(excelDate);

    Style style = worksheet.GetCells().Get(u"A1").GetStyle();
    style.SetCustom(u"d-mmm-yy");
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    worksheet.GetCells().Get(u"A2").PutValue(20);
    style = worksheet.GetCells().Get(u"A2").GetStyle();
    style.SetCustom(u"0.0%");
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    worksheet.GetCells().Get(u"A3").PutValue(2546);
    style = worksheet.GetCells().Get(u"A3").GetStyle();
    style.SetCustom(u"£#,##0;[Red]$-#,##0");
    worksheet.GetCells().Get(u"A3").SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Wenn Sie die Eigenschaft [**Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/) verwenden, um das Zahlformat festzulegen, wird jedes zuvor festgelegte Format, das unter Verwendung der Eigenschaft [**Number**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getnumber/) festgelegt wurde, überschrieben, und umgekehrt.

{{% /alert %}}

## **Erweiterte Themen**
- [Benutzerdefiniertes Zahlenformat beim Festlegen von Style.Custom-Eigenschaft überprüfen](/cells/de/cpp/check-custom-number-format-when-setting-style-custom-property/)
- [Liste der unterstützten Zahlenformate](/cells/de/cpp/list-of-supported-number-formats/)
- [Benutzerdefiniertes Datumsformatmuster g und ge mm dd anzeigen](/cells/de/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Benutzerdefinierte Dezimal- und Gruppentrennzeichen für Arbeitsmappe festlegen](/cells/de/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Benutzerdefiniertes DBNum-Formatmusterformat festlegen](/cells/de/cpp/specifying-dbnum-custom-pattern-formatting/)
