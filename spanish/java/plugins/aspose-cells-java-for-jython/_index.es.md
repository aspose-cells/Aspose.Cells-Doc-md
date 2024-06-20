---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /es/java/aspose-cells-java-for-jython/
---

## **Introducción**

### **¿Qué es Jython?**

Jython es una implementación de Java de Python que combina poder expresivo con claridad. Jython está disponible de forma gratuita tanto para uso comercial como no comercial y se distribuye con el código fuente. Jython es complementario con Java y es especialmente adecuado para las siguientes tareas:

- **Scripting incorporado** - Los programadores de Java pueden agregar las bibliotecas de Jython a su sistema para permitir a los usuarios finales escribir scripts simples o complicados que añaden funcionalidad a la aplicación.
- **Experimentación interactiva** - Jython proporciona un intérprete interactivo que puede ser utilizado para interactuar con paquetes de Java o con aplicaciones Java en ejecución. Esto permite a los programadores experimentar y depurar cualquier sistema Java usando Jython.
- **Desarrollo rápido de aplicaciones** - Los programas de Python suelen ser de 2 a 10 veces más cortos que los programas equivalentes en Java. Esto se traduce directamente en una mayor productividad de los programadores. La interacción fluida entre Python y Java permite a los desarrolladores mezclar libremente los dos lenguajes tanto durante el desarrollo como en la distribución de productos.

### **Aspose.Cells for Java**

Aspose.Cells for Java es una biblioteca de clases avanzada para Java que le permite realizar una amplia gama de tareas de procesamiento de documentos directamente dentro de su aplicación Java
aplicaciones.

Aspose.Cells for Java admite el procesamiento de Celdas (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF y todos los formatos de imagen. Con Aspose.Cells puedes
generar, modificar y convertir documentos sin usar Microsoft Cells.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java para Jython es un proyecto que demuestra / proporciona ejemplos de uso de la API Aspose.Cells for Java en Jython.

## **Requisitos del sistema y plataformas compatibles**

### **Requisitos del sistema**

**A continuación se presentan los requisitos del sistema para usar Aspose.Cells Java para Jython:**

- Java 1.5 o superior instalado
- Se ha descargado el componente Aspose.Cells
- Jython 2.7.0

### **Plataformas compatibles**

**A continuación se presentan las plataformas compatibles:**

- Aspose.Cells 15.4 y superior.
- IDE de Java (Eclipse, NetBeans ...)

## **Descargar Instalación y Uso**

### **Descargando**

**Descargar ejemplos de sitios de programación social**

Las versiones de ejemplos en ejecución están disponibles para descargar en todos los siguientes sitios de programación social mencionados a continuación:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Descargar componente Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Instalación**

- Coloque el archivo jar descargado Aspose.Cells for Java en el directorio "lib".
- Reemplace "su-lib" con el nombre de archivo jar descargado en el archivo _*init*_.py.

### **Usando**

Puede crear un documento HelloWorld utilizando el siguiente código de ejemplo:

{{< highlight java >}}

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

## **Soporte, Ampliación y Contribución**

### **Soporte**

Desde los primeros días de Aspose, supimos que simplemente proporcionar buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que resulta cuando un problema técnico o una peculiaridad en el software le impide hacer lo que necesita. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquier persona que use nuestro producto, ya sea que los haya comprado o esté usando una evaluación, merece nuestra completa atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.Cells Java for Jython utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Ampliar y Contribuir**

Aspose.Cells Java for Jython es de código abierto y su código fuente está disponible en los principales sitios web de codificación social enumerados a continuación. Se alienta a los desarrolladores a descargar el código fuente y contribuir sugiriendo o agregando nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de ello.

### **Código Fuente**

Puede obtener el último código fuente en una de las siguientes ubicaciones

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
