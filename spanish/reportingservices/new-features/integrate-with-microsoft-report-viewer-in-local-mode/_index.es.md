---
title: Integrar con Microsoft Visor de informes en modo local
type: docs
weight: 30
url: /es/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Report Viewer es un poderoso control .NET que permite usar informes RDL y RDLC en aplicaciones WinForms y ASP.NET. Permite a los usuarios ver y exportar informes a diferentes formatos. El control se incluye con Microsoft Visual Studio 2005 y 2008, y también está disponible como descarga gratuita desde Microsoft.

Report Viewer puede generar informes de forma independiente utilizando un motor integrado (conocido como "modo local"), o puede mostrar informes generados en un servidor de informes de SQL Server Reporting Services Microsoft ("modo remoto"):

- En modo remoto, Report Viewer puede exportar informes a todos los formatos instalados en el servidor de informes al que está conectado. Por lo tanto, para exportar informes a más formatos de Excel Microsoft, solo necesita instalar Aspose.Cells para Reporting Services en el servidor.
- Sin embargo, en el modo local, Report Viewer no se conecta a un servidor de informes y la lista de formatos de exportación se limita a solo unos pocos formatos integrados.

 Al instalar Aspose.Cells para Reporting Services en una máquina de desarrollo y seguir los pasos a continuación, puede exportar a más formatos de Excel Microsoft desde Report Viewer trabajando en modo local.

{{% /alert %}} 
### **Trabajando con Aspose.Cells en modo local**
1.  Referencia**Aspose.Cells.ReportingServices.dll** en el proyecto:
 1. Abra el proyecto en Visual Studio.
 1. Haga clic derecho en el**Referencias** carpeta y seleccione**Añadir referencia**.
 1. Seleccione el**Navegar** y busque el siguiente ensamblaje:
      <InstallDir>/ReportView/Aspose.Cells.ReportingServices.dll
 (dónde<InstallDir> es el directorio donde instaló o descomprimió Aspose.Cells para Reporting Services.

      **Agregar una referencia a Aspose.Cells.ReportingServices.dll a un proyecto** 

![todo:imagen_alternativa_texto](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Copie y pegue el siguiente método AddExtension en el proyecto.
 Este método agrega la extensión de representación especificada a la lista de extensiones admitidas en el Visor de informes Microsoft mediante la reflexión privada.

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

1.  Invoque el método AddExtension desde el código.
 - Puede llamar a AddExtension (que se muestra en el paso anterior) cada vez que necesite agregar Aspose.Cells para los formatos de exportación de Reporting Services a una instancia de control de Report Viewer. Considere llamar desde el Formulario_Cargar o Página_Cargue el controlador de eventos de una aplicación WinForms o ASP .NET.
 - Puede agregar todas o solo algunas exportaciones Aspose.Cells para los formatos de exportación de Reporting Services. Puede especificar cualquier nombre de visualización para que los formatos aparezcan en el Visor de informes.
 Para agregar Aspose.Cells para formatos de exportación de Reporting Services a Microsoft Visor de informes en modo local, use el siguiente código:

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

1.  Pruebe los nuevos formatos de exportación.
1. Ejecute su aplicación.
 Debería notar una serie de nuevos formatos de exportación disponibles en el**Exportar** menú en el Visor de informes.
 1. Seleccione uno de los formatos y ejecute la exportación.
 1. Verifique que el documento se haya creado de la manera que esperaba.

**Aparecen nuevos formatos de exportación en Report Viewer ejecutándose en modo local** 

![todo:imagen_alternativa_texto](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
