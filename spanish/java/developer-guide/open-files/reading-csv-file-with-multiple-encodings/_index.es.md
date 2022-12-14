---
title: Lectura de archivos CSV con múltiples codificaciones
type: docs
weight: 140
url: /es/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

En algún momento, su archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc.). Aspose.Cells le permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}} 

 Aspose.Cells proporciona el método TxtLoadOptions.setMultiEncoded(), que debe configurar para**verdadero** para cargar correctamente su archivo CSV con múltiples codificaciones.

 La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en**ANSI** codificación y la segunda línea está en**Unicode** codificación

**Fichero de entrada** 

![todo:imagen_alternativa_texto](reading-csv-file-with-multiple-encodings_1.png)

La siguiente captura de pantalla muestra el archivo XLSX convertido a partir del archivo CSV anterior sin establecer el método TxtLoadOptions.setMultiEncoded() en verdadero. Como puede ver, el texto Unicode no se convirtió correctamente.

**Archivo de salida 1: no se realizaron adaptaciones para la codificación múltiple** 

![todo:imagen_alternativa_texto](reading-csv-file-with-multiple-encodings_2.png)

La siguiente captura de pantalla muestra el archivo XSLX convertido a partir del archivo CSV anterior después de establecer el método TxtLoadOptions.setMultiEncoded() en verdadero. Como puede ver, el texto Unicode ahora se convierte correctamente.

**Archivo de salida 2: IsMultiEncoded se establece en verdadero** 

![todo:imagen_alternativa_texto](reading-csv-file-with-multiple-encodings_3.png)

A continuación se muestra el código de muestra que convierte correctamente el archivo CSV anterior al formato XLSX.

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
