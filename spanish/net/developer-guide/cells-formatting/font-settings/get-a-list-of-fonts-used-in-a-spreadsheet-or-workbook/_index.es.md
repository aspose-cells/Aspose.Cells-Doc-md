---
title: Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo. Admite la obtención de una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo, lo que permite a los usuarios obtener información sobre las fuentes utilizadas en un documento. Este artículo le mostrará cómo utilizar la biblioteca Aspose.Cells para obtener una lista de fuentes.
keywords: Aspose.Cells, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /es/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
##  **Posibles escenarios de uso**

A menudo es necesario conocer las fuentes que se utilizan en su libro de trabajo para fines de renderizado. Cuando convierte su libro de trabajo en PDF o imagen, Aspose.Cells requiere que todas las fuentes necesarias estén instaladas en su sistema o presentes en su *directorio de fuentes**. Si Aspose.Cells no puede encontrar la fuente necesaria, intenta reemplazarla con alguna otra fuente adecuada que esté presente en su sistema o en su directorio de fuentes y puede sustituir su fuente real. Esto no sólo da como resultado la representación no deseada de PDF o imágenes, sino que también requiere tiempo de procesamiento para encontrar las fuentes adecuadas.

Para hacer frente a estos casos, debe saber qué fuentes utiliza su libro de trabajo y luego instalarlas en su sistema en el caso del entorno Windows o colocarlas en su directorio de fuentes en el caso de un entorno Windows o Linux.

 Aspose.Cells proporciona la**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**método que devuelve la lista de todas las fuentes utilizadas en su libro u hoja de cálculo.

##  **Obtenga una lista de fuentes utilizadas en una hoja de cálculo o libro de trabajo**

 El siguiente código de muestra carga el archivo fuente de Excel y recupera la lista de fuentes utilizadas en su interior. Tiene una hoja de trabajo ficticia a la que se le han agregado algunas fuentes ficticias con fines ilustrativos. Cuando el código imprime todas las fuentes dentro del libro, también imprime esas fuentes ficticias. La siguiente captura de pantalla muestra la[archivo de excel de muestra](25395211.xlsx) y cómo se enumeran las fuentes ficticias.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

##  **Salida de consola**

 Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el dado[archivo de excel de muestra](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
