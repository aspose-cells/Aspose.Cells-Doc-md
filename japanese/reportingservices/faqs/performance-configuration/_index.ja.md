---
title: パフォーマンス構成
type: docs
weight: 20
url: /ja/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

ユーザーはパフォーマンスをある程度最適化できます。で一部の属性とパラメータを構成できます。**Aspose.Cells.ReportingServices.xml**以下に説明するファイル。

{{% /alert %}} 
### **パフォーマンスセクション**
これは、デフォルトのパフォーマンス セクションを示しています。

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
### **性能パラメータ**
- LimitCellsNumberForMerged – パラメータのデフォルト値は 1000000 です。パラメータ値はクライアントによって設定され、パフォーマンス パラメータのスイッチの影響を受けません。以下の構成を参照してください。

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit – true または false のいずれかになります。
 - Performance パラメータが「off」に設定されている場合、デフォルト値は false です。
 - Performance パラメータが「on」に設定されている場合、デフォルト値は true です。
 - Performance パラメータが「on」に設定されている場合、サブ要素レポートはレポートの AutoRowFile パラメータを再設定できます。
以下の構成を参照してください。

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

-  IsMerged – true または false のいずれかになります。
 - Performance パラメータが「off」に設定されている場合、デフォルト値は false です。
 - Performance パラメータが「on」に設定されている場合、デフォルト値は true です。
 - Performance パラメータが「on」に設定されている場合、サブ要素レポートはレポートの AutoRowFile パラメータを再設定できます。
以下の構成を参照してください。

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

-  IsSetStyle – true または false のいずれかになります。
 - Performance パラメータが「off」に設定されている場合、デフォルト値は false です。
 - Performance パラメータが「on」に設定されている場合、デフォルト値は true です。
 - Performance パラメータが「on」に設定されている場合、サブ要素レポートはレポートの AutoRowFile パラメータを再設定できます。
以下の構成を参照してください。

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

- IsConditionalFormatting – true または false のいずれかになります。
 - Performance パラメータが「off」に設定されている場合、デフォルト値は false です。
 - Performance パラメータが「on」に設定されている場合、デフォルト値は true です。
 - パフォーマンス パラメーターが「オン」に設定されている場合、サブ要素レポートはポイント レポートの AutoRowFile パラメーターを再設定できます。
 - IsSetStyle パラメーターが false に設定されている場合、Performance パラメーターの値は無効です。
以下の構成を参照してください。

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
