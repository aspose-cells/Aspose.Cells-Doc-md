---
title: Preguntas frecuentes (FAQ)
type: docs
weight: 100
url: /es/net/faq/
---

## **¿Cómo solucionar la excepción System.StackOverflowException en Workbook.CalculateFormula?**
A veces, los usuarios se enfrentan a la excepción System.StackOverflowException en el método Workbook.CalculateFormula. Esta excepción suele ocurrir porque el tamaño de la pila por defecto del IIS es demasiado pequeño (solo 265k). Puede solucionar este error creando otro hilo con un tamaño de pila aumentado y luego moviendo su código relacionado con Workbook.CalculateFormula adentro.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problema de grosor de líneas al renderizar Excel a PDF**
A veces, cuando se convierte un archivo de Excel a PDF, el grosor de las líneas es diferente en el PDF de salida. Este problema no es causado por Aspose.Cells. Es causado por **Adobe Reader** cuando sus configuraciones **"Alisar arte de línea"** y **"Mejorar líneas finas"** están marcadas. Desmarcar estas opciones mostrará bien el PDF.

Si se marca **"Alisar arte de línea"** y **"Mejorar líneas finas"**, el grosor de las líneas será diferente. Ve los siguientes pasos cómo se hace:

- Ir a **Editar**
- Seleccionar **Preferencias**
- En la categoría **Visualización de página** marca **"Alisar arte de línea"** y **"Mejorar líneas finas"**

Si desmarca **"Suavizar líneas de arte"** y **"Mejorar líneas delgadas"**, el grosor de las líneas será el mismo. Para lograr esto, siga los siguientes pasos:

- Ir a **Editar**
- Seleccionar **Preferencias**
- En la categoría **Visualización de página**, desmarque **"Suavizar líneas de arte"** y **"Mejorar líneas delgadas"**
## **Cómo solucionar System.OutOfMemoryException al cargar hojas de cálculo grandes?**
Existe la posibilidad de que el constructor de Workbook arroje System.OutOfMemoryException al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo se debe cargar habilitando las [Preferencias de memoria](/cells/es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Las API de Aspose.Cells proporcionan Preferencias de memoria para optimizar el consumo de memoria al cargar y procesar hojas de cálculo. Estas opciones también son útiles para cargar eficientemente hojas de cálculo grandes que contienen enormes conjuntos de datos en el objeto Workbook, como se muestra a continuación.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Determinar qué tamaño de pila se necesita para cierto Workbook**
Aunque hemos mejorado el motor de cálculo de fórmulas de Aspose.Cells y en la mayoría de los casos, debería poder calcular todas las fórmulas con éxito para un archivo de plantilla dado sin especificar un tamaño de pila más pequeño, aún así, a veces la StackOverFlowException en el método Workbook.CalculateFormula podría ser inevitable. Proporcionamos nuevas API para que los usuarios realicen un seguimiento de los cálculos de fórmulas. Hemos agregado una clase llamada "AbstractCalculationMonitor" y proporcionamos una propiedad, es decir, *CalculationOptions.CalculationMonitor* para hacer frente/rastrear el problema.

Los usuarios pueden rastrear el tamaño de la pila por sí mismos utilizando las API. Tenga en cuenta que verificar la pila para cada celda seguramente degradará el rendimiento en gran medida. Consulte el segmento de código de muestra para su referencia:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

No hay una mejor forma de obtener el tamaño de la pila utilizado en tiempo de ejecución. El código proporcionado anteriormente es solo un ejemplo. El rendimiento se degradará significativamente, sin duda. Por lo tanto, creemos que el código puede ser optimizado por los usuarios (que realmente deseen utilizarlo) de acuerdo con sus diferentes escenarios y requisitos. Por ejemplo, verificar la pila cuando el recuento de celdas recursivas alcanza cierto número, reunir la tasa de aumento promedio de la pila para una celda recursiva y determinar la frecuencia para verificar la pila, etc.

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
