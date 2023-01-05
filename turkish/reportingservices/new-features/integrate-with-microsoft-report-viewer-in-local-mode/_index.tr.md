---
title: Yerel Modda Microsoft Rapor Görüntüleyici ile entegre edin
type: docs
weight: 30
url: /tr/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Rapor Görüntüleyici, RDL ve RDLC raporlarının WinForms ve ASP.NET uygulamalarında kullanılmasına izin veren güçlü bir .NET denetimidir. Kullanıcıların raporları farklı biçimlerde görüntülemesine ve dışa aktarmasına olanak tanır. Denetim, Microsoft Visual Studio 2005 ve 2008'e dahildir ve ayrıca Microsoft'den ücretsiz olarak indirilebilir.

Rapor Görüntüleyici, yerleşik bir motor ("yerel mod" olarak bilinir) kullanarak bağımsız olarak raporlar oluşturabilir veya bir Microsoft SQL Server Raporlama Hizmetleri Rapor Sunucusunda ("uzak mod") oluşturulan raporları görüntüleyebilir:

- Uzak modda, Rapor Görüntüleyici, raporları bağlı olduğu Rapor Sunucusunda yüklü olan tüm formatlara aktarabilir. Bu nedenle, raporları daha fazla Microsoft Excel formatına aktarmak için sunucuya yalnızca Aspose.Cells for Reporting Services yüklemeniz gerekir.
- Ancak yerel modda, Rapor Görüntüleyici bir Rapor Sunucusuna bağlanmaz ve dışa aktarma biçimlerinin listesi yalnızca birkaç yerleşik biçimle sınırlıdır.

Aspose.Cells for Reporting Services'i bir geliştirme makinesine yükleyerek ve aşağıdaki adımları izleyerek, yerel modda çalışan Report Viewer'dan daha fazla Microsoft Excel formatına dışa aktarabilirsiniz.

{{% /alert %}} 
### **Aspose.Cells ile Yerel Modda Çalışma**
1.  Referans**Aspose.Cells.ReportingServices.dll** projenin içinde:
 1. Projeyi Visual Studio'da açın.
 1. Sağ tıklayın**Referanslar** klasör ve seçin**Referans ekle**.
 1.**Araştır** sekmesine gidin ve aşağıdaki derlemeye göz atın:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
 (nerede<InstallDir> Aspose.Cells for Reporting Services'i kurduğunuz veya paketinden çıkardığınız dizindir.

      **Bir projeye Aspose.Cells.ReportingServices.dll başvurusu ekleme** 

![yapılacaklar:resim_alternatif_metin](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Aşağıdaki AddExtension yöntemini kopyalayıp projeye yapıştırın.
 Bu yöntem, belirtilen işleme uzantısını özel yansıma kullanarak Microsoft Rapor Görüntüleyici'de desteklenen uzantılar listesine ekler.

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

1.  Koddan AddExtension yöntemini çağırın.
 Bir Report Viewer kontrol örneğine Aspose.Cells for Reporting Services dışa aktarma biçimleri eklemeniz gerektiğinde AddExtension'ı (önceki adımda gösterilen) arayabilirsiniz. Formdan aramayı düşünün_Yükle veya Sayfa_Bir WinForms veya ASP .NET uygulamasının olay işleyicisini yükleyin.
 - Aspose.Cells for Reporting Services dışa aktarma biçimlerinin tümünü veya yalnızca bazılarını ekleyebilirsiniz. Rapor Görüntüleyici'de görünecek biçimler için herhangi bir görünen ad belirtebilirsiniz.
 Yerel modda Aspose.Cells for Reporting Services dışa aktarma biçimlerini Microsoft Rapor Görüntüleyici'ye eklemek için aşağıdaki kodu kullanın:

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

1.  Yeni dışa aktarma biçimlerini test edin.
 1. Uygulamanızı çalıştırın.
 Bir dizi yeni dışa aktarma formatının mevcut olduğunu fark edeceksiniz.**İhracat** Rapor Görüntüleyici'deki menü.
 1. Biçimlerden birini seçin ve dışa aktarmayı çalıştırın.
 1. Belgenin beklediğiniz gibi oluşturulduğunu doğrulayın.

**Yerel modda çalışan Rapor Görüntüleyici'de yeni dışa aktarma biçimleri görünüyor** 

![yapılacaklar:resim_alternatif_metin](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
