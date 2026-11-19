---
title: SmartMarker-Darstellung eines Arrays in einer einzelnen Zelle | Aspose.Cells .NET
description: Erfahren Sie, wie Sie mit den Smart-Marker-Attributen arrayassingle und arraydelimiter in Aspose.Cells for .Net Arraydaten in einer einzelnen Zelle darstellen.
linktitle: SmartMarker-Arraydarstellung | Aspose.Cells
url: /de/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, .NET-Bibliothek, Tabellenkalkulation, Smart-Marker, arrayassingle, arraydelimiter, Einzelzell-Array, Array-Darstellung, Vorlage
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kann eine Array-Datenquelle mithilfe von Smart-Markern in einer einzigen Zelle darstellen. Das Attribut `arrayassingle` deaktiviert das standardmäßige elementweise Verteilen, und das Attribut `arraydelimiter` bestimmt das Trennzeichen zwischen den zusammengeführten Elementen – standardmäßig ein Komma oder ein von Ihnen angegebenes einzelnes Zeichen beziehungsweise eine mehrzeichige Zeichenkette in Anführungszeichen.
{{% /alert %}}

## **Einleitung**

Smart-Marker in Aspose.Cells sind eine vorlagenbasierte Funktion, mit der Tabellendaten dynamisch mithilfe von Markerausdrücken wie `&=DataSource.Field` befüllt werden. Der Marker wird in einer Designer-Arbeitsmappe platziert und beim Verarbeiten der Vorlage durch den `WorkbookDesigner` durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig wird ein Array ausgeweitet, wenn ein Smart Marker auf eine Arrayeigenschaft verweist (beispielsweise `&=Product.Tags`, das an ein `string[]` mit vier Werten gebunden ist), und die Engine platziert jedes Element in einer eigenen Zelle, wobei die Werte in der Spalte unterhalb des Markers vertikal verteilt werden. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle darstellen möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `arrayassingle` und `arraydelimiter`, die in den Klammern eines Smart Markers im Format `name:value` geschrieben werden, erfüllen genau diese Anforderung. Sie ermöglichen kompakte und vorhersehbare Berichtslayouts und arbeiten dabei weiterhin nativ mit Array-Datenquellen.

## **Warum diese Funktion benötigt wird**

### **Standardmäßiges Verteilen von Arrays**

Wenn ein Smart Marker auf eine Arrayeigenschaft verweist, verteilt Aspose.Cells das Array standardmäßig auf mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in einer eigenen Zelle unterhalb des Markers. Dadurch werden andere Vorlageninhalte nach außen verschoben und sorgfältig entworfene Berichtslayouts möglicherweise beeinträchtigt.

### **Einschränkungen bei Anwendungsfällen**

In vielen praktischen Szenarien ist das standardmäßige Verteilen unerwünscht:
- **Zusammenfassende Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Etikett- oder Stichwortlisten**, die innerhalb einer einzelnen Zelle als durch Komma oder senkrechten Strich getrennte Werte angezeigt werden sollen.
- **Filterchips oder Statusanzeigen**, die mehrere Werte zur besseren Lesbarkeit an einem Ort gruppieren.
- **Nachgelagerte Verarbeitungsketten** (CSV-Export, PDF-Darstellung, Serienmail), die einen einzelnen konsolidierten Wert pro Zelle statt eines ausgeweiteten Bereichs erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Verbraucher keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die Lücke, die diese Funktion schließt**

Ohne integrierten Mechanismus müssten Entwickler die Daten in C# oder VB.NET vorverarbeiten und Arrays vor der Bindung an den `WorkbookDesigner` in durch Trennzeichen getrennte Strings zusammenführen. Dies dupliziert die Logik, kompliziert die Datenmodelle und erhöht das Fehlerrisiko. Die Attribute `arrayassingle` und `arraydelimiter` beseitigen diesen Umweg, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst übernehmen.

## **Vorteile der Funktion**

Die Verwendung der Attribute `arrayassingle` und `arraydelimiter` in Ihren Smart Markern bietet mehrere Vorteile:
- **In einer einzigen Zelle**: Alle Arrayelemente werden in genau eine Zelle dargestellt, sodass Layouts kompakt und vorhersehbar bleiben.
- **Steuerung des Trennzeichens**: Legen Sie das gewünschte Trennzeichen fest – das Standardkomma, ein Semikolon, einen Bindestrich, einen senkrechten Strich oder eine mehrzeichige Zeichenkette in Anführungszeichen wie `" | "`.
- **Vorlagenbasierte Formatierung**: Für die Vorverarbeitung der Daten ist kein zusätzlicher Code erforderlich; die Formatierungsregeln stehen im Smart-Marker-Tag.
- **Übersichtlichere Berichte**: Arraydaten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielfältige Datentypen**: Funktioniert mit String-Arrays und numerischen Arrays aus Objekt-Datenquellen.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass vorhandene Vorlagen weiterhin unverändert funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**

Die Attribute `arrayassingle` und `arraydelimiter` verwenden die Attributgrammatik `name:value` von Aspose.Cells innerhalb der Klammern eines standardmäßigen Smart Markers. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Der Marker besteht aus den folgenden Teilen:
- `&=DataSource.ArrayProperty` – der standardmäßige Smart Marker, der auf die Arrayeigenschaft in der gebundenen Datenquelle verweist.
- `arrayassingle:true` – weist die Engine an, das gesamte Array in einer einzelnen Zelle darzustellen, statt die Elemente zu verteilen.
- `arraydelimiter:;` – optional; legt das Trennzeichen zwischen den Arrayelementen fest. Wenn es weggelassen wird, wird ein Komma verwendet.

{{% alert color="warning" %}}
Schreiben Sie Attribute im Format `name:value` (mit Doppelpunkt, nicht mit Gleichheitszeichen) und trennen Sie mehrere Attribute durch ein Komma **ohne Leerzeichen**. Ein Leerzeichen nach dem Komma verschiebt den analysierten Wert um ein Zeichen – `(arrayassingle:true, arraydelimiter:;)` würde mit dem fehlerhaften Trennzeichen `:;` statt `;` zusammengeführt.
{{% /alert %}}

### **Schreibweisen von Trennzeichen**

- Ein einzelnes Zeichen folgt unmittelbar auf den Doppelpunkt: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Ein mehrzeichiges Trennzeichen wird in doppelten Anführungszeichen geschrieben: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie Sie mithilfe von Smart Markern ein Array in einer einzigen Zelle darstellen.
1. **Datenquelle vorbereiten**: Erstellen Sie eine Klasse mit einer Eigenschaft, die ein Array zurückgibt, etwa `string[]` oder `int[]`, und binden Sie eine `List<T>` dieser Klasse, sodass die Engine pro Zeile einen Datensatz liest.
2. **Designer-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die mit dem Attribut `arrayassingle` auf die Arrayeigenschaft verweist (und `arraydelimiter` enthält, wenn ein benutzerdefiniertes Trennzeichen benötigt wird).
3. **WorkbookDesigner instanziieren**: Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe und binden Sie Ihre Datenquelle mit `SetDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.Process()` auf, um die Smart Marker zu verarbeiten und die Arbeitsmappe mit echten Daten zu füllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe im XLSX-Format oder einem anderen unterstützten Dateiformat auf der Festplatte.

### **Codebeispiel 1 – Grundlegende Darstellung eines String-Arrays**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

Das Beispiel gibt den zusammengeführten Wert des gesamten Arrays aus. Die vier Schlagwörter landen in einer Zelle und werden durch das Standardkomma getrennt:

```
C#,Aspose,SmartMarker,Excel
```

### **Codebeispiel 2 – Numerisches Array mit einem benutzerdefinierten Trennzeichen**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Numerische Arrays werden genauso zusammengeführt wie String-Arrays – jedes Element behält seinen einfachen numerischen Text:

```
95-88-76-100-67
```

### **Codebeispiel 3 – Vergleich der Standarddarstellung mit der Darstellung in einer einzelnen Zelle**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

Der Standardmarker füllt Spalte B untereinander mit einer Zelle pro Element, während der Marker `arrayassingle` dasselbe Array in Spalte C in einer einzigen Zelle zusammenfasst:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Hinweise und bewährte Vorgehensweisen**

Beachten Sie beim Arbeiten mit den Attributen `arrayassingle` und `arraydelimiter` die folgenden Punkte:
- Attributwerte verwenden das Format `name:value`. Die Form mit Gleichheitszeichen, etwa `arrayassingle=true`, wird nicht erkannt und fällt stillschweigend auf das standardmäßige Verteilungsverhalten zurück.
- Trennen Sie Attribute durch ein Komma ohne Leerzeichen; ein Leerzeichen nach dem Komma verschiebt den Wert des Trennzeichens um ein Zeichen (siehe Warnung oben).
- Der Wert von `arraydelimiter` kann ein einzelnes Zeichen sein, das unmittelbar nach dem Doppelpunkt geschrieben wird, oder eine mehrzeichige Zeichenkette in doppelten Anführungszeichen.
- Wird `arraydelimiter` weggelassen, werden die Elemente durch ein Komma zusammengeführt.
- Die Datenquelle muss der Engine ermöglichen, Datensätze aufzuzählen: Binden Sie eine `List<T>` (oder eine andere Sammlung), deren Elementtyp die Arrayeigenschaft verfügbar macht. Beim Binden eines einzelnen Objekts bleiben die Marker im Rumpf unaufgelöst.
- Dieselben Attribute funktionieren mit String- und numerischen Arrays; jedes Element wird mit seinem einfachen Werttext dargestellt.

## **Verwandte Artikel**
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for .NET hinzufügen](/cells/de/net/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for .NET anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Ändern des Seitenfeldlayouts in einer Pivot-Tabelle](/cells/de/net/change-page-field-layout/)
- [Sparkline in Aspose.Cells for .NET in Bild und HTML konvertieren](/cells/de/net/convert-sparkline-to-image-and-html/)
- [Konvertieren von Excel in das OFD-Format](/cells/de/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}