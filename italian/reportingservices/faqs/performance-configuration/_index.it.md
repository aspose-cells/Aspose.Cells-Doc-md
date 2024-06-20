---
title: Configurazione delle prestazioni
type: docs
weight: 20
url: /it/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Gli utenti possono ottimizzare le prestazioni fino a un certo punto. È possibile configurare alcuni attributi e parametri nel file **Aspose.Cells.ReportingServices.xml** come descritto di seguito.

{{% /alert %}} 
### **Sezione prestazioni**
Questa sezione mostra le prestazioni come sono di default.

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
### **Parametri di performance**
- LimitaNumeroCellePerFusione – Il valore predefinito del parametro è 1000000. Il valore del parametro è impostato dal client e non è influenzato dallo switch dei parametri di performance. Si prega di fare riferimento alla seguente configurazione. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – Può essere vero o falso: 
  - Quando il parametro di performance è impostato su 'off', il valore predefinito è falso.
  - Quando il parametro di performance è impostato su 'on', il valore predefinito è vero.
  - Quando il parametro di performance è impostato su 'on', un report di sotto-elemento può reimpostare il parametro AutoRowFile del report.
    Si prega di fare riferimento alla seguente configurazione. 

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

- IsMerged – Può essere vero o falso: 
  - Quando il parametro di performance è impostato su 'off', il valore predefinito è falso.
  - Quando il parametro di performance è impostato su 'on', il valore predefinito è vero.
  - Quando il parametro di performance è impostato su 'on', un report di sotto-elemento può reimpostare il parametro AutoRowFile del report.
    Si prega di fare riferimento alla seguente configurazione. 

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

- IsSetStyle – Può essere vero o falso: 
  - Quando il parametro di performance è impostato su 'off', il valore predefinito è falso.
  - Quando il parametro di performance è impostato su 'on', il valore predefinito è vero.
  - Quando il parametro di performance è impostato su 'on', un report di sotto-elemento può reimpostare il parametro AutoRowFile del report.
    Si prega di fare riferimento alla seguente configurazione. 

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

- IsConditionalFormatting – Può essere vero o falso: 
  - Quando il parametro di performance è impostato su 'off', il valore predefinito è falso.
  - Quando il parametro di performance è impostato su 'on', il valore predefinito è vero.
  - Quando il parametro Performance è impostato su 'on', il report del sub-elemento può ripristinare il parametro AutoRowFile del report di punto.
  - Quando il parametro IsSetStyle è impostato su false, il valore del parametro Performance non è valido.
    Si prega di fare riferimento alla seguente configurazione. 

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
