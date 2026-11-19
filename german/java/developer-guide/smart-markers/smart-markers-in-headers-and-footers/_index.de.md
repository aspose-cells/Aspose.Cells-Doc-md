---
title: Smart Marker in Kopf- und Fußzeilen | Aspose.Cells for Java
linktitle: Kopf- und Fußzeilen-Smart-Marker | Aspose.Cells
description: Platzieren Sie Smart-Marker-Platzhalter in Seiten-Kopf- und Fußzeilen mit der Doppel-Spitze-Klammer-Syntax und dem Schalter WorkbookDesigner.setEnableHeaderFooterMarkers unter Verwendung von Getter-Bean-Listen oder JSON-Datenquellen und binden Sie Bilder über Daten-URIs ein, in Aspose.Cells for Java.
keywords: Aspose.Cells for Java, Smart Marker, Kopfzeilen, Fußzeilen, Header-Footer-Marker, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, Getter-Bean, JSON-Datenquelle, Datenbindung, Bild, Daten-URI, Java
type: docs
weight: 196
url: /de/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsszenarien**
Seiten-Kopf- und Fußzeilen enthalten üblicherweise Berichts-Metadaten wie den Berichtstitel, den Berichtszeitraum, den Autor und die Abteilung. Wenn diese Informationen bereits in der Datenquelle vorhanden sind, die zum Befüllen der Arbeitsmappe verwendet wird, führt das manuelle Wiederholen zu unnötiger Duplizierung.  
Die klassische Smart-Marker-Syntax `&=Source.Field` wird in den Arbeitsblatt-Körperzellen verarbeitet. Wenn Sie einen klassischen Marker über `PageSetup.setHeader` oder `PageSetup.setFooter` in einer Kopf- oder Fußzeile platzieren, bleibt er unverändert als Text erhalten, weil Kopf- und Fußzeilen-Zeichenketten nicht Teil des Worksheet-Zellrasters sind, das von `WorkbookDesigner.process()` durchsucht wird.  
Ab **Aspose.Cells for Java 26.11** ist die `WorkbookDesigner`-Option für Kopf-/Fußzeilen-Marker standardmäßig auf `false` gesetzt. Rufen Sie `designer.setEnableHeaderFooterMarkers(true)` auf, bevor Sie `designer.process()` aufrufen, um Platzhalter, die als `<<Source.Field>>` in den Kopf- und Fußzeilen-Abschnitts-Zeichenketten geschrieben wurden, aufzulösen. Kopf- und Fußzeilen-Platzhalter verwenden dieselbe Datenquelle wie Arbeitsblatt-Marker.  
Jede Kopf- und Fußzeile enthält drei adressierbare Abschnitte:
- Abschnitt `0` ist der linke Abschnitt.
- Abschnitt `1` ist der mittlere Abschnitt.
- Abschnitt `2` ist der rechte Abschnitt.  
Verwenden Sie `PageSetup.setHeader(int section, String value)` und `PageSetup.setFooter(int section, String value)`, um diese Abschnitte zu schreiben. Nach der Verarbeitung nutzen Sie `PageSetup.getHeader(int section)` und `PageSetup.getFooter(int section)`, um den fertigen Text abzurufen.

{{% alert color="primary" %}}
Ein Platzhalter wie `<<Source.Field>>` fügt den Feldwert als Text in die Abschnittszeichenkette ein. Bilder werden mit dem Suffix `(picture)` und einem Daten-URI-Wert gebunden.
{{% /alert %}}

## **Kopf-/Fußzeilen-Marker mit einer Getter-Bean-Liste aktivieren**
Verwenden Sie die folgende Reihenfolge, um Kopf- und Fußzeilen-Platzhalter mithilfe einer Getter-Bean-Liste in **Aspose.Cells for Java 26.11** aufzulösen:
1. Erstellen Sie ein `Workbook` und erhalten Sie das erste `Worksheet` am Index `0`, zum Beispiel mit `workbook.getWorksheets().get(0)`.
2. Schreiben Sie `<<Source.Field>>`-Platzhalter in die gewünschten Kopf- und Fußzeilen-Abschnitte mit `PageSetup.setHeader` und `PageSetup.setFooter`.
3. Definieren Sie eine kleine PUBLIC-Bean-Klasse mit einem Getter (z. B. `getName()`) für jedes Platzhalter-Feld und wählen Sie einen Quell-Namen, der dem Präfix der Platzhalter entspricht. Beispielsweise unterstützt eine Quelle mit dem Namen `node` Platzhalter wie `<<node.Name>>`. Zwei Bindungsregeln werden auf dieser Plattform verifiziert: Eine Bean mit öffentlichen FIELDS bindet nichts (die Engine liest Getter, nicht Felder), und eine PACKAGE-PRIVATE-Klasse bindet ebenfalls nichts — die Introspektion sieht nur öffentliche Klassen, und eine nicht-öffentliche Bean führt zu einer NullPointerException bei `process()`.
4. Erstellen Sie einen `WorkbookDesigner` für die Arbeitsmappe.
5. Rufen Sie `designer.setEnableHeaderFooterMarkers(true)` vor der Verarbeitung auf.
6. Verbinden Sie die Liste und ihren Quell-Namen mit `designer.setDataSource("node", table)`.
7. Rufen Sie `designer.process()` auf.
8. Nach der Verarbeitung sind die Platzhalter nicht mehr im Kopf- oder Fußzeilentext vorhanden. Verwenden Sie `PageSetup.getHeader` und `PageSetup.getFooter`, um die fertigen Abschnitts-Zeichenketten abzurufen.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **JSON-Datenquelle verwenden**
Sie können JSON anstelle einer Getter-Bean-Liste nutzen, wenn die Berichtsdaten bereits im JSON-Format vorliegen. Rufen Sie `WorkbookDesigner.setJsonDataSource(String name, String json)` auf, um die Quelle anzuhängen.  
Das Argument `name` ist der Quell-Name, der von den Platzhaltern verwendet wird. Beispielsweise unterstützt der Name `node` Platzhalter wie `<<node.Company>>` und `<<node.Title>>`.  
Übergeben Sie Zeilendaten direkt an `setJsonDataSource`:
- Ein Zeilen-Array, z. B. ein JSON-Array mit einem oder mehreren Zeilen-Objekten, wird unterstützt.
- Ein einzelnes Zeilen-Objekt kann ebenfalls direkt übergeben werden.
- Wickeln Sie die Zeilen nicht unter einem benannten Top-Level-Schlüssel wie `{"rows":[...]}` ein. Dieser Wrapper entspricht nicht dem erwarteten zeilenorientierten Eingabeformat für diesen Workflow.  
Eine JSON-Quelle kann beide Marker-Stile während desselben `designer.process()`-Aufrufs befüllen. Sie kann einen klassischen `&=`-Marker in einer Arbeitsblatt-Körperzelle und Doppel-Spitze-Klammer-Platzhalter `<<>>` in Kopf- und Fußzeilen-Abschnitten auflösen. Sie müssen dennoch `EnableHeaderFooterMarkers` aktivieren, damit die Kopf- und Fußzeilen-Platzhalter aufgelöst werden.

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **Schalter und Mehrzeilen-Quell-Semantik**
Die Einstellung `EnableHeaderFooterMarkers` ist standardmäßig auf `false` gesetzt, und der Schalter steuert ausschließlich die Kopf-/Fußzeilen-Platzhalter `<<Source.Field>>`. Ist der Schalter deaktiviert, löst `designer.process()` weiterhin klassische `&=`-Body-Marker auf, aber ein `<<Source.Field>>`-Platzhalter in einer Kopf- oder Fußzeile bleibt unverändert als Text.  
Ein Kopf- oder Fußzeilen-Abschnitt ist eine einzelne Zeichenkette, kein wiederholendes Band. Enthält die Datenquelle mehrere Zeilen, liefert die erste Zeile die Werte für Kopf- und Fußzeile. Sobald sie aufgelöst sind, werden die Werte zu gewöhnlichem Kopf- bzw. Fußzeilentext. Sie bleiben in der Arbeitsmappe erhalten, nachdem Sie `workbook.save(...)` aufgerufen haben, und sind beim erneuten Laden des gespeicherten Workbooks vorhanden.  
Das folgende Beispiel erstellt zwei Arbeitsmappen mit derselben Mehrzeilen-Bean-Liste, um das Verhalten mit deaktiviertem bzw. aktiviertem Schalter zu vergleichen. Der `plainDesigner` lässt den Platzhalter unverändert, während der `enabledDesigner` ihn mithilfe der ersten Zeile auflöst.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **Bild in eine Kopf- oder Fußzeile einbinden**
Das Suffix `(picture)` bindet ein Bild in einen Kopf- oder Fußzeilen-Abschnitt ein. Schreiben Sie `<<node.logo(picture)>>` an die Stelle, an der das Bild erscheinen soll, und stellen Sie den Feldwert als Daten-URI bereit — das Präfix `data:image/png;base64,` gefolgt vom Base64-Text der Bild-Bytes. Eine reine Base64-Zeichenkette ohne das `data:`-Präfix bettet kein Bild ein.  
Nach `designer.process()`:
1. Der Platzhalter wird durch `&G` ersetzt, den standardmäßigen Bild-Code für Kopf- und Fußzeilen. Da der Marker zu einem Code innerhalb der Abschnittszeichenkette wird, kann er in längerem Text wie `Logo: <<node.logo(picture)>>` vorkommen.
2. Die Bild-Bytes werden im Arbeitsmappe als Media-Teil dem Zeichen-Layer der Kopf-/ Fußzeile dieses Arbeitsblatts beigefügt, sodass das Bild beim Drucken mit der Kopf- bzw. Fußzeile erscheint.

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

Der gedruckte `&G` ist der Bild-Code, den Excel beim Rendern der Kopfzeile interpretiert — die `logo.png`-Bytes leben jetzt in `HeaderFooterPicture.xlsx` und das Bild wird anstelle des Codes gedruckt.  
Um Kopf- und Fußzeilen-Smart-Marker zu verwenden, schreiben Sie `<<Source.Field>>`-Platzhalter in die linken, mittleren und rechten Kopf- bzw. Fußzeilen-Abschnitte mit `PageSetup.setHeader` und `PageSetup.setFooter`. Rufen Sie `designer.setEnableHeaderFooterMarkers(true)` auf dem `WorkbookDesigner` auf, bevor Sie `designer.process()` ausführen, und stellen Sie Werte über `designer.setDataSource(name, list)` mit einer Getter-Bean-Liste oder `designer.setJsonDataSource(name, json)` bereit. Lesen Sie die fertigen Abschnitte mit `PageSetup.getHeader` und `PageSetup.getFooter`. dieselbe Datenquelle kann sowohl Arbeitsblatt-Marker als auch Kopf-/Fußzeilen-Platzhalter in einem Verarbeitungsdurchlauf befüllen. Fügen Sie das Suffix `(picture)` mit einem Daten-URI-Wert hinzu, um ein Bild in einen Abschnitt zu binden.

## Verwandte Artikel
- [SmartMarker-Einzelzellen-Array-Rendering](/cells/de/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}