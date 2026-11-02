---
title: Mostrar valores como en Tabla Dinámica
linktitle: Mostrar valores como en Tabla Dinámica
description: Muestra los valores de los campos de datos de una tabla dinámica como un porcentaje del total, una diferencia respecto a un elemento base, totales acumulados, rangos y más con Aspose.Cells for Java.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, formato de visualización de datos, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /es/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Una tabla dinámica normalmente agrega cada campo de datos con una función de agregación como `Sum` o `Count`. La característica **Mostrar valores como** de Excel reemplaza cada resultado mostrado con un cálculo secundario derivado de esa agregación—por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base seleccionado o un rango—para que pueda realizar análisis comparativos sin fórmulas auxiliares ni columnas calculadas.  
Los usos típicos incluyen análisis de participación del total, con porcentajes de filas, columnas o total general; informes acumulativos usando un total acumulado en un campo de periodo; análisis de variación frente a un elemento de referencia mediante diferencia o diferencia porcentual respecto a un elemento base; y clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for Java, `PivotFieldDataDisplayFormat` selecciona el cálculo secundario. El método de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` y `setBaseItemIndex(...)` configuran el comportamiento; el método de conveniencia `PivotField.showValuesAs(...)` aplica los mismos cuatro ajustes en una sola llamada. Aplique estos ajustes a un campo de datos o de valor obtenido de `PivotTable.getDataFields()`.

## **Miembros de la enumeración PivotFieldDataDisplayFormat**
El campo de datos conserva su función de agregación, como Sum o Count, mientras que Mostrar valores como transforma solo la forma en que se muestra el valor agregado.  
Además de usar directamente los setters de `PivotShowValuesSetting` (ver la última sección), un método de conveniencia de una sola llamada aplica la misma configuración:

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| Parámetro | Significado | Cuándo es necesario |
| --- | --- | --- |
| `displayFormat` | El cálculo secundario `PivotFieldDataDisplayFormat` a aplicar. | Siempre. |
| `baseField` | Índice base‑cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base). | Solo para los seis formatos relativos a la base que se indican a continuación (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`); los demás formatos lo ignoran. |
| `baseItemPositionType` | Cómo se elige el elemento base respecto al elemento actual: `PivotItemPositionType.PREVIOUS`, `NEXT` o `CUSTOM`. | Solo para los tres formatos con elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`); los demás formatos lo ignoran. |
| `baseItem` | Índice base‑cero del elemento base. | Sólo cuando `baseItemPositionType` es `CUSTOM` (el índice del elemento selecciona el elemento base exacto); ignorado para `PREVIOUS` / `NEXT` y por cualquier formato que no sea de base — pasar `0`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `NORMAL` | No hay cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como una diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_OF` | Muestra el valor como un porcentaje del valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como la diferencia porcentual respecto al valor de un elemento base en un campo base. | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM` (`baseItem` solo con `CUSTOM`) |
| `RUNNING_TOTAL_IN` | Muestra el valor como un total acumulado para los elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos impulsa la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como un porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como un porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como un porcentaje del total general. | — |
| `INDEX` | Muestra el valor usando la fórmula de índice de Excel ((valor * total general) / (total fila * total columna)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como un porcentaje del total de la fila padre (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como un porcentaje del total de la columna padre (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como un porcentaje de su total padre. | `baseField` (el campo principal de referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como un porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | — |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | — |

{{% alert color="primary" %}}
`showValuesAs(...)` establece los valores de `PivotShowValuesSetting` mediante `setCalculationType(...)`, `setBaseFieldIndex(...)`, `setBaseItemPositionType(...)` y `setBaseItemIndex(...)`; el método y el objeto de propiedades son dos formas de configurar el mismo estado, reflejando los selectores de campo base y elemento base en el cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs(...)` con `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` para convertir cada celda de campo de datos, incluido el total general, en su participación del total general. Los números mostrados, por lo tanto, se leen como proporciones del conjunto de resultados completo. Este formato mide cada valor únicamente contra el total general, por lo que no necesita campo base ni elemento base; los argumentos finales (`0`, `PivotItemPositionType.PREVIOUS`, `0`) son marcadores de posición que el formato ignora, según indica la tabla de parámetros anterior.

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

## **Obtener y configurar PivotField.getShowValuesSetting**
Lea la configuración actual mediante `PivotField.getShowValuesSetting()`: el getter de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas cuatro propiedades describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.showValuesAs(...)`; escribe los cuatro ajustes en una sola llamada, por lo que nunca necesita establecer cada propiedad individualmente.  
El objeto `PivotShowValuesSetting` expone las cuatro propiedades que `showValuesAs(...)` escribe:
- `getCalculationType()` / `setCalculationType(...)` selecciona el cálculo secundario `PivotFieldDataDisplayFormat`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` especifica el índice base‑cero del campo base dentro de los campos de la tabla dinámica. Es usado por los formatos relativos a la base.
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` determina cómo se posiciona el elemento base respecto al elemento actual y acepta `PivotItemPositionType.NEXT`, `PivotItemPositionType.PREVIOUS` o `PivotItemPositionType.CUSTOM`.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` especifica el índice base‑cero del elemento base y se usa cuando `BaseItemPositionType` es `CUSTOM`.
Después de llamar a `showValuesAs(...)`, invoque `PivotTable.calculateData()` nuevamente para que el cuerpo de la tabla dinámica se recalcule y se vuelva a renderizar con la configuración actualizada.

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

## **Artículos relacionados**
- [Administrar campos de valor en Tabla Dinámica](/cells/es/java/manage-value-fields/)
- [Actualizar Tabla Dinámica](/cells/es/java/refresh-pivot-table/)
- [Aplicar estilo a Tabla Dinámica](/cells/es/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}