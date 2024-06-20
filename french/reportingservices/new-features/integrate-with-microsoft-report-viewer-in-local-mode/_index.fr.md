---
title: Intégrer avec Microsoft Report Viewer en mode local
type: docs
weight: 30
url: /fr/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

Microsoft Report Viewer est un puissant contrôle .NET qui permet d'utiliser des rapports RDL et RDLC dans des applications WinForms et ASP.NET. Il permet aux utilisateurs de visualiser et d'exporter des rapports dans différents formats. Le contrôle est inclus avec Microsoft Visual Studio 2005 et 2008, et est également disponible en téléchargement gratuit depuis Microsoft.

Report Viewer peut générer des rapports de manière indépendante en utilisant un moteur intégré (appelé 'mode local'), ou il peut afficher des rapports qui sont générés sur un serveur de rapports de Microsoft SQL Server Reporting Services ('mode distant'):

- En mode distant, Report Viewer peut exporter des rapports vers tous les formats installés sur le serveur de rapports auquel il est connecté. Par conséquent, pour exporter des rapports vers plus de formats Microsoft Excel, vous devez simplement installer Aspose.Cells for Reporting Services sur le serveur.
- En mode local cependant, Report Viewer ne se connecte pas à un serveur de rapports et la liste des formats d'exportation est limitée à seulement quelques formats intégrés.

En installant Aspose.Cells for Reporting Services sur une machine de développement et en suivant les étapes ci-dessous, vous pouvez exporter vers plus de formats Microsoft Excel à partir de Report Viewer fonctionnant en mode local. 

{{% /alert %}} 
### **Travailler avec Aspose.Cells en mode local**
1. Référencez **Aspose.Cells.ReportingServices.dll** dans le projet : 
   1. Ouvrez le projet dans Visual Studio.
   1. Cliquez avec le bouton droit sur le dossier **Références** et sélectionnez **Ajouter une référence**.
   1. Sélectionnez l'onglet **Parcourir** et accédez à l'assembly suivant :
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **Ajout d'une référence à Aspose.Cells.ReportingServices.dll à un projet** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Copiez et collez la méthode AddExtension suivante dans le projet.
   Cette méthode ajoute l'extension de rendu spécifiée à la liste des extensions prises en charge dans Microsoft Report Viewer en utilisant la réflexion privée. 

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

1. Appelez la méthode AddExtension depuis le code. 
   - Vous pouvez appeler AddExtension (comme indiqué dans l'étape précédente) chaque fois que vous avez besoin d'ajouter des formats d'exportation Aspose.Cells for Reporting Services à une instance de contrôle Report Viewer. Considérez l'appeler depuis le gestionnaire d'événements Form_Load ou Page_Load d'une application WinForms ou ASP .NET.
   - Vous pouvez ajouter tous ou seulement certains des formats d'exportation Aspose.Cells for Reporting Services. Vous pouvez spécifier un nom d'affichage pour les formats à apparaître dans Report Viewer.
     Pour ajouter des formats d'exportation Aspose.Cells for Reporting Services à Microsoft Report Viewer en mode local, utilisez le code suivant : 

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

1. Testez les nouveaux formats d'exportation. 
   1. Exécutez votre application.
      Vous devriez remarquer un certain nombre de nouveaux formats d'exportation disponibles dans le menu **Export** dans le Visualiseur de rapports. 
   1. Sélectionnez l'un des formats et lancez l'exportation.
   1. Vérifiez que le document est créé comme vous l'attendiez.

**De nouveaux formats d'exportation apparaissent dans le Visualiseur de rapports en mode local** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
