---
title: Prestanda
type: docs
weight: 30
url: /sv/reportingservices/performance/
---
 För att förbättra prestandan, ställ in parametern Performance till**PÅ**.

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

De olika prestandaparametrarna är följande:

- **LimitCellsNumberForMerged** : det maximala antalet celler som kan slås samman. Standardvärdet 1 000 000. Parametervärdet ställs in av användaren och påverkas inte av prestandaparameteromkopplaren.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : När värdet på Performance är**av** , värdet på IsAutoRowFit är**falsk** som standard. När värdet på prestandaparametern är**på** , värdet är**Sann** som standard. När värdet av Performance är**på** , kan en underelementrapport återställa punktrapporten till AutoRowFit-värdet.

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




- **IsMerged** : När värdet på Performance är**av** , IsMerged standardvärde är**falsk** . När värdet av Performance är**på** , är standardvärdet**Sann** . När värdet Performance parameter är**på** , kan en underelementrapport återställa punktrapporten till AutoRowFit-värdet.

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




- **IsSetStyle** : När värdet på Performance är**av** , är standardvärdet**falsk** . När Performance är**på** , är standardvärdet**Sann** . Också när Performance är**på** , kan en underelementrapport återställa punktrapporten till AutoRowFit-värdet.

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




- **IsConditionalFormatting** : När Performance är**av** , är standardvärdet**falsk** . När Performance är**på** , är standardvärdet**Sann** . Också när Performance är**på** , kan en underelementrapport återställa punktrapporten till AutoRowFit-värdet. När parametervärdet IsSetStyle är inställt på**falsk** , värdet på Performance är ogiltigt.

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
