---
title: Performance
type: docs
weight: 30
url: /fr/reportingservices/performance/
---

Pour améliorer les performances, définissez le paramètre Performance sur **ON**.

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

Les différents paramètres de performance sont les suivants:

- **LimitCellsNumberForMerged**: le nombre maximum de cellules pouvant être fusionnées. La valeur par défaut est de 1 000 000. La valeur du paramètre est définie par l'utilisateur et n'est pas impactée par la commutation du paramètre de performance. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: lorsque la valeur de Performance est **off**, la valeur de IsAutoRowFit est **false** par défaut. Lorsque la valeur du paramètre de performance est **on**, la valeur est **true** par défaut. Lorsque la valeur de Performance est **on**, un rapport de sous-élément peut réinitialiser le point du rapport à la valeur AutoRowFit. 

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




- **IsMerged**: lorsque la valeur de Performance est **off**, la valeur par défaut de IsMerged est **false**. Lorsque la valeur de Performance est **on**, la valeur par défaut est **true**. Lorsque la valeur du paramètre de performance est **on**, un rapport de sous-élément peut réinitialiser le point du rapport à la valeur AutoRowFit. 

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




- **IsSetStyle**: lorsque la valeur de Performance est **off**, la valeur par défaut est **false**. Lorsque la valeur de Performance est **on**, la valeur par défaut est **true**. De plus, lorsque la valeur de Performance est **on**, un rapport de sous-élément peut réinitialiser le point du rapport à la valeur AutoRowFit. 

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




- **IsConditionalFormatting**: lorsque Performance est **off**, la valeur par défaut est **false**. Lorsque Performance est **on**, la valeur par défaut est **true**. De plus, lorsque Performance est **on**, un rapport de sous-élément peut réinitialiser le point du rapport à la valeur AutoRowFit. Lorsque la valeur du paramètre IsSetStyle est définie sur **false**, la valeur de Performance est invalide. 

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
