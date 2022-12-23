---
title: 在本地模式下与 Microsoft Report Viewer 集成
type: docs
weight: 30
url: /zh/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Report Viewer 是一个功能强大的 .NET 控件，允许在 WinForms 和 ASP.NET 应用程序中使用 RDL 和 RDLC 报告。它使用户能够查看报告并将其导出为不同的格式。该控件包含在 Microsoft Visual Studio 2005 和 2008 中，也可以从 Microsoft 免费下载。

Report Viewer 可以使用内置引擎（称为“本地模式”）独立生成报告，也可以显示在 Microsoft SQL Server Reporting Services Report Server 上生成的报告（“远程模式”）：

- 在远程模式下，报表查看器可以将报表导出为安装在它所连接的报表服务器上的所有格式。因此，要将报表导出为更多Microsoft Excel格式，只需在服务器上安装Aspose.Cells for Reporting Services即可。
- 然而，在本地模式下，报表查看器不连接到报表服务器，并且导出格式列表仅限于几种内置格式。

通过在开发机器上安装 Aspose.Cells for Reporting Services 并按照以下步骤操作，您可以从在本地模式下工作的 Report Viewer 导出更多 Microsoft Excel 格式。

{{% /alert %}} 
### **在本地模式下使用 Aspose.Cells**
1. 参考**Aspose.Cells.ReportingServices.dll**在项目中：
 1. 在 Visual Studio 中打开项目。
 1. 右击**参考**文件夹并选择**添加参考**.
1. 选择**浏览**选项卡并浏览到以下程序集：
      <InstallDir>/ReportView/Aspose.Cells.ReportingServices.dll
 （在哪里<InstallDir>是你安装或解压的目录 Aspose.Cells for Reporting Services.

      **将对 Aspose.Cells.ReportingServices.dll 的引用添加到项目** 

![待办事项：图片_替代_文本](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. 将以下 AddExtension 方法复制并粘贴到项目中。
此方法使用私有反射将指定的呈现扩展添加到 Microsoft Report Viewer 中支持的扩展列表。

**C#**

{{< highlight "csharp" >}}



using System.Collections;

using System.Reflection;

using Microsoft.ReportingServices.ReportRendering;

// Use one of the two namespaces below depending on whether you are developing

// a WinForms or WebForms application.

using Microsoft.Reporting.WinForms;

// -- or --

// using Microsoft.Reporting.WebForms;





/// <summary>

/// Adds the specified rendering extension to the specified ReportViewer instance.

/// </summary>

/// <param name="viewer">A ReportViewer control instance.</param>

/// <param name="formatName">The name of the export format to appear on the dropdown list.</param>

/// <param name="extensionType">The class of the rendering extension to add.</param>

private static void AddExtension(ReportViewer viewer, string formatName, Type extensionType)

{

const BindingFlags flags = BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Instance;

// CommonService.ListRenderingExtension is an internal method that returns a list of supported

// rendering extensions. This list is also stored in a class field so we can simply get this list

// and add Aspose.Cells for Reporting Services rendering extensions to make Microsoft Excel

// export formats appear on the dropdown.

// Get the service type.

FieldInfo previewService = viewer.LocalReport.GetType().GetField("m_previewService", flags);

// Get the ListRenderingExtensions method info.

MethodInfo listRenderingExtensions = previewService.FieldType.GetMethod("ListRenderingExtensions", flags);

// Obtan a list of existing rendering extensions.

IList extensions = listRenderingExtensions.Invoke(previewService.GetValue(viewer.LocalReport), null) as IList;

// LocalRenderingExtensionInfo is a class that holds information about a rendering extension.

// We should create an instance of this class to add the info about the specified extension.

// Since the IRenderingExtension interface is defined in the Microsoft.ReportViewer.Common

// assembly, use this trick to obtain the corresponding Assembly instance. This will work for

// both Report Viewer 2005 (8.0) and 2008 (9.0).

Assembly commonAssembly = typeof(IRenderingExtension).Assembly;

// Now, get the LocalRenderingExtensionInfo type as it is defined in the same assembly.

Type localRenderingExtensionInfoType = commonAssembly.GetType("Microsoft.Reporting.LocalRenderingExtensionInfo");

// Get the LocalRenderingExtensionInfo constructor info.

ConstructorInfo ctor = localRenderingExtensionInfoType.GetConstructor(flags,

null,

new Type[] { typeof(string), typeof(string), typeof(bool), typeof(Type), typeof(bool) },

null);

// Create an instance of LocalRenderingExtensionInfo.

object instance = ctor.Invoke(new object[] { formatName, formatName, true, extensionType, true });

// Finally, add the info about our rendering extension to the list.

extensions.Add(instance);

}



{{< /highlight >}}




**VB .NET**

{{< highlight "csharp" >}}



Imports System.Collections

Imports System.Reflection

Imports Microsoft.ReportingServices.ReportRendering

// Use one of the two namespaces below depending on whether you are developing

// a WinForms or WebForms application.

Imports Microsoft.Reporting.WinForms

// -- or --

// Imports Microsoft.Reporting.WebForms





'' Adds the specified rendering extension to the specified ReportViewer instance.

Private Shared Sub AddExtension(ByVal viewer As ReportViewer, ByVal formatName As String, ByVal extensionType As Type)

    Const flags As BindingFlags = BindingFlags.NonPublic Or BindingFlags.Public Or BindingFlags.Instance



    ' CommonService.ListRenderingExtension is an internal method that returns a list of supported

    ' rendering extensions. This list is also stored in a class field so we can simply get this list

    ' and add Aspose.Cells for Reporting Services rendering extensions to make Microsoft Excel

    ' export formats appear on the dropdown.



    ' Get the service type.

    Dim previewService As FieldInfo = viewer.LocalReport.GetType().GetField("m_previewService", flags)



    ' Get the ListRenderingExtensions method info.

    Dim listRenderingExtensions As MethodInfo = previewService.FieldType.GetMethod("ListRenderingExtensions", flags)



    ' Obtan a list of existing rendering extensions.

    Dim extensions As IList = TryCast(listRenderingExtensions.Invoke(previewService.GetValue(viewer.LocalReport), Nothing), IList)



    ' LocalRenderingExtensionInfo is a class that holds information about a rendering extension.

    ' We should create an instance of this class to add the info about the specified extension.



    ' Since the IRenderingExtension interface is defined in the Microsoft.ReportViewer.Common assembly, use this trick

    ' to obtain the corresponding Assembly instance. This will work for both Report Viewer 2005 (8.0) and 2008 (9.0).

    Dim commonAssembly As System.Reflection.Assembly = GetType(IRenderingExtension).Assembly



    ' Now, get the LocalRenderingExtensionInfo type as it is defined in the same assembly.

    Dim localRenderingExtensionInfoType As Type = commonAssembly.GetType("Microsoft.Reporting.LocalRenderingExtensionInfo")



    ' Get the LocalRenderingExtensionInfo constructor info.

    Dim ctor As ConstructorInfo = localRenderingExtensionInfoType.GetConstructor(flags, Nothing, New Type() { GetType(String), GetType(String), GetType(Boolean), GetType(Type), GetType(Boolean) }, Nothing)



    ' Create an instance of LocalRenderingExtensionInfo. 

    Dim instance As Object = ctor.Invoke(New Object() { formatName, formatName, True, extensionType, True })



    ' Finally, add the info about our rendering extension to the list.

    extensions.Add(instance)

End Sub



{{< /highlight >}}

1. 从代码中调用 AddExtension 方法。
 只要您需要将 Aspose.Cells for Reporting Services 导出格式添加到 Report Viewer 控件实例，您就可以调用 AddExtension（如上一步所示）。考虑从表单调用_加载或页面_加载 WinForms 或 ASP .NET 应用程序的事件处理程序。
 - 您可以添加全部或仅部分导出 Aspose.Cells for Reporting Services 导出格式。您可以为要在报表查看器中显示的格式指定任何显示名称。
要在本地模式下将 Aspose.Cells for Reporting Services 导出格式添加到 Microsoft Report Viewer，请使用以下代码：

**C#**

{{< highlight "csharp" >}}



            AddExtension(reportViewer1, "Xls - Xls via Aspose.Cells",    typeof(Aspose.Cells.ReportingServices.XlsRenderer));

            AddExtension(reportViewer1, "Xlsx - Xlsx via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.Excel2007XlsxRenderer));

			AddExtension(reportViewer1, "CSV - CSV via Aspose.Cells",    typeof(Aspose.Cells.ReportingServices.CSVRenderer));

            AddExtension(reportViewer1, "SpreadsheetML - SpreadsheetML via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.SpreadsheetMLRenderer));

            AddExtension(reportViewer1, "Txt - TabDelimited text via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.TabDelimitedRenderer)); 



{{< /highlight >}}

**VB .NET**

{{< highlight "csharp" >}}

              AddExtension(reportViewer1, "Xls - Xls via Aspose.Cells",    GetType (Aspose.Cells.ReportingServices.XlsRenderer));

            AddExtension(reportViewer1, "Xlsx - Xlsx via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.Excel2007XlsxRenderer));

			AddExtension(reportViewer1, "CSV - CSV via Aspose.Cells",    GetType (Aspose.Cells.ReportingServices.CSVRenderer));

            AddExtension(reportViewer1, "SpreadsheetML - SpreadsheetML via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.SpreadsheetMLRenderer));

            AddExtension(reportViewer1, "Txt - TabDelimited text via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.TabDelimitedRenderer));



{{< /highlight >}}

1. 测试新的导出格式。
 1. 运行您的应用程序。
您应该注意到在**出口**报告查看器中的菜单。
 1. 选择其中一种格式并运行导出。
 1. 确认文档是按照您预期的方式创建的。

**新的导出格式出现在以本地模式运行的报表查看器中** 

![待办事项：图片_替代_文本](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
