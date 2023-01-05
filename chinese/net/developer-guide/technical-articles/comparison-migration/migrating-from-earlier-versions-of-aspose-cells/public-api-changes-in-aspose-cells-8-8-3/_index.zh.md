---
title: 公共 API Aspose.Cells 8.8.3 的变化
type: docs
weight: 290
url: /zh/net/public-api-changes-in-aspose-cells-8-8-3/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.8.2 到 8.8.3 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持 ActiveX 控件**
Aspose.Cells for .NET 8.8.3 公开了允许将 ActiveX 控件添加到 ShapeCollection 的 AddActiveXControl 方法。上述方法需要7个参数来指定控件的类型、放置控件的位置和控件的大小。可以使用具有以下可能值的 ControlType 枚举来指定类型。

1. 控件类型.CheckBox
1. 控件类型.ComboBox
1. 控件类型.CommandButton
1. 控件类型.Image
1. 控件类型.标签
1. 控件类型.ListBox
1. 控件类型.RadioButton
1. 控件类型.滚动条
1. 控件类型.SpinButton
1. 控件类型.TextBox
1. 控件类型.ToggleButton
1. 控件类型.Unknown

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[将 ActiveX 控件添加到工作表](/cells/zh/net/add-activex-controls-using-aspose-cells/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 LoadOptions.SetPaperSize 方法**
Aspose.Cells for .NET 8.8.3 允许在使用新公开的 LoadOptions.SetPaperSize 方法时从默认打印机设置设置默认打印纸张尺寸，如下所示。请注意，上述方法的输入参数是来自包含预定义纸张尺寸的 PaperSizeType 枚举的值。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[加载具有指定纸张尺寸的电子表格](/cells/zh/net/load-workbook-with-specified-printer-paper-size/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of LoadOptions

var loadOptions = new LoadOptions();

// Set the PaperSize property to appropriate value

loadOptions.SetPaperSize(PaperSizeType.PaperA4);

// Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(dir + "input.xlsx", loadOptions);

{{< /highlight >}}


### **添加了 Cell.GetCharacters(flag) 方法**
Aspose.Cells API 允许使用 Cell.GetCharacters 方法以 FontSetting 数组的形式获取字符对象。在此版本中，Aspose.Cells for .NET API 公开了 Cell.GetCharacters 的重载版本，它可以接受布尔值作为参数，指示如果单元格是 ListObject 的一部分，是否必须在单元格上应用表格样式。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 OleObject.AutoLoad 属性**
Aspose.Cells for .NET 8.8.3 公开了 OleObject.AutoLoad 属性，如果基础对象的内容/数据已更改，该属性允许刷新 OleObject 的图像。上述属性设置为 true 时，会强制 Excel 应用程序在加载生成的电子表格时刷新 OleObject 的图像。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[自动刷新 OleObjects](/cells/zh/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 HTMLLoadOptions.SupportDivTag 属性**
Aspose.Cells for .NET 8.8.3 公开了 HTMLLoadOptions.SupportDivTag 属性，允许在 Aspose.Cells 对象模型中加载 HTML 文件/片段时解析嵌入在 TD 标签中的 DIV 标签。布尔类型属性的默认值为 false。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[加载时支持内部 DIV 标签 HTML](/cells/zh/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 HtmlSaveOptions.ExportGridLines 属性**
Aspose.Cells for .NET 8.8.3 公开了 HtmlSaveOptions.ExportGridLines 属性，该属性允许在将电子表格导出为 HTML 格式时呈现网格线。布尔类型属性的默认值为 false，但是，当设置为 true 时，API 将以 HTML 格式呈现可用数据范围的网格线。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[将网格线渲染到 HTML](/cells/zh/net/export-excel-to-html-with-gridlines/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook and load existing spreadsheet

var book = new Workbook(dir + "input.xlsx");

// Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set ExportGridLines to true

options.ExportGridLines = true;

// Save the result in HTML format

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **添加了 ListObject.Comment 属性**
Aspose.Cells API 现在允许获取和设置 ListObject 实例的注释。为了提供上述功能，Aspose.Cells API 公开了 ListObject.Comment 属性。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[为 ListObjects 添加注释](/cells/zh/net/set-the-comment-of-table-or-list-object-inside-the-worksheet/).

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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


### **添加了 GridWeb.SessionStorePath 属性**
Aspose.Cells.GridWeb for .NET 8.8.3 公开了 SessionStorePath 属性，当会话模式为 ViewState 时，该属性允许获取或设置会话存储路径。上述属性获取或设置当前 Web 应用程序基本目录的相对路径。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[指定临时会话文件的路径](/cells/zh/net/specify-the-path-where-gridweb-stores-temporary-session-files/).

{{% /alert %}} 

以下是简单的使用场景。
## **删除的 API**
### **删除了 Workbook.Decrypt 方法**
上述财产在一段时间前被标记为过时。此版本已将其从公共 API 中完全删除。建议将 WorkbookSettings.Password 属性设置为 null 以实现相同的目标。
