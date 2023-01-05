---
title: Открыть и сохранить электронную таблицу в xlsx4j
type: docs
weight: 40
url: /ru/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - Открыть и сохранить электронную таблицу**
Разработчики используют Aspose.Cells для открытия файлов для различных целей. Например, откройте файл, чтобы получить из него данные, или используйте предопределенный файл электронной таблицы дизайнера, чтобы ускорить процесс разработки. Aspose.Cells позволяет разработчикам открывать различные типы исходных файлов. Этими исходными файлами могут быть отчеты Excel Microsoft, SpreadsheetML, CSV или файлы с разделителями табуляции.

**Aspose.Cells**позволяет разработчикам создавать файлы Excel с нуля, используя свой гибкий API. После создания файлов Excel вам также потребуется сохранить книгу (файл). Aspose.Cells предоставляет различные способы сохранения этих файлов.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j — открыть и сохранить электронную таблицу**
В приведенном ниже примере показано, как открывать и сохранять электронные таблицы при использовании xlsx4j.

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
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
