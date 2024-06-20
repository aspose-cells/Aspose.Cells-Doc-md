---
title: Cómo especificar la ubicación de las fuentes TrueType
type: docs
weight: 30
url: /es/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

Este artículo describe:

1. [Dónde busca la API Aspose.Cells las fuentes TrueType](/cells/es/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Cómo especificar explícitamente una carpeta de fuentes TrueType para la API Aspose.Cells](/cells/es/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Cómo restringir el uso de Aspose.Cells a una sola ubicación de fuentes TrueType](/cells/es/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Trabajar con fuentes**

### **Dónde busca Aspose.Cells las fuentes TrueType en Windows**

Aspose.Cells busca las fuentes en la carpeta **Windows\Fonts**. Esta configuración predeterminada funciona la mayoría de las veces, así que solo especifique sus propias carpetas de fuentes si realmente lo necesita.

### **Dónde busca Aspose.Cells las fuentes TrueType en Linux**

De forma predeterminada, la API Aspose.Cells busca las fuentes en todas las siguientes ubicaciones, aunque las diferentes distribuciones de Linux almacenan fuentes en diferentes carpetas.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Este comportamiento predeterminado funcionará para la mayoría de las distribuciones de Linux, pero no está garantizado que funcione todo el tiempo. Es posible que necesite especificar la ubicación de las fuentes TrueType explícitamente. 

{{% /alert %}}

### **Cómo especificar explícitamente una carpeta de fuentes**

Las API de Aspose.Cells han expuesto muchos métodos de fábrica para la clase FontConfigs para especificar las fuentes o carpetas de fuentes como se describe a continuación.

1. El método setFontFolder acepta un primer parámetro de tipo String con la ubicación del directorio de fuentes, mientras que el segundo parámetro de tipo Boolean sirve para indicar a las APIs de Aspose.Cells que busquen en las carpetas de forma recursiva en busca de archivos de fuentes.
1. El método setFontFolders acepta una matriz de tipo String para que puedas especificar muchas carpetas de fuentes mediante este enfoque. También puedes indicar a las APIs de Aspose.Cells que busquen en las carpetas de forma recursiva especificando true como segundo parámetro.
1. El método setFontSources acepta una matriz de tipo FontSourceBase para que puedas especificar una lista de ubicaciones de fuentes individuales.

{{% alert color="primary" %}}

Al especificar la carpeta de fuentes utilizando cualquiera de los métodos mencionados anteriormente, recomendamos establecer la ubicación de la fuente al inicio de la aplicación, de lo contrario, puedes obtener resultados mal formateados.

{{% /alert %}} {{% alert color="primary" %}}

Establecer la carpeta de fuentes utilizando cualquiera de los métodos anteriores no garantiza que la API Aspose.Cells no busque las fuentes en ubicaciones predeterminadas como la carpeta de fuentes del sistema.

{{% /alert %}}

### **Cómo restringir el uso de Aspose.Cells a solo una carpeta de fuentes**

A partir de la versión Aspose.Cells for Java 8.1.0, configurar los argumentos de la JVM como **-DAspose.Cells.FontDirExc="YourFontDir** asegurará que la API Aspose.Cells solo utilice la ubicación de fuentes especificada.

Establezca los argumentos especificados utilizando el método System.setProperty como se muestra a continuación.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Tenga en cuenta lo siguiente:

- La declaración anterior debe estar al inicio de su aplicación.
- El enfoque anterior no requiere configurar el directorio de fuentes usando ninguno de los métodos de FontConfigs discutidos anteriormente.
- La cadena "FontDirSet" debe ser la ruta completa a la carpeta que contiene las fuentes requeridas.

{{% /alert %}}
