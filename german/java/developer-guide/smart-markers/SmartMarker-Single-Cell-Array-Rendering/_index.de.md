---
title: SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells Java
linktitle: SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells
description: Erfahren Sie, wie Sie Array-Daten mit den Attributen ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle rendern können mit Aspose.Cells for Java.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzellen-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, was eine flexible Formatierung für Berichte und Vorlagen ermöglicht.

{{% /alert %}}

## **Einführung**

Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellendaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage vom `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.

Standardmäßig, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (z. B. `&=DataSource.Numbers`), expandiert die Engine das Array und platziert jedes Element in eine eigene Zelle — entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie es vorziehen würden, das gesamte Array in eine einzelne Zelle zu rendern, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.

Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersagbar zu halten, während Sie weiterhin nativ mit Array-Datenquellen arbeiten.

## **Warum diese Funktion benötigt wird**

### **Standard-Array-Spreizverhalten**

Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in seine eigene Zelle, wodurch andere Vorlageninhalte nach außen gedrängt und sorgfältig gestaltete Berichtslayouts potenziell beschädigt werden.

### **Einschränkungen des Anwendungsfalls**

Es gibt viele praktische Szenarien, in denen das Standard-Spreizverhalten unerwünscht ist:

- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden müssen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte an einer Stelle zur besseren Lesbarkeit gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Serienbrief), die einen einzelnen konsolidierten Wert pro Zelle erwarten, anstatt einen erweiterten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die sich über mehrere Zellen erstrecken, nicht tolerieren können.

### **Die Lücke, die sie füllt**

Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in Java vorzuverarbeiten — Arrays zu getrennten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, kompliziert Datenmodelle und erhöht die Fehleranfälligkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diese Umgehungslösung, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst handhaben.

## **Funktionsvorteile**

Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:

- **Einzelzellen-Containment**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an — Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder einen beliebigen benutzerdefinierten Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code erforderlich, um die Daten vorzuverarbeiten; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten drängen benachbarte Vorlageninhalte nicht mehr in verschiedene Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Datumsangaben und jedem anderen Datentyp, der mit einem Trennzeichen verbunden werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, wird das ursprüngliche Spreizverhalten beibehalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **So verwenden Sie diese Funktion**

### **Smart-Marker-Syntax**

Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker besteht aus den folgenden Teilen:

- `&=DataSource.ArrayProperty` — der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` — weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellenverhalten aus.
- `extraDelimiter=", "` — definiert das Trennzeichen, das zwischen Array-Elementen platziert wird. Der Wert ist ein Zeichenkettenliteral; es kann leer, ein einzelnes Zeichen oder eine mehrteilige Zeichenkette sein.

{{% alert color="primary" %}}

Das Attribut `extraDelimiter` akzeptiert jedes Zeichenkettenliteral, einschließlich mehrteiliger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

{{% /alert %}}

### **Schritt-für-Schritt-Workflow**

Der folgende Workflow beschreibt, wie ein Array mit Smart Markers in eine einzelne Zelle gerendert wird.

1. **Bereiten Sie die Datenquelle vor**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `String[]`, `int[]` oder einen anderen unterstützten Array-Typ zurückgeben.
2. **Erstellen Sie eine Designer-Arbeitsmappe**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **Instanziieren Sie den WorkbookDesigner**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe an und binden Sie Ihre Datenquelle mit der Methode `setDataSource`.
4. **Verarbeiten Sie die Marker**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Speichern Sie das Ergebnis**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX-Format oder einem anderen unterstützten Dateiformat.

### **Codebeispiel 1 — Grundlegendes Zeichenketten-Array-Rendering**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Codebeispiel 2 — Numerisches Array mit benutzerdefiniertem Trennzeichen**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Codebeispiel 3 — Vergleich von Standard- vs. ArrayAsSingle-Verhalten**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Hinweise & bewährte Praktiken**

Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:

- Der Wert `extraDelimiter` wird als Zeichenkettenliteral behandelt; escapen Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellenverhalten aus; jeder andere Wert fällt auf das Standard-Spreizverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält eine leere Zeichenkette, abhängig vom Datentyp).
- Die Funktion funktioniert mit Objektdatenquellen sowie mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` oder `System.lineSeparator()` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle mit ausreichender Breite, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in angrenzende Zellen überlaufen.

## **Verwandte Artikel**

- [Smart Markers](/cells/de/java/smart-markers/)
- [Zellen verbinden und trennen](/cells/de/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}