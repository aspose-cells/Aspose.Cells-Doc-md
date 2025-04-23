---
title: Kommentar im Arbeitsblatt hinzufügen
type: docs
weight: 10
url: /de/net/add-comment-in-worksheet/
---

## **Aspose.Cells - Kommentar im Arbeitsblatt hinzufügen**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Setting the name of the newly added worksheet

worksheet.Name = "Adding Comment in Execl Cell";

//Adding a comment to "F5" cell

int commentIndex = worksheet.Comments.Add("F5");

//Adding a string value to the cell

worksheet.Cells["F5"].PutValue("Hello World");

//Accessing the newly added comment

Comment comment = worksheet.Comments[commentIndex];

//Setting the comment note

comment.Note = "Hello Aspose!";

//Saving the Excel file

workbook.Save("Output-AddingComment.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Kommentar im Arbeitsblatt hinzufügen**
**C#**

{{< highlight cs >}}

 HSSFWorkbook hssfworkbook = new HSSFWorkbook();

ISheet sheet = hssfworkbook.CreateSheet("Cell comments in POI HSSF");

// Create the drawing patriarch. This is the top level container for all shapes including cell comments.

HSSFPatriarch patr = (HSSFPatriarch)sheet.CreateDrawingPatriarch();

//Create a cell in row 3

ICell cell1 = sheet.CreateRow(3).CreateCell(1);

cell1.SetCellValue(new HSSFRichTextString("Hello, World"));

//anchor defines size and position of the comment in worksheet

IComment comment1 = patr.CreateCellComment(new HSSFClientAnchor(0, 0, 0, 0, 4, 2, 6, 5));

// set text in the comment

comment1.String = (new HSSFRichTextString("We can set comments in POI"));

//set comment author.

//you can see it in the status bar when moving mouse over the commented cell

comment1.Author = ("Apache Software Foundation");

// The first way to assign comment to a cell is via HSSFCell.SetCellComment method

cell1.CellComment = (comment1);

//Write the stream data of workbook to the root directory

FileStream file = new FileStream(@"OutputAddedCommentInCell.xls", FileMode.Create);

hssfworkbook.Write(file);

file.Close();


{{< /highlight >}}
## **Laufenden Code herunterladen**
Laden Sie das Formular **Bild im Arbeitsblatt hinzufügen** von einer der unten genannten Social-Coding-Websites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.3/Add.Comment.zip)

{{% alert color="primary" %}} 

Für weitere Details besuchen Sie [Arbeiten mit Tabellenblättern](/cells/de/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
