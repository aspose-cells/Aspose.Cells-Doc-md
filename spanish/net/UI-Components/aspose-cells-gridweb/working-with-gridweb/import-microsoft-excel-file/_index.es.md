---
title: Importar archivo Excel Microsoft
type: docs
weight: 40
url: /es/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

Al igual que Aspose.Cells.GridDesktop, Aspose.Cells.GridWeb, el control puede abrir y cargar Microsoft archivos de Excel, completos con datos, formato, gráficos, imágenes, etc., pero en aplicaciones web. Este tema explica cómo.

{{% /alert %}} 
## **Importar archivos de Excel**
### **Importar desde archivo**
Para abrir un archivo de Excel usando el control Aspose.Cells.GridWeb:

1. Agregue el control Aspose.Cells.GridWeb a un formulario web.
1. Importe el archivo de Excel especificando la ruta del archivo.
1. Ejecute la aplicación.

{{% alert color="primary" %}} 

 Si no sabe cómo agregar el control a un formulario web, consulte[Agregar GridWeb al formulario web](/cells/es/net/add-gridweb-to-web-form/).

{{% /alert %}} 

Cuando se agrega el control Aspose.Cells.GridWeb a un formulario web, el control se instancia automáticamente y se agrega al formulario con un tamaño predeterminado. No tiene que crear un objeto de control Aspose.Cells.GridWeb, todo lo que tiene que hacer es arrastrar y soltar el control y comenzar a usarlo.

Sin embargo, para cargar el contenido de un archivo de Excel al control Aspose.Cells.GridWeb, debe llamar al método ImportExcelFile para especificar la ruta del archivo de Excel. Después de eso, el control Aspose.Cells.GridWeb encontrará automáticamente el archivo de la ruta especificada y mostrará su contenido. A continuación se proporciona un fragmento de código que carga el contenido de un archivo de Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


El fragmento de código anterior se puede utilizar de la forma que desee. Por ejemplo, para cargar un archivo de Excel automáticamente cuando se carga un formulario web, agregue este código al evento Page_Load del formulario. Si desea abrir un archivo cuando se hace clic en un botón, agregue un botón al formulario web y escriba el código anterior debajo del evento Click del botón.

**Un archivo de Excel se carga cuando se hace clic en un botón** 

![todo:imagen_alternativa_texto](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

Si su sistema de archivos es NTFS, debe otorgar permiso de acceso de lectura a las cuentas de usuario ASPNET o Todos o obtendrá una excepción de acceso denegado en tiempo de ejecución.

{{% /alert %}} 
### **Importar desde flujo**
Además de abrir archivos de Excel desde un archivo, el control Aspose.Cells.GridWeb puede cargar archivos de Excel desde una secuencia. Usar el archivo como flujo es un mejor enfoque para prohibir cualquier tipo de acceso a archivos o problemas de violación de uso compartido porque este enfoque garantiza el cierre de todas las conexiones a los archivos al cerrar el flujo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
