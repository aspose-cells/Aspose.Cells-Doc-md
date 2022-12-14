---
title: Интеграция со средством просмотра отчетов Microsoft в локальном режиме
type: docs
weight: 30
url: /ru/reportingservices/integrate-with-microsoft-report-viewer-in-local-mode/
---
{{% alert color="primary" %}} 

Microsoft Средство просмотра отчетов — это мощный элемент управления .NET, который позволяет использовать отчеты RDL и RDLC в приложениях WinForms и ASP.NET. Это позволяет пользователям просматривать и экспортировать отчеты в различные форматы. Элемент управления входит в состав Microsoft Visual Studio 2005 и 2008, а также доступен для бесплатной загрузки с Microsoft.

Средство просмотра отчетов может создавать отчеты независимо, используя встроенный механизм (известный как «локальный режим»), или может отображать отчеты, созданные на сервере отчетов Microsoft SQL Server Reporting Services («удаленный режим»):

- В удаленном режиме средство просмотра отчетов может экспортировать отчеты во все форматы, установленные на сервере отчетов, к которому оно подключено. Таким образом, чтобы экспортировать отчеты в другие форматы Microsoft Excel, вам нужно всего лишь установить Aspose.Cells для служб Reporting Services на сервере.
- Однако в локальном режиме средство просмотра отчетов не подключается к серверу отчетов, а список форматов экспорта ограничен лишь несколькими встроенными форматами.

 Установив Aspose.Cells для служб Reporting Services на компьютере для разработки и выполнив описанные ниже шаги, вы сможете экспортировать в другие форматы Excel Microsoft из средства просмотра отчетов, работающего в локальном режиме.

{{% /alert %}} 
### **Работа с Aspose.Cells в локальном режиме**
1.  Ссылка**Aspose.Cells.ReportingServices.dll** в проекте:
 1. Откройте проект в Visual Studio.
 1. Щелкните правой кнопкой мыши**использованная литература** папку и выберите**Добавить ссылку**.
 1. Выберите**Просматривать** вкладку и перейдите к следующей сборке:
      <InstallDir>/ReportView/Aspose.Cells.ReportingServices.dll
 (куда<InstallDir> — это каталог, в который вы установили или распаковали Aspose.Cells для служб Reporting Services.

      **Добавление ссылки на Aspose.Cells.ReportingServices.dll в проект** 

![дело:изображение_альтернативный_текст](integrate-with-microsoft-report-viewer-in-local-mode_1.png)




1. Скопируйте и вставьте в проект следующий метод AddExtension.
 Этот метод добавляет указанное расширение отрисовки в список поддерживаемых расширений в средстве просмотра отчетов Microsoft с использованием закрытого отражения.

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




**ВБ .NET**

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

1.  Вызовите метод AddExtension из кода.
 - Вы можете вызывать AddExtension (показано на предыдущем шаге), когда вам нужно добавить Aspose.Cells для форматов экспорта служб Reporting Services в экземпляр элемента управления средства просмотра отчетов. Рассмотрите возможность вызова из формы_Загрузить или Страница_Загрузить обработчик событий приложения WinForms или ASP .NET.
 - Вы можете добавить все или только некоторые экспортные форматы Aspose.Cells для служб Reporting Services. Вы можете указать любое отображаемое имя для форматов, которые будут отображаться в средстве просмотра отчетов.
 Чтобы добавить Aspose.Cells для форматов экспорта служб Reporting Services в средство просмотра отчетов Microsoft в локальном режиме, используйте следующий код:

**C#**

{{< highlight "csharp" >}}



            AddExtension(reportViewer1, "Xls - Xls via Aspose.Cells",    typeof(Aspose.Cells.ReportingServices.XlsRenderer));

            AddExtension(reportViewer1, "Xlsx - Xlsx via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.Excel2007XlsxRenderer));

			AddExtension(reportViewer1, "CSV - CSV via Aspose.Cells",    typeof(Aspose.Cells.ReportingServices.CSVRenderer));

            AddExtension(reportViewer1, "SpreadsheetML - SpreadsheetML via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.SpreadsheetMLRenderer));

            AddExtension(reportViewer1, "Txt - TabDelimited text via Aspose.Cells", typeof(Aspose.Cells.ReportingServices.TabDelimitedRenderer)); 



{{< /highlight >}}

**ВБ .NET**

{{< highlight "csharp" >}}

              AddExtension(reportViewer1, "Xls - Xls via Aspose.Cells",    GetType (Aspose.Cells.ReportingServices.XlsRenderer));

            AddExtension(reportViewer1, "Xlsx - Xlsx via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.Excel2007XlsxRenderer));

			AddExtension(reportViewer1, "CSV - CSV via Aspose.Cells",    GetType (Aspose.Cells.ReportingServices.CSVRenderer));

            AddExtension(reportViewer1, "SpreadsheetML - SpreadsheetML via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.SpreadsheetMLRenderer));

            AddExtension(reportViewer1, "Txt - TabDelimited text via Aspose.Cells", GetType (Aspose.Cells.ReportingServices.TabDelimitedRenderer));



{{< /highlight >}}

1.  Протестируйте новые форматы экспорта.
1. Запустите ваше приложение.
 Вы должны заметить ряд новых форматов экспорта, доступных в**Экспорт** меню в средстве просмотра отчетов.
 1. Выберите один из форматов и запустите экспорт.
 1. Убедитесь, что документ создан так, как вы ожидали.

**Новые форматы экспорта появляются в средстве просмотра отчетов, работающем в локальном режиме.** 

![дело:изображение_альтернативный_текст](integrate-with-microsoft-report-viewer-in-local-mode_2.png)
