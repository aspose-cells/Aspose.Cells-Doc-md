---
title: Abrir y guardar hoja de cálculo en xlsx4j
type: docs
weight: 40
url: /es/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - Abrir y guardar hoja de cálculo**
Los desarrolladores usan Aspose.Cells para abrir archivos para diferentes propósitos. Por ejemplo, abra un archivo para recuperar datos o use un archivo de hoja de cálculo de diseñador predefinido para acelerar su proceso de desarrollo. Aspose.Cells permite a los desarrolladores abrir diferentes tipos de archivos fuente. Estos archivos de origen pueden ser Microsoft informes de Excel, SpreadsheetML, CSV o archivos delimitados por tabuladores.

**Aspose.Cells**permite a los desarrolladores crear archivos de Excel desde cero utilizando su flexible API. Una vez que cree archivos de Excel, también necesitará guardar su libro de trabajo (archivo). Aspose.Cells proporciona una variedad de formas de guardar estos archivos.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Abrir y guardar hoja de cálculo**
El siguiente ejemplo muestra cómo abrir y guardar hojas de cálculo mientras usa xlsx4j.

**Java**

{{< highlight "java" >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
