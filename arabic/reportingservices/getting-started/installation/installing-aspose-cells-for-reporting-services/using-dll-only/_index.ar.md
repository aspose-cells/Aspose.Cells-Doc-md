---
title: باستخدام DLL فقط
type: docs
weight: 20
url: /ar/reportingservices/using-dll-only/
---
## كيفية تثبيت Aspose.Cells لخدمات التقارير باستخدام DLL فقط:

-  قم بزيارة Aspose.Cells لخدمات التقارير[صفحة التحميل](https://downloads.aspose.com/cells/reportingservices) وتنزيل ملف**Aspose.Cells لخدمات التقارير (الرمز البريدي)** أرشيف يحتوي على أحدث إصدار من المكون والوثائق المثبتة.
 - توجد 7 أنواع من الإصدارات Aspose.Cells.ReprotingSerivces.dll في Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. أنها تدعم منتجات خادم تقرير Microsoft مختلفة.
 - Aspose.Cells.ReportingServices.dll في مجلد SSRS2005 يدعم Microsoft SQL Server 2005 Reporting Services.
 - Aspose.Cells.ReportingServices.dll في مجلد SSRS2008 يدعم Microsoft SQL Server 2008 Reporting Services.
 - Aspose.Cells.ReportingServices.dll في مجلد SSRS2008R2 يدعم Microsoft SQL Server 2008R2 / 2012/2014 Reporting Services.
 Aspose.Cells.ReportingServices.dll في مجلد SSRS2016 يدعم Microsoft SQL Server 2016/2017/2019 Reporting Services.
   
- قم بفك ضغط الأرشيف في دليل على محرك الأقراص الثابتة.

- قم بتثبيت Aspose.Cells لـ Reporting Services Report Designer:
 - يسجل**Aspose.Cells.ReportingServices.Client.dll** باستخدام الأداة المساعدة Regasm.exe.
 - إضافة Aspose.Cells للوظيفة الإضافية Reporting Services في Excel.
   
- قم بتثبيت Aspose.Cells لخدمات التقارير لـ Microsoft SQL Server Reporting Services ، مكون الخدمات:
 - ضع ال**Aspose.Cells.ReportingServices.dll** في مجلد التثبيت $ {Microsoft SQL Server Reporting Services} \ ReportServer \ bin.
 - إضافة Aspose.Cells لملحقات عارض خدمات التقارير:
 - فتح**مجلد تثبيت خدمات تقرير خادم SQL $ {Microsoft} \ ReportServer \ rsreportserver.config**
 - أضف الأسطر التالية إلى ملف<Render>……</Render> عنصر:
{{< highlight "xml" >}}

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
 - إضافة Aspose.Cells لتصاريح خدمات التقارير للتنفيذ:
 - فتح**مجلد تثبيت خدمات تقرير خادم SQL $ {Microsoft} \ ReportServer \ rssrvpolicy.config** و أ
 - يضاف التالي كعنصر أخير في الثاني إلى الخارج<CodeGroup> العنصر (الذي يجب أن يكون<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight "xml" >}}

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

## تحقق من تثبيت Aspose.Cells لـ Reporting Services بنجاح:
 1. افتح "إدارة التقارير" وتحقق من قائمة أنواع التصدير المتوفرة لتقرير. (قم بتشغيل Report Manager عن طريق فتح مستعرض واكتب عنوان URL الخاص بـ Report Manager في شريط العناوين. (افتراضيًا ، يكون عنوان URL هو http: //<ComputerName>/ تقارير).
 1. حدد أحد التقارير الموجودة على الخادم وافتح ملف**حدد التنسيق** قائمة.
 يجب أن تشاهد قائمة تنسيقات التصدير المقدمة بواسطة Aspose.Cells لخدمات التقارير.
 1. حدد**XLS - مصنف Excel عبر Aspose.Cells**.
 1. انقر فوق**يصدّر**.
 يتم إنشاء التقرير بالتنسيق المحدد.
 1. أرسلها إلى العميل وافتحها في التطبيق المناسب. في هذه الحالة ، يتم فتح التقرير في Microsoft Excel.

تهانينا ، لقد نجحت في تثبيت Aspose.Cells لخدمات التقارير وإنشاء تقرير كملف Microsoft Excel!


 هناك 7 أنواع من الإصدارات Aspose.Cells.ReprotingSerivces.dll في Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. أنها تدعم منتجات خادم تقرير Microsoft مختلفة.