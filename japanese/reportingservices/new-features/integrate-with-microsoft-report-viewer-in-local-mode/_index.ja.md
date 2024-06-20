---
title: Microsoft Report Viewer との統合（ローカルモードで）
type: docs
weight: 30
url: /ja/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

Microsoft Report Viewer は強力な .NET コントロールで、RDL および RDLC レポートを WinForms および ASP.NET アプリケーションで使用し、異なる形式にエクスポートすることができます。このコントロールは Microsoft Visual Studio 2005 および 2008 に含まれており、Microsoft から無料でダウンロードすることもできます。

レポートビューアは、組み込みのエンジン（「ローカルモード」としても知られる）を使用して独立してレポートを生成できるか、Microsoft SQL Server Reporting Servicesレポートサーバー（「リモートモード」としても知られる）で生成されたレポートを表示できます。

- リモートモードでは、レポートビューアは接続されているReport Serverにインストールされているすべての形式にレポートをエクスポートできます。したがって、より多くのMicrosoft Excel形式にレポートをエクスポートするには、サーバーにAspose.Cells for Reporting Servicesをインストールするだけで済みます。
- しかし、ローカルモードでは、レポートビューアはReport Serverに接続せず、エクスポート形式のリストはわずかな組み込み形式のみに制限されます。

開発マシンにAspose.Cells for Reporting Servicesをインストールし、以下の手順に従うことで、ローカルモードで動作するレポートビューアからより多くのMicrosoft Excel形式にエクスポートできます。 

{{% /alert %}} 
### **ローカルモードでAspose.Cellsと連携する**
1. プロジェクトで **Aspose.Cells.ReportingServices.dll** を参照します。 
   1. Visual Studioでプロジェクトを開きます。
   1. **参照** フォルダを右クリックし、 **参照の追加** を選択します。
   1. **ブラウズ** タブを選択し、次のアセンブリに移動します。
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **プロジェクトにAspose.Cells.ReportingServices.dllへの参照を追加する** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. 次のAddExtensionメソッドをプロジェクトにコピーして貼り付けます。
   このメソッドは、プライベートリフレクションを使用してMicrosoft Report Viewerでのサポートされるエクステンションのリストに指定されたレンダリングエクステンションを追加します。 

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

1. コードからAddExtensionメソッドを呼び出します。 
   - [前の手順](/cells/ja/cpp/report-viewer-control-instance/)で示されているAddExtensionを呼び出して、Aspose.Cells for Reporting Servicesのエクスポート形式をReport Viewerコントロールインスタンスに追加できます。WinFormsまたはASP .NETアプリケーションのForm_LoadまたはPage_Loadイベントハンドラから呼び出すことを検討してください。
   - Aspose.Cells for Reporting Servicesのエクスポート形式をReport Viewerコントロールインスタンスに追加する必要がある場合は、必要なときにAddExtensionを呼び出すことができます。Report Viewerに表示される形式の表示名を指定できます。
     Report ViewerでローカルモードでAspose.Cells for Reporting Servicesのエクスポート形式を追加するには、次のコードを使用します。 

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

1. 新しいエクスポート形式をテストします。 
   1. アプリケーションを実行します。
      Report Viewerの **エクスポート** メニューで利用可能な新しいエクスポート形式の数が増えていることに気づくはずです。 
   1. 形式の1つを選択してエクスポートを実行します。
   1. 期待通りにドキュメントが作成されたかを確認します。

Report Viewerのローカルモードで新しいエクスポート形式が表示されます 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
