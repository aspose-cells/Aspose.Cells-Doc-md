---
title: Abrir un archivo de Excel
type: docs
weight: 10
url: /es/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Una característica única de Aspose.Cells Grid Suite es su compatibilidad con archivos de Excel. En este tema, demostraremos cómo los usuarios pueden abrir archivos de Excel en sus aplicaciones de Windows usando el control Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Introducción**
 Para abrir un archivo de Excel usando Aspose.Cells.GridDesktop, debe crear una aplicación de escritorio con GridDesktop Control en ella. Si no sabe cómo agregar el control Aspose.Cells.GridDesktop a su formulario de Windows, debe consultar[Cómo usar Aspose.Cells.GridDesktop](/cells/es/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop proporciona tres formas diferentes de abrir un archivo de Excel.

1. **Apertura desde un archivo**
1. **Abriendo un archivo CSV**
1. **Apertura desde un arroyo**
## **Abrir archivo de Excel**
En este ejemplo, cree una aplicación de escritorio y haga lo siguiente.

- Agregue un control GridControl al formulario.
- Agregue tres botones con sus propiedades de texto establecidas de la siguiente manera:
  - **Abrir archivo de Excel**
  - **Abrir archivo CSV**
  - **Abrir desde Stream**
### **Apertura desde un archivo**
 Para cargar el contenido de un archivo de Excel al control Aspose.Cells.GridDesktop, deberá llamar a un método del control para especificar la ruta del archivo de Excel. Después de eso, el control Aspose.Cells.GridDesktop encontrará automáticamente el archivo de la ruta especificada y mostrará su contenido. El fragmento de código para cargar el contenido de un archivo de Excel se proporciona en el siguiente ejemplo. Cree el evento Click del**Abrir archivo de Excel** botón y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


Los desarrolladores pueden utilizar el fragmento de código anterior de la forma que deseen. Por ejemplo, si desea cargar un archivo de Excel automáticamente cuando se carga un formulario de Windows, puede agregar este código en el evento Cargar de su formulario.
### **Abriendo un archivo CSV**
Aspose.Cells. El control GridDesktop también admite la carga del archivo CSV. Cree el evento Click del**Abrir archivo CSV** botón y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Apertura desde un arroyo**
 En nuestra discusión anterior, hemos discutido sobre la carga de un archivo de Excel usando su ruta de archivo, pero el control Aspose.Cells.GridDesktop también admite la carga de un archivo de Excel desde una secuencia. Cree el evento Click del**Abrir desde Stream** botón y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Usar el archivo como flujo es un mejor enfoque para prohibir cualquier tipo de acceso a archivos o problemas de violación de uso compartido porque este enfoque garantiza el cierre de todas las conexiones a los archivos al cerrar el flujo.

{{% alert color="primary" %}} 

IMPORTANTE: Un punto importante a discutir es que el control Aspose.Cells.GridDesktop también contiene un método llamado LoadFromExcel, que también se usa para cargar el contenido de un archivo de Excel en Grid. Pero, este método ahora está obsoleto. Por lo tanto, se recomienda que todos los desarrolladores utilicen el método ImportExcelFile que es más robusto y eficiente que el obsoleto.

{{% /alert %}}
