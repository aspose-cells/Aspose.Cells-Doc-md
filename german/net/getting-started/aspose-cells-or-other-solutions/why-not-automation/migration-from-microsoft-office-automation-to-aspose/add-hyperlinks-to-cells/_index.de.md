---
title: Fügen Sie Hyperlinks zu Cells hinzu
type: docs
weight: 60
url: /de/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Mit Aspose.Cells for .NET können Sie fast alle Aufgaben über Ihre Anwendung ausführen, die ein Benutzer in Microsoft Excel ausführen kann. In diesem Artikel wird verglichen, wie Sie mit VSTO und Aspose.Cells for .NET einen Hyperlink zu einer Zelle in einem Arbeitsblatt hinzufügen.

{{% /alert %}}

## **Hinzufügen von Hyperlinks zu Cells**

Führen Sie die folgenden Schritte aus, um Hyperlinks zu Zellen in einer Tabelle hinzuzufügen:

1. Erstellen Sie das Arbeitsblatt:
 1. Instanziieren Sie ein Anwendungsobjekt.
 (Nur VSTO.)
 1. Fügen Sie eine Arbeitsmappe hinzu.
 1. Holen Sie sich das erste Blatt.
 1. Fügen Sie Text zu den Zellen hinzu, denen Sie einen Hyperlink hinzufügen möchten.
1. Hyperlinks hinzufügen.
1. Speichern Sie das Dokument.

 Diese Schritte werden in den folgenden Codebeispielen gezeigt. Die ersten Beispiele zeigen die Verwendung[VSTO](/cells/de/net/add-hyperlinks-to-cells/) entweder mit C# oder Visual Basic, um einer Zelle einen Hyperlink hinzuzufügen. Die folgenden Beispiele zeigen, wie Sie dasselbe mit tun können[Aspose.Cells for .NET](/cells/de/net/add-hyperlinks-to-cells/), wieder mit C# oder Visual Basic.

Die Codebeispiele generieren eine Excel-Datei mit einem Hyperlink in Zelle A1 auf dem ersten Arbeitsblatt.

![todo: Bild_alt_Text](add-hyperlinks-to-cells_1.png)

**Zelle A1 wird ein Hyperlink hinzugefügt.**

### **Hinzufügen von Hyperlinks zu Cells mit VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Hinzufügen von Hyperlinks zu Cells mit Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
