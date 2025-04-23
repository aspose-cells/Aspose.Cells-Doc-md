---
title: Configuraciones numéricas
type: docs
weight: 10
url: /es/java/cells-number-settings/
---

## **Configuración de formatos de visualización de números y fechas**

Una característica muy fuerte de Microsoft Excel es que permite a los usuarios establecer los formatos de visualización de valores numéricos y fechas. Sabemos que los datos numéricos pueden utilizarse para representar diferentes valores, incluidos decimales, moneda, porcentaje, fracción o valores contables, etc. Todos estos valores numéricos se muestran en diferentes formatos según el tipo de información que representan. De manera similar, hay muchos formatos en los que se puede mostrar una fecha u hora.
Aspose.Cells admite esta funcionalidad y permite a los desarrolladores establecer cualquier formato de visualización para un número o fecha.

## **Configuración de formatos de visualización en Microsoft Excel**

Para establecer formatos de visualización en Microsoft Excel:

1. Haga clic derecho en cualquier celda.
1. Seleccione **Formato de celdas**. Aparecerá un cuadro de diálogo que se usa para establecer los formatos de visualización de cualquier tipo de valor.

En el lado izquierdo del cuadro de diálogo, hay muchas categorías de valores como **General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **Hora**, **Porcentaje**, etc. Aspose.Cells admite todos estos formatos de visualización.

## **Uso de formatos de números predefinidos**

Aspose.Cells ofrece algunos formatos de números predefinidos para configurar los formatos de visualización de números y fechas. Todos los formatos de números predefinidos tienen valores numéricos únicos. Los desarrolladores pueden asignar cualquier valor numérico deseado al método [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) del objeto [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) para aplicar el formato de visualización. Este enfoque es rápido. A continuación se muestran los formatos de números predefinidos admitidos por Aspose.Cells.

|**Valor**|**Tipo**|**Cadena de formato**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Uso de formatos de números personalizados**

Para definir tu propia cadena de formato personalizada para establecer el formato de visualización, usa [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Este enfoque no es tan rápido como usar formatos preestablecidos, pero es más flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

Si utilizas el [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) para establecer el formato de número, cualquier formato previo establecido con el [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) será sobrescrito y viceversa.

{{% /alert %}}

## **Temas avanzados**
- [Consulte el formato de número personalizado al configurar la propiedad Style.Custom](/cells/es/java/check-custom-number-format-when-setting-style-custom-property/)
- [Especificar separadores de números decimales y de grupo personalizados para el libro de trabajo](/cells/es/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Especificación de formato de patrón personalizado DBNum](/cells/es/java/specifying-dbnum-custom-pattern-formatting/)
{{< app/cells/assistant language="java" >}}
