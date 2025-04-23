---
title: Introducción al Editor de Hojas de Cálculo
type: docs
weight: 10
url: /es/java/spreadsheet-editor-getting-started/
---

**Tabla de contenidos**

- [Introducción](#SpreadsheetEditorGettingStarted-Introduction)
- [Requisitos del sistema](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Descarga e Instalación](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Soporte](#SpreadsheetEditorGettingStarted-Support)
- [Contribuir](#SpreadsheetEditorGettingStarted-Contribute)
- [Licencia](#SpreadsheetEditorGettingStarted-License)
### **Introducción**
Html5 Spreadsheet Editor es una aplicación web que puede ver y editar documentos de hojas de cálculo en un navegador web. Admite Excel, SpreadsheetML, CVS, OpenDocument y muchos otros formatos admitidos por Microsoft Excel. Se admiten todas las funciones básicas, incluida la edición de celdas, formato, edición de fórmulas, gestión de filas y columnas, etc.

![todo:image_alt_text](aowcrc1.png)

El Editor de Hojas de Cálculo HTML5 utiliza muchas funciones de [Aspose.Cells for Java](https://products.aspose.com/cells/java/) y muestra cómo usarlas para crear, manipular y renderizar una hoja de cálculo en tu aplicación Java.

**Características**

- Trabajar con Archivos 
  - Formatos Soportados
  - Abrir archivos locales
  - Abrir desde Dropbox
  - Abrir desde URL
  - Crear una nueva hoja de cálculo
  - Exportar a varios formatos
- Trabajar con hojas 
  - Agregar y eliminar hojas
  - Renombrar hojas
  - Cambiar entre hojas
- Trabajar con filas y columnas 
  - Agregar una fila
  - Agregar una columna
  - Eliminar una fila
  - Eliminar una columna
  - Ancho de columna y altura de fila
- Trabajar con celdas 
  - Seleccionar una celda
  - Editar una celda
  - Editar fórmula
  - Alineación de celda
  - Borrar celda
  - Agregar una celda
  - Quitar una celda
- Trabajar con formato de texto 
  - Negrita, cursiva, subrayado
  - Estilo y tamaño de fuente
  - Borrar formato
### **Requisitos del sistema**
**Requerimientos de Software**

- Servidor de aplicaciones Java con soporte CDI
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Requerimientos de Hardware**

Los requisitos de hardware varían según el servidor de aplicaciones Java que elijamos para desplegar el Editor de Hoja de Cálculo HTML5 y el número de hojas de cálculo que abrimos simultáneamente. A continuación, se presenta una estimación que ayudará a configurar inicialmente el entorno.

- 2 GHz CPU
- 2 GB RAM
- 500 MB de Disco
### **Descarga e Instalación**
El Editor de Hoja de Cálculo HTML5 es una aplicación Java EE y puede ser desplegada en cualquier servidor de aplicaciones Java con soporte CDI. Ha sido probado con [Glassfish](https://javaee.github.io/glassfish/).

**Código Fuente**

El origen del proyecto está disponible en [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). También estamos manteniendo espejos Git en los siguientes sitios:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Utilice uno de los siguientes comandos para descargar el código fuente a través de la línea de comandos:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Construir usando Maven**

El proceso de construcción del proyecto se gestiona utilizando Maven. Por lo tanto, puede preparar un archivo WAR desde la línea de comandos sin necesidad de utilizar ningún IDE. Utilice el siguiente comando para generar un archivo WAR para implementación. La documentación del servidor de aplicaciones correspondiente le ayudará a implementar el WAR generado y sus dependencias.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**Usando NetBeans**

Es muy fácil gestionar el proyecto utilizando [NetBeans IDE](https://netbeans.apache.org/). NetBeans es uno de los IDE más populares entre los desarrolladores de Java y está patrocinado por Oracle.

- Descargar el código fuente del proyecto.
- Abrir el proyecto en el IDE de NetBeans.
- Hacer clic en el botón ***Ejecutar*** en la barra de herramientas.
- Seleccionar ***Glassfish*** como servidor de aplicaciones.

**Usando Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) ofrece integración oficial para importar proyectos Maven llamada [M2Eclipse](http://www.eclipse.org/m2e/):

1. Instale M2Eclipse en su Eclipse IDE. El procedimiento de instalación se describe en su sitio web.
1. Descargue el código fuente del proyecto.
1. Abra el cuadro de dialogo ***Importar*** desde el menú Archivo.
1. Seleccione ***Proyecto Maven*** desde el cuadro de dialogo de importación.
1. Haga clic en ***Siguiente***.
1. Haga clic en ***Examinar*** para seleccionar la ubicación del código fuente.
1. Seleccione ***pom.xml*** de la lista a continuación.
1. Haga clic en ***Finalizar***.

El Eclipse IDE debería importar y cargar el proyecto.
### **Soporte**
**Informe de error**

Para enviar un informe de error, cree un nuevo problema en la [página del proyecto en Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) y aplique la etiqueta ***bug***.

**Solicitud de función**

Apreciamos mucho sus comentarios y las funciones que solicita. Para solicitar una nueva función o mejora en la actual, por favor cree un nuevo problema en la [página del proyecto en Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) y aplique la etiqueta ***mejora***.

**Preguntas y Ayuda**

Puede hacer cualquier tipo de pregunta relacionada con el Editor de Hojas de Cálculo HTML5 utilizando [los problemas de Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues). Simplemente cree un nuevo problema y aplique la etiqueta ***pregunta***.

**Foros de Aspose.Cells for Java**

Los foros de productos de Aspose brindan soporte completo tanto para clientes de prueba como para clientes pagados. Expertos están disponibles las 24 horas del día, los 7 días de la semana para brindar ayuda y responder consultas. Visite los [foros de producto aquí](https://forum.aspose.com/c/cells/9).

**Blogs de Aspose**

Manténgase en contacto con nosotros y manténgase actualizado con las últimas noticias sobre nuestros productos y ofertas. Suscríbase a [nuestro blog aquí](http://blog.aspose.com).
### **Contribuir**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


El Editor de Hojas de Cálculo HTML5 es un proyecto de código abierto que permite a todos contribuir al proyecto.

**Código Fuente**

El código fuente del proyecto está disponible en [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). También mantenemos espejos de Git en los siguientes sitios:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Solicitudes de Extracción (Pull Requests)**

Para contribuir con código fuente al proyecto, simplemente envía una solicitud de extracción a través de Github. Lee más información en el artículo de Github sobre [Crear una solicitud de extracción](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licencia**
**Licencia MIT**

Estamos utilizando una de las licencias de código abierto más liberales para mínimas responsabilidades de los contribuyentes. El Editor de Hojas de Cálculo HTML5 se publica bajo la [Licencia MIT](https://opensource.org/licenses/mit-license.php).

**Licencia Aspose**

El producto funciona sin licencia de Aspose, [con limitaciones](/cells/es/java/licensing/). Para eliminar las limitaciones, puedes adquirir una [licencia temporal gratuita](https://purchase.aspose.com/temporary-license) o [comprar una licencia completa](https://purchase.aspose.com/buy).

Por defecto, el editor intentará cargar el archivo **Aspose.Total.Java.lic** desde el directorio **src/main/resources/com/aspose/spreadsheeteditor**. Simplemente copia el archivo de licencia a este directorio. El comportamiento por defecto puede cambiarse editando la clase **AsposeLicense**.
{{< app/cells/assistant language="java" >}}
