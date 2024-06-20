---
title: Descargar y Configurar Aspose.Cells en Jython
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-cells-in-jython/
---

## **Descargando**

**Descargar ejemplos de sitios de programación social**

Las versiones de ejemplos en ejecución están disponibles para descargar en todos los siguientes sitios de programación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Descargar componente Aspose.Cells for Java**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Instalación**

- Coloque el archivo jar descargado Aspose.Cells for Java en el directorio "lib".
- Reemplace "su-lib" con el nombre de archivo jar descargado en el archivo _*init*_.py.

## **Usando**

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
