---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa datafältvärden i pivottabell som en procentsats av totalen, en skillnad från ett basobjekt, löpande totaler, rankningar och mer med Aspose.Cells for Java.
keywords: Aspose.Cells, pivottabell, visa värden som, visningsformat, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /sv/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregationsfunktion såsom `Sum` eller `Count`. Excels **Show Values As**‑funktion ersätter varje visat resultat med en sekundär beräkning härledd från det aggregerade värdet – till exempel en procentsats av totalsumman, ett löpande totalvärde, en skillnad från ett valt basobjekt eller en rangordning – så att du kan utföra jämförande analyser utan hjälpredon eller beräknade kolumner.  
Typiska användningsområden inkluderar analys av andel av totalen, inklusive procent av rad, kolumn eller total, kumulativ rapportering med ett löpande totalvärde i ett periodfält, avviksanalys mot ett referensobjekt med skillnad från eller procentuell skillnad från ett basobjekt, samt rangordning av värden från minsta till största eller omvänt.  
I Aspose.Cells for Java väljer `PivotFieldDataDisplayFormat` den sekundära beräkningen. Den skrivskyddade gettern `PivotField.getShowValuesSetting()` returnerar ett `PivotShowValuesSetting`‑objekt, vars `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` och `setBaseItemIndex(...)`‑metoder konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` applicerar samma fyra inställningar i ett anrop. Applicera dessa inställningar på ett data‑ eller värdefält som erhålls via `PivotTable.getDataFields()`.

## **PivotFieldDataDisplayFormat‑enum‑medlemmar**
Datafältet behåller sin aggregationsfunktion, såsom Sum eller Count, medan Show Values As endast förändrar hur det aggregerade värdet visas.  
Förutom att använda `PivotShowValuesSetting`‑setternas direkt (se sista avsnittet) kan en enstaka bekvämlighetsmetod applicera samma konfiguration:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Parameter | Betydelse | När krävs det |
| --- | --- | --- |
| `displayFormat` | Den `PivotFieldDataDisplayFormat`‑sekundära beräkning som ska tillämpas. | Alltid. |
| `baseField` | Nollbaserat index för basfältet bland pivottabellens basfält (t.ex. index för radfältet som basobjektet tillhör). | Endast för de sex basrelaterade formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); ignoreras av alla andra format. |
| `baseItemPositionType` | Hur basobjektet väljs i förhållande till det aktuella objektet: `PivotItemPositionType.PREVIOUS`, `NEXT` eller `CUSTOM`. | Endast för de tre basobjektformaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); ignoreras av alla andra format. |
| `baseItem` | Nollbaserat index för basobjektet. | Endast när `baseItemPositionType` är `CUSTOM` (objekt‑indexet anger exakt basobjekt); ignoreras för `PREVIOUS`/`NEXT` och av alla icke‑basformat — skicka `0`. |

| Beräkningstyp | Beteende | Basobjektparametrar |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en skillnad från värdet av ett basobjekt i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `PERCENTAGE_OF` | Visar värdet som en procentsats av värdet av ett basobjekt i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som den procentuella skillnaden från värdet av ett basobjekt i ett basfält. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` endast med `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Visar värdet som ett löpande totalvärde för på varandra följande objekt i ett basfält. | `baseField` (fältet vars objektordning driver ackumuleringen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentsats av radtotalen. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentsats av kolumntotalen. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentsats av den totala totalsumman. | — |
| `INDEX` | Visar värdet med Excel‑indexformeln ((värde × total) / (radtotal × kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentsats av dess överordnade radtotal (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentsats av dess överordnade kolumntotal (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentsats av dess överordnade total. | `baseField` (det överordnade referensfältet) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentsats av ett löpande totalvärde i ett basfält. | `baseField` (ackumuleringsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rangordnar värdet från minsta (1) till största. | — |
| `RANK_LARGEST_TO_SMALLEST` | Rangordnar värdet från största (1) till minsta. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` sätter de `PivotShowValuesSetting`‑värdena via `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` och `setBaseItemIndex(...)` — metoden och egendomsobjektet är två sätt att konfigurera samma tillstånd, vilket speglar basfält‑ och basobjekt‑väljare i Excels Show Values As‑dialog.
{{% /alert %}}

## **Visa värden som procent av totalen**
Anropa `PivotField.showValuesAs(...)` med `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` för att konvertera varje datafältcell, inklusive totalsumman, till dess andel av totalen. De visade siffrorna läses därför som proportioner av hela resultatsatsen. Detta format mäter varje värde endast mot totalen, så det kräver inget basfält eller basobjekt — de efterföljande argumenten (`0`, `PivotItemPositionType.PREVIOUS`, `0`) är platshållare som formatet ignorerar, enligt tabellen ovan.

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

## **Hämta och konfigurera PivotField.getShowValuesSetting**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()` – den skrivskyddade gettern returnerar fältets `PivotShowValuesSetting`‑objekt, vars fyra egenskaper beskriver den aktiva Show Values As‑beräkningen. För att ändra konfigurationen, anropa `PivotField.showValuesAs(...)` – den skriver alla fyra inställningarna i ett anrop, så du behöver aldrig sätta egenskaperna en i taget.  
`PivotShowValuesSetting`‑objektet exponerar de fyra egenskaper som `showValuesAs(...)` skriver:
- `getCalculationType()` / `setCalculationType(...)` väljer den sekundära beräkningen `PivotFieldDataDisplayFormat`.  
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` specificerar nollbaserat index för basfältet inom pivottabellens fält. Det används av de basrelaterade formaten.  
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` bestämmer hur basobjektet placeras i förhållande till det aktuella objektet och accepterar `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` eller `PivotItemPositionType.CUSTOM`.  
- `getBaseItemIndex()` / `setBaseItemIndex(...)` specificerar nollbaserat basobjekt‑index och används när `BaseItemPositionType` är `CUSTOM`.  
Efter att ha anropat `showValuesAs(...)`, anropa `PivotTable.calculateData()` igen så att pivottabellens kropp beräknas om och renderas med den uppdaterade konfigurationen.

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

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/java/refresh-pivot-table/)
- [Applicera format på pivottabell](/cells/sv/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}