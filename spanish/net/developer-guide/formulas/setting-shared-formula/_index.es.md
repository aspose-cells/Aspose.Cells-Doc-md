---
title: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/net/setting-shared-formula/
---
{{% alert color="primary" %}}

Si desea agregar una función en la hoja de trabajo que hará algunos cálculos. Este artículo explica cómo lograr esta tarea usando Aspose.Cells.

{{% /alert %}}

## Configuración de fórmula compartida usando Aspose.Cells

Suponga que tiene una hoja de trabajo llena de datos en el formato que se parece a la siguiente hoja de trabajo de muestra.

|**Archivo de entrada con una columna o datos**|
|:- |
|![todo:imagen_alternativa_texto](setting-shared-formula_1.png)|

 Desea agregar una función en B2 que calculará el impuesto a las ventas para la primera fila de datos. el impuesto es**9%** . La fórmula que calcula el impuesto sobre las ventas es:**"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

 Aspose.Cells le permite especificar una fórmula usando el[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)propiedad. Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, etc.) en la columna.

Haga lo que hizo para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de celda en consecuencia (A3*0,09, A4*0,09, A5*0,09, etc.). Esto requiere que se actualicen las referencias de celda para cada fila. También requiere Aspose.Cells para analizar cada fórmula individualmente, lo que puede llevar mucho tiempo para hojas de cálculo grandes y fórmulas complejas. También agrega líneas adicionales de códigos, aunque los bucles pueden reducirlos un poco.

 Otro enfoque es utilizar un**fórmula compartida** . Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. los[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)método es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
