---
title: Omslag Cell Text
type: docs
weight: 130
url: /sv/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

Radbrytning gör det lättare att läsa: en cell med raderad text expanderas för att passa texten så att texten inte visas över andra celler.

Med Aspose.Cells för .NET kan utvecklare utföra de flesta uppgifter i sina applikationer som användare kan utföra med Microsoft Excel, inklusive radbrytning av text i celler. Den här artikeln förklarar hur och jämför uppgiften med VSTO och Aspose.Cells. Aspose.Cells är optimerad för effektiv kodning och fungerar utan Microsoft Automation.

{{% /alert %}}

## **Omslag Cell Text**

Så här skapar du ett kalkylblad med två celler, en med radbruten text och en utan:

1. Konfigurera arbetsbladet:
 1. Skapa en arbetsbok.
 1. Öppna det första arbetsbladet.
1. Lägg till text:
 1. Lägg till text i cell A1.
 1. Lägg till radbruten text i cell A5.
1. Spara kalkylarket.

 Kodexemplen nedan visar hur du utför dessa steg med hjälp av[VSTO](/cells/sv/net/wrapping-cell-text/) med antingen C# eller Visual Basic. Kodexempel som visar hur man gör samma sak med hjälp av[Aspose.Cells för .NET](/cells/sv/net/wrapping-cell-text/), återigen med antingen C# eller Visual Basic följ omedelbart efter.

Att köra koden resulterar i ett kalkylblad med två celler, en som har text som inte har raderats och en som har:

|<p>**Skriv ut radbrytande celltext med VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Skriv ut radbrytande celltext med Aspose.Cells för .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **Radbrytning Cell Text med VSTO**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

    //Access vsto application

    Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

    //Access workbook 

    Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

    //Access worksheet 

    Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

    //Access vsto worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

    //Place some text in cell A1 without wrapping

    Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

    cellA1.Value = "Sample Text Unwrapped";

    //Place some text in cell A5 with wrapping

    Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

    cellA5.Value = "Sample Text Wrapped";

    cellA5.WrapText = true;

    //Save the workbook

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Radbrytning Cell Text med Aspose.Cells för .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

{

    //Create workbook

    Workbook workbook = new Workbook();

    //Access worksheet

    Worksheet worksheet = workbook.Worksheets[0];

    //Place some text in cell A1 without wrapping

    Cell cellA1 = worksheet.Cells["A1"];

    cellA1.PutValue("Some Text Unwrapped");

    //Place some text in cell A5 wrapping

    Cell cellA5 = worksheet.Cells["A5"];

    cellA5.PutValue("Some Text Wrapped");

    Style style = cellA5.GetStyle();

    style.IsTextWrapped = true;

    cellA5.SetStyle(style);

    //Autofit rows

    worksheet.AutoFitRows();

    //Save the workbook

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
