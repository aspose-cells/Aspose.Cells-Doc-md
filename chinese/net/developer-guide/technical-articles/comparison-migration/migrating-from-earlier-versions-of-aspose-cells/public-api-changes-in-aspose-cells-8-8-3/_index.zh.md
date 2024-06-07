---
title: Aspose.Cells 8.8.3中的公共API变更
type: docs
weight: 290
url: /zh/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

本文档描述了自8.8.2版本中Aspose.Cells API到8.8.3版本的变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括任何Aspose.Cells内部行为变化的描述。

{{% /alert %}} 
## **已添加API**
### **对ActiveX控件的支持**
Aspose.Cells for .NET 8.8.3现在暴露了AddActiveXControl方法，允许向ShapeCollection添加ActiveX控件。前述方法需要7个参数来指定控件类型、放置控件的位置和控件的大小。类型可以使用ControlType枚举来指定，以下是可能的值。

1. ControlType.CheckBox
1. ControlType.ComboBox
1. ControlType.CommandButton
1. ControlType.Image
1. ControlType.Label
1. ControlType.ListBox
1. ControlType.RadioButton
1. ControlType.ScrollBar
1. ControlType.SpinButton
1. ControlType.TextBox
1. ControlType.ToggleButton
1. ControlType.Unknown

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看有关将ActiveX控件添加到工作表的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Workbook();

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Add Toggle Button ActiveX Control to the ShapeCollection at specified location

var shape = sheet.Shapes.AddActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

// Access the ActiveX Control object and set its linked cell property

ActiveXControl control = shape.ActiveXControl;

control.LinkedCell = "A1";

// Save the result on disc

book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **添加了LoadOptions.SetPaperSize方法**
Aspose.Cells for .NET 8.8.3 允许在使用新公开的LoadOptions.SetPaperSize方法时，从默认打印机设置中设置默认打印纸张大小。请注意，前述方法的输入参数是PaperSizeType枚举中包含的预定义纸张大小的值。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[使用指定纸张大小加载电子表格](/cells/zh/net/load-workbook-with-specified-printer-paper-size/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **添加了Cell.GetCharacters(flag)方法**
Aspose.Cells APIs 允许使用Cell.GetCharacters方法以FontSetting数组的形式获取字符对象。通过此版本，Aspose.Cells for .NET API已公开了一个重载版本的Cell.GetCharacters，该版本可接受布尔值作为参数，指示是否应在单元格上应用表样式，如果单元格是列表对象的一部分。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access cells collection of the first worksheet

var cells = sheet.Cells;

// Access particular cell from a ListObject

// Assuming A1 resides in a ListObject

var cell = cells["A1"];

// Get all Characters objects from the cell

var characters = cell.GetCharacters(true);

{{< /highlight >}}


### **添加了OleObject.AutoLoad属性**
Aspose.Cells for .NET 8.8.3 已公开了OleObject.AutoLoad属性，允许在底层对象的内容/数据已更改时刷新OleObject的图像。当该属性设置为true时，会强制Excel应用程序在加载结果电子表格时刷新OleObject的图像。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[自动刷新OleObjects](/cells/zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access OleObjectCollection from first worksheet

var oleObjects = sheet.OleObjects;

// Access a OleObject from the collection

var oleObject = oleObjects[0];

// Set AutoLoad to true

oleObject.AutoLoad = true;

{{< /highlight >}}


### **添加了HTMLLoadOptions.SupportDivTag属性**
Aspose.Cells for .NET 8.8.3 已公开了HTMLLoadOptions.SupportDivTag属性，允许在加载HTML文件/片段到Aspose.Cells对象模型时解析嵌入在TD标记中的DIV标记。布尔类型属性的默认值为false。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[在加载HTML时支持内部DIV标记](/cells/zh/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Store the HTML snippet in a variable

var export_html = @"

<html>

<body>

    <table>

        <tr>

            <td>

                <div>This is some Text.</div>

                <div>

                    <div>

                        <span>This is some more Text</span>

                    </div>

                    <div>

                        <span>abc@abc.com</span>

                    </div>

                    <div>

                        <span>1234567890</span>

                    </div>

                    <div>

                        <span>ABC DEF</span>

                    </div>

                </div>

                <div>Generated On May 30, 2016 02:33 PM <br />Time Call Received from Jan 01, 2016 to May 30, 2016</div>

            </td>

            <td>

                <img src='ASpose_logo_100x100.png' />

            </td>

        </tr>

    </table>

</body>

</html>";

// Create an instance of MemoryStream and load the contents of the HTML

using (var stream = new MemoryStream(System.Text.Encoding.UTF8.GetBytes(export_html)))

{

    // Create an instance of HTMLLoadOptions

    var loadOptions = new HTMLLoadOptions(LoadFormat.Html);

    // Set SupportDivTag property to true

    loadOptions.SupportDivTag = true;

    // Create workbook object from the HTML using load options

    var book = new Workbook(stream, loadOptions);

    // Auto fit rows and columns of first worksheet

    var sheet = book.Worksheets[0];

    sheet.AutoFitRows();

    sheet.AutoFitColumns();

    // Save the spreadsheet on disc

    book.Save(dir + "output.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}


### **添加了HtmlSaveOptions.ExportGridLines属性**
Aspose.Cells for .NET 8.8.3 已公开了HtmlSaveOptions.ExportGridLines属性，允许在将电子表格导出为HTML格式时呈现网格线。布尔类型属性的默认值为false，但当设置为true时，API会为HTML格式中的可用数据范围呈现网格线。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[将网格线渲染到HTML](/cells/zh/net/export-excel-to-html-with-gridlines/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **添加了ListObject.Comment属性**
Aspose.Cells APIs 现在允许获取和设置列表对象实例的注释。为了提供上述功能，Aspose.Cells APIs 已公开了ListObject.Comment属性。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[为ListObjects添加评论](/cells/zh/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Access first worksheet from the collection

var sheet = book.Worksheets[0];

// Access first ListObject from the collection of ListObjects

var listObject = sheet.ListObjects[0];

// Set comments for the ListObject

listObject.Comment = "Comments";

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}


### **添加了GridWeb.SessionStorePath属性**
Aspose.Cells.GridWeb for .NET 8.8.3 已公开了SessionStorePath属性，允许在Session模式为ViewState时获取或设置会话存储路径。前述属性获取或设置相对于当前Web应用程序基础目录的路径。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[为临时会话文件指定路径](/cells/zh/net/specify-the-path-where-gridweb-stores-temporary-session-files/)上的详细文章。

{{% /alert %}} 

以下是简单的使用场景。
## **已删除APIs**
### **已删除 Workbook.Decrypt 方法**
所述属性已在一段时间前被标记为过时。此版本已彻底从公共 API 中移除该属性。建议将 WorkbookSettings.Password 属性设置为 null 以实现相同的目标。
