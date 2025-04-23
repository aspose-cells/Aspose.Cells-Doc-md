---
title: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

Si quieres agregar una función en la hoja de cálculo que realice algunos cálculos. Este artículo explica cómo lograr esta tarea usando Aspose.Cells para Python via .NET.

{{% /alert %}}

## Establecer fórmula compartida usando Aspose.Cells para Python via .NET

Supongamos que tienes una hoja de trabajo llena de datos con el formato que se muestra en la siguiente hoja de cálculo de ejemplo.

|**Archivo de entrada con una columna o datos**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Deseas agregar una función en B2 que calcule el impuesto sobre las ventas para la primera fila de datos. El impuesto es **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells para Python via .NET.

Aspose.Cells para Python via .NET te permite especificar una fórmula usando la propiedad [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula). Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, etc.) en la columna.

Haz lo que hiciste para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de celda en consecuencia (A3*0.09, A4*0.09, A5*0.09, etc.). Esto requiere actualizar las referencias de celda para cada fila. También requiere que Aspose.Cells para Python via .NET analice cada fórmula individualmente, lo cual puede ser lento para hojas de cálculo grandes y fórmulas complejas. Además, agrega líneas adicionales de código aunque los bucles pueden reducirlo en cierta medida.

Otro enfoque es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. El método [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

