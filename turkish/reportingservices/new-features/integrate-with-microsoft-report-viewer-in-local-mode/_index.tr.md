---
title: Microsoft Rapor Görüntüleyiciyi Yerel Modda Entegre Etme
type: docs
weight: 30
url: /tr/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

Microsoft Rapor Görüntüleyici, RDL ve RDLC raporlarının WinForms ve ASP.NET uygulamalarında kullanılmasına olanak tanıyan güçlü bir .NET denetimidir. Kullanıcılara raporları görüntüleme ve farklı formatlara dışa aktarma imkanı sağlar. Denetim, Microsoft Visual Studio 2005 ve 2008 ile birlikte sunulur ve aynı zamanda Microsoft'tan ücretsiz olarak indirilebilir.

Rapor Görüntüleyici, yerel modda bağımsız olarak rapor üretebilir (bilinen adıyla 'yerel mod'), veya bir Microsoft SQL Server Raporlama Servisleri Rapor Sunucusunda oluşturulan raporları görüntüleyebilir ('uzak mod'):

- Uzak modda, Rapor Görüntüleyici, bağlı olduğu Rapor Sunucusu üzerinde yüklü olan tüm formatlara raporları dışa aktarabilir. Bu nedenle, raporları daha fazla Microsoft Excel formatına dışa aktarmak için yalnızca sunucuda Aspose.Cells for Reporting Services'ü yüklemeniz yeterlidir.
- Ancak yerel modda, Rapor Görüntüleyici bir Rapor Sunucusuna bağlanmaz ve dışa aktarma formatları listesi yalnızca birkaç yerleşik formata sınırlıdır.

Geliştirme makinenize Aspose.Cells for Reporting Services yükleyerek ve aşağıdaki adımları takip ederek, Rapor Görüntüleyiciyi yerel modda çalışırken daha fazla Microsoft Excel formatına dışa aktarabilirsiniz. 

{{% /alert %}} 
### **Yerel Modda Aspose.Cells ile Çalışma**
1. Projeye **Aspose.Cells.ReportingServices.dll** başvuruyu ekleyin: 
   1. Proje dosyasını Visual Studio'da açın.
   1. **References** klasörüne sağ tıklayın ve **Referans Ekle**'yi seçin.
   1. **Gözat** sekmesini seçin ve aşağıdaki derleme yolunu belirleyin:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **Bir projeye Aspose.Cells.ReportingServices.dll referansı eklemek** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Aşağıdaki AddExtension yöntemini projeye kopyalayın ve yapıştırın.
   Bu yöntem, Microsoft Rapor Görüntüleyici içinde desteklenen uzantılar listesine belirtilen rendere uzantısını ekler, özel yansıma kullanarak. 

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

1. AddExtension yöntemini koddan çağırın. 
   - Aspose.Cells for Reporting Services dışa aktarma biçimlerini bir Rapor Görüntüleyici denetim örneğine eklemek istediğinizde AddExtension'ı (önceki adımda gösterildiği gibi) çağırabilirsiniz. WinForms veya ASP .NET uygulamasının Form_Load veya Page_Load etkinlik işleyicisinden aramayı düşünün.
   - Tüm veya yalnızca bazı Aspose.Cells for Reporting Services dışa aktarma biçimlerini ekleyebilirsiniz. Rapor Görüntüleyici'de görünecek biçimler için herhangi bir görüntü adı belirtebilirsiniz.
     Microsoft Rapor Görüntüleyiciye yerel modda Aspose.Cells for Reporting Services dışa aktarma biçimlerini eklemek için aşağıdaki kodu kullanın: 

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

1. Yeni dışa aktarma biçimlerini test edin. 
   1. Uygulamanızı çalıştırın.
      Microsoft Rapor Görüntüleyici'deki **Dışa Aktar** menüsünde bulunan bir dizi yeni dışa aktarma biçimini fark etmelisiniz. 
   1. Birini seçin ve dışa aktarımı çalıştırın.
   1. Belgenin beklendiği gibi oluşturulduğunu doğrulayın.

**Rapor Görüntüleyicide yerel modda çalışırken yeni dışa aktarma formatları görünür hale geldi** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
