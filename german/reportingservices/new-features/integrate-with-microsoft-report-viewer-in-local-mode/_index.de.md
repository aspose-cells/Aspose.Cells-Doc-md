---
title: Integration mit Microsoft Report Viewer im lokalen Modus
type: docs
weight: 30
url: /de/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Report Viewer ist ein leistungsstarkes .NET Steuerelement, mit dem RDL- und RDLC-Berichte in WinForms- und ASP.NET-Anwendungen verwendet werden können. Es ermöglicht Benutzern, Berichte in verschiedenen Formaten anzuzeigen und zu exportieren. Das Steuerelement ist in Microsoft Visual Studio 2005 und 2008 enthalten und steht auch als kostenloser Download unter Microsoft zur Verfügung.

Report Viewer kann Berichte mithilfe einer integrierten Engine (bekannt als „lokaler Modus“) unabhängig generieren oder Berichte anzeigen, die auf einem Microsoft SQL Server Reporting Services-Berichtsserver generiert werden („Remotemodus“):

- Im Remote-Modus kann Report Viewer Berichte in alle Formate exportieren, die auf dem Berichtsserver installiert sind, mit dem er verbunden ist. Um Berichte in weitere Microsoft Excel-Formate zu exportieren, müssen Sie daher nur Aspose.Cells for Reporting Services auf dem Server installieren.
- Im lokalen Modus stellt Report Viewer jedoch keine Verbindung zu einem Berichtsserver her, und die Liste der Exportformate ist auf einige wenige integrierte Formate beschränkt.

Indem Sie Aspose.Cells for Reporting Services auf einem Entwicklungscomputer installieren und die folgenden Schritte ausführen, können Sie aus Report Viewer, der im lokalen Modus arbeitet, in weitere Microsoft Excel-Formate exportieren.

{{% /alert %}} 
### **Arbeiten mit Aspose.Cells im lokalen Modus**
1.  Referenz**Aspose.Cells.ReportingServices.dll** im Projekt:
 1. Öffnen Sie das Projekt in Visual Studio.
 1. Klicken Sie mit der rechten Maustaste auf die**Verweise** Ordner und wählen Sie aus**Referenz hinzufügen**.
 1. Wählen Sie die aus**Durchsuche** Registerkarte und navigieren Sie zu der folgenden Assembly:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
 (wo<InstallDir> ist das Verzeichnis, in dem Sie Aspose.Cells for Reporting Services installiert oder entpackt haben.

      **Hinzufügen eines Verweises auf Aspose.Cells.ReportingServices.dll zu einem Projekt** 

![todo: Bild_alt_Text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Kopieren Sie die folgende AddExtension-Methode, und fügen Sie sie in das Projekt ein.
 Diese Methode fügt die angegebene Renderingerweiterung der Liste der unterstützten Erweiterungen in Microsoft Report Viewer mithilfe von privater Reflektion hinzu.

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

1.  Rufen Sie die AddExtension-Methode aus dem Code auf.
 Sie können AddExtension (im vorherigen Schritt gezeigt) aufrufen, wann immer Sie Aspose.Cells for Reporting Services-Exportformate zu einer Report Viewer-Steuerelementinstanz hinzufügen müssen. Erwägen Sie, über das Formular anzurufen_Laden oder Seite_Ereignishandler einer WinForms- oder ASP .NET-Anwendung laden.
 - Sie können alle oder nur einige Exportformate Aspose.Cells for Reporting Services hinzufügen. Sie können einen beliebigen Anzeigenamen für die Formate angeben, die in Report Viewer angezeigt werden sollen.
 Um Aspose.Cells for Reporting Services Exportformate zu Microsoft Report Viewer im lokalen Modus hinzuzufügen, verwenden Sie den folgenden Code:

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

1.  Testen Sie die neuen Exportformate.
 1. Führen Sie Ihre Anwendung aus.
 Sie sollten eine Reihe neuer Exportformate bemerken, die in der verfügbar sind**Export** Menü im Report Viewer.
 1. Wählen Sie eines der Formate aus und führen Sie den Export aus.
 1. Vergewissern Sie sich, dass das Dokument wie erwartet erstellt wurde.

**Neue Exportformate erscheinen im Report Viewer, der im lokalen Modus ausgeführt wird** 

![todo: Bild_alt_Text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
