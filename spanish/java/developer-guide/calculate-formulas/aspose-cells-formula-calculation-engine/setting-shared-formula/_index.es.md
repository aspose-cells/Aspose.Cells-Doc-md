---
title: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

Suponga que tiene una hoja de trabajo llena de datos en el formato que se parece a la siguiente hoja de trabajo de muestra.

**Archivo de entrada con una columna o datos** 

![todo:imagen_alternativa_texto](setting-shared-formula_1.png)

 Desea agregar una función en B2 que calculará el impuesto a las ventas para la primera fila de datos. el impuesto es**9%** La fórmula que calcula el impuesto sobre las ventas es:**"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

{{% /alert %}} 

 Aspose.Cells le permite especificar una fórmula usando el[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) propiedad, específicamente[Cell.setFórmula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) y[Cell.getFórmula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, etc.) en la columna.

Haga lo que hizo para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de celda en consecuencia (A3*0,09, A4*0,09, A5*0,09, etc.). Esto requiere que se actualicen las referencias de celda para cada fila. También requiere Aspose.Cells para analizar cada fórmula individualmente, lo que puede llevar mucho tiempo para hojas de cálculo grandes y fórmulas complejas. También agrega líneas adicionales de códigos, aunque los bucles pueden reducirlos un poco.

 Otro enfoque es utilizar un**fórmula compartida** Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila para que el impuesto se calcule correctamente. Él[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo. La siguiente captura de pantalla muestra el archivo de salida.

**Archivo de salida: fórmula compartida aplicada** 

![todo:imagen_alternativa_texto](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
