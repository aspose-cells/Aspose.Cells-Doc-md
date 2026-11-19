---
title: Visa värden som i pivottabell
linktitle: Visa värden som i pivottabell
description: Visa datafältsvärden i pivottabeller som procent av totalen, som differens från en baspost, som löpande totaler, som rankningar med mera med Aspose.Cells for Java.
keywords: Aspose.Cells, pivottabell, visa värden som, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /sv/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Möjliga användningsscenarier**
En pivottabell aggregerar normalt varje datafält med en aggregeringsfunktion, till exempel `Sum` eller `Count`. Excel-funktionen **Visa värden som** ersätter varje visat resultat med en sekundär beräkning som härleds från aggregeringen – till exempel en procentandel av totalsumman, en löpande total, en differens från en vald baspost eller en rankning – så att du kan utföra jämförande analys utan hjälpformler eller beräknade kolumner.
Typiska användningsområden omfattar analys av andelar av totalen, inklusive procentandelar av en rad, kolumn eller totalsumma; kumulativ rapportering med hjälp av en löpande total i ett periodfält; variansanalys mot en referenspost med hjälp av differens från eller procentuell differens från en baspost; samt rankning av värden från minsta till största eller från största till minsta.
I Aspose.Cells for Java väljer enumerationen `PivotShowValuesAsType` den sekundära beräkningen. Den skrivskyddade läsmetoden `PivotField.getShowValuesSetting()` returnerar ett `PivotShowValuesSetting`-objekt, vars metoder `setShowValuesAs(...)`, `setBaseFieldIndex(...)` och `setBaseItemIndex(...)` konfigurerar beteendet; bekvämlighetsmetoden `PivotField.showValuesAs(...)` tillämpar samma inställningar med ett enda anrop. Tillämpa dessa inställningar på ett datafält eller värdefält som har hämtats från `PivotTable.getDataFields()`.

## **Medlemmar i PivotShowValuesAsType**
Datafältet behåller sin aggregeringsfunktion, till exempel `Sum` eller `Count`, medan Visa värden som endast ändrar hur det aggregerade värdet visas.
Utöver att använda inställningsmetoderna i `PivotShowValuesSetting` direkt (se det sista avsnittet) finns en bekvämlighetsmetod som tillämpar samma konfiguration med ett enda anrop. Den har två överlagringar – en som anger basfältet och basposten via index och en som anger dem via namn:

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| Parameter | Betydning | När parametern krävs |
| --- | --- | --- |
| `showValuesAsType` | Den sekundära beräkningstypen `PivotShowValuesAsType` som ska tillämpas. | Alltid. |
| `baseField` | Det nollbaserade indexet för basfältet bland pivottabellens basfält (till exempel indexet för radfältet som basposten tillhör), eller – i överlagringen för `String` – namnet på basfältet. | De åtta basrelaterade formaten nedan (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`) kräver `baseField`; för alla andra format anger du `0` (eller `null` i överlagringen för `String`). |
| `baseItem` | Det nollbaserade indexet för basposten, med två specialvärden: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) väljer den föregående posten och `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) den följande posten. Överlagringen för `String` tar i stället baspostens rubrik, eller `null` när det valda formatet inte behöver någon baspost. | Endast de tre baspostrelaterade formaten (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) använder basposten; de fem fältrelaterade formaten (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, båda rankningarna) ignorerar den – ange `0` eller `null`. |

| Beräkningstyp | Beteende | Parametrar för basfält och baspost |
| --- | --- | --- |
| `NORMAL` | Ingen sekundär beräkning; det aggregerade värdet visas som det är (standard). | — |
| `DIFFERENCE_FROM` | Visar värdet som en differens från värdet för en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en rubrik, eller specialvärdet för föregående/nästa post) |
| `PERCENTAGE_OF` | Visar värdet som en procentandel av värdet för en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en rubrik, eller specialvärdet för föregående/nästa post) |
| `PERCENTAGE_DIFFERENCE_FROM` | Visar värdet som den procentuella differensen från värdet för en baspost i ett basfält. | `baseField` + `baseItem` (ett index eller en rubrik, eller specialvärdet för föregående/nästa post) |
| `RUNNING_TOTAL_IN` | Visar värdet som en löpande total för efterföljande poster i ett basfält. | `baseField` (fältet vars postordning styr ackumulationen) |
| `PERCENTAGE_OF_ROW` | Visar värdet som en procentandel av radens total. | — |
| `PERCENTAGE_OF_COLUMN` | Visar värdet som en procentandel av kolumnens total. | — |
| `PERCENTAGE_OF_TOTAL` | Visar värdet som en procentandel av totalsumman. | — |
| `INDEX` | Visar värdet med Excel-indexformeln ((värde * totalsumma) / (radtotal * kolumntotal)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Visar värdet som en procentandel av den överordnade radens total (för nästlade radfält). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Visar värdet som en procentandel av den överordnade kolumnens total (för nästlade kolumnfält). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Visar värdet som en procentandel av totalen för det överordnade fältet. | `baseField` (det överordnade fält vars total används som referens) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Visar värdet som en procentandel av en löpande total i ett basfält. | `baseField` (ackumulationsfältet) |
| `RANK_SMALLEST_TO_LARGEST` | Rankar värdet från minsta (1) till största. | `baseField` (fältet vars poster avgränsar rankningen) |
| `RANK_LARGEST_TO_SMALLEST` | Rankar värdet från största (1) till minsta. | `baseField` (fältet vars poster avgränsar rankningen) |

{{% alert color="primary" %}}
`showValuesAs(...)` anger exakt tillståndet i `PivotShowValuesSetting` via `setShowValuesAs(...)`, `setBaseFieldIndex(...)` och `setBaseItemIndex(...)` – metoden och inställningsobjektet är två sätt att konfigurera samma tillstånd, vilket motsvarar valen av basfält och baspost i dialogruten Visa värden som i Excel.
{{% /alert %}}

## **Visa värden som procent av totalsumman**
Anropa metoden `PivotField.showValuesAs(...)` med `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` för att omvandla varje cell i datafältet, inklusive totalsumman, till en andel av totalsumman. De visade talen representerar därför andelar av hela resultatet. Den här beräkningen mäter varje värde enbart i förhållande till totalsumman och kräver därför varken basfält eller baspost – de två sista argumenten (`0`, `0`) är platshållare som formatet ignorerar, enligt parametertabellen ovan.

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **Hämta och konfigurera PivotField.getShowValuesSetting**
Läs den aktuella konfigurationen via `PivotField.getShowValuesSetting()`: den skrivskyddade läsmetoden returnerar fältets `PivotShowValuesSetting`-objekt, vars egenskaper beskriver den aktuella inställningen för Visa värden som. Anropa metoden `PivotField.showValuesAs(...)` för att ändra konfigurationen – metoden ställer in alla inställningar med ett enda anrop, så att egenskaperna inte behöver anges en i taget.
Via `PivotShowValuesSetting`-objektet får du åtkomst till det tillstånd som `showValuesAs(...)` anger:
- `getShowValuesAs()` / `setShowValuesAs(...)` väljer den sekundära beräkningstypen `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` anger basfältets nollbaserade index bland pivotfälten. Indexet används av de basrelaterade formaten.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` anger basposten: det nollbaserade indexet för en specifik pivotpost, eller ett av de två specialvärdena – `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) för den föregående posten och `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) för den följande posten. Det används av de baspostrelaterade formaten.
- `getBaseFieldName()` och `getBaseItemCaption()` är skrivskyddade läsmetoder som returnerar namnet på det upplösta basfältet och rubriken för basposten; till exempel returnerar `getBaseItemCaption()` `(previous)` efter att specialvärdet för den föregående posten har valts.
Efter att ha anropat `showValuesAs(...)` ska du anropa `PivotTable.calculateData()` igen, så att data i pivottabellen beräknas om och visas på nytt med den uppdaterade konfigurationen.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **Relaterade artiklar**
- [Hantera värdefält i pivottabell](/cells/sv/java/manage-value-fields/)
- [Uppdatera pivottabell](/cells/sv/java/refresh-pivot-table/)
- [Tillämpa en stil på pivottabell](/cells/sv/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}