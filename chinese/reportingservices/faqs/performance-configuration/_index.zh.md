---
title: 性能配置
type: docs
weight: 20
url: /zh/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

用户可以在 **Aspose.Cells.ReportingServices.xml** 文件中配置一些属性和参数，以对性能进行优化。

{{% /alert %}} 
### **性能部分**
这显示了性能部分的默认内容。

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}
### **性能参数**
- LimitCellsNumberForMerged – 参数的默认值为1000000。参数值由客户端设置，不受性能参数开关的影响。请参阅以下配置。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – 可以为true或false： 
  - 当Performance参数设置为'off'时，默认值为false。
  - 当Performance参数设置为'on'时，默认值为true。
  - 当Performance参数设置为'on'时，子元素报表可以重新设置报表的AutoRowFile参数。
    请参考以下配置。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    	<Report name="Test">

      	<AutoRowFit value="False"/>

      	<SetStyle value="True"/>

      	<Merged value="True"/>

      	<ConditionalFormatting value="True"/>

      	</Report>

</Performance>



{{< /highlight >}}

- IsMerged – 可以为true或false： 
  - 当Performance参数设置为'off'时，默认值为false。
  - 当Performance参数设置为'on'时，默认值为true。
  - 当Performance参数设置为'on'时，子元素报表可以重新设置报表的AutoRowFile参数。
    请参考以下配置。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

- IsSetStyle – 可以设置为true或false: 
  - 当Performance参数设置为'off'时，默认值为false。
  - 当Performance参数设置为'on'时，默认值为true。
  - 当Performance参数设置为'on'时，子元素报表可以重新设置报表的AutoRowFile参数。
    请参考以下配置。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

- IsConditionalFormatting – 可以设置为true或false: 
  - 当Performance参数设置为'off'时，默认值为false。
  - 当Performance参数设置为'on'时，默认值为true。
  - 当Performance参数设置为'on'时，子级元素报表可以重新设置点报表的AutoRowFile参数。
  - 当IsSetStyle参数设置为false时，Performance参数的值无效。
    请参考以下配置。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

</Performance>



{{< /highlight >}}
