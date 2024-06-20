---
title: Configuración del modo de cálculo de fórmulas del libro de trabajo
type: docs
weight: 130
url: /es/java/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel te permite establecer el modo de cálculo de fórmulas, es decir, la forma en que se calculan las fórmulas. Hay tres valores posibles:

- Automático: recalcula cada vez que algo cambia, y cada vez que se abre un libro.
- Automático excepto para tablas de datos: recalcula cada vez que algo cambia, pero deja fuera las tablas de datos.
- Manual: recalcula solo cuando el usuario lo solicita explícitamente presionando F9 o CTRL+ALT+F9, o cuando se guarda el libro.

{{% /alert %}}

Para establecer el modo de cálculo de fórmulas en Microsoft Excel:

1. Selecciona **Fórmulas** y luego **Opciones de cálculo**.
1. Selecciona una de las opciones.

Aspose.Cells también te permite establecer el **Modo de cálculo de fórmulas** utilizando la propiedad [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#CalculationMode). Puedes asignarle la enumeración [**CalcModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/CalcModeType) que tiene uno de los siguientes valores:

- [**CalcModeType.AUTOMATIC**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC)
- [**CalcModeType.AUTOMATIC_EXCEPT_TABLE**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#AUTOMATIC_EXCEPT_TABLE)
- [**CalcModeType.MANUAL**](https://reference.aspose.com/cells/java/com.aspose.cells/calcmodetype#MANUAL)

El siguiente código de muestra primero crea un libro, luego establece el modo de cálculo de fórmulas a **Manual** y guarda el libro como archivo de Excel de salida en el disco.

**El archivo de salida. Nota el modo de cálculo de fórmulas.**

![todo:image_alt_text](setting-formula-calculation-mode-of-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetFormulaCalculationMode-SetFormulaCalculationMode.java" >}}
