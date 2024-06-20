---
title: Apertura de archivos en Ruby
type: docs
weight: 10
url: /es/java/opening-files-in-ruby/
---

## **Aspose.Cells - Formas sencillas de abrir archivos de Excel**
### **Apertura a través de la Ruta**
Simplemente abre un archivo de Microsoft Excel haciendo referencia a la ruta del archivo

**Código Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Apertura a través de un flujo**
A veces, el archivo de Excel que desea abrir se almacena como un flujo. En ese caso, use una versión sobrecargada del método Abrir que tome el objeto Flujo que contiene el archivo de Excel para abrir el archivo.

**Código Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
