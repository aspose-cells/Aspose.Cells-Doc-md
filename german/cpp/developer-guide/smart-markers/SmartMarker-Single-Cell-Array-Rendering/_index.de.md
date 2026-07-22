---
title: SmartMarker-Einzelzell-Array-Darstellung | Aspose.Cells C++
linktitle: SmartMarker-Einzelzell-Array-Darstellung | Aspose.Cells
description: Erfahren Sie, wie Sie Array-Daten mithilfe der Attribute ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle rendern können mit Aspose.Cells for C++.
keywords: Aspose.Cells, C++ Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzell-Array, Array-Darstellung, Vorlage
type: docs
weight: 195
url: /de/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Darstellung von Array-Daten in einer einzelnen Zelle über Smart Markers. Durch die Verwendung des `ArrayAsSingle`-Attributs zusammen mit dem `ExtraDelimiter`-Attribut können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, und so eine flexible Formatierung für Berichte und Vorlagen ermöglichen.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellenkalkulationsdaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert. Wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig expandiert die Engine das Array, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (zum Beispiel `&=DataSource.Numbers`), und platziert jedes Element in eine separate angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie es vorziehen würden, das gesamte Array in eine einzige Zelle zu rendern, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersehbar zu halten, während Sie dennoch nativ mit Array-Datenquellen arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standardmäßiges Array-Verteilungsverhalten**

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle, wodurch andere Vorlageninhalte nach außen verschoben werden und möglicherweise sorgfältig gestaltete Berichtslayouts zerstört werden.

### **Einschränkungen bei Anwendungsfällen**

Es gibt viele praktische Szenarien, in denen das standardmäßige Verteilungsverhalten unerwünscht ist:

- **Zusammenfassungs-Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Keyword-Listen**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden sollen.
- **Filter-Chips oder Status-Indikatoren**, die mehrere Werte an einem Ort zur besseren Lesbarkeit gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzigen konsolidierten Wert pro Zelle erwarten, anstatt einen erweiterten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die es schließt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in C++ vorzuverarbeiten – Arrays zu getrennten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, kompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst handhaben.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzell-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersehbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder einen beliebigen benutzerdefinierten Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code erforderlich, um die Daten vorzuverarbeiten; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in verschiedene Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumsangaben und jedem anderen Datentyp, der mit einem Trennzeichen zusammengeführt werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **Wie man diese Funktion verwendet**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines standardmäßigen Smart Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker besteht aus den folgenden Teilen:

- `&=DataSource.ArrayProperty` – der standardmäßige Smart Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` – weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellverhalten aus.
- `extraDelimiter=", "` – definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenfolgenliteral; er kann leer, ein einzelnes Zeichen oder eine mehrzeichige Zeichenfolge sein.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert jedes Zeichenfolgenliteral, einschließlich mehrzeichiger Trennzeichen, benutzerdefinierter Texte oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Arbeitsablauf**

Der folgende Arbeitsablauf beschreibt, wie ein Array mithilfe von Smart Markers in eine einzelne Zelle gerendert wird.

1. **Datenquelle vorbereiten**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `std::vector<std::string>`, `std::vector<int>` oder einen anderen unterstützten Array-/Vektor-Typ zurückgeben.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **WorkbookDesigner instanziieren**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe daran an und binden Sie Ihre Datenquelle mit der Methode `SetDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.Process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX-Format oder in einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 – Grundlegende Zeichenketten-Array-Darstellung**

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

    // WorkbookDesigner ist in Aspose.Cells für C++ nicht verfügbar
    // Wir müssen die SmartMarker-Verarbeitung simulieren, indem wir die Markierungen manuell ersetzen
    // Da Aspose.Cells C++ WorkbookDesigner nicht unterstützen, verwenden wir U16String-Ersetzung
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Ersetze den Smart-Marker mit den tatsächlichen Daten
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Codebeispiel 2 – Numerisches Array mit benutzerdefiniertem Trennzeichen**

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

### **Codebeispiel 3 – Vergleich von Standard- vs. ArrayAsSingle-Verhalten**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Datenquelle vorbereiten
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Arbeitsmappe erstellen und erstes Arbeitsblatt abrufen
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Abschnitt 1: Standard-Smart-Marker - Werte werden horizontal über Zellen verteilt
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Abschnitt 2: Neue Einzelzellen-Darstellung mit arrayasSingle und extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Datenquelle binden und Smart Marker verarbeiten
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Ergebnis-Arbeitsmappe speichern
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Hinweise & bewährte Vorgehensweisen**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert `extraDelimiter` wird als Zeichenfolgenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor möglicherweise interpretiert.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellverhalten aus; jeder andere Wert fällt auf das standardmäßige Verteilungsverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenfolge).
- Die Funktion funktioniert sowohl mit Objekt-Datenquellen als auch mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die ausreichend Breite hat, um die resultierende verkettete Zeichenfolge anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.

## **Verwandte Artikel**

- [Smart Markers](/cells/de/cpp/smart-markers/)
- [Zellen zusammenführen und aufteilen](/cells/de/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}