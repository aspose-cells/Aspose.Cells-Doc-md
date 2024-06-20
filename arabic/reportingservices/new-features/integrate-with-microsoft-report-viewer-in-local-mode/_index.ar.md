---
title: دمج مع عارض التقرير Microsoft في الوضع المحلي
type: docs
weight: 30
url: /ar/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---

{{% alert color="primary" %}} 

عارض التقرير من مايكروسوفت هو عنصر تحكم .NET قوي يسمح باستخدام تقارير RDL و RDLC في تطبيقات WinForms و ASP.NET. يتيح للمستخدمين عرض وتصدير التقارير إلى تنسيقات مختلفة. يتم تضمين العنصر التحكم مع Microsoft Visual Studio 2005 و 2008، ويتوفر أيضا كتنزيل مجاني من مايكروسوفت.

يمكن لعارض التقرير إنشاء تقارير بشكل مستقل باستخدام محرك مدمج (المعروف بـ 'الوضع المحلي')، أو يمكنه عرض التقارير التي تم إنشاؤها على خادم تقارير خدمات تقارير Microsoft SQL Server ('الوضع البعيد'):

- في الوضع البعيد، يمكن لعارض التقرير تصدير التقارير إلى جميع التنسيقات المثبتة على خادم التقارير الذي يتصل به. لذلك، لتصدير التقارير إلى المزيد من تنسيقات جداول البيانات Microsoft Excel، يتعين فقط تثبيت Aspose.Cells for Reporting Services على الخادم.
- في الوضع المحلي، ومع ذلك، لا يتصل عارض التقرير بخادم تقارير وقائمة تنسيقات التصدير محدودة إلى عدد قليل فقط من التنسيقات المدمجة.

من خلال تثبيت Aspose.Cells for Reporting Services على الجهاز التطويري واتباع الخطوات أدناه، يمكنك تصدير إلى المزيد من تنسيقات جداول بيانات Microsoft Excel من عارض التقرير العامل في الوضع المحلي. 

{{% /alert %}} 
### **العمل مع Aspose.Cells في الوضع المحلي**
1. الإشارة إلى **Aspose.Cells.ReportingServices.dll** في المشروع: 
   1. فتح المشروع في Visual Studio.
   1. انقر بزر الماوس الأيمن على مجلد **المراجع** وحدد **إضافة مرجع**.
   1. حدد علامة التبويب **تصفح** وانتقل إلى التجميع التالي:
      <InstallDir>/ ReportView/Aspose.Cells.ReportingServices.dll
      (where <InstallDir> is the directory where you installed or unpacked Aspose.Cells for Reporting Services. 

      **إضافة مرجع إلى Aspose.Cells.ReportingServices.dll إلى المشروع** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. انسخ والصق طريقة AddExtension التالية في المشروع.
   تقوم هذه الطريقة بإضافة تمديد التقديم المحدد إلى قائمة التمديدات المدعومة في عارض التقرير Microsoft باستخدام الانعكاس الخاص. 

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

1. استدعي طريقة AddExtension من الكود. 
   - يمكنك استدعاء AddExtension (الموضح في الخطوة السابقة) كلما كنت بحاجة لإضافة تنسيقات تصدير Aspose.Cells for Reporting Services إلى مثيل عنصر تحكم عارض التقرير. يُعتَبَر استدعاء ذلك من حدث Form_Load أو Page_Load handler لتطبيقات WinForms أو ASP .NET.
   - يمكنك إضافة جميع تنسيقات تصدير Aspose.Cells for Reporting Services أو فقط بعضها. يمكنك تحديد أي اسم عرض للتنسيقات لتظهر في عارض التقرير.
     لإضافة Aspose.Cells for Reporting Services تنسيقات تصدير إلى Microsoft Report Viewer في الوضع المحلي، استخدم الكود التالي: 

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

1. اختبار تنسيقات التصدير الجديدة. 
   1. قم بتشغيل تطبيقك.
      يجب أن تلاحظ عددًا من تنسيقات التصدير الجديدة المتوفرة في قائمة التصدير في Report Viewer. 
   1. حدد أحد التنسيقات وقم بتشغيل التصدير.
   1. تحقق من أن المستند تم إنشاؤه بالطريقة التي توقعتها.

**تظهر تنسيقات التصدير الجديدة في Report Viewer أثناء التشغيل في الوضع المحلي** 

![todo:image_alt_text](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
