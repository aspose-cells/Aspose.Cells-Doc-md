---
title: Använd formler och funktioner för att bearbeta data
type: docs
weight: 140
url: /sv/net/use-formulas-functions-to-process-data/
---

{{% alert color="primary" %}}

Denna tekniska tips kommer att illustrera hur du kan använda formler/funktioner för att bearbeta data med **VSTO** och **Aspose.Cells for .NET** genom kod. 

{{% /alert %}}




## **1) VSTO**

**C#**

{{< highlight csharp >}}

 //Note: To help you better, the code uses full namespacing

void AddingCellFormula()

{

    //Access vsto application

    Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

    //Access workbook

    Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

    //Access worksheet

    Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

    //Access vsto worksheet

    Microsoft.Office.Tools.Excel.Worksheet worksheet = Globals.Factory.GetVstoObject(m_sheet);

    //Access cells A1, A2, A3 , A4

    Microsoft.Office.Interop.Excel.Range cellA1 = worksheet.Range["A1"];

    Microsoft.Office.Interop.Excel.Range cellA2 = worksheet.Range["A2"];

    Microsoft.Office.Interop.Excel.Range cellA3 = worksheet.Range["A3"];

    Microsoft.Office.Interop.Excel.Range cellA4 = worksheet.Range["A4"];

    //Set integer values in cells A1, A2 and A3

    cellA1.Value = 10;

    cellA2.Value = 20;

    cellA3.Value = 30;

    //Add formula in cell A4

    cellA4.Formula = "=Sum(A1:A3)";

    //Set the font bold in cell A4

    cellA4.Font.Bold = true;

    //Set the background color to Yellow in cell A4

    cellA4.Interior.Color = Excel.XlRgbColor.rgbYellow;

    //Save the workbook

    workbook.SaveAs("D:\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}



{{< /highlight >}}

## **2) Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 void AddingCellFormula()

{

    //Create workbook

    Workbook workbook = new Workbook();

    //Access worksheet

    Worksheet worksheet = workbook.Worksheets[0];

    //Access cells A1, A2, A3 , A4

    Cell cellA1 = worksheet.Cells["A1"];

    Cell cellA2 = worksheet.Cells["A2"];

    Cell cellA3 = worksheet.Cells["A3"];

    Cell cellA4 = worksheet.Cells["A4"];

    //Set integer values in cells A1, A2 and A3

    cellA1.Value = 10;

    cellA2.Value = 20;

    cellA3.Value = 30;

    //Add formula in cell A4

    cellA4.Formula = "=Sum(A1:A3)";

    //Set the font bold in cell A4

    //and set the background color to Yellow in cell A4

    Style style = cellA4.GetStyle();

    style.Font.IsBold = true;

    style.Pattern = BackgroundType.Solid;

    style.ForegroundColor = Color.Yellow;

    cellA4.SetStyle(style);

    //Save the workbook

    workbook.Save("D:\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Output**

### **1) VSTO**

![todo:image_alt_text](use-formulas-functions-to-process-data_1.png)

**Figur 1:** Utdata med formler med VSTO

### **2) Aspose.Cells for .NET**

![todo:image_alt_text](use-formulas-functions-to-process-data_2.png)

**Figur 2:** Utdata med formler med Aspose.Cells for .NET
{{< app/cells/assistant language="csharp" >}}
