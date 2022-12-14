---
title: Cómo especificar la ubicación de las fuentes TrueType
type: docs
weight: 30
url: /es/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

Este artículo describe:

1. [Donde el Aspose.Cells API busca fuentes TrueType](/cells/es/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Cómo especificar explícitamente carpetas de fuentes TrueType para Aspose.Cells API](/cells/es/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Cómo restringir el Aspose.Cells API para usar solo una ubicación de fuentes TrueType](/cells/es/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Trabajar con fuentes**

### **Donde Aspose.Cells busca fuentes TrueType en Windows**

 Aspose.Cells busca fuentes en el**Windows\Fuentes** carpeta. Esta configuración predeterminada funciona la mayor parte del tiempo, así que solo especifique sus propias carpetas de fuentes si realmente lo necesita.

### **Dónde Aspose.Cells busca fuentes TrueType en Linux**

De manera predeterminada, Aspose.Cells API busca las fuentes en todas las ubicaciones siguientes, aunque las diferentes distribuciones de Linux almacenan las fuentes en carpetas diferentes.

1. /usr/share/fuentes
1. /usr/local/share/fuentes

{{% alert color="primary" %}}

 Este comportamiento predeterminado funcionará para la mayoría de las distribuciones de Linux, pero no se garantiza que funcione todo el tiempo. Es posible que deba especificar la ubicación de las fuentes TrueType explícitamente.

{{% /alert %}}

### **Cómo especificar explícitamente una carpeta de fuentes**

Aspose.Cells Las API han expuesto muchos métodos de fábrica para que la clase FontConfigs especifique las fuentes o las carpetas de fuentes, como se describe a continuación.

1. El método setFontFolder acepta el primer parámetro de tipo String con ubicación en el directorio de fuentes, mientras que el segundo parámetro de tipo Boolean es para dirigir las API Aspose.Cells para buscar archivos de fuentes en las carpetas de forma recursiva.
1. El método setFontFolders acepta una matriz de tipo String, por lo que puede especificar muchos directorios de fuentes utilizando este enfoque. También puede indicarle al AP Aspose.Cells que busque las carpetas de forma recursiva especificando verdadero como segundo parámetro.
1. El método setFontSources acepta una matriz de tipo FontSourceBase para que especifique una lista de ubicaciones de fuentes individuales.

{{% alert color="primary" %}}

Al especificar la carpeta de fuentes utilizando cualquiera de los métodos mencionados anteriormente, recomendamos configurar la ubicación de la fuente al inicio de la aplicación; de lo contrario, puede obtener resultados con un formato deficiente.

{{% /alert %}} {{% alert color="primary" %}}

Configurar la carpeta de fuentes con cualquiera de los métodos anteriores no garantiza que Aspose.Cells API no busque las fuentes en ubicaciones predeterminadas, como la carpeta de fuentes del sistema.

{{% /alert %}}

### **Cómo restringir el Aspose.Cells para usar solo una carpeta de fuentes**

 A partir de Aspose.Cells for Java 8.1.0, establecer los argumentos de JVM como**-DAspose.Cells.FontDirExc="TuFontDir**se asegurará de que el Aspose.Cells API solo use la ubicación de las fuentes como se especifica.

Establezca los argumentos especificados mediante el método System.setProperty como se muestra a continuación.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Tenga en cuenta lo siguiente:

- La declaración anterior debe estar al comienzo de su solicitud.
- El uso del enfoque anterior no requiere configurar el directorio de fuentes usando ninguno de los métodos FontConfigs discutidos anteriormente.
- La cadena "FontDirSet" debe ser la ruta completa a la carpeta que contiene las fuentes requeridas.

{{% /alert %}}
