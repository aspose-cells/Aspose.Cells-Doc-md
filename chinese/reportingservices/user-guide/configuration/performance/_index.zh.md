---
title: 性能
type: docs
weight: 30
url: /zh/reportingservices/performance/
---

要提高性能，请将性能参数设置为 **ON**。

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

- **LimitCellsNumberForMerged**：可以合并的单元格的最大数量。默认值为 1,000,000。参数值由用户设置，不受性能参数开关影响。 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**：当 Performance 的值为 **off** 时，默认情况下 IsAutoRowFit 的值为 **false**。当性能参数的值为 **on** 时，默认情况下该值为 **true**。当 Performance 的值为 **on** 时，一个子元素报告可以重新设置点报告到 AutoRowFit 值。 

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




- **IsMerged**：当 Performance 的值为 **off** 时，IsMerged 默认值为 **false**。当 Performance 的值为 **on** 时，默认值为 **true**。当性能参数的值为 **on** 时，一个子元素报告可以重新设置点报告到 AutoRowFit 值。 

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




- **IsSetStyle**：当 Performance 的值为 **off** 时，默认值为 **false**。当 Performance 的值为 **on** 时，默认值为 **true**。此外，当 Performance 的值为 **on** 时，一个子元素报告可以重新设置点报告到 AutoRowFit 值。 

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




- **IsConditionalFormatting**：当 Performance 的值为 **off** 时，默认值为 **false**。当 Performance 的值为 **on** 时，默认值为 **true**。此外，当 Performance 的值为 **on** 时，一个子元素报告可以重新设置点报告到 AutoRowFit 值。当 IsSetStyle 参数值设置为 **false** 时，性能的值无效。 

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
