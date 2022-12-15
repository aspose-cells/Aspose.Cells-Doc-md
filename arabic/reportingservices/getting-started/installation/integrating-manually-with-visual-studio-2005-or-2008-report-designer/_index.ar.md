---
title: التكامل يدويًا مع Visual Studio 2005 أو 2008 Report Designer
type: docs
weight: 30
url: /ar/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

يرجى تنفيذ الخطوات التالية بالترتيب إذا كنت تريد تثبيت Aspose.Cells for Reporting Services يدويًا لـ Microsoft Visual Studio Report Designer ، بدون مثبت MSI. نوصيك باستخدام مثبّت MSI لأنه يقوم بتنفيذ جميع عمليات التثبيت والتكوين اللازمة تلقائيًا. ومع ذلك ، إذا فشلت في التثبيت باستخدام مثبّت MSI ، فيرجى اتباع الإرشادات التالية.
 يصف هذا القسم كيفية تثبيت Aspose.Cells for Reporting Services على جهاز كمبيوتر مع Business Intelligence Development Studio. سيمكنك هذا من تصدير التقارير إلى تنسيقات Microsoft Excel في وقت التصميم من Microsoft Visual Studio 2005 أو 2008 Report Designer.

{{% /alert %}} 
- **عملية التكامل**
1.  ينسخ**Aspose.Cells.ReportingServices.dll** إلى دليل Visual Studio.
 1. للتكامل مع Visual Studio 2005 Report Designer: نسخة**Aspose.Cells.ReportingServices.dll** إلى الدليل C: \ Program Files \ Microsoft Visual Studio 8 \ Common7 \ IDE \ PrivateAssemblies Directory.
 1. للتكامل مع Visual Studio 2008 Report Designer: نسخة**Aspose.Cells.ReportingServices.dll**إلى الدليل C: \ Program Files \ Microsoft Visual Studio 9.0 \ Common7 \ IDE \ PrivateAssemblies Directory.
1.  تسجيل Aspose.Cells for Reporting Services كامتداد تصيير:
 1. فتح**C: \ Program Files \ Microsoft Visual Studio <الإصدار> \ Common7 \ IDE \ PrivateAssemblies \ RSReportDesigner.config** 
 (أين<Version> هو "8" لبرنامج Visual Studio 2005 أو "9.0" لبرنامج Visual Studio 2008) وأضف الأسطر التالية إلى ملف<Render> عنصر:

**XML**

{{< highlight "csharp" >}}

 <Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />



{{< /highlight >}}

1.  امنح Aspose.Cells for Reporting Services أذونات للتنفيذ:
 1. افتح C: \ Program Files \ Microsoft Visual Studio<Version>\ Common7 \ IDE \ PrivateAssemblies \ RSPreviewPolicy.config
 (أين<Version> هو "8" لبرنامج Visual Studio 2005 أو "9.0" لبرنامج Visual Studio 2008) وأضف ما يلي كعنصر أخير في العنصر الثاني إلى الخارجي<CodeGroup> العنصر (الذي يجب أن يكون<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

**XML**

{{< highlight "csharp" >}}

 <CodeGroup>

  ...

  <CodeGroup>

    ...

    <!--Start here.-->

   <CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust" Name="Aspose.Cells_for_Reporting_Services" Description="This code group grants full trust to the Aspose.Cells for Reporting Services assembly.">

                <IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001002780c08eaa89aedfb00b1b96137cca3e15f32826e0e4fd1da3c98d1e3968a03a019aa7b7228b151f6e5dae4dcb00f98479770f507626b04e786e5e93ec3757c1cc4ed1ac4b72c7649c4438e9d3a5f44d8b7522043686a2e8c2a495e04b917e0505d3201015c828e3c15afc8a46ab78293574b9e0475df68627bbabc5b564addd" />

              </CodeGroup> 

    <!--End here.-->

  </CodeGroup>

</CodeGroup>



{{< /highlight >}}

1.  تحقق من تثبيت Aspose.Cells for Reporting Services بنجاح:
 1. قم بتشغيل أو إعادة تشغيل Microsoft Visual Studio 2005 أو 2008 Report Designer.
 يجب أن تلاحظ تنسيقات جديدة متوفرة في قائمة تنسيقات التصدير.

**عند تسجيل المكون ، تظهر تنسيقات تصدير جديدة في "مصمم التقارير"** 

![ما يجب القيام به: image_بديل_نص](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
