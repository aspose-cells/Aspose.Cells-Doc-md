---
title: Aspose.Cells 8.8.3中的公共API变更
type: docs
weight: 300
url: /zh/java/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

本文档描述了自8.8.2版本中Aspose.Cells API到8.8.3版本的变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括任何Aspose.Cells内部行为变化的描述。

{{% /alert %}} 
## **已添加API**
### **对ActiveX控件的支持**
Aspose.Cells for Java 8.8.3已公开addActiveXControl方法，允许向ShapeCollection添加ActiveX控件。 该方法需要7个参数以指定控件类型、放置控件的位置和控件的大小。 类型可以使用ControlType枚举来指定，其可能值如下。

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

要了解更多关于此功能的详情，请查看[向工作表添加 ActiveX 控件](/cells/zh/java/add-activex-controls-using-aspose-cells/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

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
### **新增 LoadOptions.setPaperSize 方法**
使用 Aspose.Cells for Java 8.8.3 可以在使用新公开的 LoadOptions.setPaperSize 方法时，设置默认打印纸张大小为默认打印机设置的值。请注意，上述方法的输入参数是 PaperSizeType 枚举中包含的预定义纸张大小的值。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[以指定的纸张大小装载电子表格](/cells/zh/java/load-workbook-with-specified-printer-paper-size/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **新增 Cell.getCharacters(flag) 方法**
Aspose.Cells API 允许通过使用 Cell.getCharacters 方法以 FontSetting 数组的形式获取字符对象。通过此版本, Aspose.Cells for Java API 公开了 Cell.getCharacters 方法的重载版本，该方法可以接受 Boolean 参数，指示是否应在单元格上应用表样式，如果单元格是列表对象的一部分。

**Java**

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
### **添加了OleObject.AutoLoad属性**
Aspose.Cells for Java 8.8.3 已公开了 OleObject.AutoLoad 属性，允许在底层对象的内容/数据已更改时刷新 OleObject 的图像。前述属性设置为 true 时，会强制 Excel 应用程序在加载结果电子表格时刷新 OleObject 的图像。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[通过 Aspose.Cells 自动刷新 OleObjects](/cells/zh/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

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
### **添加了HTMLLoadOptions.SupportDivTag属性**
Aspose.Cells for Java 8.8.3 已公开了 HTMLLoadOptions.SupportDivTag 属性，允许在装载 HTML 文件/片段到 Aspose.Cells 对象模型时解析嵌入在 TD 标签中的 DIV 标签。布尔类型属性具有默认值 false。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[在装载 HTML 时支持内嵌 DIV 标记](/cells/zh/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

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
Aspose.Cells for Java 8.8.3 已公开了 HtmlSaveOptions.ExportGridLines 属性，允许在将电子表格导出到 HTML 格式时呈现网格线。布尔类型属性的默认值为 false，但当设置为 true 时，API 将为 HTML 格式中的可用数据范围呈现网格线。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[将网格线呈现到 HTML 中](/cells/zh/java/export-excel-to-html-with-gridlines/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

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
Aspose.Cells APIs 现在允许获取和设置列表对象实例的注释。为了提供上述功能，Aspose.Cells APIs 已公开了ListObject.Comment属性。

{{% alert color="primary" %}} 

要了解更多关于此功能的详情，请查看[为列表对象添加注释](/cells/zh/java/set-the-comment-of-table-or-list-object/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

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
## **已删除APIs**
### **删除了 Workbook.decrypt 方法**
所述属性已在一段时间前被标记为过时。此版本已彻底从公共 API 中移除该属性。建议将 WorkbookSettings.Password 属性设置为 null 以实现相同的目标。
