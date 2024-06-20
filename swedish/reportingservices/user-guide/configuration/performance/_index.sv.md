---
title: Prestanda
type: docs
weight: 30
url: /sv/reportingservices/performance/
---

För att förbättra prestandan, sätt parametern Prestanda till **PÅ**.

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

De olika prestanda parametrarna är följande:

- **LimitCellsNumberForMerged**: det maximala antalet celler som kan sammanslås. Standardvärdet är 1 000 000. Parametervärdet sätts av användaren och påverkas inte av prestandaparameterns växling. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: När värdet för prestanda är **av**, är standardvärdet för IsAutoRowFit **falskt**. När värdet för prestandaparametern är **på**, är värdet **sant** som standard. När värdet för prestanda är **på** kan en underliggande elementrapport återställa punktrapport till AutoRowFit-värdet. 

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




- **IsMerged**: När värdet för prestanda är **av**, är standardvärdet för IsMerged **falskt**. När värdet för prestanda är **på**, är standardvärdet **sant**. När prestandaparameterns värde är **på**, kan en underliggande elementrapport återställa punktrapporten till AutoRowFit-värdet. 

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




- **IsSetStyle**: När värdet för prestanda är **av**, är standardvärdet **falskt**. När prestanda är **på**, är standardvärdet **sant**. Dessutom kan när prestanda är **på** en underliggande elementrapport återställa punktrapporten till AutoRowFit-värdet. 

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




- **IsConditionalFormatting**: När Prestanda är **av**, är standardvärdet **falskt**. När Prestanda är **på**, är standardvärdet **sant**. Dessutom kan när Prestanda är **på** en underliggande elementrapport återställa punktrapporten till AutoRowFit-värdet. När IsSetStyle parameter värdet är satt till **falskt**, är värdet för Prestanda ogiltigt. 

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
