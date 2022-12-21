---
title: ローカル モードで Microsoft Report Viewer と統合する
type: docs
weight: 30
url: /ja/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Report Viewer は、RDL および RDLC レポートを WinForms および ASP.NET アプリケーションで使用できる強力な .NET コントロールです。これにより、ユーザーはレポートを表示してさまざまな形式にエクスポートできます。コントロールは Microsoft Visual Studio 2005 および 2008 に含まれており、Microsoft から無料でダウンロードすることもできます。

レポート ビューアーは、組み込みエンジン (「ローカル モード」と呼ばれる) を使用して個別にレポートを生成したり、Microsoft SQL Server Reporting Services レポート サーバー (「リモート モード」) で生成されたレポートを表示したりできます。

- リモート モードでは、Report Viewer は、接続先の Report Server にインストールされているすべての形式にレポートをエクスポートできます。したがって、レポートをより多くの Microsoft Excel 形式にエクスポートするには、サーバーに Aspose.Cells for Reporting Services をインストールするだけで済みます。
- ただし、ローカル モードでは、Report Viewer は Report Server に接続せず、エクスポート形式のリストはいくつかの組み込み形式に限定されます。

 Aspose.Cells for Reporting Services を開発マシンにインストールし、以下の手順に従うと、ローカル モードで動作している Report Viewer からより多くの Microsoft Excel 形式にエクスポートできます。

{{% /alert %}} 
### **ローカル モードで Aspose.Cells を操作する**
1. リファレンス**Aspose.Cells.ReportingServices.dll**プロジェクトで：
 1. Visual Studio でプロジェクトを開きます。
 1. 右クリック**参考文献**フォルダと選択**参照を追加**.
1.**ブラウズ**タブを開き、次のアセンブリを参照します。
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
 （どこ<InstallDir> Aspose.Cells for Reporting Services をインストールまたは解凍したディレクトリです。

      **Aspose.Cells.ReportingServices.dll への参照をプロジェクトに追加する** 

![todo:画像_代替_文章](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. 次の AddExtension メソッドをコピーしてプロジェクトに貼り付けます。
このメソッドは、プライベート リフレクションを使用して、指定された表示拡張機能を Microsoft Report Viewer のサポートされている拡張機能のリストに追加します。

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

1. コードから AddExtension メソッドを呼び出します。
 - Aspose.Cells for Reporting Services エクスポート形式を Report Viewer コントロール インスタンスに追加する必要があるときはいつでも、AddExtension (前の手順で示した) を呼び出すことができます。 Form からの呼び出しを検討する_ロードまたはページ_WinForms または ASP .NET アプリケーションのイベント ハンドラーを読み込みます。
 - すべてまたは一部のエクスポート Aspose.Cells for Reporting Services エクスポート形式を追加できます。レポート ビューアーに表示される形式の表示名を指定できます。
ローカル モードで Aspose.Cells for Reporting Services エクスポート形式を Microsoft Report Viewer に追加するには、次のコードを使用します。

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

1. 新しいエクスポート形式をテストします。
 1. アプリケーションを実行します。
で使用できる新しいエクスポート形式がいくつかあることに気付くはずです。**輸出**レポート ビューアーのメニュー。
 1. いずれかの形式を選択し、エクスポートを実行します。
 1. ドキュメントが期待どおりに作成されていることを確認します。

**ローカル モードで実行されているレポート ビューアに新しいエクスポート形式が表示されます** 

![todo:画像_代替_文章](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
