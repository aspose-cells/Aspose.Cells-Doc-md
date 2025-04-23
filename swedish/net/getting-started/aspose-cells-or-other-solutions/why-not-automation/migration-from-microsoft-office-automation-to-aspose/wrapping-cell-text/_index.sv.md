---
title: Radbrytning av celltext
type: docs
weight: 130
url: /sv/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

Radbrytning av text gör det lättare att läsa: en cell med radbrytning expanderar för att passa texten så att texten inte visas över andra celler.

Med Aspose.Cells for .NET kan utvecklare utföra de flesta uppgifter i sina applikationer som användare kan utföra med Microsoft Excel, inklusive radbrytning av text i celler. Den här artikeln förklarar hur och jämför uppgiften med VSTO och Aspose.Cells. Aspose.Cells är optimerat för effektiv kodning och fungerar utan Microsoft Automation.

{{% /alert %}}

## **Radbrytning av celltext**

För att skapa ett kalkylblad med två celler, en med omvikt text och en utan:

1. Ställ in kalkylbladet:
   1. Skapa en arbetsbok.
   1. Kom åt det första kalkylbladet.
1. Lägg till text:
   1. Lägg till text i cell A1.
   1. Lägg till omvikit text i cell A5.
1. Spara kalkylarket.

Kodexemplen nedan visar hur du utför dessa steg med [VSTO](/cells/sv/net/wrapping-cell-text/) med antingen C# eller Visual Basic. Kodexemplen som visar hur man gör samma sak med [Aspose.Cells for .NET](/cells/sv/net/wrapping-cell-text/) följer omedelbart efter.

Körningen av koden resulterar i ett kalkylblad med två celler, en som har text som inte har varit omviktad, och en som har:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **Inlindning av celltext med VSTO**

**C#**

{{< highlight csharp >}}

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

### **Inlindning av celltext med Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
