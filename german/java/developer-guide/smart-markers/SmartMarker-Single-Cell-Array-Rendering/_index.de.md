---
title: Rendering eines SmartMarker-Arrays in einer einzelnen Zelle | Aspose.Cells for Java
description: Erfahren Sie, wie Sie mithilfe der Smart-Marker-Attribute `arrayassingle` und `arraydelimiter` in Aspose.Cells for Java Arraydaten in einer einzigen Zelle rendern.
linktitle: SmartMarker-Array in einer Zelle | Aspose.Cells
url: /de/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Smart Markers, arrayassingle, arraydelimiter, Array in einer Einzelzelle, Array-Rendering, Vorlage
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kann eine Array-Datenquelle mithilfe von Smart Markers in einer einzigen Zelle rendern. Das Attribut `arrayassingle` deaktiviert die standardmäßige elementweise Verteilung, und das Attribut `arraydelimiter` legt den Trenner fest, der zwischen den zusammengeführten Elementen platziert wird – standardmäßig ein Komma oder alternativ ein beliebiges einzelnes Zeichen oder eine von Ihnen angegebene Zeichenfolge aus mehreren Zeichen in Anführungszeichen.
{{% /alert %}}

## **Einleitung**

Smart Markers in Aspose.Cells sind eine vorlagenbasierte Funktion, die Tabellendaten dynamisch mithilfe von Markerausdrücken wie `&=DataSource.Field` befüllt. Der Marker wird in einer Entwurfs-Arbeitsmappe platziert. Wenn die Vorlage durch den `WorkbookDesigner` verarbeitet wird, werden die Marker durch Werte aus der bereitgestellten Datenquelle ersetzt.
Standardmäßig wird das Array erweitert, wenn ein Smart Marker auf eine Arrayeigenschaft verweist. Beispielsweise wird bei einem Marker wie `&=Product.Tags`, der an ein `String[]` mit vier Werten gebunden ist, jedes Element in einer eigenen Zelle abgelegt und die Werte unterhalb des Markers vertikal in der Spalte nach unten verteilt. Zwar ist dieses Verhalten in vielen Szenarien praktisch, in anderen Situationen ist es jedoch vorzuziehen, das gesamte Array in einer einzigen Zelle zu rendern, wobei die Elemente verkettet und durch ein Trennzeichen Ihrer Wahl getrennt werden.
Die Attribute `arrayassingle` und `arraydelimiter`, die in den Klammern eines Smart Markers in der Form `name:value` geschrieben werden, decken genau diesen Anforderungsfall ab. Sie ermöglichen kompakte und vorhersagbare Berichtslayouts und arbeiten gleichzeitig nativ mit Array-Datenquellen.

## **Warum diese Funktion erforderlich ist**

### **Standardverhalten bei der Arrayverteilung**

Wenn ein Smart Marker auf eine Arrayeigenschaft verweist, verteilt Aspose.Cells das Array standardmäßig über mehrere Zellen. Beispielsweise wird bei einem Marker wie `&=Product.Tags` und einem `String[]` mit vier Werten jeder Wert in einer eigenen Zelle unterhalb des Markers abgelegt. Dadurch werden andere Vorlageninhalte verschoben und sorgfältig entworfene Berichtslayouts möglicherweise beeinträchtigt.

### **Grenzen des Standardverhaltens**

Es gibt zahlreiche praktische Szenarien, in denen das standardmäßige Verteilungsverhalten unerwünscht ist:
- **Zusammenfassungsberichte**, die ein kompaktes Layout mit einer Zeile pro Datensatz benötigen.
- **Tag-, Label- oder Schlüsselwortlisten**, die in einer einzelnen Zelle als kommagetrennte oder Pipe-getrennte Werte angezeigt werden sollen.
- **Filterchips oder Statusindikatoren**, die mehrere Values zur besseren Lesbarkeit an einer Stelle gruppieren.
- **Nachgelagerte Verarbeitungspipelines** (CSV-Export, PDF-Rendering, Mailmerge), die pro Zelle einen einzelnen konsolidierten Wert statt eines erweiterten Bereichs erwarten.
- **Plattformübergreifende Kompatibilität**, bei der einige Verbraucher keine Arrays tolerieren können, die sich über mehrere Zellen erstrecken.

### **Die damit geschlossene Lücke**

Ohne einen integrierten Mechanismus müssten Entwickler die Daten in Java vorverarbeiten und Arrays vor der Bindung an den Workbook Designer in durch Trennzeichen getrennte Strings zusammenführen. Dadurch wird Logik dupliziert, werden Datenmodelle komplexer und steigt die Wahrscheinlichkeit von Fehlern. Die Attribute `arrayassingle` und `arraydelimiter` beseitigen diese Umgehungslösung, indem sie die Formatierung deklativ direkt im Smart Marker übernehmen.

## **Vorteile der Funktion**

Die Verwendung der Attribute `arrayassingle` und `arraydelimiter` in Smart Markers bietet mehrere Vorteile:
- **Inhalt in einer einzigen Zelle**: Alle Arrayelemente werden in genau einer Zelle gerendert, wodurch Layouts kompakt und vorhersagbar bleiben.
- **Individuelles Trennzeichen**: Geben Sie das gewünschte Trennzeichen an – das Standardkomma, ein Semikolon, einen Bindestrich, einen senkrechten Strich oder eine Zeichenfolge aus mehreren Zeichen in Anführungszeichen, beispielsweise `" | "`.
- **Vorlagenbasierte Formatierung**: Für die Vorverarbeitung der Daten ist kein zusätzlicher Code erforderlich; die Formatierungsregeln stehen im Smart-Marker-Tag.
- **Übersichtlichere Berichte**: Arraydaten verschieben benachbarte Vorlageninhalte nicht mehr in andere Zeilen oder Spalten.
- **Vielfältige Datentypen**: Die Funktion unterstützt Arrays aus Strings sowie numerische Werte aus Bean-Datenquellen, die als Strings dargestellt werden.
- **Abwärtskompatibilität**: Wenn die Attribute weggelassen werden, bleibt das ursprüngliche Verteilungsverhalten erhalten, sodass vorhandene Vorlagen unverändert weiter funktionieren.

## **Verwendung dieser Funktion**

### **Smart-Marker-Syntax**

Die Attribute `arrayassingle` und `arraydelimiter` verwenden innerhalb der Klammern eines standardmäßigen Smart Markers die Attributgrammatik `name:value` von Aspose.Cells. Die allgemeine Syntax lautet:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Der Marker besteht aus den folgenden Komponenten:
- `&=DataSource.ArrayProperty` — der standardmäßige Smart Marker, der auf die Arrayeigenschaft der gebundenen Datenquelle verweist.
- `arrayassingle:true` — weist die Engine an, das gesamte Array in einer einzigen Zelle zu rendern, anstatt die Elemente zu verteilen.
- `arraydelimiter:;` — optional; definiert das Trennzeichen zwischen den Arrayelementen. Wenn dieser Teil weggelassen wird, wird ein Komma verwendet.

{{% alert color="warning" %}}
Schreiben Sie die Attribute in der Form `name:value` (mit einem Doppelpunkt, nicht mit einem Gleichheitszeichen) und trennen Sie mehrere Attribute durch ein Komma **ohne Leerzeichen**. Ein Leerzeichen nach dem Komma verschiebt den geparsten Wert um ein Zeichen – `(arrayassingle:true, arraydelimiter:;)` würde mit dem fehlerhaften Trenner `:;` anstelle von `;` verbinden.
{{% /alert %}}

### **Formen des Trennzeichens**

- Ein einzelnes Zeichen wird direkt nach dem Doppelpunkt angegeben: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Ein Trenner aus mehreren Zeichen wird in doppelten Anführungszeichen angegeben: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Schritt-für-Schritt-Arbeitsablauf**

Der folgende Arbeitsablauf beschreibt, wie ein Array mithilfe von Smart Markers in einer einzigen Zelle gerendert wird.
1. **Datenquelle vorbereiten**: Erstellen Sie eine öffentliche Bean-Klasse mit einem Getter, der das Array zurückgibt, z. B. `String[] getTags()`, und binden Sie eine `java.util.List` von Beans, damit die Engine pro Zeile einen Datensatz liest. Öffentliche Felder allein werden nicht gebunden – die Engine liest JavaBean-Getter.
2. **Entwurfs-Arbeitsmappe erstellen**: Erstellen Sie eine neue `Workbook`, fügen Sie eine Kopfzeile hinzu und platzieren Sie eine Smart-Marker-Zelle, die mit dem Attribut `arrayassingle` auf die Arrayeigenschaft verweist (und bei Bedarf `arraydelimiter` enthält).
3. **WorkbookDesigner instanziieren**: Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe und binden Sie Ihre Liste mit `setDataSource`.
4. **Marker verarbeiten**: Rufen Sie die Methode `WorkbookDesigner.process()` auf, um die Smart Marker zu erweitern und die Arbeitsmappe mit realen Daten zu befüllen.
5. **Ergebnis speichern**: Speichern Sie die resultierende Arbeitsmappe im XLSX-Format oder in einem anderen unterstützten Dateiformat auf dem Datenträger.

### **Codebeispiel 1 – Grundlegendes Rendering eines `String`-Arrays**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

Das Beispiel gibt den durch Zusammenführung gebildeten Wert des gesamten Arrays aus. Die vier Schlagwörter werden in einer Zelle durch das Standardkomma getrennt dargestellt:

```
C#,Aspose,SmartMarker,Excel
```

### **Codebeispiel 2 – Zahlenwerte mit einem benutzerdefinierten Trennzeichen**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Numerische Werte werden genauso zusammengeführt wie Strings, wenn die Arrayeigenschaft `String[]` zurückgibt:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Verwenden Sie die Arrayeigenschaft in Java weiterhin als `String[]`. Eine primitive `int[]`-Eigenschaft, die in einer einzigen Zelle zusammengeführt wird, rendert den `toString`-Text des Arrayobjekts (zum Beispiel `[I@1a2b3c4d`) anstelle der Zahlen, da die Zusammenführung auf der String-Form jedes Elements beruht und ein primitives Array ein undurchsichtiges Einzelelement ist.
{{% /alert %}}

### **Codebeispiel 3 – Vergleich des Standard-Renderings mit dem Rendering in einer einzigen Zelle**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

Der Standardmarker füllt in Spalte B nach unten eine Zelle pro Element, während der `arrayassingle`-Marker dasselbe Array in einer einzigen Zelle in Spalte C zusammenfasst:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Hinweise und bewährte Vorgehensweisen**

Beachten Sie beim Arbeiten mit den Attributen `arrayassingle` und `arraydelimiter` die folgenden Punkte:
- Attributwerte verwenden die Form `name:value`. Eine Form mit Gleichheitszeichen, z. B. `arrayassingle=true`, wird nicht erkannt und fällt stillschweigend auf das standardmäßige Verteilungsverhalten zurück.
- Trennen Sie Attribute durch ein Komma ohne Leerzeichen; ein Leerzeichen nach dem Komma verschiebt den Trennerwert um ein Zeichen (siehe die Warnung oben).
- Der Wert von `arraydelimiter` kann ein einzelnes Zeichen sein, das direkt nach dem Doppelpunkt steht, oder eine Zeichenfolge aus mehreren Zeichen in doppelten Anführungszeichen.
- Wenn `arraydelimiter` weggelassen wird, werden die Elemente durch ein Komma verbunden.
- Binden Sie eine `java.util.List` öffentlicher JavaBeans mit Array-Gettern. Ein einzelnes Bean-Objekt oder öffentliche Felder allein lassen die Marker nicht aufgelöst.
- Behalten Sie Arrayeigenschaften als `String[]` bei; bei einem primitiven `int[]` wird beim Zusammenführen dessen `toString`-Text gerendert (siehe den Hinweis oben).
- Platzieren Sie den Smart Marker in einer Zelle, die breit genug ist, um den resultierenden verketteten String anzuzeigen; andernfalls kann der Inhalt je nach Format visuell in benachbarte Zellen überlaufen.

## **Verwandte Artikel**
- [Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for Java hinzufügen](/cells/de/java/add-page-field-in-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen in Aspose.Cells for Java](/cells/de/java/apply-style-to-pivot-table/)
- [Ändern des Seitenfeldlayouts in einer Pivot-Tabelle](/cells/de/java/change-page-field-layout/)
- [Sparkline in Bild und HTML in Aspose.Cells for Java konvertieren](/cells/de/java/convert-sparkline-to-image-and-html/)
- [Konvertieren von Excel in das OFD-Format](/cells/de/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}