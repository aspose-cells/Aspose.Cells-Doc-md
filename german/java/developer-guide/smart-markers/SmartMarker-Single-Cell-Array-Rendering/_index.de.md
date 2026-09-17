---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells Java
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells Java
description: Erfahren Sie, wie Sie Array-Daten mit den Attributen ArrayAsSingle und ExtraDelimiter in Smart Markers in eine einzelne Zelle rendern mit Aspose.Cells for Java.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Smart Markers, ArrayAsSingle, ExtraDelimiter, Einzelzell-Array, Array-Rendering, Vorlage
type: docs
weight: 195
url: /de/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Rendern von Array-Daten in eine einzelne Zelle über Smart Markers. Durch die Verwendung des Attributs `ArrayAsSingle` zusammen mit dem Attribut `ExtraDelimiter` können Entwickler steuern, wie Array-Elemente innerhalb einer einzelnen Zelle getrennt werden, und erhalten so eine flexible Formatierung für Berichte und Vorlagen.

## **Introduction**
Smart Markers in Aspose.Cells sind eine leistungsstarke, vorlagenbasierte Funktion, mit der Sie Tabellendaten dynamisch mithilfe von Marker-Ausdrücken wie `&=DataSource.Field` befüllen können. Der Marker wird in einer Designer-Arbeitsmappe platziert, und wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig expandiert die Engine das Array, wenn ein Smart Marker auf eine Array-Eigenschaft verweist (zum Beispiel `&=DataSource.Numbers`), und platziert jedes Element in eine separate angrenzende Zelle – entweder horizontal über eine Zeile oder vertikal über eine Spalte. Obwohl dieses Verhalten in vielen Szenarien praktisch ist, gibt es Situationen, in denen Sie das gesamte Array lieber in einer einzigen Zelle rendern möchten, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `ArrayAsSingle` und `ExtraDelimiter`, die zusammen innerhalb eines Smart-Marker-Tags verwendet werden, erfüllen genau diese Anforderung. Sie ermöglichen es Ihnen, Berichtslayouts kompakt und vorhersagbar zu halten und gleichzeitig nativ mit Array-Datenquellen zu arbeiten.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Wenn ein Smart Marker auf eine Array-Eigenschaft verweist, expandiert Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise platziert ein Marker wie `&=Product.Tags` bei einem `string[]` mit vier Werten jeden Wert in eine eigene Zelle, wodurch andere Vorlageninhalte nach außen gedrängt und sorgfältig gestaltete Berichtslayouts möglicherweise beschädigt werden.

### **Use Case Limitations**
Es gibt viele praktische Szenarien, in denen das standardmäßige Spreizverhalten unerwünscht ist:
- **Zusammenfassungsartige Berichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Beschriftungs- oder Stichwortlisten**, die als kommagetrennte oder pipe-getrennte Werte innerhalb einer einzelnen Zelle angezeigt werden müssen.
- **Filter-Chips oder Statusindikatoren**, die mehrere Werte zur besseren Lesbarkeit an einem Ort gruppieren.
- **Nachgelagerte Pipelines** (CSV-Export, PDF-Rendering, Seriendruck), die einen einzigen konsolidierten Wert pro Zelle erwarten, anstatt einen expandierten Bereich.
- **Plattformübergreifende Kompatibilität**, bei der einige Konsumenten Arrays, die sich über mehrere Zellen erstrecken, nicht tolerieren können.

### **The Gap It Fills**
Ohne einen eingebauten Mechanismus wären Entwickler gezwungen, Daten in Java vorzuverarbeiten – Arrays zu begrenzten Zeichenketten zusammenzufügen, bevor sie sie an den Workbook-Designer binden. Dies dupliziert Logik, verkompliziert Datenmodelle und erhöht die Fehleranfälligkeit. Die Attribute `ArrayAsSingle` und `ExtraDelimiter` beseitigen diesen Workaround, indem sie die Formatierung deklarativ innerhalb des Smart Markers selbst handhaben.

## **Feature Benefits**
Die Verwendung der Attribute `ArrayAsSingle` und `ExtraDelimiter` in Ihren Smart Markers bietet mehrere Vorteile:
- **Einzelne Zellenkapselung**: Alle Array-Elemente werden in genau eine Zelle gerendert, wodurch die Layouts kompakt und vorhersagbar bleiben.
- **Benutzerdefinierte Trennzeichensteuerung**: Geben Sie eine beliebige Trennzeichenfolge an – Komma, Semikolon, Bindestrich, Pipe, Zeilenumbruch oder beliebiger benutzerdefinierter Text.
- **Vorlagengesteuerte Formatierung**: Es ist kein zusätzlicher Code erforderlich, um die Daten vorzuverarbeiten; Formatierungsregeln leben innerhalb des Smart-Marker-Tags.
- **Sauberere Berichte**: Array-Daten drängen benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielseitige Datentypen**: Funktioniert mit Zeichenketten, Zahlen, Daten und jeden anderen Datentyp, der mit einem Trennzeichen zusammengefügt werden kann.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Spreizverhalten erhalten, sodass bestehende Vorlagen unverändert weiter funktionieren.

## **How to Use This Feature**

### **Smart Marker Syntax**
Die Attribute `ArrayAsSingle` und `ExtraDelimiter` werden als Schlüssel-Wert-Paare innerhalb der Klammern eines Standard-Smart-Markers übergeben. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Der Marker setzt sich aus den folgenden Teilen zusammen:
- `&=DataSource.ArrayProperty` — der Standard-Smart-Marker, der auf die Array-Eigenschaft der gebundenen Datenquelle verweist.
- `arrayasSingle=true` — weist die Engine an, das gesamte Array in eine einzelne Zelle zu rendern. Nur der Wert `true` löst das Einzelzellverhalten aus.
- `extraDelimiter=", "` — definiert das Trennzeichen, das zwischen den Array-Elementen platziert wird. Der Wert ist ein Zeichenkettenliteral; er kann leer sein, ein einzelnes Zeichen oder eine mehrzeichige Zeichenkette.

{{% alert color="primary" %}}
Das Attribut `extraDelimiter` akzeptiert jedes Zeichenkettenliteral, einschließlich mehrzeichiger Trennzeichen, benutzerdefiniertem Text oder Escape-Sequenzen wie `\n` für zeilenumbruchgetrennte Ausgabe. Wenn das Array leer ist, bleibt die resultierende Zelle leer.

### **Step-by-Step Workflow**
Der folgende Workflow beschreibt, wie Sie ein Array mit Smart Markers in eine einzelne Zelle rendern.
1. **Bereiten Sie die Datenquelle vor**: Erstellen Sie eine Klasse (oder Datenstruktur), die eine Eigenschaft bereitstellt, die ein Array zurückgibt. Die Eigenschaft kann `String[]`, `int[]` oder jeden anderen unterstützten Array-Typ zurückgeben.
2. **Erstellen Sie eine Designer-Arbeitsmappe**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die auf die Array-Eigenschaft mit den Attributen `arrayasSingle` und `extraDelimiter` verweist.
3. **Instanziieren Sie den WorkbookDesigner**: Erstellen Sie ein `WorkbookDesigner`-Objekt, hängen Sie die Designer-Arbeitsmappe daran an und binden Sie Ihre Datenquelle mit der Methode `setDataSource`.
4. **Verarbeiten Sie die Marker**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart Markers zu expandieren und die Arbeitsmappe mit echten Daten zu befüllen.
5. **Speichern Sie das Ergebnis**: Speichern Sie die resultierende Arbeitsmappe auf der Festplatte im XLSX- oder einem anderen unterstützten Dateiformat.

### **Code Example 1 — Basic String Array Rendering**

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

### **Code Example 2 — Numeric Array with Custom Delimiter**

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

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

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

### **Notes & Best Practices**
Beachten Sie die folgenden Punkte, wenn Sie mit den Attributen `ArrayAsSingle` und `ExtraDelimiter` arbeiten:
- Der Wert `extraDelimiter` wird als Zeichenkettenliteral behandelt; maskieren Sie alle Sonderzeichen, die Ihr Vorlagenprozessor interpretieren könnte.
- Das Attribut `arrayasSingle` akzeptiert einen booleschen Wert (`true` / `false`). Nur `true` löst das Einzelzellverhalten aus; jeder andere Wert fällt auf das standardmäßige Spreizverhalten zurück.
- Wenn das Array leer oder null ist, bleibt die Zelle leer (oder enthält je nach Datentyp eine leere Zeichenkette).
- Die Funktion funktioniert mit Objekt-Datenquellen sowie mit `DataSet`- und `DataTable`-Quellen, bei denen eine Spalte in Arrays aufgeteilt werden kann.
- Für zeilenumbruchgetrennte Ausgabe können Sie `\n` oder `System.lineSeparator()` als Trennzeichenwert verwenden.
- Platzieren Sie den Smart Marker in einer Zelle, die ausreichend breit ist, um die resultierende verkettete Zeichenkette anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Filter-Felder zu einer Pivot-Tabelle in Aspose.Cells for Java hinzufügen](/cells/de/java/add-page-field-in-pivot-table/)
- [Stile auf Pivot-Tabellen in Aspose.Cells for Java anwenden](/cells/de/java/apply-style-to-pivot-table/)
- [Seitenfeldlayout in der Pivot-Tabelle ändern](/cells/de/java/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for Java konvertieren](/cells/de/java/convert-sparkline-to-image-and-html/)
- [Excel in das OFD-Format konvertieren](/cells/de/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}