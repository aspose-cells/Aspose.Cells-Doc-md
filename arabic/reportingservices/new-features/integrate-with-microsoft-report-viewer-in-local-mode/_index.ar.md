---
title: التكامل مع Microsoft عارض التقرير في الوضع المحلي
type: docs
weight: 30
url: /ar/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Report Viewer هو عنصر تحكم .NET قوي يسمح باستخدام تقارير RDL و RDLC في تطبيقات WinForms و ASP.NET. يتيح للمستخدمين عرض التقارير وتصديرها بتنسيقات مختلفة. تم تضمين عنصر التحكم مع Microsoft Visual Studio 2005 و 2008 ، وهو متاح أيضًا للتنزيل المجاني من Microsoft.

يمكن لـ Report Viewer إنشاء تقارير بشكل مستقل باستخدام محرك مضمن (يُعرف باسم "الوضع المحلي") ، أو يمكنه عرض التقارير التي تم إنشاؤها على خادم تقرير خدمات تقارير خادم SQL Microsoft ("الوضع البعيد"):

- في الوضع البعيد ، يمكن لـ Report Viewer تصدير التقارير إلى جميع التنسيقات المثبتة على Report Server المتصل به. لذلك ، لتصدير التقارير إلى المزيد من تنسيقات Excel Microsoft ، ما عليك سوى تثبيت Aspose.Cells لـ Reporting Services على الخادم.
- ومع ذلك ، في الوضع المحلي ، لا يتصل عارض التقرير بخادم التقارير وقائمة تنسيقات التصدير تقتصر على عدد قليل من التنسيقات المضمنة.

 بتثبيت Aspose.Cells Reporting Services على جهاز تطوير واتباع الخطوات التالية ، يمكنك التصدير إلى المزيد من تنسيقات Excel Microsoft من عارض التقارير التي تعمل في الوضع المحلي.

{{% /alert %}} 
### **العمل مع Aspose.Cells في الوضع المحلي**
1.  المرجعي**Aspose.Cells.ReportingServices.dll** في المشروع:
 1. افتح المشروع في Visual Studio.
 1. انقر بزر الماوس الأيمن فوق ملف**مراجع** مجلد وحدد**يضيف مرجعا**.
 1. حدد ملف**تصفح** علامة التبويب واستعرض التجميع التالي:
      <InstallDir>/ ReportView / Aspose.Cells.ReportingServices.dll
 (أين<InstallDir> هو الدليل حيث قمت بتثبيت Aspose.Cells أو فك حزمه لخدمات التقارير.

      **إضافة مرجع إلى Aspose.Cells.ReportingServices.dll إلى مشروع** 

![ما يجب القيام به: image_بديل_نص](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. انسخ والصق طريقة AddExtension التالية في المشروع.
 تضيف هذه الطريقة امتداد العرض المحدد إلى قائمة الامتدادات المدعومة في Microsoft Report Viewer باستخدام الانعكاس الخاص.

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

1.  استدعاء الأسلوب AddExtension من التعليمات البرمجية.
 - يمكنك استدعاء AddExtension (كما هو موضح في الخطوة السابقة) متى احتجت إلى إضافة Aspose.Cells لتنسيقات تصدير Reporting Services إلى مثيل عنصر تحكم عارض التقارير. ضع في اعتبارك الاتصال من النموذج_تحميل أو صفحة_تحميل معالج الحدث لتطبيق WinForms أو ASP .NET.
 - يمكنك إضافة كل أو بعض الصادرات Aspose.Cells فقط لتنسيقات تصدير Reporting Services. يمكنك تحديد أي اسم عرض للتنسيقات لتظهر في عارض التقارير.
 لإضافة Aspose.Cells لتنسيقات تصدير Reporting Services إلى Microsoft Report Viewer في الوضع المحلي ، استخدم الكود التالي:

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

1.  اختبر تنسيقات التصدير الجديدة.
1. قم بتشغيل التطبيق الخاص بك.
 يجب أن تلاحظ عددًا من تنسيقات التصدير الجديدة المتوفرة في ملف**يصدّر** القائمة في عارض التقرير.
 1. حدد أحد التنسيقات وقم بتشغيل التصدير.
 1. تحقق من إنشاء المستند بالطريقة التي تتوقعها.

**تظهر تنسيقات التصدير الجديدة في عارض التقارير قيد التشغيل في الوضع المحلي** 

![ما يجب القيام به: image_بديل_نص](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
