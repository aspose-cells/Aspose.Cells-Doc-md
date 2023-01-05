---
title: Editor de hojas de cálculo Primeros pasos
type: docs
weight: 10
url: /es/java/spreadsheet-editor-getting-started/
---
**Tabla de contenido**

- [Introducción](#SpreadsheetEditorGettingStarted-Introduction)
- [Requisitos del sistema](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Descarga e Instalación](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Soporte](#SpreadsheetEditorGettingStarted-Support)
- [Contribuir](#SpreadsheetEditorGettingStarted-Contribute)
- [Licencia](#SpreadsheetEditorGettingStarted-License)
### **Introducción**
Html5 Spreadsheet Editor es una aplicación web que puede ver y editar documentos de hojas de cálculo en un navegador web. Es compatible con Excel, SpreadsheetML, CVS, OpenDocument y muchos otros formatos compatibles con Microsoft Excel. Se admiten todas las funciones básicas, incluida la edición de celdas, el formato, la edición de fórmulas, la gestión de filas y columnas, etc.

![todo:imagen_alternativa_texto](aowcrc1.png)

 Editor de hojas de cálculo HTML5 utiliza muchas características de[Aspose.Cells for Java](https://products.aspose.com/cells/java/) y muestra cómo usarlos para crear, manipular y representar una hoja de cálculo en su aplicación Java.

**Características**

- Trabajar con archivos
 - Formatos soportados
 - Abrir archivos locales
 - Abrir desde Dropbox
 - Abrir desde URL
 - Crear una nueva hoja de cálculo
 - Exportar a varios formatos
-  Trabajar con hojas
 - Agregar y quitar hojas
 - Cambiar el nombre de las hojas
 - Cambiar entre hojas
-  Trabajar con filas y columnas
 - Agregar una fila
 - Agregar una columna
 - Eliminar una fila
 - Eliminar una columna
 - Ancho de columna y alto de fila
-  Trabajando con Cells
 - Seleccionar una celda
 - Edición de una celda
 - Fórmula de edición
 - Cell alineación
 - Claro Cell
 - Agregar una celda
 - Eliminar una celda
-  Trabajar con formato de texto
 - Negrita, cursiva, subrayado
 - Estilo y tamaño de fuente
 - Formato claro
### **Requisitos del sistema**
**Requisitos de Software**

- Servidor de aplicaciones Java compatible con CDI
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [Caras del servidor Java 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Requisitos de hardware**

Los requisitos de hardware varían según el servidor de aplicaciones Java que elegimos para implementar HTML5 Spreadsheet Editor y la cantidad de hojas de cálculo que abrimos simultáneamente. A continuación se muestra una estimación, que ayudará a configurar inicialmente el entorno.

- CPU de 2 GHz
- 2GB RAM
- Disco de 500MB
### **Descarga e Instalación**
 HTML5 Spreadsheet Editor es una aplicación Java EE y se puede implementar en cualquier perfil web de servidor de aplicaciones Java compatible con CDI. Ha sido probado con[Pez cristal](https://javaee.github.io/glassfish/).

**Código fuente**

 La fuente del proyecto está disponible en[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). También mantenemos réplicas de Git en los siguientes sitios:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Código Google](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [FuenteForja](https://sourceforge.net/p/html5-spreadsheet-editor/)

Use uno de los siguientes comandos para descargar el código fuente a través de la línea de comandos:

**Github**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Código Google**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**FuenteForja**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Construir usando Maven**

El proceso de creación del proyecto se gestiona mediante Maven. Por lo tanto, puede preparar un archivo WAR desde la línea de comandos sin ningún IDE. Utilice el siguiente comando para generar un WAR para la implementación. La documentación del servidor de aplicaciones correspondiente lo ayudará a implementar el WAR generado y sus dependencias.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**Usando NetBeans**

 Es muy fácil administrar el proyecto usando[IDE de NetBeans](https://netbeans.apache.org/). NetBeans es uno de los IDE populares entre los desarrolladores de Java y está patrocinado por Oracle.

- Descarga el código fuente del proyecto.
- Abra el proyecto en NetBeans IDE.
-  Hacer clic***Correr*** botón en la barra de herramientas.
-  Seleccione***Pez cristal*** servidor como servidor de aplicaciones.

**Usando Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) proporciona integración oficial para importar Maven proyectos llamados[Eclipse M2](http://www.eclipse.org/m2e/):

1. Instale M2Eclipse en su IDE de Eclipse. El procedimiento de instalación se describe en su sitio web.
1. Descarga el código fuente del proyecto.
1. Abre el***Importar*** cuadro de diálogo del menú Archivo.
1.  Seleccione***Maven Proyecto*** desde el cuadro de diálogo de importación.
1.  Hacer clic***Próximo***.
1.  Hacer clic***Navegar*** para seleccionar la ubicación del código fuente.
1.  Seleccione***pom.xml*** de la lista a continuación.
1.  Hacer clic***Finalizar***.

El IDE de Eclipse debería importar y cargar el proyecto.
### **Soporte**
**Informe de error**

 Para enviar un informe de error, cree un nuevo problema en[Página del proyecto Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) y aplicar la etiqueta***insecto***.

**Solicitud de función**

 Apreciamos mucho sus comentarios y las funciones que solicita. Para solicitar una nueva característica o una mejora en la existente, cree un nuevo problema en[Página del proyecto Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) y aplicar la etiqueta***mejora***.

**Preguntas y Ayuda**

 Puede hacer todo tipo de preguntas relacionadas con HTML5 Spreadsheet Editor usando[Problema de Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Simplemente cree un nuevo problema y aplique el***pregunta*** etiqueta.

**Aspose.Cells for Java Foros**

 Los foros de productos Aspose brindan soporte completo para clientes de prueba y pagos. Los expertos están sentados las 24 horas del día, los 7 días de la semana para brindar ayuda y responder consultas. Visitar[foros de productos aquí](https://forum.aspose.com/c/cells/9).

**Aspose blogs**

 Póngase en contacto con nosotros y manténgase actualizado con las últimas noticias sobre nuestros productos y ofertas. Suscribirse a[nuestro blog aquí](http://blog.aspose.com).
### **Contribuir**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:imagen_texto_alterno\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Hoja de cálculo_Editor_por_Aspose.Cells_por_Java)


HTML5 Spreadsheet Editor es un proyecto de código abierto que permite máximas opciones para que todos contribuyan al proyecto.

**Código fuente**

 La fuente del proyecto está disponible en[Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). También mantenemos réplicas de Git en los siguientes sitios:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [FuenteForja](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Solicitudes de extracción**

 Para contribuir con el código fuente al proyecto, simplemente envíe una solicitud de extracción a través de Github. Lea más información en el artículo de Github sobre[Crear una solicitud de extracción](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licencia**
**Licencia MIT**

 Estamos utilizando una de las licencias de código abierto más liberales para obligaciones mínimas de los contribuyentes. Editor de hojas de cálculo HTML5 se publica bajo[Licencia MIT](https://opensource.org/licenses/mit-license.php).

**Aspose Licencia**

 El producto funciona sin licencia Aspose,[con limitaciones](/cells/es/java/licensing/) . Para eliminar las limitaciones, puede adquirir un[licencia temporal gratuita](https://purchase.aspose.com/temporary-license) o[comprar licencia completa](https://purchase.aspose.com/buy).

 Por defecto, el editor intentará cargar**Aspose.Total.Java.lic** archivo de**src/main/resources/com/aspose/spreadsheeteditor** directorio. Simplemente copie el archivo de licencia en este directorio. El comportamiento predeterminado se puede cambiar editando el**AsposeLicencia** clase.
