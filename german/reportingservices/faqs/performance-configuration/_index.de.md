---
title: Leistungskonfiguration
type: docs
weight: 20
url: /de/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

 Benutzer können die Leistung bis zu einem gewissen Grad optimieren. Sie können einige Attribute und Parameter in der konfigurieren**Aspose.Cells.ReportingServices.xml** Datei wie unten beschrieben.

{{% /alert %}} 
### **Leistungsbereich**
Dies zeigt den Performance-Bereich so an, wie er standardmäßig ist.

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
### **Leistungsparameter**
-  LimitCellsNumberForMerged – Der Standardwert des Parameters ist 1000000. Der Parameterwert wird vom Client festgelegt und wird nicht durch den Schalter des Leistungsparameters beeinflusst. Bitte beachten Sie die folgende Konfiguration.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit – Kann entweder wahr oder falsch sein:
 - Wenn der Performance-Parameter auf „off“ gesetzt ist, ist der Standardwert „false“.
 - Wenn der Performance-Parameter auf „on“ eingestellt ist, ist der Standardwert „true“.
 - Wenn der Leistungsparameter auf „on“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Berichts zurücksetzen.
Bitte beachten Sie die folgende Konfiguration.

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

-  IsMerged – Kann entweder wahr oder falsch sein:
 - Wenn der Performance-Parameter auf „off“ gesetzt ist, ist der Standardwert „false“.
 - Wenn der Performance-Parameter auf „on“ eingestellt ist, ist der Standardwert „true“.
 - Wenn der Leistungsparameter auf „on“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Berichts zurücksetzen.
Bitte beachten Sie die folgende Konfiguration.

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

-  IsSetStyle – Kann entweder wahr oder falsch sein:
 - Wenn der Performance-Parameter auf „off“ gesetzt ist, ist der Standardwert „false“.
 - Wenn der Performance-Parameter auf „on“ eingestellt ist, ist der Standardwert „true“.
 - Wenn der Leistungsparameter auf „on“ gesetzt ist, kann ein Unterelementbericht den AutoRowFile-Parameter des Berichts zurücksetzen.
Bitte beachten Sie die folgende Konfiguration.

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

-  IsConditionalFormatting – Kann entweder wahr oder falsch sein:
 - Wenn der Performance-Parameter auf „off“ gesetzt ist, ist der Standardwert „false“.
 - Wenn der Performance-Parameter auf „on“ eingestellt ist, ist der Standardwert „true“.
 - Wenn der Leistungsparameter auf „on“ gesetzt ist, kann der Unterelementbericht den AutoRowFile-Parameter des Punktberichts zurücksetzen.
 - Wenn der IsSetStyle-Parameter auf „false“ gesetzt ist, ist der Wert des Performance-Parameters ungültig.
Bitte beachten Sie die folgende Konfiguration.

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
