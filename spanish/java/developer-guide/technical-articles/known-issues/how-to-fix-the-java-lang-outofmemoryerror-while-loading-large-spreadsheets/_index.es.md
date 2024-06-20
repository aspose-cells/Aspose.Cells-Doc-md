---
title: Cómo solucionar el java.lang.OutOfMemoryError al cargar hojas de cálculo grandes
type: docs
weight: 20
url: /es/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Existe la posibilidad de que el constructor de Workbook lance java.lang.OutOfMemoryError al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse habilitando las [Preferencias de Memoria](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Cómo solucionar el java.lang.OutOfMemoryError al cargar hojas de cálculo grandes**
Las API de Aspose.Cells proporcionan Preferencias de memoria para optimizar el consumo de memoria al cargar y procesar hojas de cálculo. Estas opciones también son útiles para cargar eficientemente hojas de cálculo grandes que contienen enormes conjuntos de datos en el objeto Workbook, como se muestra a continuación. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
