---
title: Configuración de página y opciones de impresión
type: docs
weight: 10
url: /es/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

A veces, los desarrolladores necesitan configurar la configuración de la página y la configuración de impresión para controlar el proceso de impresión. La configuración de página y la configuración de impresión ofrecen varias opciones y son totalmente compatibles con Aspose.Cells.

Este artículo muestra cómo crear una aplicación de consola y aplicar la configuración de página y las opciones de impresión a una hoja de trabajo con unas pocas líneas simples de código usando el Aspose.Cells API.

{{% /alert %}}

## **Trabajar con la configuración de página e impresión**

Para este ejemplo, creamos un libro de trabajo en Microsoft Excel y usamos Aspose.Cells para configurar la configuración de página y las opciones de impresión.

### **Configuración de las opciones de configuración de página**

Primero cree una hoja de trabajo simple en Microsoft Excel. Luego aplique las opciones de configuración de página. Ejecutar el código cambia las opciones de Configuración de página como se muestra en la siguiente captura de pantalla.

**Archivo de salida** 

![todo:imagen_alternativa_texto](page-setup-and-printing-options_1.png)

1. Cree una hoja de trabajo con algunos datos en Microsoft Excel:
 1. Abra un nuevo libro de trabajo en Microsoft Excel.
 1. Agregue algunos datos.
 A continuación se muestra una captura de pantalla del archivo.

      **Fichero de entrada**

![todo:imagen_alternativa_texto](page-setup-and-printing-options_2.png)

1. Establecer opciones de configuración de página:
 Aplicar opciones de configuración de página al archivo. A continuación se muestra una captura de pantalla de las opciones predeterminadas, antes de que se apliquen las nuevas opciones.

   **Opciones de configuración de página predeterminada**

![todo:imagen_alternativa_texto](page-setup-and-printing-options_3.png)

1. Descargar e instalar Aspose.Cells:
   1. [Descargar](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Descomprímalo en su computadora de desarrollo.
 Todos[Aspose](http://www.aspose.com/) Los componentes, cuando están instalados, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inyecta marcas de agua en los documentos producidos.
1. Crea un proyecto.
 Cree un proyecto usando un editor Java, por ejemplo, Eclipse, o cree un programa simple usando un editor de texto.
1. Agregue una ruta de clase.
1. Extraiga Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
 1. Establezca el classpath del proyecto en Eclipse:
 1. Seleccione su proyecto en Eclipse y luego haga clic en**Proyecto** seguido por**Propiedades**.
 1. Seleccione**Java Ruta de construcción** la izquierda del cuadro de diálogo.
 1. Seleccione la pestaña Bibliotecas, haga clic en**Agregar JAR** o**Agregar JAR externos** para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de compilación.
 O puede configurarlo en tiempo de ejecución en un indicador de DOS en Windows:

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Escriba la aplicación que invoca las API:
 A continuación se muestra el código utilizado por el componente en este ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Configuración de las opciones de impresión**

Los ajustes de configuración de página también proporcionan varias opciones de impresión (también llamadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de trabajo. Permiten a los usuarios:

- Seleccione un área de impresión específica de una hoja de cálculo.
- Imprimir títulos.
- Imprimir líneas de cuadrícula.
- Imprimir encabezados de fila/columna.
- Consiga calidad de borrador.
- Imprimir comentarios.
- Imprimir errores de celda.
- Definir el orden de las páginas.

El siguiente ejemplo aplica opciones de impresión al archivo creado en el ejemplo anterior (PageSetup.xls). La siguiente captura de pantalla muestra las opciones de impresión predeterminadas antes de que se apliquen nuevas opciones.
**Documento de entrada**

![todo:imagen_alternativa_texto](page-setup-and-printing-options_4.png)

Ejecutar el código cambia las opciones de impresión.
**Archivo de salida**

![todo:imagen_alternativa_texto](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Resumen**

{{% alert color="primary" %}}

Este artículo muestra cómo configurar la configuración de página y las opciones de impresión de hojas usando Aspose.Cells. Con suerte, le dará una idea y puede usar estas opciones en sus propios escenarios.

 Aspose.Cells se beneficia de años de investigación, diseño y ajuste cuidadoso. Agradecemos sus consultas, comentarios y sugerencias en[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
