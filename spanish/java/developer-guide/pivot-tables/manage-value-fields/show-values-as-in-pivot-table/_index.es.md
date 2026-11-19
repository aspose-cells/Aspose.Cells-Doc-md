---
title: Mostrar valores como en una tabla dinámica
linktitle: Mostrar valores como en una tabla dinámica
description: Muestre los valores de los campos de datos de una tabla dinámica como porcentaje del total, diferencia respecto a un elemento base, totales acumulados, clasificaciones y más con Aspose.Cells for Java.
keywords: Aspose.Cells, tabla dinámica, mostrar valores como, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /es/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica normalmente agrega cada campo de datos mediante una función de agregación como `Sum` o `Count`. La función **Mostrar valores como** de Excel sustituye cada resultado mostrado por un cálculo secundario derivado de dicho valor agregado; por ejemplo, un porcentaje del total general, un total acumulado, una diferencia respecto a un elemento base elegido o una clasificación. Esto permite realizar análisis comparativos sin necesidad de fórmulas auxiliares o columnas calculadas.
Los usos típicos incluyen el análisis de la participación en el total, con porcentajes del total de una fila, una columna o el total general; los informes acumulativos que utilizan un total acumulado en un campo de período; el análisis de variaciones respecto de un elemento de referencia mediante la diferencia o la diferencia porcentual respecto de un elemento base; y la clasificación de valores de menor a mayor o de mayor a menor.
En Aspose.Cells for Java, la enumeración `PivotShowValuesAsType` selecciona el cálculo secundario. El getter de solo lectura `PivotField.getShowValuesSetting()` devuelve un objeto `PivotShowValuesSetting`, cuyos métodos `setShowValuesAs(...)`, `setBaseFieldIndex(...)` y `setBaseItemIndex(...)` configuran el comportamiento; el método `PivotField.showValuesAs(...)` permite aplicar la misma configuración en una sola llamada. Aplique esta configuración a un campo de datos o de valor obtenido de `PivotTable.getDataFields()`.

## **Miembros de la enumeración PivotShowValuesAsType**
El campo de datos conserva su función de agregación, como `Sum` o `Count`, mientras que Mostrar valores como transforma únicamente la forma en que se muestra el valor agregado.
Además de utilizar directamente los métodos `setShowValuesAs(...)`, `setBaseFieldIndex(...)` y `setBaseItemIndex(...)` (consulte la última sección), puede aplicar la misma configuración mediante una sola llamada. Este método ofrece dos sobrecargas: una acepta el campo base y el elemento base por índice y la otra, por nombre:

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

| Parámetro | Significado | Cuándo es obligatorio |
| --- | --- | --- |
| `showValuesAsType` | Cálculo secundario `PivotShowValuesAsType` que se debe aplicar. | Siempre. |
| `baseField` | Índice basado en cero del campo base entre los campos base de la tabla dinámica (por ejemplo, el índice del campo de fila al que pertenece el elemento base), o — en la sobrecarga `String` — el nombre del campo base. | Los ocho formatos relativos a la base siguientes (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`, `RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN`, `RANK_SMALLEST_TO_LARGEST`, `RANK_LARGEST_TO_SMALLEST`); para todos los demás formatos, pase `0` (o `null` en la sobrecarga `String`). |
| `baseItem` | Índice basado en cero del elemento base, con dos constantes centinela: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) selecciona el elemento anterior y `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2), el siguiente. La sobrecarga `String` acepta en su lugar el rótulo del elemento base y debe ser `null` cuando el formato seleccionado no necesita ningún elemento base. | Solo los tres formatos relativos al elemento base (`DIFFERENCE_FROM`, `PERCENTAGE_OF`, `PERCENTAGE_DIFFERENCE_FROM`) utilizan el elemento base; los cinco formatos relativos al campo (`RUNNING_TOTAL_IN`, `PERCENTAGE_OF_PARENT_TOTAL`, `PERCENTAGE_OF_RUNNING_TOTAL_IN` y ambas clasificaciones) lo omiten; pase `0` o `null`. |

| Tipo de cálculo | Comportamiento | Parámetros del elemento base |
| --- | --- | --- |
| `NORMAL` | No se aplica ningún cálculo secundario; el valor agregado se muestra tal cual (predeterminado). | — |
| `DIFFERENCE_FROM` | Muestra el valor como la diferencia respecto al valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o la constante centinela del elemento anterior o siguiente) |
| `PERCENTAGE_OF` | Muestra el valor como porcentaje del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o la constante centinela del elemento anterior o siguiente) |
| `PERCENTAGE_DIFFERENCE_FROM` | Muestra el valor como la diferencia porcentual respecto del valor de un elemento base en un campo base. | `baseField` + `baseItem` (un índice o un rótulo, o la constante centinela del elemento anterior o siguiente) |
| `RUNNING_TOTAL_IN` | Muestra el valor como total acumulado para elementos sucesivos de un campo base. | `baseField` (el campo cuyo orden de elementos determina la acumulación) |
| `PERCENTAGE_OF_ROW` | Muestra el valor como porcentaje del total de la fila. | — |
| `PERCENTAGE_OF_COLUMN` | Muestra el valor como porcentaje del total de la columna. | — |
| `PERCENTAGE_OF_TOTAL` | Muestra el valor como porcentaje del total general. | — |
| `INDEX` | Muestra el valor mediante la fórmula de índice de Excel ((value * grand total) / (row total * column total)). | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | Muestra el valor como porcentaje del total de su fila superior (para campos de fila anidados). | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | Muestra el valor como porcentaje del total de su columna superior (para campos de columna anidados). | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | Muestra el valor como porcentaje del total del campo superior. | `baseField` (el campo superior cuyo total sirve como referencia) |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | Muestra el valor como porcentaje de un total acumulado en un campo base. | `baseField` (el campo de acumulación) |
| `RANK_SMALLEST_TO_LARGEST` | Clasifica el valor de menor (1) a mayor. | `baseField` (el campo cuyos elementos definen el ámbito de la clasificación) |
| `RANK_LARGEST_TO_SMALLEST` | Clasifica el valor de mayor (1) a menor. | `baseField` (el campo cuyos elementos definen el ámbito de la clasificación) |

{{% alert color="primary" %}}
`showValuesAs(...)` establece exactamente el estado de `PivotShowValuesSetting` mediante `setShowValuesAs(...)`, `setBaseFieldIndex(...)` y `setBaseItemIndex(...)`; el método y el objeto de propiedades ofrecen dos formas de configurar el mismo estado, de forma similar a los selectores de campo base y elemento base del cuadro de diálogo Mostrar valores como de Excel.
{{% /alert %}}

## **Mostrar valores como porcentaje del total**
Llame al método `PivotField.showValuesAs(...)` con `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` para convertir cada celda de un campo de datos, incluido el total general, en su porcentaje del total general. Por lo tanto, los números mostrados representan proporciones del conjunto completo de resultados. Este formato mide cada valor únicamente respecto del total general, por lo que no necesita un campo base ni un elemento base; los argumentos finales (`0`, `0`) son marcadores de posición que el formato ignora, como se indica en la tabla de parámetros anterior.

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

## **Obtener y configurar PivotField.getShowValuesSetting**
Consulte la configuración actual mediante `PivotField.getShowValuesSetting()`: el getter de solo lectura devuelve el objeto `PivotShowValuesSetting` del campo, cuyas propiedades describen el cálculo activo de Mostrar valores como. Para cambiar la configuración, llame al método `PivotField.showValuesAs(...)`; el método escribe toda la configuración en una sola llamada, por lo que nunca necesita establecer las propiedades una por una.
El objeto `PivotShowValuesSetting` expone el estado que `showValuesAs(...)` escribe:
- `getShowValuesAs()` / `setShowValuesAs(...)` selecciona el cálculo secundario `PivotShowValuesAsType`.
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` especifica el índice basado en cero del campo base dentro de los campos de la tabla dinámica. Se utiliza en los formatos relativos a la base.
- `getBaseItemIndex()` / `setBaseItemIndex(...)` especifica el elemento base: un índice basado en cero de un elemento específico de la tabla dinámica, o una de las dos constantes centinela: `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) para el elemento anterior y `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) para el siguiente. Se utiliza en los formatos relativos al elemento base.
- `getBaseFieldName()` y `getBaseItemCaption()` proporcionan el nombre resuelto del campo base y el rótulo resuelto del elemento base; son accesores de solo lectura. Por ejemplo, después de seleccionar la constante centinela del elemento anterior, `getBaseItemCaption()` devuelve `(previous)`.
Para que el cuerpo de la tabla dinámica se recalcule y vuelva a mostrarse con la configuración actualizada, llame de nuevo a `PivotTable.calculateData()` después de invocar `showValuesAs(...)`.

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

## **Artículos relacionados**
- [Administrar campos de valor en una tabla dinámica](/cells/es/java/manage-value-fields/)
- [Actualizar una tabla dinámica](/cells/es/java/refresh-pivot-table/)
- [Aplicar un estilo a una tabla dinámica](/cells/es/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}