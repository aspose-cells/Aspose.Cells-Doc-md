---
title: パフォーマンス
type: docs
weight: 30
url: /ja/reportingservices/performance/
---
パフォーマンスを向上させるには、Performance パラメータを**オン**.

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

さまざまなパフォーマンス パラメータは次のとおりです。

- **LimitCellsNumberForMerged** : 結合できるセルの最大数。デフォルト値は 1,000,000 です。パラメータ値はユーザーによって設定され、パフォーマンス パラメータの切り替えの影響を受けません。

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : Performance の値が**オフ**、IsAutoRowFit の値は**間違い**デフォルトで。パフォーマンスパラメータの値が**の上**、値は**真実**デフォルトで。パフォーマンスの値が**の上**、サブ要素レポートは、ポイント レポートを AutoRowFit 値にリセットできます。

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




- **IsMerged** : Performance の値が**オフ** 、IsMerged のデフォルト値は**間違い**.パフォーマンスの値が**の上**、デフォルト値は**真実**.パフォーマンスパラメータの値が**の上**、サブ要素レポートは、ポイント レポートを AutoRowFit 値にリセットできます。

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




- **IsSetStyle** : Performance の値が**オフ**、デフォルト値は**間違い** .パフォーマンスが**の上**、デフォルト値は**真実**.また、パフォーマンスが**の上**、サブ要素レポートは、ポイント レポートを AutoRowFit 値にリセットできます。

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




- **IsConditionalFormatting** ：パフォーマンスが**オフ**、デフォルト値は**間違い** .パフォーマンスが**の上**、デフォルト値は**真実**.また、パフォーマンスが**の上**、サブ要素レポートは、ポイント レポートを AutoRowFit 値にリセットできます。 IsSetStyle パラメーターの値が に設定されている場合**間違い**、パフォーマンスの値が無効です。

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
