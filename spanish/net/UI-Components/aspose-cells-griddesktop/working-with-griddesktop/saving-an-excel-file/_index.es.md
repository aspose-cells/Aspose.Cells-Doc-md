---
title: Guardando un archivo de Excel
type: docs
weight: 20
url: /es/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop, guardar, archivo
description: Este artículo presenta cómo guardar un archivo en GridDesktop.
---

{{% alert color="primary" %}} 

Usando el control Aspose.Cells.GridDesktop, los usuarios no solo pueden crear nuevos archivos de Excel, sino también gestionar los existentes. Pero, en ambos casos, sería necesario guardar el contenido del Aspose.Cells.GridDesktop. Así que, este es el tema de nuestra discusión ahora para informar a nuestros usuarios sobre cómo pueden guardar su contenido de Grid como un archivo de Excel.

{{% /alert %}} 
## **Introducción**
Para guardar el contenido del control Aspose.Cells.GridDesktop como un archivo de Excel, Aspose.Cells.GridDesktop proporciona los siguientes métodos.

1. **Guardar como archivo**
1. **Guardar como secuencia**
## **Guardar archivo**
Cree una aplicación de escritorio y agregue dos botones con un control GridControl al formulario. Establezca las propiedades de texto de los botones como **Guardar como archivo** y **Guardar como secuencia** respectivamente.
### **Guardar como archivo**
Cree el evento Click del botón **Guardar como archivo** y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Un punto importante a discutir es que el control Aspose.Cells.GridDesktop también contiene un método llamado SaveToExcel, que solía cargaba contenido de un archivo de Excel a la cuadrícula. Sin embargo, este método ahora está obsoleto. Por lo tanto, se recomienda que todos los desarrolladores utilicen el método ExportExcelFile, que es más sólido y eficiente que el obsoleto.

{{% /alert %}} 
### **Guardar como secuencia**
A veces, los desarrolladores pueden necesitar guardar el contenido de su cuadrícula en una secuencia (por ejemplo, MemoryStream). Para facilitar esta tarea, el control Aspose.Cells.GridDesktop también admite guardar datos de la cuadrícula en una secuencia. Cree el evento Click del botón **Guardar como secuencia** y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Microsoft Excel admite que las hojas de Excel pueden contener un máximo de 65,536 filas y 256 columnas. Aspose.Cells.GridDesktop también sigue los mismos estándares. En el control Aspose.Cells.GridDesktop, los desarrolladores pueden crear más filas y columnas que el límite estándar, pero al guardar los datos de la cuadrícula en un archivo de Excel, se producirá una excepción. Esto significa que solo los datos contenidos en las 65,536 filas y 256 columnas se pueden guardar en un archivo de Excel mediante Aspose.Cells.GridDesktop.

{{% /alert %}}
