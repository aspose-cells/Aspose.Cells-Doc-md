---
title: 性能配置
type: docs
weight: 20
url: /zh/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

用户可以在一定程度上优化性能。您可以在中配置一些属性和参数**Aspose.Cells.ReportingServices.xml**文件如下所述。

{{% /alert %}} 
### **表演部分**
这显示了默认情况下的性能部分。

**XML**

{{< highlight "csharp" >}}

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
- LimitCellsNumberForMerged – 该参数的默认值为1000000。该参数值由客户端设置，不受性能参数开关的影响。请参考以下配置。

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit – 可以是 true 或 false：
 - 当 Performance 参数设置为“off”时，默认值为 false。
 - 当 Performance 参数设置为“on”时，默认值为 true。
 - 当 Performance 参数设置为“on”时，子元素报表可以重新设置报表的 AutoRowFile 参数。
请参考以下配置。

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    	<Report name="Test">

      	<AutoRowFit value="False"/>

      	<SetStyle value="True"/>

      	<Merged value="True"/>

      	<ConditionalFormatting value="True"/>

      	</Report>

</Performance>



{{< /highlight >}}

-  IsMerged – 可以是 true 或 false：
 - 当 Performance 参数设置为“off”时，默认值为 false。
 - 当 Performance 参数设置为“on”时，默认值为 true。
 - 当 Performance 参数设置为“on”时，子元素报表可以重新设置报表的 AutoRowFile 参数。
请参考以下配置。

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

-  IsSetStyle – 可以是 true 或 false：
 - 当 Performance 参数设置为“off”时，默认值为 false。
 - 当 Performance 参数设置为“on”时，默认值为 true。
 - 当 Performance 参数设置为“on”时，子元素报表可以重新设置报表的 AutoRowFile 参数。
请参考以下配置。

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

</Performance>



{{< /highlight >}}

-  IsConditionalFormatting – 可以是 true 或 false：
 - 当 Performance 参数设置为“off”时，默认值为 false。
 - 当 Performance 参数设置为“on”时，默认值为 true。
 - 当 Performance 参数设置为 'on' 时，子元素报告可以重新设置点报告的 AutoRowFile 参数。
 - 当 IsSetStyle 参数设置为 false 时，Performance 参数的值无效。
请参考以下配置。

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

</Performance>



{{< /highlight >}}
