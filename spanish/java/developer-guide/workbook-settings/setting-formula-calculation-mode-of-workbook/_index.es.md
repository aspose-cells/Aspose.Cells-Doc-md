---
title: Configuración del modo de cálculo de fórmulas del libro de trabajo
type: docs
weight: 130
url: /es/java/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel le permite configurar el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: vuelve a calcular cada vez que se cambia algo y cada vez que se abre un libro.
- Automático excepto para las tablas de datos: vuelve a calcular cada vez que se cambia algo, pero omite las tablas de datos.
- Manual: vuelva a calcular solo cuando el usuario lo solicite explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarde el libro.

{{% /alert %}}

Para configurar el modo de cálculo de fórmula en Microsoft Excel:

1.  Seleccione**Fórmulas** y luego**Opciones de cálculo**.
1. Seleccione una de las opciones.

 Aspose.Cells también le permite configurar el**Modo de cálculo de fórmula** utilizando la[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode) propiedad. Puedes asignarle el[**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType)enumeración que tiene uno de los siguientes valores:

- [**CalcModeType.AUTOMÁTICO**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

El siguiente código de ejemplo primero crea un libro de trabajo, luego establece el modo de cálculo de fórmulas en**Manual** y guarda el libro de trabajo como archivo de salida de Excel en el disco.

**El archivo de salida. Tenga en cuenta el modo de cálculo de la fórmula.**

![todo:imagen_alternativa_texto](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
