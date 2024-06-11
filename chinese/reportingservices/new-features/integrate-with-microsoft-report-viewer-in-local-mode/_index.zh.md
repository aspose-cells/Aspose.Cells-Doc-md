---
title: 集成到本地模式中的Microsoft Report Viewer
type: docs
weight: 30
url: /zh/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

Microsoft Report Viewer是一个强大的.NET控件，允许在WinForms和ASP.NET应用程序中使用RDL和RDLC报表。它使用户能够查看和导出报表到不同的格式。该控件包含在Microsoft Visual Studio 2005和2008中，并且还可以从Microsoft免费下载。

Report Viewer可以独立生成报表，使用内置引擎(称为“本地模式”)，也可以显示在Microsoft SQL Server Reporting Services报表服务器上生成的报表(“远程模式”)：

- 在远程模式下，Report Viewer可以将报表导出到与其连接的报表服务器上安装的所有格式。因此，要将报表导出为更多的Microsoft Excel格式，只需在服务器上安装Aspose.Cells for Reporting Services。
- 但是在本地模式下，Report Viewer不连接到报表服务器，导出格式列表仅限于一些内置格式。

通过在开发计算机上安装Aspose.Cells for Reporting Services，并按照以下步骤，您可以从工作在本地模式的Report Viewer导出更多的Microsoft Excel格式。 

{{% /alert %}} 
### **在本地模式中使用Aspose.Cells**
1. 在项目中引用**Aspose.Cells.ReportingServices.dll**: 
   1. 在Visual Studio中打开项目。
   1. 右键单击**References**文件夹，选择**添加引用**。
   1. 选择**浏览**选项卡，并浏览到以下程序集:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **向项目添加对Aspose.Cells.ReportingServices.dll的引用** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. 复制并粘贴以下AddExtension方法到项目中。
   此方法使用私有反射将指定的呈现扩展添加到 Microsoft Report Viewer 中支持的扩展列表。 

**C#**

{{< highlight csharp >}}



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

{{< highlight csharp >}}



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
   - 每当需要向 Report Viewer 控件实例添加 Aspose.Cells for Reporting Services 导出格式时，可以调用 AddExtension（如前一步骤所示）。考虑从 WinForms 或 ASP.NET 应用程序的 Form_Load 或 Page_Load 事件处理程序中调用。
   - 您可以添加所有或部分导出 Aspose.Cells for Reporting Services 导出格式。您可以为格式指定任何显示名称，以在 Report Viewer 中显示。
     要在本地模式下向 Microsoft Report Viewer 添加 Aspose.Cells for Reporting Services 导出格式，请使用以下代码： 

**C#**

{{< highlight csharp >}}



            AddExtension(reportViewer1, "Xls - Xls via Aspose.Cells",    typeof(Aspose.Cells.ReportingServices.XlsRenderer));

            AddExtension(reportViewer1, "Xlsx - Xlsx via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.Excel2007XlsxRenderer));

			AddExtension(reportViewer1, "CSV - CSV via Aspose.Cells",    typeof(Aspose.Cells.ReportingServices.CSVRenderer));

            AddExtension(reportViewer1, "SpreadsheetML - SpreadsheetML via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.SpreadsheetMLRenderer));

            AddExtension(reportViewer1, "Txt - TabDelimited text via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.TabDelimitedRenderer)); 



{{< /highlight >}}

**VB .NET**

{{< highlight csharp >}}

              AddExtension(reportViewer1, "Xls - Xls via Aspose.Cells",    GetType (Aspose.Cells.ReportingServices.XlsRenderer));

            AddExtension(reportViewer1, "Xlsx - Xlsx via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.Excel2007XlsxRenderer));

			AddExtension(reportViewer1, "CSV - CSV via Aspose.Cells",    GetType (Aspose.Cells.ReportingServices.CSVRenderer));

            AddExtension(reportViewer1, "SpreadsheetML - SpreadsheetML via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.SpreadsheetMLRenderer));

            AddExtension(reportViewer1, "Txt - TabDelimited text via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.TabDelimitedRenderer));



{{< /highlight >}}

1. 测试新的导出格式。 
   1. 运行您的应用程序。
      您应该注意到 **导出** 菜单中有许多新的导出格式。 
   1. 选择其中一种格式并运行导出。
   1. 验证文档是否按预期创建。

**在本地模式下运行的 Report Viewer 中会出现新的导出格式** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
