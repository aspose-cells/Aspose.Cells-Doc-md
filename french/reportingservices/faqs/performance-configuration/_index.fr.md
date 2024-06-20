---
title: Configuration des performances
type: docs
weight: 20
url: /fr/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Les utilisateurs peuvent optimiser les performances dans une certaine mesure. Vous pouvez configurer certains attributs et paramètres dans le fichier **Aspose.Cells.ReportingServices.xml** comme décrit ci-dessous.

{{% /alert %}} 
### **Section des performances**
Cela montre la section Performance telle qu'elle est par défaut.

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
### **Paramètres de performance**
- LimitCellsNumberForMerged - La valeur par défaut du paramètre est 1000000. La valeur du paramètre est définie par le client et n'est pas affectée par le commutateur de paramètres de performance. Veuillez vous référer à la configuration suivante. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit - Peut être vrai ou faux : 
  - Lorsque le paramètre de performance est réglé sur 'désactivé', la valeur par défaut est fausse.
  - Lorsque le paramètre Performance est défini sur 'on', la valeur par défaut est true.
  - Lorsque le paramètre de performance est réglé sur 'activé', un sous-élément de rapport peut réinitialiser le paramètre AutoRowFile du rapport.
    Veuillez consulter la configuration suivante. 

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

- IsMerged - Peut être vrai ou faux : 
  - Lorsque le paramètre de performance est réglé sur 'désactivé', la valeur par défaut est fausse.
  - Lorsque le paramètre Performance est défini sur 'on', la valeur par défaut est true.
  - Lorsque le paramètre de performance est réglé sur 'activé', un sous-élément de rapport peut réinitialiser le paramètre AutoRowFile du rapport.
    Veuillez consulter la configuration suivante. 

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

- IsSetStyle - Peut être vrai ou faux : 
  - Lorsque le paramètre de performance est réglé sur 'désactivé', la valeur par défaut est fausse.
  - Lorsque le paramètre Performance est défini sur 'on', la valeur par défaut est true.
  - Lorsque le paramètre de performance est réglé sur 'activé', un sous-élément de rapport peut réinitialiser le paramètre AutoRowFile du rapport.
    Veuillez consulter la configuration suivante. 

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

- IsConditionalFormatting - Peut être vrai ou faux : 
  - Lorsque le paramètre de performance est réglé sur 'désactivé', la valeur par défaut est fausse.
  - Lorsque le paramètre Performance est défini sur 'on', la valeur par défaut est true.
  - Lorsque le paramètre Performance est défini sur 'on', le rapport sub-élément peut réinitialiser le paramètre AutoRowFile du rapport point.
  - Lorsque le paramètre IsSetStyle est défini sur false, la valeur du paramètre Performance n'est pas valide.
    Veuillez consulter la configuration suivante. 

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
