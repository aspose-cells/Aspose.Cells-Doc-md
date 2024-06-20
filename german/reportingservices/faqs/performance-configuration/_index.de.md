---
title: Leistungs Konfiguration
type: docs
weight: 20
url: /de/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Benutzer können die Leistung in gewissem Maße optimieren. Sie können einige Attribute und Parameter in der **Aspose.Cells.ReportingServices.xml**-Datei wie folgt konfigurieren.

{{% /alert %}} 
### **Leistungs Abschnitt**
Dies zeigt den Leistungsabschnitt wie er standardmäßig ist.

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
### **Leistungsparameter**
- LimitCellsNumberForMerged – Der Standardwert des Parameters ist 1000000. Der Parameterwert wird vom Client festgelegt und wird nicht vom Leistungsparameter-Schalter beeinflusst. Bitte beachten Sie die folgende Konfiguration. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – Kann entweder true oder false sein: 
  - Wenn der Leistungsparameter auf „aus“ gesetzt ist, ist der Standardwert false.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, ist der Standardwert true.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Berichts neu setzen.
    Bitte beachten Sie die folgende Konfiguration. 

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

- IsMerged – Kann entweder true oder false sein: 
  - Wenn der Leistungsparameter auf „aus“ gesetzt ist, ist der Standardwert false.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, ist der Standardwert true.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Berichts neu setzen.
    Bitte beachten Sie die folgende Konfiguration. 

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

- IsSetStyle – Kann entweder true oder false sein: 
  - Wenn der Leistungsparameter auf „aus“ gesetzt ist, ist der Standardwert false.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, ist der Standardwert true.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Berichts neu setzen.
    Bitte beachten Sie die folgende Konfiguration. 

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

- IsConditionalFormatting – Kann entweder true oder false sein: 
  - Wenn der Leistungsparameter auf „aus“ gesetzt ist, ist der Standardwert false.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, ist der Standardwert true.
  - Wenn der Leistungsparameter auf „an“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Punktberichts neu setzen.
  - Wenn der Parameter IsSetStyle auf false gesetzt ist, ist der Wert des Parameters Performance ungültig.
    Bitte beachten Sie die folgende Konfiguration. 

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
