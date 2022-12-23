---
title: Guardar un archivo de Excel
type: docs
weight: 20
url: /es/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

Con el control Aspose.Cells.GridDesktop, los usuarios no solo pueden crear nuevos archivos de Excel, sino también administrar los existentes. Pero, en ambos casos, sería necesario guardar el contenido del Aspose.Cells.GridDesktop. Entonces, este es el tema de nuestra discusión ahora para que nuestros usuarios sepan cómo pueden guardar sus contenidos de Grid como un archivo de Excel.

{{% /alert %}} 
## **Introducción**
Para guardar el contenido del control Aspose.Cells.GridDesktop como un archivo de Excel, Aspose.Cells.GridDesktop proporciona los siguientes métodos.

1. **Guardar como archivo**
1. **Guardar como flujo**
## **Guardar archivo**
 Cree una aplicación de escritorio y agregue dos botones con un control GridControl al formulario. Establecer las propiedades de texto de los botones como**Guardar como archivo** y**Guardar como transmisión** respectivamente.
### **Guardar como archivo**
 Cree el evento Click del**Guardar como archivo** botón y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Un punto importante a discutir es que el control Aspose.Cells.GridDesktop también contiene un método llamado SaveToExcel, que también se usa para cargar el contenido de un archivo de Excel en Grid. Pero, este método ahora está obsoleto. Por lo tanto, se recomienda que todos los desarrolladores utilicen el método ExportExcelFile que es más robusto y eficiente que el obsoleto.

{{% /alert %}} 
### **Guardar como flujo**
 A veces, los desarrolladores pueden solicitar que guarden el contenido de su cuadrícula en una secuencia (por ejemplo, MemoryStream). Para facilitar esta tarea, el control Aspose.Cells.GridDesktop también admite guardar datos de Grid en una secuencia. Cree el evento Click del**Guardar como transmisión** botón y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel admite hojas de Excel que pueden contener 65 536 filas y 256 columnas como máximo. Aspose.Cells. GridDesktop también sigue los mismos estándares. En el control Aspose.Cells.GridDesktop, los desarrolladores pueden crear más filas y columnas que el límite estándar, pero al guardar los datos de la cuadrícula en un archivo de Excel, se generará una excepción. Significa que solo los datos contenidos en las 65 536 filas y las 256 columnas se pueden guardar en un archivo de Excel usando Aspose.Cells.GridDesktop.

{{% /alert %}}
