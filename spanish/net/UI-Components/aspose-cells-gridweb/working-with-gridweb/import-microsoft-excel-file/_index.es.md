---
title: Importar archivo de Microsoft Excel
type: docs
weight: 40
url: /es/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb, importar
description: Este artículo presenta cómo importar archivos en GridWeb.
---

{{% alert color="primary" %}} 

Al igual que Aspose.Cells.GridDesktop, el control Aspose.Cells.GridWeb puede abrir y cargar archivos de Microsoft Excel, completos con datos, formato, gráficos, imágenes, etc., pero en aplicaciones web. Este tema explica cómo.

{{% /alert %}} 
## **Importar archivos de Excel**
### **Importar desde archivo**
Para abrir un archivo de Excel usando el control Aspose.Cells.GridWeb:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Importe el archivo de Excel especificando la ruta del archivo.
1. Ejecute la aplicación.

{{% alert color="primary" %}} 

Si no sabe cómo agregar el control a un formulario web, consulte [Agregar GridWeb a un formulario web](/cells/es/net/aspose-cells-gridweb/add-gridweb-to-web-form/).

{{% /alert %}} 

Cuando el control Aspose.Cells.GridWeb se agrega a un formulario web, el control se instancia automáticamente y se agrega al formulario con un tamaño predeterminado. No es necesario crear un objeto de control Aspose.Cells.GridWeb, solo tiene que arrastrar y soltar el control y empezar a usarlo.

Sin embargo, para cargar el contenido de un archivo de Excel en el control Aspose.Cells.GridWeb, tiene que llamar al método ImportExcelFile para especificar la ruta del archivo de Excel. Después de eso, el control Aspose.Cells.GridWeb buscará automáticamente el archivo en la ruta especificada y mostrará su contenido. A continuación, se proporciona un fragmento de código que carga el contenido de un archivo de Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


El fragmento de código anterior se puede utilizar de la forma que desee. Por ejemplo, para cargar un archivo de Excel automáticamente cuando se carga un formulario web, agregue este código al evento Page_Load del formulario. Si desea abrir un archivo cuando se hace clic en un botón, agregue un botón al formulario web y escriba el código anterior en el evento Click del botón.

**Se carga un archivo de Excel cuando se hace clic en un botón** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Si su sistema de archivos es NTFS, debe otorgar permiso de acceso de lectura a las cuentas de usuario ASPNET o Everyone, o recibirá una excepción de acceso denegado en tiempo de ejecución.

{{% /alert %}} 
### **Importar desde flujo**
Además de abrir archivos de Excel desde un archivo, el control Aspose.Cells.GridWeb puede cargar archivos de Excel desde un flujo. Utilizar un archivo como flujo es un enfoque mejor para evitar cualquier tipo de problemas de acceso o violación de uso compartido de archivos, ya que este enfoque garantiza el cierre de todas las conexiones a los archivos mediante el cierre del flujo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
