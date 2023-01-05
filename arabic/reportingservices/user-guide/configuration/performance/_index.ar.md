---
title: أداء
type: docs
weight: 30
url: /ar/reportingservices/performance/
---
 لتحسين الأداء ، قم بتعيين معلمة الأداء إلى**تشغيل**.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

    <AutoRowFit value="True"/>

    <SetStyle value="True"/>

    <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}

معلمات الأداء المختلفة هي كما يلي:

- **LimitCellsNumberForMerged** : الحد الأقصى لعدد الخلايا التي يمكن دمجها. القيمة الافتراضية 1،000،000. يتم تعيين قيمة المعلمة من قبل المستخدم ولا تتأثر بمفتاح معلمة الأداء.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : عندما تكون قيمة الأداء**إيقاف** ، قيمة IsAutoRowFit هي**خاطئة** بشكل افتراضي. عندما تكون قيمة معلمة الأداء**تشغيل** ، القيمة**حقيقي** بشكل افتراضي. عندما تكون قيمة الأداء**تشغيل** ، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="Test">

      <AutoRowFit value="False"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **هو دمج** : عندما تكون قيمة الأداء**إيقاف** ، القيمة الافتراضية IsMerged هي**خاطئة** . عندما تكون قيمة الأداء**تشغيل** ، النظام الأساسي**حقيقي** . عندما تكون قيمة معلمة الأداء**تشغيل** ، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsSetStyle** : عندما تكون قيمة الأداء**إيقاف** ، النظام الأساسي**خاطئة** . عندما يكون الأداء**تشغيل** ، النظام الأساسي**حقيقي** . أيضا ، عندما يكون الأداء**تشغيل** ، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit.

{{< highlight "java" >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **تنسيق مشروط** : عندما يكون الأداء**إيقاف** ، النظام الأساسي**خاطئة** . عندما يكون الأداء**تشغيل** ، النظام الأساسي**حقيقي** . أيضا ، عندما يكون الأداء**تشغيل** ، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit. عندما يتم تعيين قيمة المعلمة IsSetStyle على**خاطئة** ، فإن قيمة الأداء غير صالحة.

{{< highlight "java" >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

   </Performance>

{{< /highlight >}}
