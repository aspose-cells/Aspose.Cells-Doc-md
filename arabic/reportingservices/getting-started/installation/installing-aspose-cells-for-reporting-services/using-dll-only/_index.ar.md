---
title: استخدام DLL فقط
type: docs
weight: 20
url: /ar/reportingservices/using-dll-only/
---

## كيفية تثبيت Aspose.Cells for Reporting Services باستخدام ملف DLL فقط:

- قم بزيارة صفحة التنزيل الخاصة بـ Aspose.Cells for Reporting Services (https://downloads.aspose.com/cells/reportingservices) وقم بتنزيل الأرشيف **Aspose.Cells for Reporting Services (zip)** الذي يحتوي على أحدث إصدار من المكون والوثائق المثبتة.
   - هناك 7 أنواع من نسخ Aspose.Cells.ReprotingSerivces.dll في Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. تدعم منتجات خادم تقارير Microsoft المختلفة.
       - Aspose.Cells.ReportingServices.dll في مجلد SSRS2005 تدعم Microsoft SQL Server 2005 Reporting Services.
       - Aspose.Cells.ReportingServices.dll في مجلد SSRS2008 تدعم Microsoft SQL Server 2008 Reporting Services.
       - Aspose.Cells.ReportingServices.dll في مجلد SSRS2008R2 تدعم Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
       - Aspose.Cells.ReportingServices.dll في مجلد SSRS2016 تدعم Microsoft SQL Server 2016/2017/2019 Reporting Services.

- قم بفك الأرشيف إلى دليل على القرص الصلب الخاص بك.

- قم بتثبيت مصمم تقارير Aspose.Cells for Reporting Services:
   - سجّل **Aspose.Cells.ReportingServices.Client.dll** باستخدام أداة Regasm.exe.
   - أضف إضافة Aspose.Cells for Reporting Services في Excel.

- قم بتثبيت Aspose.Cells for Reporting Services لخدمة تقارير Microsoft SQL Server:
   - ضع **Aspose.Cells.ReportingServices.dll** في مجلد التثبيت ${مجلد تثبيت Microsoft SQL Server Reporting Services}\ReportServer\bin. 
   - قم بإضافة ملحقات منظم Aspose.Cells for Reporting Services :  
      - افتح **${مجلد تثبيت خدمات تقارير Microsoft SQL Server}\ReportServer\rsreportserver.config**
      - Add the following lines into the <Render>……</Render> element: 
{{< highlight xml >}}

 <Render>

...

<!--Start here.-->

<Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX(Data Only)" Type="Aspose.Cells.ReportingServices.Excel2007SimpleXlsxRenderer,Aspose.Cells.ReportingServices"/>

<Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXPS" Type="Aspose.Cells.ReportingServices.XpsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACMD" Type="Aspose.Cells.ReportingServices.MarkdownRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTIFF" Type="Aspose.Cells.ReportingServices.TIFFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPDF" Type="Aspose.Cells.ReportingServices.PDFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPNG" Type="Aspose.Cells.ReportingServices.PNGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJPG" Type="Aspose.Cells.ReportingServices.JPGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACEMF" Type="Aspose.Cells.ReportingServices.EMFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACDIF" Type="Aspose.Cells.ReportingServices.DifRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACSVG" Type="Aspose.Cells.ReportingServices.SvgRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJSON" Type="Aspose.Cells.ReportingServices.JsonRenderer,Aspose.Cells.ReportingServices" />
<!--End here.-->

</Render>

{{< /highlight >}}
   - أضف أذونات Aspose.Cells for Reporting Services للتشغيل:
      - افتح **${مجلد تثبيت خدمات تقارير Microsoft SQL Server}\ReportServer\rssrvpolicy.config** و
      - Add the following as the last item in the second to the outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight xml >}}

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

## تحقق من نجاح تثبيت Aspose.Cells for Reporting Services:
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. حدد أحد التقارير على الخادم وافتح قائمة **اختيار التنسيق**.
      يجب أن ترى قائمة تنسيقات التصدير المقدمة من قبل Aspose.Cells for Reporting Services.
   1. حدد **XLS – دفتر عمل إكسل عبر Aspose.Cells**.
   1. انقر على **تصدير**.
      يتم إنشاء التقرير في التنسيق المحدد.
   1. أرسله إلى العميل وافتحه في تطبيق مناسب. في هذه الحالة، يتم فتح التقرير في Microsoft Excel.

تهانينا، لقد قمت بتثبيت Aspose.Cells for Reporting Services بنجاح وأنشأت تقرير كملف Microsoft Excel!


هناك 7 أنواع من إصدارات Aspose.Cells.ReprotingSerivces.dll في Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. تدعم منتجات خوادم التقارير المختلفة من Microsoft. 
