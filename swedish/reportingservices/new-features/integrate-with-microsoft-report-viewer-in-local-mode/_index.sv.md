---
title: Integrera med Microsoft Report Viewer i lokal läge
type: docs
weight: 30
url: /sv/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

Microsoft Report Viewer är en kraftfull .NET-kontroll som gör att RDL- och RDLC-rapporter kan användas i WinForms- och ASP.NET-applikationer. Det gör det möjligt för användare att visa och exportera rapporter till olika format. Kontrollen ingår i Microsoft Visual Studio 2005 och 2008, och är också tillgänglig som en gratis nedladdning från Microsoft.

Rapportvisaren kan generera rapporter självständigt med hjälp av en inbyggd motor (känd som 'lokalt läge'), eller så kan den visa rapporter som genererats på en Microsoft SQL Server Reporting Services-rapportserver ('fjärrläge')

- I fjärrläge kan rapportvisaren exportera rapporter till alla format installerade på rapportservern den är ansluten till. Därför behöver du bara installera Aspose.Cells for Reporting Services på servern för att exportera rapporter till fler Microsoft Excel-format.
- I lokal läge ansluter dock inte rapportvisaren till en rapportserver och listan över exportformat är begränsad till endast några inbyggda format.

Genom att installera Aspose.Cells for Reporting Services på en utvecklingsmaskin och följa stegen nedan kan du exportera till fler Microsoft Excel-format från Rapportvisaren som fungerar i lokal läge. 

{{% /alert %}} 
### **Arbeta med Aspose.Cells i lokal läge**
1. Referera till **Aspose.Cells.ReportingServices.dll** i projektet: 
   1. Öppna projektet i Visual Studio.
   1. Högerklicka på mappen **Referenser** och välj **Lägg till referens**.
   1. Välj fliken **Bläddra** och bläddra till följande assembly:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **Lägga till en referens till Aspose.Cells.ReportingServices.dll till ett projekt** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Kopiera och klistra in följande AddExtension-metod i projektet.
   Denna metod lägger till den angivna renderingsutökningen i listan över stödda utökningar i Microsoft Report Viewer med hjälp av privat reflektion. 

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

1. Anropa AddExtension-metoden från koden. 
   - Du kan anropa AddExtension (som visas i det föregående steget) när som helst du behöver lägga till Aspose.Cells for Reporting Services exportformat till en Report Viewer-kontrollinstans. Överväg att kalla från Form_Load eller Page_Load-händelseshanteraren för en WinForms- eller ASP .NET-applikation.
   - Du kan lägga till alla eller endast några export Aspose.Cells for Reporting Services exportformat. Du kan ange valfritt visningsnamn för formaten som ska visas i Rapportvisaren.
     För att lägga till Aspose.Cells for Reporting Services exportformat till Microsoft Report Viewer i lokalt läge, använd följande kod: 

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

1. Testa de nya exportformaten. 
   1. Kör din applikation.
      Du bör märka att ett antal nya exportformat finns tillgängliga i **Exportera**-menyn i Report Viewer. 
   1. Välj ett av formaten och kör export.
   1. Verifiera att dokumentet skapas på det sätt du förväntade dig.

**Nya exportformat visas i Report Viewer som körs i lokalt läge** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
