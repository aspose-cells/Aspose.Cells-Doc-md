---
title: 公共 API Aspose.Cells 8.8.3 的变化
type: docs
weight: 300
url: /zh/java/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.8.2 到 8.8.3 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 ActiveX 控件**
Aspose.Cells for Java 8.8.3 公开了允许将 ActiveX 控件添加到 ShapeCollection 的 addActiveXControl 方法。上述方法需要7个参数来指定控件的类型、放置控件的位置和控件的大小。可以使用具有以下可能值的 ControlType 枚举来指定类型。

1. 控件类型.CHECK_BOX
1. 控件类型.COMBO_BOX
1. 控制类型.COMMAND_BUTTON
1. 控件类型.IMAGE
1. 控件类型.LABEL
1. 控件类型.LIST_BOX
1. 控制类型.RADIO_BUTTON
1. 控件类型.SCROLL_BAR
1. 控件类型.SPIN_BUTTON
1. 控件类型.TEXT_BOX
1. 控件类型.TOGGLE_BUTTON
1. 控件类型.UNKNOWN

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[将 ActiveX 控件添加到工作表](/cells/zh/java/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

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
### **添加了 LoadOptions.setPaperSize 方法**
Aspose.Cells for Java 8.8.3 允许在使用新公开的 LoadOptions.setPaperSize 方法时从默认打印机设置设置默认打印纸张尺寸，如下所示。请注意，上述方法的输入参数是来自包含预定义纸张尺寸的 PaperSizeType 枚举的值。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[加载具有指定纸张尺寸的电子表格](/cells/zh/java/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set the PaperSize property to appropriate value

loadOptions.setPaperSize(PaperSizeType.PAPER_A_4);

//Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}
### **添加了 Cell.getCharacters(flag) 方法**
Aspose.Cells API 允许使用 Cell.getCharacters 方法获取 FontSetting 数组形式的字符对象。在此版本中，Aspose.Cells for Java API 公开了 Cell.getCharacters 的重载版本，它可以接受布尔值作为参数，指示如果单元格是 ListObject 的一部分，是否必须在单元格上应用表格样式。

**Java**

{{< highlight "csharp" >}}

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

FontSetting[]characters = cell.getCharacters(true);

{{< /highlight >}}
### **添加了 OleObject.AutoLoad 属性**
Aspose.Cells for Java 8.8.3 公开了 OleObject.AutoLoad 属性，如果基础对象的内容/数据已更改，该属性允许刷新 OleObject 的图像。上述属性设置为 true 时，会强制 Excel 应用程序在加载生成的电子表格时刷新 OleObject 的图像。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[自动刷新 OleObjects](/cells/zh/java/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

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
### **添加了 HTMLLoadOptions.SupportDivTag 属性**
Aspose.Cells for Java 8.8.3 公开了 HTMLLoadOptions.SupportDivTag 属性，允许在 Aspose.Cells 对象模型中加载 HTML 文件/片段时解析嵌入在 TD 标签中的 DIV 标签。布尔类型属性的默认值为 false。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[加载时支持内部 DIV 标签 HTML](/cells/zh/java/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

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
### **添加了 HtmlSaveOptions.ExportGridLines 属性**
Aspose.Cells for Java 8.8.3 公开了 HtmlSaveOptions.ExportGridLines 属性，该属性允许在将电子表格导出为 HTML 格式时呈现网格线。布尔类型属性的默认值为 false，但是，当设置为 true 时，API 将以 HTML 格式呈现可用数据范围的网格线。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[将网格线渲染到 HTML](/cells/zh/java/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load existing spreadsheet

Workbook book = new Workbook(dir + "input.xlsx");

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set ExportGridLines to true

options.setExportGridLines(true);

//Save the result in HTML format

book.save(dir + "output.html", options);

{{< /highlight >}}
### **添加了 ListObject.Comment 属性**
Aspose.Cells API 现在允许获取和设置 ListObject 实例的注释。为了提供上述功能，Aspose.Cells API 公开了 ListObject.Comment 属性。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[为 ListObjects 添加注释](/cells/zh/java/set-the-comment-of-table-or-list-object/).

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

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
## **删除的 API**
### **删除了 Workbook.decrypt 方法**
上述财产在一段时间前被标记为过时。此版本已将其从公共 API 中完全删除。建议将 WorkbookSettings.Password 属性设置为 null 以实现相同的目标。
