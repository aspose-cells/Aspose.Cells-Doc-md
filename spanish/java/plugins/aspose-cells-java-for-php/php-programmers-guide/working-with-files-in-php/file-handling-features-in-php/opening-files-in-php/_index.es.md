---
title: Abrir archivos en PHP
type: docs
weight: 10
url: /es/java/opening-files-in-php/
---
## **Aspose.Cells - Formas sencillas de abrir archivos de Excel**
### **Apertura a través de Camino**
Simplemente abra un archivo de Excel Microsoft haciendo referencia a la ruta del archivo

**Código PHP**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **Apertura a través de Stream**
A veces, el archivo de Excel que desea abrir se almacena como una secuencia. En ese caso, use una versión sobrecargada del método Open que toma el objeto Stream que contiene el archivo de Excel para abrir el archivo.

**Código PHP**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Abrir archivos (Aspose.Cells)**de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
