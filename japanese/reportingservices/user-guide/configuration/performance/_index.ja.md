---
title: パフォーマンス
type: docs
weight: 30
url: /ja/reportingservices/performance/
---

パフォーマンスを向上させるには、Performanceパラメータを**ON**に設定します。

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

様々なパフォーマンスパラメータは以下の通りです:

- **LimitCellsNumberForMerged**: 結合できるセルの最大数。デフォルト値は1,000,000です。パラメータ値はユーザーによって設定され、パフォーマンスパラメータスイッチの影響を受けません。 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: Performanceの値が**off**の場合、IsAutoRowFitの値はデフォルトで**false**です。Performanceパラメータの値が**on**の場合、デフォルトで**true**になります。 

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




- **IsMerged**: Performanceの値が**off**の場合、IsMergedのデフォルト値は**false**です。Performanceパラメータの値が**on**の場合、デフォルト値は**true**になります。 

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




- **IsSetStyle**: Performanceの値が**off**の場合、デフォルト値は**false**です。Performanceが**on**の場合、デフォルト値は**true**になります。また、Performanceが**on**の場合、サブエレメントレポートはAutoRowFit値をリセットできます。 

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




- **IsConditionalFormatting**: Performanceが**off**の場合、デフォルト値は**false**です。Performanceが**on**の場合、デフォルト値は**true**になります。また、Performanceが**on**の場合、サブエレメントレポートはAutoRowFit値をリセットできます。IsSetStyleパラメータの値が**false**に設定されている場合、Performanceの値は無効です。 

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
