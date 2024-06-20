---
title: Производительность
type: docs
weight: 30
url: /ru/reportingservices/performance/
---

Чтобы улучшить производительность, установите параметр Производительность на **ON**.

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

Различные параметры производительности следующие:

- **LimitCellsNumberForMerged**: максимальное количество ячеек, которые можно объединить. Значение по умолчанию 1,000,000. Значение параметра задается пользователем и не зависит от коммутатора параметра производительности. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: Когда значение Производительность **off**, значение IsAutoRowFit по умолчанию **false**. Когда значение параметра производительности **on**, значение по умолчанию **true**. Когда значение Производительность **on**, вложенный отчет может сбросить точки отчета на значение AutoRowFit. 

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




- **IsMerged**: Когда значение Производительность **off**, значение IsMerged по умолчанию **false**. Когда значение Производительность **on**, значение по умолчанию **true**. Когда значение параметра производительности **on**, вложенный отчет может сбросить точечный отчет на значение AutoRowFit. 

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




- **IsSetStyle**: Когда значение Производительность **off**, значение по умолчанию **false**. Когда значение Производительность **on**, значение по умолчанию **true**. Также, когда значение Производительность **on**, вложенный отчет может сбросить точечный отчет на значение AutoRowFit. 

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




- **IsConditionalFormatting**: Когда Производительность **off**, значение по умолчанию **false**. Когда Производительность **on**, значение по умолчанию **true**. Также, когда Производительность **on**, вложенный отчет может сбросить точечный отчет на значение AutoRowFit. Когда значение параметра IsSetStyle установлено в **false**, значение Производительность не действительно. 

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
