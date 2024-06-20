---
title: パフォーマンスの構成
type: docs
weight: 20
url: /ja/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

ユーザーは一定の範囲でパフォーマンスを最適化できます。以下で説明するように、**Aspose.Cells.ReportingServices.xml**ファイルでいくつかの属性とパラメータを構成できます。

{{% /alert %}} 
### **パフォーマンスセクション**
これはデフォルトのパフォーマンスセクションを示します。

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
### **パフォーマンスパラメータ**
- 結合セルの数を制限 - パラメータのデフォルト値は1000000です。パラメータの値はクライアントによって設定され、パフォーマンスパラメータのスイッチに影響を受けません。以下の構成を参照してください。 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- 自動行のフィットが可能か - trueまたはfalseにできます。 
  - パフォーマンスパラメータが「オフ」に設定されているとき、デフォルトの値はfalseです。
  - パフォーマンスパラメータが「オン」に設定されているとき、デフォルトの値はtrueです。
  - パフォーマンスパラメータが「オン」に設定されているとき、サブエレメントレポートはレポートのAutoRowFileパラメータを再設定できます。
    以下の構成を参照してください。 

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

- 結合されているか - trueまたはfalseにできます。 
  - パフォーマンスパラメータが「オフ」に設定されているとき、デフォルトの値はfalseです。
  - パフォーマンスパラメータが「オン」に設定されているとき、デフォルトの値はtrueです。
  - パフォーマンスパラメータが「オン」に設定されているとき、サブエレメントレポートはレポートのAutoRowFileパラメータを再設定できます。
    以下の構成を参照してください。 

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

- スタイルを設定するか - trueまたはfalseにできます。 
  - パフォーマンスパラメータが「オフ」に設定されているとき、デフォルトの値はfalseです。
  - パフォーマンスパラメータが「オン」に設定されているとき、デフォルトの値はtrueです。
  - パフォーマンスパラメータが「オン」に設定されているとき、サブエレメントレポートはレポートのAutoRowFileパラメータを再設定できます。
    以下の構成を参照してください。 

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

- 条件付き書式が可能か - trueまたはfalseにできます。 
  - パフォーマンスパラメータが「オフ」に設定されているとき、デフォルトの値はfalseです。
  - パフォーマンスパラメータが「オン」に設定されているとき、デフォルトの値はtrueです。
  - パフォーマンスパラメータが「オン」に設定されているとき、サブエレメントレポートはレポートのAutoRowFileパラメータを再設定できます。
  - IsSetStyleパラメータがfalseに設定されているとき、パフォーマンスパラメータの値は無効です。
    以下の構成を参照してください。 

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
