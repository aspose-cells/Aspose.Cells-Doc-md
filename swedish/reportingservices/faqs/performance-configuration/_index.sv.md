---
title: Prestandakonfiguration
type: docs
weight: 20
url: /sv/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Användare kan optimera prestandan till en viss del. Du kan konfigurera vissa attribut och parametrar i filen **Aspose.Cells.ReportingServices.xml** enligt beskrivningen nedan.

{{% /alert %}} 
### **Prestandaavsnitt**
Detta visar prestandaavsnittet som det är som standard.

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
### **Prestandaparametrar**
- LimitCellsNumberForMerged – Standardvärdet för parametern är 1000000. Parametervärdet ställs in av klienten och påverkas inte av prestandaparameterns växel. Se följande konfiguration. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – Kan vara antingen sant eller falskt: 
  - När prestandaparametern är inställd på 'av' är standardvärdet falskt.
  - När prestandaparametern är inställd på 'på', är standardvärdet sant.
  - När prestandaparametern är inställd på 'på' kan en underenhet i rapporten återställa rapportens AutoRowFile-paramater.
    Vänligen hänvisa till följande konfiguration. 

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

- IsMerged – Kan vara antingen sant eller falskt: 
  - När prestandaparametern är inställd på 'av' är standardvärdet falskt.
  - När prestandaparametern är inställd på 'på', är standardvärdet sant.
  - När prestandaparametern är inställd på 'på' kan en underenhet i rapporten återställa rapportens AutoRowFile-paramater.
    Vänligen hänvisa till följande konfiguration. 

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

- IsSetStyle – Kan vara antingen sant eller falskt: 
  - När prestandaparametern är inställd på 'av' är standardvärdet falskt.
  - När prestandaparametern är inställd på 'på', är standardvärdet sant.
  - När prestandaparametern är inställd på 'på' kan en underenhet i rapporten återställa rapportens AutoRowFile-paramater.
    Vänligen hänvisa till följande konfiguration. 

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

- IsConditionalFormatting – Kan vara antingen sant eller falskt: 
  - När prestandaparametern är inställd på 'av' är standardvärdet falskt.
  - När prestandaparametern är inställd på 'på', är standardvärdet sant.
  - När prestandaparametern är inställd på 'på', kan delrapporten återställa punktrapportens AutoRowFile-parametrar.
  - När IsSetStyle-parametern är inställd på false är värdet för prestandaparametern ogiltigt.
    Vänligen hänvisa till följande konfiguration. 

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
