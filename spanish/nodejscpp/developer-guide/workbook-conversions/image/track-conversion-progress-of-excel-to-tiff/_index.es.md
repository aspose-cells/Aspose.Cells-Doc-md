---
title: Seguimiento del progreso de conversión de Excel a TIFF con Node.js a través de C++
linktitle: Seguir el progreso de conversión de Excel a TIFF
type: docs
weight: 190
url: /es/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: Aprende cómo realizar el seguimiento del progreso de conversión de archivos de Excel a TIFF usando Aspose.Cells for Node.js via C++. Mejora la experiencia del usuario durante el proceso de conversión.
---

## **Escenarios de uso posibles**

A veces, convertir archivos grandes de Excel puede tomar algo de tiempo. Durante este tiempo, quizás quieras mostrar el progreso de la conversión del documento en lugar de solo una pantalla de carga para mejorar la usabilidad de tu aplicación. Aspose.Cells for Node.js via C++ soporta rastrear el proceso de conversión del documento proporcionando la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). La interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) ofrece [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) y [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) métodos que puedes implementar en tu clase personalizada. También puedes controlar qué páginas se renderizan, como se demuestra en la clase personalizada *TestPageSavingCallback*.

## **Seguir el progreso de conversión de Excel a TIFF**

 El siguiente ejemplo de código carga el [archivo de origen de Excel](95584311.xlsx) y muestra su progreso de conversión en la consola usando la clase personalizada *TestPageSavingCallback* que implementa la interfaz [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback). El archivo de salida generado está adjunto para tu referencia.

[Output File](95584312.tiff)

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

 El siguiente es el código para la clase personalizada *TestTiffPageSavingCallback*.

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **Salida de la consola**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
