---
title: Descargar y configurar Aspose.Cells en Ruby
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-cells-in-ruby/
---
## **Descargar bibliotecas requeridas**
Descargue las bibliotecas necesarias que se mencionan a continuación. Estos son los necesarios para ejecutar Aspose.Cells Java para ejemplos de Ruby.

- [Aspose.Cell for Java Componente](https://downloads.aspose.com/cells/java/)
## **Descargar ejemplos de sitios de codificación social**
Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

**GitHub**

- [Aspose.Cells Java para rubí](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Instalando**
Es muy simple y fácil de instalar Aspose.cells Java para Ruby gem, siga estos sencillos pasos:

1.  Agregue esta línea al Gemfile de su aplicación.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1.  luego ejecutar

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**O**

1.  Ejecute el siguiente comando.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Usando**
Incluya los archivos necesarios para trabajar con el ejemplo de helloworld.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Entendamos el código anterior.

1. La primera línea se asegura de que las celdas aspose estén cargadas y disponibles.
1. Incluya los archivos necesarios para acceder a las celdas de Aspose.
1. Inicializar las bibliotecas. Las clases JAVA de aspose se cargan desde la ruta proporcionada en el archivo aspose.yml/
