---
title: Performance
type: docs
weight: 30
url: /reportingservices/performance/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

To improve performance, set the Performance parameter to **ON**.

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

The various performance parameters are as follows:

- **LimitCellsNumberForMerged**: the maximum number of cells that can be merged. The default value is 1,000,000. The parameter value is set by the user and is not affected by the Performance parameter switch. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}

- **IsAutoRowFit**: When the value of Performance is **off**, IsAutoRowFit is **false** by default. When the Performance parameter is **on**, the value is **true** by default. When Performance is **on**, a sub‑element report can reset the report's AutoRowFit value. 

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

- **IsMerged**: When the value of Performance is **off**, IsMerged is **false** by default. When the value of Performance is **on**, the default value is **true**. When the Performance parameter is **on**, a sub‑element report can reset the report's Merged value. 

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

- **IsSetStyle**: When the value of Performance is **off**, the default value is **false**. When Performance is **on**, the default value is **true**. Also, when Performance is **on**, a sub‑element report can reset the report's SetStyle value. 

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

- **IsConditionalFormatting**: When Performance is **off**, the default value is **false**. When Performance is **on**, the default value is **true**. Also, when Performance is **on**, a sub‑element report can reset the report's ConditionalFormatting value. When the IsSetStyle parameter is **false**, the ConditionalFormatting setting is ignored. 

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
