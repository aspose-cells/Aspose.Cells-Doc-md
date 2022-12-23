---
title: Prestandakonfiguration
type: docs
weight: 20
url: /sv/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

 Användare kan optimera prestanda till viss del. Du kan konfigurera vissa attribut och parametrar i**Aspose.Cells.ReportingServices.xml** fil enligt beskrivningen nedan.

{{% /alert %}} 
### **Prestanda avsnitt**
Detta visar avsnittet Prestanda som det är som standard.

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
### **Prestandaparametrar**
-  LimitCellsNumberForMerged – Standardvärdet för parametern är 1000000. Parametervärdet ställs in av klienten och påverkas inte av prestandaparameterns switch. Se följande konfiguration.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit – Kan vara antingen sant eller falskt:
 - När parametern Performance är inställd på 'av' är standardvärdet falskt.
 - När parametern Performance är inställd på 'on' är standardvärdet sant.
 - När parametern Prestanda är inställd på "på", kan en delelementsrapport återställa rapportens AutoRowFile-parameter.
Se följande konfiguration.

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

-  IsMerged – Kan vara antingen sant eller falskt:
 - När parametern Performance är inställd på 'av' är standardvärdet falskt.
 - När parametern Performance är inställd på 'on' är standardvärdet sant.
 - När parametern Prestanda är inställd på "på", kan en delelementsrapport återställa rapportens AutoRowFile-parameter.
Se följande konfiguration.

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

-  IsSetStyle – Kan vara antingen sant eller falskt:
 - När parametern Performance är inställd på 'av' är standardvärdet falskt.
 - När parametern Performance är inställd på 'on' är standardvärdet sant.
 - När parametern Prestanda är inställd på "på", kan en delelementsrapport återställa rapportens AutoRowFile-parameter.
Se följande konfiguration.

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

-  IsConditionalFormatting – Kan vara antingen sant eller falskt:
 - När parametern Performance är inställd på 'av' är standardvärdet falskt.
 - När parametern Performance är inställd på 'on' är standardvärdet sant.
 - När parametern Prestanda är inställd på "på", kan underelementrapporten återställa punktrapportens AutoRowFile-parameter.
 - När parametern IsSetStyle är inställd på false är värdet på parametern Performance ogiltigt.
Se följande konfiguration.

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
