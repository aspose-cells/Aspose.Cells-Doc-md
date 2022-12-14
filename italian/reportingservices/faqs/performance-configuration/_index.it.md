---
title: Configurazione delle prestazioni
type: docs
weight: 20
url: /it/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

 Gli utenti possono ottimizzare le prestazioni in una certa misura. È possibile configurare alcuni attributi e parametri nel file**Aspose.Cells.ReportingServices.xml** file come descritto di seguito.

{{% /alert %}} 
### **Sezione prestazioni**
Questo mostra la sezione Prestazioni così com'è per impostazione predefinita.

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
### **Parametri di prestazione**
-  LimitCellsNumberForMerged – Il valore predefinito del parametro è 1000000. Il valore del parametro viene impostato dal client e non viene influenzato dall'opzione del parametro delle prestazioni. Si prega di fare riferimento alla seguente configurazione.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit – Può essere vero o falso:
 - Quando il parametro Performance è impostato su 'off', il valore predefinito è false.
 - Quando il parametro Performance è impostato su 'on', il valore predefinito è true.
 - Quando il parametro Performance è impostato su "on", un report di sottoelemento può reimpostare il parametro AutoRowFile del report.
Si prega di fare riferimento alla seguente configurazione.

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

-  IsMerged – Può essere vero o falso:
 - Quando il parametro Performance è impostato su 'off', il valore predefinito è false.
 - Quando il parametro Performance è impostato su 'on', il valore predefinito è true.
 - Quando il parametro Performance è impostato su "on", un report di sottoelemento può reimpostare il parametro AutoRowFile del report.
Si prega di fare riferimento alla seguente configurazione.

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

-  IsSetStyle – Può essere vero o falso:
 - Quando il parametro Performance è impostato su 'off', il valore predefinito è false.
 - Quando il parametro Performance è impostato su 'on', il valore predefinito è true.
 - Quando il parametro Performance è impostato su "on", un report di sottoelemento può reimpostare il parametro AutoRowFile del report.
Si prega di fare riferimento alla seguente configurazione.

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

-  IsConditionalFormatting – Può essere vero o falso:
 - Quando il parametro Performance è impostato su 'off', il valore predefinito è false.
 - Quando il parametro Performance è impostato su 'on', il valore predefinito è true.
 - Quando il parametro Performance è impostato su 'on', il sottoelemento report può reimpostare il parametro AutoRowFile del report punto.
 - Quando il parametro IsSetStyle è impostato su false, il valore del parametro Performance non è valido.
Si prega di fare riferimento alla seguente configurazione.

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
