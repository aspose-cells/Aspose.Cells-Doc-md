---
title: Abrir archivos en Ruby
type: docs
weight: 10
url: /es/java/opening-files-in-ruby/
---
## **Aspose.Cells - Formas sencillas de abrir archivos de Excel**
### **Apertura a través de Camino**
Simplemente abra un archivo de Excel Microsoft haciendo referencia a la ruta del archivo

**código rubí**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

{{< /highlight >}}
### **Apertura a través de Stream**
A veces, el archivo de Excel que desea abrir se almacena como una secuencia. En ese caso, use una versión sobrecargada del método Open que toma el objeto Stream que contiene el archivo de Excel para abrir el archivo.

**código rubí**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

fstream = IO.sysopen(@data_dir + 'Book1.xls')

workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

{{< /highlight >}}
