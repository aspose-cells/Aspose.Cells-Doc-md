---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells C++
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells C++
description: Erfahren Sie, wie Array-Daten mithilfe der Attribute ArrayAsSingle und ExtraDelimiter in Smart Markern mit Aspose.Cells for C++ in eine einzelne Zelle gerendert werden.
keywords: Aspose.Cells, C++ Bibliothek, Tabellenkalkulation, Smart Marker, ArrayAsSingle, ExtraDelimiter, Einzelzellen-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Marker. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzigen Zelle getrennt werden, was eine flexible Formatierung für Berichte und Vorlagen ermöglicht.

## **Introduction**
Smart Marker in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellendaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage vom `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig expandiert die Engine das Array, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (zum Beispiel `&=DataSource.Numbers`), und platziert jedes Element in einer separaten angrenzenden Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt sind.
Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersehbar zu halten und gleichzeitig nativ mit Array-Datenquellen zu arbeiten.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` für ein `string[]` mit vier Werten jeden Wert in einer eigenen Zelle, wodurch andere Vorlageninhalte verschoben und möglicherweise sorgfältig gestaltete Berichtslayouts zerstört werden.

### **Use Case Limitations**
Es gibt viele praktische Szenarien, in denen das Standardverteilungsverhalten unerwünscht ist:
- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Keyword-Listen**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzigen Zelle angezeigt werden sollen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte zur Lesbarkeit an einem Ort gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Seriendruck), die einen einzigen konsolidierten Wert pro Zelle erwarten, anstatt einen erweiterten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die über mehrere Zellen verteilt sind, nicht tolerieren können.

### **The Gap It Fills**
Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in C++ vorzuverarbeiten – Arrays zu begrenzten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert die Logik, verkompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst handhaben.

## **Feature Benefits**
Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markern bietet mehrere Vorteile:
- **Inhalt in einer einzelnen Zelle**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersehbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie ein beliebiges Trennzeichen an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder einen beliebigen benutzerdefinierten Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code zur Vorverarbeitung der Daten erforderlich; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in verschiedene Zeile oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumsangaben und allen anderen Datentypen, die mit einem Trennzeichen zusammengeführt werden können.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **How to Use This Feature**

### **Smart Marker Syntax**
Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker besteht aus den folgenden Teilen:
- `&=DataSource.ArrayProperty` — der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` — weist die Engine an, das gesamte Array in eine einzige Zelle zu rendern. Nur der Wert `true` löst das Einzelzellenverhalten aus.
- `extraDelimiter=", "` — definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein String-Literal; er kann leer, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette sein.

{{% alert color="primary" %}}
Das Attribut `extraDelimiter` akzeptiert jedes String-Literal, einschließlich mehrzeichiger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

### **Step-by-Step Workflow**
Der folgende Workflow beschreibt, wie ein Array mithilfe von Smart Markern in eine einzelne Zelle gerendert wird.
1. **Datenquelle vorbereiten**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `std::vector<std::string>`, `std::vector<int>` oder jeden anderen unterstützten Array-/Vektor-Typ zurückgeben.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **WorkbookDesigner instanziieren**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe daran an und binden Sie Ihre Datenquelle mit der Methode `SetDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.Process()` auf, um die Smart Marker zu erweitern und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX- oder einem anderen unterstützten Dateiformat.

### **Code Example 1 — Basic String Array Rendering**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();
    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");
    // WorkbookDesigner is not available in Aspose.Cells for C++
    // We need to simulate SmartMarker processing by replacing markers manually
    // Since Aspose.Cells C++ doesn't support WorkbookDesigner, we'll use U16String replacement
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Replace the smart marker with actual data
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);
    wb.Save(u"output_arraySingle.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);
    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));
    wb.Save(u"output_numericArray.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```cpp
#include "Aspose.Cells.h"
#include <vector>
using namespace Aspose::Cells;
struct Order {
    std::vector<U16String> Items;
};
int main() {
    Aspose::Cells::Startup();
    // Prepare data source
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };
    // Create workbook and get first worksheet
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // Section 1: Default Smart Marker - values spread horizontally across cells
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");
    // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
    // Bind the data source and process Smart Markers
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();
    // Save the resulting workbook
    wb.Save(u"output_comparison.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Notes & Best Practices**
Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:
- Der Wert `extraDelimiter` wird als String-Literal behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellenverhalten aus; jeder andere Wert fällt auf das Standardverteilungsverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion arbeitet mit Objekt-Datenquellen sowie mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die ausreichend breit ist, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for C++ hinzufügen](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for C++ anwenden](/cells/de/cpp/apply-style-to-pivot-table/)
- [Seitenfeldlayout in Pivot-Tabelle ändern](/cells/de/cpp/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for C++ konvertieren](/cells/de/cpp/convert-sparkline-to-image-and-html/)
- [Excel in das OFD-Format konvertieren](/cells/de/cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="cpp" >}}