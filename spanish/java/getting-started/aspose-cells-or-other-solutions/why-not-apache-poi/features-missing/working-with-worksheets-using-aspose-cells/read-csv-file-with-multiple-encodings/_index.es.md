---
title: Leer archivo CSV con múltiples codificaciones
type: docs
weight: 70
url: /es/java/read-csv-file-with-multiple-encodings/
---

## **Aspose.Cells - Leer archivo CSV con múltiples codificaciones**
A veces, su archivo CSV contiene múltiples codificaciones (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells le permite cargar dichos archivos CSV y convertirlos a otros formatos, por ejemplo, PDF o XLSX.

**Java**

{{< highlight java >}}

 //Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(dataDir + "MultiEncoded.csv", options);

//Save it in XLSX format

workbook.save(dataDir + "EncodedNewFile_Out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/workbook/ReadingCSVFileWithMultipleEncodings.java)

{{% alert color="primary" %}} 

Para más detalles, visita [Lectura de archivos CSV con múltiples codificaciones](/cells/es/java/reading-csv-file-with-multiple-encodings).

{{% /alert %}}
