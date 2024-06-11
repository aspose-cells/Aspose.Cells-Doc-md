---
title: Aspose.Cells 8.8.3 中的公共 API 更改
type: docs
weight: 300
url: /zh/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.8.2 到 8.8.3 的 Aspose.Cells API 更改，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、新增和删除的类等，还包括 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 ActiveX 控件**
Aspose.Cells for Java 8.8.3版本已暴露了addActiveXControl方法，允许向ShapeCollection添加ActiveX控件。上述方法需要7个参数来指定控件类型、放置控件的位置和控件的大小。类型可以使用ControlType枚举来指定，可能的值如下。

1. ControlType.CHECK_BOX
1. ControlType.COMBO_BOX
1. ControlType.COMMAND_BUTTON
1. ControlType.IMAGE
1. ControlType.LABEL
1. ControlType.LIST_BOX
1. ControlType.RADIO_BUTTON
1. ControlType.SCROLL_BAR
1. ControlType.SPIN_BUTTON
1. ControlType.TEXT_BOX
1. ControlType.TOGGLE_BUTTON
1. ControlType.UNKNOWN

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [向工作表添加 ActiveX 控件](/cells/zh/java/add-activex-controls-using-aspose-cells/) 上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Add Toggle Button ActiveX Control to the ShapeCollection at specified location

Shape shape = sheet.getShapes().addActiveXControl(ControlType.TOGGLE_BUTTON, 4, 0, 4, 0, 100, 30);

//Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.getActiveXControl();

control.setLinkedCell("A1");

//Save the result on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **添加 LoadOptions.setPaperSize 方法**
Aspose.Cells for Java 8.8.3版本允许使用新暴露的LoadOptions.setPaperSize方法来设置默认打印纸张大小为默认打印机设置。请注意，上述方法的输入参数是PaperSizeType枚举中包含的预定义纸张大小的值。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [加载指定纸张大小的电子表格](/cells/zh/java/load-workbook-with-specified-printer-paper-size/) 上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **添加 Cell.getCharacters(flag) 方法**
Aspose.Cells API允许通过使用Cell.getCharacters方法以FontSetting数组的形式获取字符对象。通过此版本，Aspose.Cells for Java API已暴露了Cell.getCharacters的重载版本，可接受布尔值作为参数，指示是否应在单元格是列表对象的一部分时应用表格样式。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access cells collection of the first worksheet

Cells cells = sheet.getCells();

//Access particular cell from a ListObject

//Assuming A1 resides in a ListObject

Cell cell = cells.get("A1");

//Get all Characters objects from the cell

FontSetting[] characters = cell.getCharacters(true);

{{< /highlight >}}
### **添加 OleObject.AutoLoad 属性**
Aspose.Cells for Java 8.8.3版本已暴露了OleObject.AutoLoad属性，允许刷新OleObject的图像，如果底层对象的内容/数据已更改。当该属性设置为true时，强制Excel应用程序在加载结果电子表格时刷新OleObject的图像。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [通过 Aspose.Cells 自动刷新 Ole 对象的详细文章](/cells/zh/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access OleObjectCollection from first worksheet

OleObjectCollection oleObjects = sheet.getOleObjects();

//Access a OleObject from the collection

OleObject oleObject = oleObjects.get(0);

//Set AutoLoad to true

oleObject.setAutoLoad(true);

{{< /highlight >}}
### **添加 HTMLLoadOptions.SupportDivTag 属性**
Aspose.Cells for Java 8.8.3版本已暴露了HTMLLoadOptions.SupportDivTag属性，允许在加载HTML文件/片段到Aspose.Cells对象模型时解析嵌入在TD标记中的DIV标记。布尔类型属性的默认值为false。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看 [在加载 HTML 时支持内部 DIV 标签的详细文章](/cells/zh/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Store the HTML snippet in a variable

String export_html = "<html>"

\+ "<body>"

\+ " <table>"

\+ "     <tr>"

\+ "         <td>"

\+ "             <div>This is some Text.</div>"

\+ "             <div>"

\+ "                 <div>"

\+ "                     <span>This is some more Text</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>abc@abc.com</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>1234567890</span>"

\+ "                 </div>"

\+ "                 <div>"

\+ "                     <span>ABC DEF</span>"

\+ "                 </div>"

\+ "             </div>"

\+ "             <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>"

\+ "         </td>"

\+ "         <td>"

\+ "             <img src='ASpose_logo_100x100.png' />"

\+ "         </td>"

\+ "     </tr>"

\+ " </table>"

\+ "</body>"

\+ "</html>";

//Convert HTML string to InputStream

InputStream stream = new ByteArrayInputStream(export_html.getBytes(StandardCharsets.UTF_8));

//Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

// Set SupportDivTag property to true

loadOptions.setSupportDivTag(true);

//Create workbook object from the HTML using load options

Workbook book = new Workbook(stream, loadOptions);

//Save the spreadsheet on disc

book.save(dir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **添加了HtmlSaveOptions.ExportGridLines属性**
Aspose.Cells for Java 8.8.3版本已暴露了HtmlSaveOptions.ExportGridLines属性，允许在将电子表格导出为HTML格式时渲染网格线。布尔类型属性的默认值为false，但当设置为true时，API会在HTML格式中为可用数据范围渲染网格线。

{{% alert color="primary" %}} 

有关此功能的更多详情，请参阅[将网格线呈现到HTML](/cells/zh/java/export-excel-to-html-with-gridlines/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **添加了ListObject.Comment属性**
Aspose.Cells API现在允许为ListObject实例获取和设置评论。为了提供上述功能，Aspose.Cells API已暴露了ListObject.Comment属性。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查阅[为ListObjects添加注释](/cells/zh/java/set-the-comment-of-table-or-list-object/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

Java

{{< highlight csharp >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Access first worksheet from the collection

Worksheet sheet = book.getWorksheets().get(0);

//Access first ListObject from the collection of ListObjects

ListObject listObject = sheet.getListObjects().get(0);

//Set comments for the ListObject

listObject.setComment("Comments");

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}
## **删除了 API**
### **删除了Workbook.decrypt方法**
该属性已在一段时间前被标记为过时。此版本已完全将其从公共API中移除。建议将WorkbookSettings.Password属性设置为null以实现相同的目标。
