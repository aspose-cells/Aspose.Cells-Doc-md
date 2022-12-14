---
title: Ny linje på Cells
type: docs
weight: 30
url: /sv/java/new-line-in-cells/
---
## **Aspose.Cells - Ny linje i Cells**
För att säkerställa att text i en cell kan läsas kan explicita radbrytningar och textbrytning tillämpas. Textbrytning förvandlar en rad till flera i en cell, vilka explicita radbrytningar sätts i brytningar precis där du vill ha dem.

Om du vill radbryta text i en cell använder du metoden Style.setTextWrapped.

**Java**

{{< highlight "java" >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Ny linje i Cells**
CellStyle.setWrapText ska vara sant för radbruten text.

**Java**

{{< highlight "java" >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

 För mer information, besök[Radbrytningar och textbrytning](/java/line-breaks-and-text-wrapping).

{{% /alert %}}
