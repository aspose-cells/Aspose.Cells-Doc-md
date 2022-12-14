---
title: Cómo corregir el error java.lang.OutOfMemoryError al cargar hojas de cálculo grandes
type: docs
weight: 20
url: /es/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Hay buenas posibilidades de que el constructor del libro de trabajo arroje java.lang.OutOfMemoryError al cargar hojas de cálculo grandes. Esta excepción sugiere que la memoria disponible es insuficiente para cargar completamente la hoja de cálculo en la memoria, por lo tanto, la hoja de cálculo debe cargarse mientras se habilita el[Preferencias de memoria](/cells/es/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Cómo corregir java.lang.OutOfMemoryError al cargar una hoja de cálculo grande**
Aspose.Cells Las API brindan preferencias de memoria para optimizar el consumo de memoria al cargar y procesar hojas de cálculo. Estas opciones también son útiles para cargar de manera eficiente las hojas de cálculo grandes que contienen grandes conjuntos de datos en el objeto Workbook, como se muestra a continuación.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
