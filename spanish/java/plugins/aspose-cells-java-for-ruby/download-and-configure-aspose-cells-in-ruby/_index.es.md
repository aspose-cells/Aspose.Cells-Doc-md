---
title: Descargar e Instalar Aspose.Cells en Ruby
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-cells-in-ruby/
---

## **Descargar Bibliotecas Requeridas**
Descargue las bibliotecas necesarias mencionadas a continuación. Estas son necesarias para ejecutar ejemplos de Aspose.Cells Java para Ruby.

- [Componente Aspose.Cell for Java](https://downloads.aspose.com/cells/java/)
## **Descargar Ejemplos de Sitios de Codificación Social**
Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Instalación**
Es muy sencillo y fácil instalar Aspose.Cells Java para Ruby, por favor sigue estos sencillos pasos:

1. Agrega esta línea a tu Gemfile de la aplicación. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Y luego ejecuta 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**O**

1. Ejecuta el siguiente comando. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Usando**
Incluye los archivos necesarios para trabajar con el ejemplo de helloworld.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Entendamos el código anterior.

1. La primera línea asegura que aspose cells esté cargado y disponible.
1. Incluye los archivos necesarios para acceder a aspose cells.
1. Inicializa las bibliotecas. Las clases JAVA de aspose se cargan desde la ruta proporcionada en el archivo aspose.yml/
