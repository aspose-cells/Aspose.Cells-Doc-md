---
title: 性能配置
type: docs
weight: 20
url: /zh/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

用户可以在一定程度上优化性能。可以在**Aspose.Cells.ReportingServices.xml**文件中配置一些属性和参数，如下所述。

{{% /alert %}} 
### **性能部分**
以下是默认的性能部分配置。

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
- LimitCellsNumberForMerged - 参数的默认值为1000000。该参数的值由客户端设置，不受性能参数开关的影响。请参考以下配置。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit - 可以是true或false： 
  - 当Performance参数设为‘关’时，默认值为false。
  - 当Performance参数设为‘开’时，默认值为true。
  - 当Performance参数设为‘开’时，子元素报告可以重设报告的AutoRowFile参数。
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

- IsMerged - 可以是true或false： 
  - 当Performance参数设为‘关’时，默认值为false。
  - 当Performance参数设为‘开’时，默认值为true。
  - 当Performance参数设为‘开’时，子元素报告可以重设报告的AutoRowFile参数。
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

- IsSetStyle - 可以是true或false： 
  - 当Performance参数设为‘关’时，默认值为false。
  - 当Performance参数设为‘开’时，默认值为true。
  - 当Performance参数设为‘开’时，子元素报告可以重设报告的AutoRowFile参数。
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

- IsConditionalFormatting – 可以是true或false： 
  - 当Performance参数设为‘关’时，默认值为false。
  - 当Performance参数设为‘开’时，默认值为true。
  - 当Performance参数设为‘开’时，子元素报告可以重设点报告的AutoRowFile参数。
  - 当IsSetStyle参数设为false时，Performance参数的值无效。
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
