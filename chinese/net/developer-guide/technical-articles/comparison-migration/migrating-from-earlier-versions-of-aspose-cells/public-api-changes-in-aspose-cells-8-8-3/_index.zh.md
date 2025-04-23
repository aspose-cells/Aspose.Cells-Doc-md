---
title: Aspose.Cells 8.8.3 中的公共 API 更改
type: docs
weight: 290
url: /zh/net/public-api-changes-in-aspose-cells-8-8-3/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.8.2 到 8.8.3 的 Aspose.Cells API 更改，可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法、新增和删除的类等，还包括 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 ActiveX 控件**
Aspose.Cells for .NET 8.8.3已经公开了AddActiveXControl方法，允许将一个ActiveX控件添加到ShapeCollection中。所述方法需要7个参数来指定控件类型、放置控件的位置和控件的大小。类型可以使用ControlType枚举来指定，可能的值有以下。

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

有关此功能的更多详细信息，请查看[向工作表添加ActiveX控件](/cells/zh/net/add-activex-controls-using-aspose-cells/)上的详细文章。

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


### **添加LoadOptions.SetPaperSize方法**
Aspose.Cells for .NET 8.8.3允许在使用新公开的LoadOptions.SetPaperSize方法时从默认打印机设置设置默认打印纸张大小，如下所示。请注意，上述方法的输入参数是来自PaperSizeType枚举的值，其中包含预定义的纸张尺寸。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查阅《[以指定纸张大小加载电子表格](/cells/zh/net/load-workbook-with-specified-printer-paper-size/)》详细文章。

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


### **添加Cell.GetCharacters(flag)方法**
Aspose.Cells APIs允许通过使用Cell.GetCharacters方法以FontSetting数组的形式获取字符对象。通过此版本，Aspose.Cells for .NET API已经公开了Cell.GetCharacters的另一个重载版本，可以接受布尔值作为参数，指示如果单元格属于ListObject，则是否要应用表格样式。

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


### **添加 OleObject.AutoLoad 属性**
Aspose.Cells for .NET 8.8.3已经公开了OleObject.AutoLoad属性，允许刷新OleObject的图像，如果底层对象的内容/数据已更改。设置上述属性为true时，会强制Excel应用在加载结果电子表格时刷新OleObject的图像。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查阅《[自动刷新OleObjects](/cells/zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)》详细文章。

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


### **添加 HTMLLoadOptions.SupportDivTag 属性**
Aspose.Cells for .NET 8.8.3已经公开了HTMLLoadOptions.SupportDivTag属性，允许解析包含在Aspose.Cells对象模型中的HTML文件/代码片段中的TD标签中嵌入的DIV标签。布尔类型的属性的默认值为false。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查阅《[加载HTML时支持内部DIV标签](/cells/zh/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)》详细文章。

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
Aspose.Cells for .NET 8.8.3已经公开了HtmlSaveOptions.ExportGridLines属性，允许在将电子表格导出为HTML格式时呈现网格线。布尔类型的属性默认值为false，但当设置为true时，API会在HTML格式中为可用数据范围呈现网格线。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查阅《[以HTML渲染网格线](/cells/zh/net/export-excel-to-html-with-gridlines/)》详细文章。

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
Aspose.Cells API现在允许为ListObject实例获取和设置评论。为了提供上述功能，Aspose.Cells API已暴露了ListObject.Comment属性。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查阅《[为ListObjects添加注释](/cells/zh/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/)》详细文章。

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
Aspose.Cells.GridWeb for .NET 8.8.3已经暴露了SessionStorePath属性，允许在会话模式为ViewState时获取或设置会话存储路径。上述属性获取或设置相对于当前Web应用程序基目录的路径。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[指定临时会话文件路径](/cells/zh/net/specify-the-path-where-gridweb-stores-temporary-session-files/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。
## **删除了 API**
### **移除了Workbook.Decrypt方法**
该属性已在一段时间前被标记为过时。此版本已完全将其从公共API中移除。建议将WorkbookSettings.Password属性设置为null以实现相同的目标。
{{< app/cells/assistant language="csharp" >}}
