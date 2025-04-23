---
title: Lectura de archivo CSV con múltiples codificaciones
type: docs
weight: 140
url: /es/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

A veces, su archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells le permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

{{% /alert %}} 

Aspose.Cells proporciona el método TxtLoadOptions.setMultiEncoded(), que debe establecer en **true** para cargar correctamente su archivo CSV con múltiples codificaciones.

La siguiente captura de pantalla muestra un archivo CSV de muestra que contiene dos líneas. La primera línea está en codificación **ANSI** y la segunda línea está en codificación **Unicode**

**Archivo de entrada** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

La siguiente captura de pantalla muestra el archivo XLSX convertido del archivo CSV anterior sin establecer el método TxtLoadOptions.setMultiEncoded() en verdadero. Como puede ver, el texto Unicode no se convirtió correctamente.

**Archivo de salida 1: no se hizo ninguna adaptación para la codificación múltiple** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

La siguiente captura de pantalla muestra el archivo XLSX convertido del archivo CSV anterior después de establecer el método TxtLoadOptions.setMultiEncoded() en verdadero. Como puede ver, el texto Unicode se ha convertido correctamente.

**Archivo de salida 2: se establece IsMultiEncoded en verdadero** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

A continuación se muestra el código de ejemplo que convierte el archivo CSV anterior en formato XLSX adecuadamente.

**Java**

{{< highlight csharp >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
