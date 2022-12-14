---
title: 表现
type: docs
weight: 30
url: /zh/reportingservices/performance/
---
要提高性能，请将性能参数设置为**上**.

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

各项性能参数如下：

- **LimitCellsNumberForMerged** ：可以合并的最大单元格数。默认值 1,000,000。参数值由用户设定，不受性能参数切换的影响。

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** ：当 Performance 的值为**离开** IsAutoRowFit 的值为**错误的**默认。当性能参数的值为**上** 值为**真的**默认。当 Performance 的值为**上**，子元素报告可以将点报告重置为 AutoRowFit 值。

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




- **已合并** ：当 Performance 的值为**离开** IsMerged 默认值为**错误的**.当 Performance 的值为**上**，默认值为**真的**.当 Performance 参数的值为**上**，子元素报告可以将点报告重置为 AutoRowFit 值。

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




- **设置样式** ：当 Performance 的值为**离开**，默认值为**错误的**.当性能是**上**，默认值为**真的**.此外，当性能是**上**，子元素报告可以将点报告重置为 AutoRowFit 值。

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




- **是条件格式**：当性能是**离开**，默认值为**错误的**.当性能是**上**，默认值为**真的**.此外，当性能是**上**，子元素报告可以将点报告重置为 AutoRowFit 值。当 IsSetStyle 参数值设置为**错误的** Performance 的值无效。

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
