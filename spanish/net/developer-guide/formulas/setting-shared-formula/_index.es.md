---
title: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Si quieres agregar una función en la hoja de cálculo que realice algunos cálculos. Este artículo explica cómo lograr esta tarea usando Aspose.Cells.

{{% /alert %}}

## Estableciendo fórmula compartida usando Aspose.Cells

Supongamos que tienes una hoja de trabajo llena de datos con el formato que se muestra en la siguiente hoja de cálculo de ejemplo.

|**Archivo de entrada con una columna o datos**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Quieres agregar una función en B2 que calculará el impuesto sobre las ventas para la primera fila de datos. El impuesto es del **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

Aspose.Cells te permite especificar una fórmula utilizando la propiedad [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula). Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, y así sucesivamente) en la columna.

O haz lo que hiciste para la primera celda, estableciendo efectivamente la fórmula para cada celda, actualizando la referencia de la celda en consecuencia (A3*0.09, A4*0.09, A5*0.09 y así sucesivamente). Esto requiere que las referencias de celda para cada fila se actualicen. También requiere que Aspose.Cells analice cada fórmula individualmente, lo que puede ser consume tiempo para hojas de cálculo grandes y fórmulas complejas. También agrega líneas de código adicionales, aunque los bucles pueden reducirlas en cierta medida.

Otro enfoque es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. El método [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
