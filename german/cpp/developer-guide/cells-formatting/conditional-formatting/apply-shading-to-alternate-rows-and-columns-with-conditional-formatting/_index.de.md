---
title: Schattierung abwechselnder Zeilen und Spalten mit bedingter Formatierung in C++ anwenden
linktitle: Schattierung abwechselnder Zeilen und Spalten anwenden
description: So verwenden Sie die Aspose.Cells Bibliothek in C++, um Schatten für abwechselnde Zeilen und Spalten mit bedingter Formatierung anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, C++, Abwechselnde Zeilen, Abwechselnde Spalten, Schatten
type: docs
weight: 30
url: /de/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Die Aspose.Cells-APIs bieten die Möglichkeit, bedingte Formatierungsregeln für das [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Objekt hinzuzufügen und zu manipulieren. Diese Regeln können auf vielfältige Weise angepasst werden, um das gewünschte Format basierend auf Bedingungen oder Regeln zu erzielen. Dieser Artikel zeigt die Verwendung der APIs mit der Nummer Aspose.Cells for C++, um Schattierungen für abwechselnde Zeilen & Spalten mithilfe bedingter Formatierungsregeln und Excel-Funktionen anzuwenden.

{{% /alert %}}

Dieser Artikel verwendet integrierte Funktionen von Excel wie ROW, COLUMN & MOD. Hier sind einige Details zu diesen Funktionen, um das Code-Snippet, das im Folgenden bereitgestellt wird, besser zu verstehen.

- Die **ROW()**-Funktion gibt die Zeilennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die ROW-Funktion eingegeben wurde.
- Die **COLUMN()**-Funktion gibt die Spaltennummer einer Zellreferenz zurück. Wenn der Referenzparameter ausgelassen wird, nimmt die Funktion an, dass die Referenz die Zelladresse ist, in die die COLUMN-Funktion eingegeben wurde.
- Die **MOD()**-Funktion gibt den Rest nach der Division einer Zahl durch einen Divisor zurück, wobei der erste Parameter der numerische Wert ist, von dem Sie den Rest finden möchten, und der zweite Parameter die Zahl ist, durch die die Nummernparameter dividiert werden. Wenn der Divisor 0 ist, wird der Fehler #DIV/0! zurückgegeben.

Lassen Sie uns mit der Verwendung der API Aspose.Cells for C++ beginnen, um dieses Ziel zu erreichen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Die folgende Momentaufnahme zeigt die resultierende Tabelle, die in der Excel-Anwendung geladen wird.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Um die Schattierung auf alternative Spalten anzuwenden, müssen Sie lediglich die Formel **=MOD(ZEILE(),2)=0** durch **=MOD(SPALTE(),2)=0** ersetzen, d.h. anstatt den Zeilenindex zu erhalten, ändern Sie die Formel, um den Spaltenindex abzurufen. 
Die resultierende Tabelle wird in diesem Fall folgendermaßen aussehen.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
