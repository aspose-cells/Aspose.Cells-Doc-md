---
title: Configuración de fórmula compartida
type: docs
weight: 10
url: /es/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Supongamos que tienes una hoja de trabajo llena de datos con el formato que se muestra en la siguiente hoja de cálculo de ejemplo.

**Archivo de entrada con una columna de datos** 

![todo:image_alt_text](setting-shared-formula_1.png)

Quieres agregar una función en B2 que calculará el impuesto sobre las ventas para la primera fila de datos. El impuesto es del **9%**. La fórmula que calcula el impuesto sobre las ventas es: **"=A2*0.09"**. Este artículo explica cómo aplicar esta fórmula con Aspose.Cells.

{{% /alert %}} 

Aspose.Cells te permite especificar una fórmula utilizando la propiedad [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), específicamente [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) y [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Hay dos opciones para agregar fórmulas a las otras celdas (B3, B4, B5, y así sucesivamente) en la columna.

O bien, hacer lo que hiciste para la primera celda, configurando efectivamente la fórmula para cada celda, actualizando la referencia de celda correspondientemente (`A3*0.09`, `A4*0.09`, `A5*0.09`, y así sucesivamente). Esto requiere que se actualicen las referencias de celda para cada fila. También requiere que Aspose.Cells analice cada fórmula individualmente, lo que puede llevar tiempo para hojas de cálculo grandes y fórmulas complejas. También agrega líneas de código adicionales, aunque los bucles pueden reducirlas en cierta medida.

Otra estrategia es usar una **fórmula compartida**. Con una fórmula compartida, las fórmulas se actualizan automáticamente para las referencias de celda en cada fila de modo que el impuesto se calcule correctamente. El método [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula-java.lang.String-int-int-) es más eficiente que el primer método.

El siguiente ejemplo demuestra cómo usarlo. La captura de pantalla a continuación muestra el archivo de salida.

**Archivo de salida: fórmula compartida aplicada** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
