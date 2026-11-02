---
title: Werte anzeigen als in Pivot-Tabelle
linktitle: Werte anzeigen als in Pivot-Tabelle
description: Zeigt Werte von Datenfeldern einer Pivot-Tabelle als Prozentsatz der Gesamtsumme, als Unterschied zu einem Basiselement, laufende Summen, Ranglisten und mehr mit Aspose.Cells for Java an.
keywords: Aspose.Cells, Pivot-Tabelle, Werte anzeigen als, Datenanzeigeformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /de/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine Pivot‑Tabelle aggregiert jedes Datenfeld normalerweise mit einer Aggregatfunktion wie `Sum` oder `Count`. Die Excel‑Funktion **Show Values As** ersetzt jedes angezeigte Ergebnis durch eine sekundäre Berechnung, die aus dieser Aggregation abgeleitet wird – zum Beispiel ein Prozentsatz der Gesamtsumme, eine laufende Summe, ein Unterschied zu einem ausgewählten Basiselement oder ein Rang – sodass Sie vergleichende Analysen ohne Hilfsspalten oder berechnete Spalten durchführen können. Typische Anwendungen umfassen Anteil‑am‑Gesamt‑Analysen, einschließlich Prozentsätze einer Zeile, Spalte oder Gesamtsumme; kumulative Berichte mit einer laufenden Summe in einem Periodenfeld; Abweichungsanalysen gegenüber einem Benchmark‑Element mittels Unterschied oder prozentualer Unterschied von einem Basiselement; sowie das Rangordnen von Werten vom Kleinsten zum Größten oder umgekehrt. In Aspose.Cells for Java wählt `PivotFieldDataDisplayFormat` die sekundäre Berechnung aus. Der schreibgeschützte Getter `PivotField.getShowValuesSetting()` liefert ein `PivotShowValuesSetting`‑Objekt, dessen Methoden `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` und `setBaseItemIndex(...)` das Verhalten konfigurieren; die Komfortmethode `PivotField.showValuesAs(...)` wendet dieselben vier Einstellungen in einem Aufruf an. Wenden Sie diese Einstellungen auf ein Daten‑ oder Werte‑Feld an, das Sie über `PivotTable.getDataFields()` erhalten.

## **PivotFieldDataDisplayFormat‑Aufzählungsmitglieder**
Das Datenfeld behält seine Aggregatfunktion, z. B. Summe oder Anzahl, während **Show Values As** nur die Anzeige des aggregierten Wertes verändert. Neben der direkten Verwendung der `PivotShowValuesSetting`‑Setter (vgl. den letzten Abschnitt) wendet eine einmalige Komfortmethode dieselbe Konfiguration an:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Parameter | Bedeutung | Wenn erforderlich |
| --- | --- | --- |
| `displayFormat` | Die sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat`, die angewendet werden soll. | Immer. |
| `baseField` | Nullbasierter Index des Basisfeldes unter den Basisfeldern der Pivot‑Tabelle (z. B. der Index des Zeilenfeldes, zu dem das Basis‑Item gehört). | Nur für die sechs unten aufgeführten basisbezogenen Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); von allen anderen Formaten wird es ignoriert. |
| `baseItemPositionType` | Wie das Basis‑Item relativ zum aktuellen Item ausgewählt wird: `PivotItemPositionType.PREVIOUS`, `NEXT` oder `CUSTOM`. | Nur für die drei Basis-Element-Formate (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); von allen anderen Formaten wird es ignoriert. |
| `baseItem` | Nullbasierter Index des Basis‑Items. | Nur wenn `baseItemPositionType` auf `CUSTOM` gesetzt ist (der Index wählt das exakte Basis‑Item); bei `PREVIOUS` / `NEXT` und allen nicht‑Basis‑Formaten ignoriert – übergeben Sie `0`. |

| Berechnungstyp | Verhalten | Basis‑Item‑Parameter |
| --- | --- | --- |
| `NORMAL` | Keine sekundäre Berechnung; der aggregierte Wert wird unverändert angezeigt (Standard). | — |
| `DIFFERENCE_FROM` | Zeigt den Wert als Differenz zum Wert eines Basis‑Items in einem Basis‑Feld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `PERCENTAGE_OF` | Zeigt den Wert als Prozentsatz des Wertes eines Basis‑Items in einem Basis‑Feld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Zeigt den Wert als prozentuale Differenz zum Wert eines Basis‑Items in einem Basis‑Feld an. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` nur bei `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Zeigt den Wert als laufende Summe für aufeinanderfolgende Items eines Basis‑Feldes an. | `baseField` (das Feld, dessen Item‑Reihenfolge die Akkumulation bestimmt) |
| `PERCENTAGE_OF_ROW` | Zeigt den Wert als Prozentsatz der Zeilensumme an. | — |
| `PERCENTAGE_OF_COLUMN` | Zeigt den Wert als Prozentsatz der Spaltensumme an. | — |
| `PERCENTAGE_OF_TOTAL` | Zeigt den Wert als Prozentsatz der Gesamtsumme an. | — |
| `INDEX` | Zeigt den Wert mithilfe der Excel‑Index‑Formel ((Wert * Gesamtsumme) / (Zeilensumme * Spaltensumme)) an. | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Zeilensumme an (für verschachtelte Zeilenfelder). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Spaltensumme an (für verschachtelte Spaltenfelder). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Zeigt den Wert als Prozentsatz der übergeordneten Gesamtsumme an. | `baseField` (das übergeordnete Referenzfeld) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Zeigt den Wert als Prozentsatz einer laufenden Summe in einem Basis‑Feld an. | `baseField` (das Akkumulationsfeld) |
| `RANK_SMALLEST_TO_LARGEST` | Rangiert den Wert vom Kleinsten (1) zum Größten. | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangiert den Wert vom Größten (1) zum Kleinsten. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` setzt die Werte von `PivotShowValuesSetting` über `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` und `setBaseItemIndex(...)` – die Methode und das Property‑Objekt sind zwei Wege, denselben Zustand zu konfigurieren, analog zu den Basis‑Feld‑ und Basis‑Item‑Auswahlen im Dialogfeld **Show Values As** von Excel.
{{% /alert %}}

## **Werte als Prozentsatz der Gesamtsumme anzeigen**
Rufen Sie die Methode `PivotField.showValuesAs(...)` mit `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` auf, um jede Zelle des Datenfeldes, einschließlich der Gesamtsumme, in ihren Anteil an der Gesamtsumme zu konvertieren. Die angezeigten Zahlen stellen somit Anteile des gesamten Ergebnis‑Sets dar. Dieses Format misst jeden Wert ausschließlich gegen die Gesamtsumme, sodass kein Basis‑Feld oder Basis‑Item erforderlich ist – die nachfolgenden Argumente (`0`, `PivotItemPositionType.PREVIOUS`, `0`) sind Platzhalter, die das Format ignoriert, wie die obige Parametertabelle zeigt.

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Abrufen und Konfigurieren von PivotField.getShowValuesSetting**
Lesen Sie die aktuelle Konfiguration über `PivotField.getShowValuesSetting()`: Der schreibgeschützte Getter liefert das `PivotShowValuesSetting`‑Objekt des Feldes, dessen vier Eigenschaften die aktive **Show Values As**‑Berechnung beschreiben. Um die Konfiguration zu ändern, rufen Sie die Methode `PivotField.showValuesAs(...)` auf – sie schreibt alle vier Einstellungen in einem Aufruf, sodass Sie die Eigenschaften nicht einzeln setzen müssen. Das Objekt `PivotShowValuesSetting` stellt die vier Eigenschaften bereit, die von `showValuesAs(...)` geschrieben werden:
- `getCalculationType()` / `setCalculationType(...)` wählt die sekundäre Berechnung vom Typ `PivotFieldDataDisplayFormat` aus.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` gibt den nullbasierten Index des Basis‑Feldes innerhalb der Pivot‑Felder an. Er wird von den Basis‑Item‑Formaten verwendet.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` bestimmt, wie das Basis‑Item relativ zum aktuellen Item positioniert wird, und akzeptiert `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` oder `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` gibt den nullbasierten Index des Basis‑Items an und wird verwendet, wenn `BaseItemPositionType` auf `CUSTOM` gesetzt ist.
Nachdem Sie `showValuesAs(...)` aufgerufen haben, führen Sie `PivotTable.calculateData()` erneut aus, damit der Pivot‑Körper mit der aktualisierten Konfiguration neu berechnet und gerendert wird.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Verwandte Artikel**
- [Verwalten von Werte‑Feldern in Pivot‑Tabellen](/cells/de/java/manage-value-fields/)
- [Pivot‑Tabelle aktualisieren](/cells/de/java/refresh-pivot-table/)
- [Stil auf Pivot‑Tabelle anwenden](/cells/de/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}