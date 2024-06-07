---
title: 性能
type: docs
weight: 30
url: /zh/reportingservices/performance/
---

为了改善性能，将性能参数设置为 **ON**。

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

各种性能参数如下：

- **LimitCellsNumberForMerged**：可以合并的最大单元格数。默认值为 1,000,000。参数值由用户设置，不受性能参数开关影响。 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**：当性能值为 **off** 时，默认值为 **false**。当性能参数值为 **on** 时，默认值为 **true**。当性能值为 **on** 时，子元素报告可以将点报告重置为 AutoRowFit 值。 

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




- **IsMerged**：当性能值为 **off** 时，IsMerged 默认值为 **false**。当性能值为 **on** 时，默认值为 **true**。当性能参数值为 **on** 时，子元素报告可以将点报告重置为 AutoRowFit 值。 

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




- **IsSetStyle**：当性能值为 **off** 时，默认值为 **false**。当性能为 **on** 时，默认值为 **true**。此外，当性能为 **on** 时，子元素报告可以将点报告重置为 AutoRowFit 值。 

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




- **IsConditionalFormatting**：当性能为 **off** 时，默认值为 **false**。当性能为 **on** 时，默认值为 **true**。此外，当性能为 **on** 时，子元素报告可以将点报告重置为 AutoRowFit 值。将 IsSetStyle 参数值设置为 **false** 时，性能值无效。 

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
