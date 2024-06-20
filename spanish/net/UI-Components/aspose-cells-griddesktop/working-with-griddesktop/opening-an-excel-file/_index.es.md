---
title: Abrir un archivo de Excel
type: docs
weight: 10
url: /es/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop, abrir, archivo
description: Este artículo presenta cómo abrir un archivo en GridDesktop.
---

{{% alert color="primary" %}} 

Una característica única de la Suite de Cuadrícula Aspose.Cells es su compatibilidad con los archivos de Excel. En este tema, demostraremos cómo los usuarios pueden abrir archivos de Excel en sus aplicaciones de Windows utilizando el control Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **Introducción**
Para abrir un archivo de Excel utilizando Aspose.Cells.GridDesktop, debe crear una aplicación de escritorio con el Control GridDesktop en ella. Si no sabe cómo agregar el control Aspose.Cells.GridDesktop a su formulario de Windows, consulte [Cómo usar Aspose.Cells.GridDesktop](/cells/es/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop proporciona tres formas diferentes de abrir un archivo de Excel.

1. **Apertura desde un archivo**
1. **Apertura de un archivo CSV**
1. **Apertura desde un flujo**
## **Abriendo archivo de Excel**
En este ejemplo, cree una aplicación de escritorio y realice lo siguiente.

- Agregue un control GridControl al formulario.
- Agregue tres botones con sus propiedades de texto configuradas de la siguiente manera:
  - **Abrir archivo de Excel**
  - **Abrir archivo CSV**
  - **Abrir desde secuencia**
### **Abriendo desde un archivo**
Para cargar el contenido de un archivo de Excel al control Aspose.Cells.GridDesktop, tendrá que llamar a un método del control para especificar la ruta del archivo de Excel. Después de eso, el control Aspose.Cells.GridDesktop encontrará automáticamente el archivo desde la ruta especificada y mostrará su contenido. El código para cargar el contenido de un archivo de Excel se proporciona en el siguiente ejemplo. Cree el evento Click del botón **Abrir archivo de Excel** y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


El fragmento de código anterior puede ser utilizado por los desarrolladores de la manera que deseen. Por ejemplo, si desean cargar un archivo de Excel automáticamente cuando se carga un formulario de Windows, pueden agregar este código bajo el evento Load de su formulario.
### **Abriendo un archivo CSV**
El control Aspose.Cells.GridDesktop también es compatible con la carga de archivos CSV. Cree el evento Click del botón **Abrir archivo CSV** y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **Abriendo desde una secuencia**
En nuestra discusión anterior, hemos hablado sobre la carga de un archivo de Excel utilizando su ruta de archivo, pero el control Aspose.Cells.GridDesktop también es compatible con la carga de archivos de Excel desde una secuencia. Cree el evento Click del botón **Abrir desde secuencia** y pegue el siguiente código dentro de él.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



Utilizar el archivo como una secuencia es un enfoque mejor para evitar cualquier tipo de problema de acceso o violación de compartir archivos porque este enfoque garantiza cerrar todas las conexiones a los archivos al cerrar la secuencia.

{{% alert color="primary" %}} 

IMPORTANTE: Un punto importante a discutir es que el control Aspose.Cells.GridDesktop también contiene un método llamado LoadFromExcel, que también se utiliza para cargar el contenido de un archivo de Excel al Grid. Pero, este método ahora está obsoleto. Por lo tanto, se recomienda a todos los desarrolladores que utilicen el método ImportExcelFile, que es más robusto y eficiente que el obsoleto.

{{% /alert %}}
