---
title: Configuración de página y opciones de impresión
type: docs
weight: 10
url: /es/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

A veces, los desarrolladores necesitan configurar la configuración de página y las opciones de impresión para controlar el proceso de impresión. La configuración de página y las opciones de impresión ofrecen varias opciones y son totalmente compatibles con Aspose.Cells.

Este artículo muestra cómo crear una aplicación de consola y aplicar la configuración de página y las opciones de impresión a una hoja de cálculo con unas pocas líneas simples de código utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Trabajar con configuraciones de página y de impresión**

Para este ejemplo, creamos un libro en Microsoft Excel y utilizamos Aspose.Cells para establecer la configuración de página y las opciones de impresión.

### **Configuración de opciones de configuración de página**

Primero crea una hoja de cálculo simple en Microsoft Excel. Luego aplica opciones de configuración de página en ella. Ejecutar el código cambia las opciones de configuración de página como se muestra en la captura de pantalla a continuación.

Archivo de salida 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Crea una hoja de cálculo con algunos datos en Microsoft Excel:
   1. Abra un nuevo libro en Microsoft Excel.
   1. Agregue algunos datos.
      A continuación se muestra una captura de pantalla del archivo.

      **Archivo de entrada**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Configure las opciones de la configuración de página:
   Aplique las opciones de configuración de página al archivo. A continuación se muestra una captura de pantalla de las opciones predeterminadas, antes de que se apliquen las nuevas opciones.

   **Opciones de configuración de página predeterminadas**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Descargue e instale Aspose.Cells:
   1. [Descargar](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Descomprímelo en tu computadora de desarrollo.
      Todos los componentes [Aspose](http://www.aspose.com/), cuando se instalan, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. Crear un proyecto.
   Cree un proyecto usando un editor de Java, como Eclipse, o cree un programa simple usando un editor de texto.
1. Agregar una ruta de clase.
   1. Extrae Aspose.Cells.jar y dom4j_1.6.1.jar de Aspose.Cells.zip.
   1. Configura la ruta de clase del proyecto en Eclipse:
   1. Seleccionar su proyecto en Eclipse y luego hacer clic en **Proyecto** seguido de **Propiedades**.
   1. Seleccionar **Ruta de compilación de Java** a la izquierda del cuadro de diálogo.
   1. Seleccionar la pestaña de Bibliotecas, hacer clic en **Agregar JARs** o **Agregar JARs externos** para seleccionar Aspose.Cells.jar y dom4j_1.6.1.jar y agregarlos a las rutas de compilación.
      O puede configurarlo en tiempo de ejecución en un símbolo del sistema en Windows:

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Escribir la aplicación que invoca las APIs:
   A continuación se muestra el código utilizado por el componente en este ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Configuración de opciones de impresión**

Las configuraciones de la configuración de página también proporcionan varias opciones de impresión (también llamadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo. Permiten a los usuarios:

- Seleccionar un área de impresión específica de una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Encabezados de fila/columna de impresión.
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

El ejemplo que sigue aplica opciones de impresión al archivo creado en el ejemplo anterior (PageSetup.xls). La captura de pantalla a continuación muestra las opciones de impresión predeterminadas antes de aplicar nuevas opciones.
**Documento de entrada**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

Ejecutar el código cambia las opciones de impresión.
Archivo de salida

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Resumen**

{{% alert color="primary" %}}

Este artículo muestra cómo configurar la página de configuración y las opciones de impresión de hojas utilizando Aspose.Cells. Con suerte, le dará una idea, y podrá usar estas opciones en sus propios escenarios.

Aspose.Cells se beneficia de años de investigación, diseño y ajustes cuidadosos. Le damos la bienvenida cordialmente a sus consultas, comentarios y sugerencias en el [Foro de Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantizamos una pronta respuesta.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
