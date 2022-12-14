---
title: Aspose.Cells for Java 20.5 Notas de la versión
type: docs
weight: 20
url: /es/java/aspose-cells-for-java-20-5-release-notes/
---
{{% alert color="primary" %}}

 Esta página contiene notas de la versión para[Aspose.Cells for Java 20.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.5/).

{{% /alert %}}

|**Llave**|**Resumen**|**Categoría**|
|:- |:- |:- |
|CELLSJAVA-43173|Cuando el campo de grupo tiene un valor nulo, el resultado de subtotalN pierde el subtotal para el grupo nulo|Mejora|
|CELLSJAVA-43162|Representación de Excel a HTML: el proceso de conversión lleva mucho tiempo|Insecto|
|CELLSJAVA-43164|La conversión de HTML a Excel no conserva los formatos de texto enriquecido en la salida|Insecto|
|CELLSJAVA-43166|El texto girado no se representa correctamente en la conversión de XLSX a HTML|Insecto|
|CELLSJAVA-43178|Los formatos RichText se pierden al exportar el archivo a HTML|Insecto|
|CELLSJAVA-43165|Cadena "20TT1" reemplazada con el número 43850 durante la conversión de CSV a XLSB|Insecto|
|CELLSJAVA-43026|Después de representar el gráfico en la imagen, las etiquetas de datos cambian de estilo y los valores no son los mismos|Insecto|
|CELLSJAVA-43154|Algunos puntos del gráfico se superponen por etiqueta|Insecto|
|CELLSJAVA-43089|El gráfico de radar está invertido y los valores de los ejes no son idénticos al gráfico original en la conversión de XLS a PDF|Insecto|
|CELLSJAVA-43171|El documento se rompe después de copiar las hojas.|Insecto|
|CELLSJAVA-43172|Un problema con los marcadores inteligentes en las celdas combinadas|Insecto|
|CELLSJAVA-43183|Excepción "ClassCastException: ...." al calcular la tabla dinámica|Excepción|
|CELLSJAVA-43177|El nuevo libro de trabajo con archivo CSV da como resultado "java.lang.IndexOutOfBoundsException: milisegundo"|Excepción|
|CELLSJAVA-43168|Excepción "IllegalStateException: este no es un archivo de almacenamiento estructurado" al fusionar archivos de Excel|Excepción|
|CELLSJAVA-43179|Excepción NumberFormatException: Para la cadena de entrada: "preservar"|Excepción|
|CELLSJAVA-43182|Excepción 'lang.IllegalStateException: codificación no válida: nulo' al cargar el archivo XLS|Excepción|
## **Public API y cambios incompatibles con versiones anteriores**
La siguiente es una lista de los cambios realizados al público API, como miembros agregados, renombrados, eliminados o obsoletos, así como cualquier cambio no compatible con versiones anteriores realizado en Aspose.Cells for Java. Si tiene inquietudes sobre cualquier cambio enumerado, plantéelo en el foro de soporte Aspose.Cells.
### **Agrega el método WorkbookSettings.GetThemeFont().**
Obtiene la fuente del tema.
### **Agrega la propiedad DataLabels.LinkedSource.**
Obtiene y establece la fuente vinculada.
### **Agrega la enumeración DefaultEditLanguage.**
Representa el idioma de edición predeterminado.
### **Agrega la propiedad ImageOrPrintOptions.DefaultEditLanguage.**
Obtiene o establece el idioma de edición predeterminado.
Puede mostrar/representar diferentes diseños para párrafos de texto cuando se configuran diferentes idiomas de edición.
### **Agrega la propiedad PdfSaveOptions.DefaultEditLanguage.**
Obtiene o establece el idioma de edición predeterminado.
Puede mostrar/representar diferentes diseños para párrafos de texto cuando se configuran diferentes idiomas de edición.
