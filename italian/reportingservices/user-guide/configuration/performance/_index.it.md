---
title: Prestazioni
type: docs
weight: 30
url: /it/reportingservices/performance/
---

Per migliorare le prestazioni, impostare il parametro Performance su **ON**.

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

I vari parametri di performance sono i seguenti:

- **LimitaNumeroCelleFusione**: il numero massimo di celle che possono essere fuse. Il valore predefinito è 1.000.000. Il valore del parametro è impostato dall'utente e non è influenzato dallo switch del parametro di performance. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **EAutoAdattaRiga**: Quando il valore di Performance è **off**, il valore di IsAutoRowFit è **false** per impostazione predefinita. Quando il valore del parametro di performance è **on**, il valore è **true** per impostazione predefinita. Quando il valore di Performance è **on**, un report di sotto-elemento può reimpostare il report di punto al valore AutoRowFit. 

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




- **ÈFuso**: Quando il valore di Performance è **off**, il valore predefinito di IsMerged è **false**. Quando il valore di Performance è **on**, il valore predefinito è **true**. Quando il parametro di Performance è **on**, un report di sotto-elemento può reimpostare il report di punto al valore AutoRowFit. 

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




- **ImpostaStile**: Quando il valore di Performance è **off**, il valore predefinito è **false**. Quando Performance è **on**, il valore predefinito è **true**. Inoltre, quando Performance è **on**, un report di sotto-elemento può reimpostare il report di punto al valore AutoRowFit. 

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




- **FormattazioneCondizionale**: Quando Performance è **off**, il valore predefinito è **false**. Quando Performance è **on**, il valore predefinito è **true**. Inoltre, quando Performance è **on**, un report di sotto-elemento può reimpostare il report di punto al valore AutoRowFit. Quando il valore del parametro ImpostaStile è impostato su **false**, il valore di Performance non è valido. 

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
