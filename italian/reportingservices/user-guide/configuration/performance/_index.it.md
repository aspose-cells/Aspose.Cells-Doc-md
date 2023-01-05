---
title: Prestazione
type: docs
weight: 30
url: /it/reportingservices/performance/
---
 Per migliorare le prestazioni, impostare il parametro Prestazioni su**SU**.

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

I vari parametri prestazionali sono i seguenti:

- **LimitCellsNumberForMerged** : il numero massimo di celle che possono essere unite. Il valore predefinito 1.000.000. Il valore del parametro viene impostato dall'utente e non è influenzato dall'interruttore del parametro delle prestazioni.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : quando il valore di Performance è**spento** , il valore di IsAutoRowFit è**falso** per impostazione predefinita. Quando il valore del parametro delle prestazioni è**Su** , il valore è**VERO** per impostazione predefinita. Quando il valore della Performance è**Su** , un report di sottoelemento può reimpostare il report del punto sul valore AutoRowFit.

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




- **IsMerged** : quando il valore di Performance è**spento** , il valore predefinito di IsMerged è**falso** . Quando il valore della Performance è**Su** , il valore predefinito è**VERO** . Quando il valore del parametro Prestazioni è**Su** , un report di sottoelemento può reimpostare il report del punto sul valore AutoRowFit.

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




- **IsSetStyle** : quando il valore di Performance è**spento** , il valore predefinito è**falso** . Quando le prestazioni sono**Su** , il valore predefinito è**VERO** . Inoltre, quando Performance è**Su** , un report di sottoelemento può reimpostare il report del punto sul valore AutoRowFit.

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




- **IsConditionalFormattazione** : Quando le prestazioni sono**spento** , il valore predefinito è**falso** . Quando le prestazioni sono**Su** , il valore predefinito è**VERO** . Inoltre, quando Performance è**Su** , un report di sottoelemento può reimpostare il report del punto sul valore AutoRowFit. Quando il valore del parametro IsSetStyle è impostato su**falso** , il valore di Performance non è valido.

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
