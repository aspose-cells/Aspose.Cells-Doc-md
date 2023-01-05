---
title: Preguntas más frecuentes
type: docs
weight: 100
url: /es/net/faq/
---
## **¿Cómo arreglar System.StackOverFlowException en Workbook.CalculateFormula?**
A veces, los usuarios se enfrentan a System.StackOverFlowException en el método Workbook.CalculateFormula. Esta excepción generalmente ocurre porque el tamaño de pila predeterminado de IIS es demasiado pequeño (solo 265k). Puede corregir este error creando otro subproceso con un mayor tamaño de pila y luego moviendo su código relacionado Workbook.CalculateFormula dentro de él.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problema con el grosor de las líneas al renderizar Excel a PDF**
 veces, cuando el archivo de Excel se convierte a PDF, el grosor de las líneas es diferente en la salida PDF. Este problema no es causado por Aspose.Cells. Es causado por**Adobe Reader** cuando su configuración**"Arte de línea suave"** y**"Mejora las líneas finas"** se comprueban. Desmarcar estas opciones mostrará PDF bien.

 Si marca**"Arte de línea suave"** y**"Mejora las líneas finas"**, el grosor de las líneas es diferente. Vea los siguientes pasos cómo se hace:

-  Ir a**Editar**
-  Seleccione**preferencias**
-  En el**Visualización de página** Categoría Verifique la**"Arte de línea suave"** y**"Mejora las líneas finas"**

 Si desmarca**"Arte de línea suave"** y**"Mejora las líneas finas"**, el grosor de las líneas es el mismo. Para lograr esto solo sigue los siguientes pasos:

-  Ir a**Editar**
-  Seleccione**preferencias**
-  En el**Visualización de página** Categoría Desmarque la**"Arte de línea suave"** y**"Mejora las líneas finas"**
## **¿Cómo arreglar System.OutOfMemoryException al cargar hojas de cálculo grandes?**
Hay buenas posibilidades de que el constructor del libro de trabajo arroje System.OutOfMemoryException al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse mientras se habilita el[Preferencias de memoria](/cells/es/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells Las API brindan preferencias de memoria para optimizar el consumo de memoria al cargar y procesar hojas de cálculo. Estas opciones también son útiles para cargar de manera eficiente las hojas de cálculo grandes que contienen grandes conjuntos de datos en el objeto Workbook, como se muestra a continuación.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Determine qué tamaño de pila se necesita para un libro de trabajo determinado**
Aunque hemos mejorado el motor de cálculo de fórmulas Aspose.Cells y, en la mayoría de los casos, debería poder obtener todas las fórmulas calculadas correctamente para un archivo de plantilla determinado sin especificar un tamaño de pila más pequeño. Pero aún así, a veces StackOverFlowException en el método Workbook.CalculateFormula puede ser inevitable. Proporcionamos nuevas API para que los usuarios realicen un seguimiento de los cálculos de fórmulas. Agregamos una clase llamada "AbstractCalculationMonitor" y proporcionamos una propiedad, es decir,*CalculationOptions.CalculationMonitor*para hacer frente a / rastrear el problema.

Los usuarios pueden rastrear el tamaño de la pila por sí mismos utilizando las API. Tenga en cuenta que verificar la pila de cada celda seguramente degradará el rendimiento en mayor medida. Vea el segmento de código de muestra para su referencia:

`     ` clase pública MyCalculationMonitor: AbstractCalculationMonitor
`     `{  ` `public override void BeforeCalculate(int sheetIndex, int rowIndex, int colIndex)  ` `{  ` `if(new StackTrace(false).FrameCount > 2000)  ` `{  ` `lanzar nueva excepción(" Detenga el cálculo de la fórmula debido al riesgo de StackOverflowException");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

No hay mejor manera de usar el tamaño de la pila en tiempo de ejecución. El código anterior que proporcionamos es solo un ejemplo. El rendimiento se degradará significativamente con seguridad. Por lo tanto, creemos que los usuarios (que realmente quieren usarlo) pueden optimizar el código de acuerdo con sus diferentes escenarios y requisitos. Por ejemplo, verificar la pila cuando el recuento de celdas recursivas alcanza cierto número, recopilar la tasa de aumento promedio de la pila para una celda recursiva y determinar la frecuencia para verificar la pila, etc.

{{% /alert %}}

