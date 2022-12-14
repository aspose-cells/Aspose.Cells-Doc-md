---
title: Aspose.Cells Java para Jython
type: docs
weight: 70
url: /es/java/aspose-cells-java-for-jython/
---
## **Introducción**

### **¿Qué es Jython?**

Jython es una implementación Java de Python que combina poder expresivo con claridad. Jython está disponible gratuitamente para uso comercial y no comercial y se distribuye con el código fuente. Jython es complementario a Java y es especialmente adecuado para las siguientes tareas:

- **Secuencias de comandos integradas** Java Los programadores pueden agregar las bibliotecas Jython a su sistema para permitir que los usuarios finales escriban scripts simples o complicados que agreguen funcionalidad a la aplicación.
- **Experimentación interactiva** - Jython proporciona un intérprete interactivo que se puede usar para interactuar con paquetes Java o con aplicaciones Java en ejecución. Esto permite a los programadores experimentar y depurar cualquier sistema Java usando Jython.
- **Desarrollo rápido de aplicaciones** - Los programas Python suelen ser de 2 a 10 veces más cortos que el programa equivalente Java. Esto se traduce directamente en una mayor productividad del programador. La perfecta interacción entre Python y Java permite a los desarrolladores mezclar libremente los dos idiomas durante el desarrollo y el envío de productos.

### **Aspose.Cells for Java**

Aspose.Cells for Java es una biblioteca de clase avanzada for Java que le permite realizar una gran variedad de tareas de procesamiento de documentos directamente dentro de su Java
aplicaciones

Aspose.Cells for Java admite el procesamiento Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF y todos los formatos de imagen. Con el Aspose.Cells puedes
generar, modificar y convertir documentos sin usar Microsoft Cells.

### **Aspose.Cells Java para Jython**

Aspose.Cells Java para Jython es un proyecto que demuestra/proporciona los ejemplos de uso Aspose.Cells for Java API en Jython.

## **Requisitos del sistema y plataformas compatibles**

### **Requisitos del sistema**

**Los siguientes son los requisitos del sistema para usar Aspose.Cells Java para Jython:**

- Java 1.5 o superior instalado
- Componente Aspose.Cells descargado
- Jython 2.7.0

### **Plataformas compatibles**

**Las siguientes son las plataformas compatibles:**

- Aspose.Cells 15.4 y superior.
- Java IDE (Eclipse, NetBeans...)

## **Descargar Instalación y Uso**

### **Descargando**

**Descargar ejemplos de sitios web de codificación social**

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en todos los sitios de codificación social mencionados a continuación:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Descargar Aspose.Cells for Java componente**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Instalando**

- Coloque el archivo jar descargado Aspose.Cells for Java en el directorio "lib".
- Reemplace "your-lib" con el nombre del archivo jar descargado en el archivo _*init*_.py.

### **Usando**

Puede crear un documento HelloWorld usando el siguiente código de ejemplo:

{{< highlight "java" >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Apoyar, Extender y Contribuir**

### **Apoyo**

Desde los primeros días de Aspose, sabíamos que solo dar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software le impiden hacer lo que debe hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté usando una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.Cells Java para Jython utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Extender y contribuir**

Aspose.Cells Java para Jython es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se alienta a los desarrolladores a descargar el código fuente y contribuir sugiriendo o agregando nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de ellas.

### **Código fuente**

Puede obtener el código fuente más reciente de una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
