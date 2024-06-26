---
title: Agregar Comentarios en la Hoja de Cálculo en xlsx4j
type: docs
weight: 10
url: /es/java/add-comments-in-spreadsheet-in-xlsx4j/
---

## **Aspose.Cells - Agregar Comentarios en la Hoja de Cálculo**
Añade un comentario a una celda llamando al método addComments de la colección Shapes (encapsulada en el objeto Worksheet). El nuevo objeto Comment puede ser accedido desde la colección Comments pasando el índice del comentario. Después de acceder al objeto Comment, personaliza la nota del comentario usando el método setNote del objeto Comment.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a comment to cell

int commentIndex = worksheet.getComments().add("A1");

Comment comment = worksheet.getComments().get(commentIndex);

//Setting the comment note

comment.setNote("Hello Aspose!");

{{< /highlight >}}
## **xlsx4j - Agregar Comentarios en la Hoja de Cálculo**
La clase CommentsPart está disponible para agregar comentarios en la hoja de cálculo usando xlsx4j.

**Java**

{{< highlight java >}}

 public static void main(String[] args) {

    try {

        String outputfilepath = dataDir + "AddComments-Xlsx4j.xlsx";

        SpreadsheetMLPackage pkg = SpreadsheetMLPackage.createPackage();

        WorksheetPart sheet = pkg.createWorksheetPart(new PartName("/xl/worksheets/sheet1.xml"), "Sheet1", 1);

        addContent(sheet);

        pkg.save(new File(outputfilepath));

        System.out.println("\n\n done .. " + outputfilepath);

    }

    catch (Exception e)

    {

        e.printStackTrace();

    }

}

private static void addContent(WorksheetPart sheet) throws JAXBException, Docx4JException {

    // Minimal content already present

    SheetData sheetData = sheet.getContents().getSheetData();

    // Now add

    Row row = Context.getsmlObjectFactory().createRow();

    Cell cell = Context.getsmlObjectFactory().createCell();

    cell.setV("1234");

    row.getC().add(cell);

    row.getC().add(createCell("hello world!"));

    sheetData.getRow().add(row);

    // ADD A COMMENT TO CELL A1

    CommentsPart cp = new CommentsPart();

    cp.setContents(createComment("A1"));

    sheet.addTargetPart(cp);

    // Add <legacyDrawing r:id="rId1"/>

    VMLPart vmlPart = new VMLPart();

    vmlPart.setContents(getVml(0,0));  // corresponds to A1

      // you'll need extra VML for each comment

    Relationship rel = sheet.addTargetPart(vmlPart);

    CTLegacyDrawing legacyDrawing = Context.getsmlObjectFactory().createCTLegacyDrawing();

    legacyDrawing.setId(rel.getId());

    sheet.getContents().setLegacyDrawing(legacyDrawing);

}

private static Cell createCell(String content) {

    Cell cell = Context.getsmlObjectFactory().createCell();

    CTXstringWhitespace ctx = Context.getsmlObjectFactory().createCTXstringWhitespace();

    ctx.setValue(content);

    CTRst ctrst = new CTRst();

    ctrst.setT(ctx);

    cell.setT(STCellType.INLINE_STR);

    cell.setIs(ctrst); // add ctrst as inline string

    return cell;

}

public static CTComments createComment(String cell) throws JAXBException {

    String openXML = "<comments xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">"

            + "<authors>"

                + "<author>Author</author>"

            +"</authors>"

            + "<commentList>"

                + "<comment authorId=\"0\" ref=\"" + cell + "\">"

                    + "<text>"

                        + "<r>"

                            + "<rPr>"

                                + "<b/>"

                                + "<sz val=\"9\"/>"

                                + "<color indexed=\"81\"/>"

                                + "<rFont val=\"Tahoma\"/>"

                                + "<charset val=\"1\"/>"

                            +"</rPr>"

                            + "<t>Thomas: hello world!</t>"

                        +"</r>"

                    +"</text>"

                +"</comment>"

            +"</commentList>"

        +"</comments>";

    CTComments comments = (CTComments)XmlUtils.unwrap(

        XmlUtils.unmarshalString(openXML, Context.jcSML));

    return comments;

}

public static org.docx4j.vml.root.Xml getVml(int row, int col) throws JAXBException {

    String openXML = "<xml xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:x=\"urn:schemas-microsoft-com:office:excel\">"

        + "<o:shapelayout v:ext=\"edit\" >"

        + "<o:idmap data=\"1\" v:ext=\"edit\"/>"

        + "</o:shapelayout>"

        + "<v:shapetype coordsize=\"21600,21600\" id=\"_x0000_t202\" o:spt=\"202\" path=\"m,l,21600r21600,l21600,xe\" >"

        + "<v:stroke joinstyle=\"miter\"/>"

        + "<v:path gradientshapeok=\"t\" o:connecttype=\"rect\"/>"

        + "</v:shapetype>"

        // The VML part must have a <v:shape> element for each comment

        + "<v:shape fillcolor=\"#ffffe1\" id=\"_x0000_s1025\" o:insetmode=\"auto\" style=\"position:absolute;   margin-left:107.25pt;margin-top:7.5pt;width:108pt;height:59.25pt;z-index:1;   visibility:visible\" type=\"#_x0000_t202\" >"

        + "<v:fill color2=\"#ffffe1\"/>"

        + "<v:shadow color=\"black\" obscured=\"t\" on=\"t\"/>"

        + "<v:path o:connecttype=\"none\"/>"

        + "<v:textbox style=\"mso-direction-alt:auto\">"

        + "<div style=\"text-align:left\"/>"

        + "</v:textbox>"

        + "<x:ClientData ObjectType=\"Note\">" + "<x:MoveWithCells/>"

        + "<x:SizeWithCells/>"

        + "<x:Anchor>2, 15, 0, 10, 4, 31, 4, 9</x:Anchor>"

        + "<x:AutoFill>False</x:AutoFill>"

        + "<x:Row>" + row + "</x:Row>"

        + "<x:Column>" + col + "</x:Column>"

        + "</x:ClientData>"

        + "</v:shape></xml>";

        return (org.docx4j.vml.root.Xml) XmlUtils.unmarshalString(openXML, org.docx4j.jaxb.Context.jc);

}

{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/addcomments)

{{% alert color="primary" %}} 

Para más detalles, visita [Agregar Comentarios](/java/adding-comments).

{{% /alert %}}
