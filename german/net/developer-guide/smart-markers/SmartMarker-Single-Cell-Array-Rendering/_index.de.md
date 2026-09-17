---
title: SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells .NET
linktitle: SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells .NET
description: Erfahren Sie, wie Sie Array-Daten mit den Attributen ArrayAsSingle und ExtraDelimiter in Smart Markers in Aspose.Cells for .NET in eine einzelne Zelle rendern.
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzellen-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, und so eine flexible Formatierung für Berichte und Vorlagen ermöglichen.
{{% /alert %}}

## **Introduction**
Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellenkalkulationsdaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig expandiert die Engine das Array und platziert jedes Element in einer separaten angrenzenden Zelle, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (zum Beispiel `&=DataSource.Numbers`) – entweder horizontal über eine Zeile oder vertikal entlang einer Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzelnen Zelle rendern möchten, wobei die Elemente zusammengefügt und durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersagbar zu halten und gleichzeitig nativ mit Array-Datenquellen zu arbeiten.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise wird ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle platzieren, wodurch andere Vorlageninhalte nach außen verschoben und sorgfältig gestaltete Berichtslayouts möglicherweise beschädigt werden.

### **Use Case Limitations**
Es gibt viele praktische Szenarien, in denen das Standard-Spreizungsverhalten unerwünscht ist:
- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden sollen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte zur besseren Lesbarkeit an einem Ort gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzigen konsolidierten Wert pro Zelle erwarten, anstatt einen expandierten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die sich über mehrere Zellen erstrecken, nicht tolerieren können.

### **The Gap It Fills**
Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in C# oder VB.NET vorzuverarbeiten – Arrays zu getrennten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, verkompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diese Umgehungslösung, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst behandeln.

## **Feature Benefits**
Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:
- **Einzelzellen-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebiger benutzerdefinierter Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code zur Vorverarbeitung der Daten erforderlich; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumswerten und jedem anderen Datentyp, der mit einem Trennzeichen zusammengefügt werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Spreizungsverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **How to Use This Feature**

### **Smart Marker Syntax**
Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker besteht aus den folgenden Teilen:
- `&=DataSource.ArrayProperty` — der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` — weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellen-Verhalten aus.
- `extraDelimiter=", "` — definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenkettenliteral; er kann leer, ein einzelnes Zeichen oder eine mehrteilige Zeichenkette sein.

{{% alert color="primary" %}}
Das Attribut `extraDelimiter` akzeptiert jedes Zeichenkettenliteral, einschließlich mehrteiliger Trennzeichen, benutzerdefinierten Texts oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

### **Step-by-Step Workflow**
Der folgende Workflow beschreibt, wie ein Array mit Smart Markers in eine einzelne Zelle gerendert wird.
1. **Datenquelle vorbereiten**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `string[]`, `int[]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **WorkbookDesigner instanziieren**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe daran an und binden Sie Ihre Datenquelle mithilfe der Methode `SetDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.Process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe als XLSX oder in einem anderen unterstützten Dateiformat auf der Festplatte.

### **Code Example 1 — Basic String Array Rendering**

```csharp
using System;
using Aspose.Cells;
class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }
    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");
        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();
        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}
public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));
        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```csharp
using System;
using Aspose.Cells;
public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;
        // Section 1: Default Smart Marker - values spread horizontally across cells
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // Bind the data source and process Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // Save the resulting workbook
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes & Best Practices**
Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:
- Der Wert `extraDelimiter` wird als Zeichenkettenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellen-Verhalten aus; jeder andere Wert fällt auf das Standard-Spreizungsverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion arbeitet mit Objekt-Datenquellen sowie mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` oder `Environment.NewLine` als Trennzeichenwert verwenden.
{{% /alert %}}

## Related Articles
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for .NET hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for .NET anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Seitenfeldlayout in einer Pivot-Tabelle ändern](/cells/de/net/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for .NET konvertieren](/cells/de/net/convert-sparkline-to-image-and-html/)
- [Excel in das OFD-Format konvertieren](/cells/de/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}