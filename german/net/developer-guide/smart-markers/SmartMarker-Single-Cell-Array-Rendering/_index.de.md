---
title: SmartMarker Einzelzell-Array-Rendering | Aspose.Cells .NET
description: Erfahren Sie, wie Sie Array-Daten mithilfe der Attribute ArrayAsSingle und ExtraDelimiter in Smart Markers mit Aspose.Cells for .NET in eine einzelne Zelle rendern.
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzell-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, was eine flexible Formatierung für Berichte und Vorlagen ermöglicht.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellenkalkulationsdaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage vom `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (zum Beispiel `&=DataSource.Numbers`), erweitert die Engine das Array und platziert jedes Element in eine separate angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie es bevorzugen würden, das gesamte Array in einer einzelnen Zelle zu rendern, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersehbar zu halten, während Sie weiterhin nativ mit Array-Datenquellen arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standardmäßiges Array-Spreizverhalten**

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, erweitert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle, wodurch andere Vorlageninhalte nach außen gedrängt und möglicherweise sorgfältig gestaltete Berichtslayouts zerstört werden.

### **Einschränkungen bei Anwendungsfällen**

Es gibt viele praktische Szenarien, in denen das standardmäßige Spreizverhalten unerwünscht ist:

- **Zusammenfassungsartige Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden müssen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte zur besseren Lesbarkeit an einer Stelle gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzelnen konsolidierten Wert pro Zelle erwarten, anstatt einen erweiterten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die sich über mehrere Zellen erstrecken, nicht tolerieren können.

### **Die Lücke, die sie füllt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in C# oder VB.NET vorzuverarbeiten – Arrays in durch Trennzeichen getrennte Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert die Logik, kompliziert Datenmodelle und erhöht die Fehlerwahrscheinlichkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst handhaben.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzell-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersehbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebigen benutzerdefinierten Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code zur Vorverarbeitung der Daten erforderlich; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten drängen benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumswerten und allen anderen Datentypen, die mit einem Trennzeichen zusammengefügt werden können.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Spreizverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **Wie man diese Funktion verwendet**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax ist:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker setzt sich aus den folgenden Teilen zusammen:

- `&=DataSource.ArrayProperty` – der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` – weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellverhalten aus.
- `extraDelimiter=", "` – definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenkettenliteral; er kann leer, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette sein.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert beliebige Zeichenkettenliterale, einschließlich mehrzeichiger Trennzeichen, benutzerdefinierter Texte oder Escapesequenzen wie `\n` für zeilenumbruchgetrennte Ausgaben. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie ein Array mithilfe von Smart Markers in eine einzelne Zelle gerendert wird.

1. **Datenquelle vorbereiten**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `string[]`, `int[]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **WorkbookDesigner instanziieren**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe daran an und binden Sie Ihre Datenquelle mit der Methode `SetDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.Process()` auf, um die Smart Markers zu erweitern und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX- oder einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 — Einfaches Zeichenketten-Array-Rendering**

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

### **Codebeispiel 2 — Numerisches Array mit benutzerdefiniertem Trennzeichen**

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

### **Codebeispiel 3 — Vergleich des Standardverhaltens mit dem ArrayAsSingle-Verhalten**

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

        // Abschnitt 1: Standard-Smart-Marker - Werte werden horizontal über Zellen verteilt
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // Abschnitt 2: Neue Einzelzellendarstellung mit arrayasSingle und extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // Datenquelle binden und Smart Marker verarbeiten
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // Die resultierende Arbeitsmappe speichern
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **Hinweise & bewährte Verfahren**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert `extraDelimiter` wird als Zeichenkettenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellverhalten aus; jeder andere Wert fällt auf das standardmäßige Spreizverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion funktioniert mit Objektdatenquellen sowie mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für eine zeilenumbruchgetrennte Ausgabe können Sie `\n` oder `Environment.NewLine` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die eine ausreichende Breite hat, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.

## **Verwandte Artikel**

- [Smart Markers](/cells/de/net/smart-markers/)
- [Zellen zusammenführen und aufteilen](/cells/de/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}