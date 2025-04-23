---
title: Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo
type: docs
weight: 20
url: /es/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Escenarios de uso posibles**

A menudo es necesario saber las fuentes que se están utilizando en su libro de trabajo con fines de renderización. Cuando convierte su libro de trabajo en PDF o imagen, Aspose.Cells requiere que todas las fuentes necesarias estén instaladas en su sistema o presentes en su **directorio de fuentes**. Si Aspose.Cells no puede encontrar la fuente necesaria, intenta reemplazarla con alguna otra fuente adecuada que esté presente en su sistema o en su directorio de fuentes y pueda sustituir su fuente real. Esto no solo resulta en la renderización no deseada de PDF o imágenes, sino que también tarda tiempo de procesamiento en encontrar fuentes adecuadas.

Para hacer frente a tales casos, debe saber qué fuentes se están utilizando en su libro de trabajo, luego instalar esas fuentes en su sistema en caso de entorno Windows o colocarlas en su directorio de fuentes en caso de entorno Windows o Linux.

Aspose.Cells proporciona el método [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) que devuelve la lista de todas las fuentes utilizadas en su libro de trabajo o hoja de cálculo.

## **Obtener una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo**

El siguiente código de muestra carga el archivo de Excel de origen y recupera la lista de fuentes utilizadas en él. Tiene una hoja de cálculo ficticia que tiene algunas fuentes ficticias agregadas con fines ilustrativos. Cuando el código imprime todas las fuentes dentro del libro de trabajo, también imprime esas fuentes ficticias. La siguiente captura de pantalla muestra el [archivo de Excel de muestra](sampleGetFonts.xlsx) y cómo se enumeran las fuentes ficticias.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](sampleGetFonts.xlsx) dado.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
