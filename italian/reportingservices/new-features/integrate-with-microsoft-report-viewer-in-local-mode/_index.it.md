---
title: Integrazione con il visualizzatore di report di Microsoft in modalità locale
type: docs
weight: 30
url: /it/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

Microsoft Report Viewer è un potente controllo .NET che consente l'utilizzo di report RDL e RDLC nelle applicazioni WinForms e ASP.NET. Consente agli utenti di visualizzare ed esportare report in diversi formati. Il controllo è incluso in Microsoft Visual Studio 2005 e 2008, ed è anche disponibile come download gratuito da Microsoft.

Report Viewer può generare report indipendentemente utilizzando un motore integrato (noto come 'modalità locale'), oppure può visualizzare report generati su un server di report di Microsoft SQL Server Reporting Services ('modalità remota'):

- In modalità remota, Report Viewer può esportare report in tutti i formati installati sul Server di report a cui è collegato. Pertanto, per esportare report in più formati di Microsoft Excel è sufficiente installare sulel server il Aspose.Cells for Reporting Services.
- Tuttavia, in modalità locale, Report Viewer non si collega a un server di report e l'elenco dei formati di esportazione è limitato a pochi formati integrati.

Installando il Aspose.Cells for Reporting Services su una macchina di sviluppo e seguendo i passaggi seguenti, è possibile esportare in più formati di Microsoft Excel da Report Viewer che lavora in modalità locale. 

{{% /alert %}} 
### **Lavorare con Aspose.Cells in modalità locale**
1. Fare riferimento a **Aspose.Cells.ReportingServices.dll** nel progetto: 
   1. Aprire il progetto in Visual Studio.
   1. Fare clic con il pulsante destro del mouse sulla cartella **Riferimenti** e selezionare **Aggiungi riferimento**.
   1. Selezionare la scheda **Sfoglia** e cercare l'assembly seguente:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **Aggiunta di un riferimento a Aspose.Cells.ReportingServices.dll a un progetto** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Copiare e incollare il seguente metodo AddExtension nel progetto.
   Questo metodo aggiunge l'estensione di rendering specificata all'elenco delle estensioni supportate in Microsoft Report Viewer utilizzando la riflessione privata. 

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

1. Invochi il metodo AddExtension dal codice. 
   - Puoi chiamare AddExtension (mostrato nel passaggio precedente) ogni volta che hai bisogno di aggiungere formati di esportazione Aspose.Cells for Reporting Services a un'istanza di controllo Report Viewer. Considera di chiamarlo dall'handle dell'evento Form_Load o Page_Load di un'applicazione WinForms o ASP .NET.
   - Puoi aggiungere tutti o solo alcuni formati di esportazione Aspose.Cells for Reporting Services. Puoi specificare qualsiasi nome di visualizzazione per i formati da visualizzare in Report Viewer.
     Per aggiungere formati di esportazione Aspose.Cells for Reporting Services a Microsoft Report Viewer in modalità locale, utilizza il seguente codice: 

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

1. Testare i nuovi formati di esportazione. 
   1. Esegui la tua applicazione.
      Dovresti notare una serie di nuovi formati di esportazione disponibili nel menu **Esporta** in Report Viewer. 
   1. Seleziona uno dei formati e esegui l'esportazione.
   1. Verifica che il documento sia creato nel modo previsto.

**Nuovi formati di esportazione appaiono in Report Viewer in modalità locale** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
