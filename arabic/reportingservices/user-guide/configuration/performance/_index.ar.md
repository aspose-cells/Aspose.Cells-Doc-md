---
title: الأداء
type: docs
weight: 30
url: /ar/reportingservices/performance/
---

لتحسين الأداء، قم بتعيين معلمة الأداء إلى **ON**.

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

    <AutoRowFit value="True"/>

    <SetStyle value="True"/>

    <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}

معلمات الأداء المختلفة على النحو التالي:

- **LimitCellsNumberForMerged**: الحد الأقصى لعدد الخلايا التي يمكن دمجها. القيمة الافتراضية 1،000،000. تعيين قيمة المعلمة من قبل المستخدم ولا تتأثر بمفتاح معلمة الأداء. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: عندما تكون قيمة الأداء **off**، تكون قيمة IsAutoRowFit **false** افتراضيًا. عندما تكون قيمة معلمة الأداء **on**، تكون القيمة **true** افتراضيًا. عندما تكون قيمة معلمة الأداء **on**، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="Test">

      <AutoRowFit value="False"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsMerged**: عندما تكون قيمة الأداء **off**، تكون القيمة الافتراضية لـ IsMerged **false**. عندما تكون قيمة معلمة الأداء **on**، تكون القيمة الافتراضية **true**. عندما تكون قيمة معلمة الأداء **on**، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsSetStyle**: عندما تكون قيمة الأداء **off**، تكون القيمة الافتراضية **false**. عندما تكون معلمة الأداء **on**، تكون القيمة الافتراضية **true**. أيضًا، عندما تكون معلمة الأداء **on**، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit. 

{{< highlight java >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **IsConditionalFormatting**: عندما تكون قيمة الأداء **off**، تكون القيمة الافتراضية **false**. عندما تكون معلمة الأداء **on**، تكون القيمة الافتراضية **true**. أيضًا، عندما تكون معلمة الأداء **on**، يمكن لتقرير العنصر الفرعي إعادة تعيين تقرير النقطة إلى قيمة AutoRowFit. عندما يكون قيمة IsSetStyle **false**، فإن قيمة الأداء غير صالحة. 

{{< highlight java >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

   </Performance>

{{< /highlight >}}
