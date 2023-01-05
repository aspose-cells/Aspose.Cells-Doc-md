---
title: Performance
type: docs
weight: 30
url: /fr/reportingservices/performance/
---
 Pour améliorer les performances, définissez le paramètre Performance sur**AU**.

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

Les différents paramètres de performance sont les suivants :

- **LimitCellsNumberForMerged** : le nombre maximum de cellules pouvant être fusionnées. La valeur par défaut 1 000 000. La valeur du paramètre est définie par l'utilisateur et n'est pas affectée par le commutateur de paramètre de performance.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFitIsAutoRowFit** : Lorsque la valeur de Performance est**à l'arrêt** , la valeur de IsAutoRowFit est**faux** par défaut. Lorsque la valeur du paramètre de performance est**au** , la valeur est**vrai** par défaut. Lorsque la valeur de Performance est**au** , un rapport de sous-élément peut réinitialiser le rapport de points à la valeur AutoRowFit.

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




- **EstFusionné** : Lorsque la valeur de Performance est**à l'arrêt** , la valeur par défaut de IsMerged est**faux** . Lorsque la valeur de Performance est**au** , La valeur par défaut est**vrai** . Lorsque la valeur du paramètre Performance est**au** , un rapport de sous-éléments peut réinitialiser le rapport de point sur la valeur AutoRowFit.

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




- **IsSetStyle** : Lorsque la valeur de Performance est**à l'arrêt** , La valeur par défaut est**faux** . Lorsque les performances sont**au** , La valeur par défaut est**vrai** . De même, lorsque Performance est**au** , un rapport de sous-éléments peut réinitialiser le rapport de point sur la valeur AutoRowFit.

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




- **EstFormatageConditionnel** : Lorsque les performances sont**à l'arrêt** , La valeur par défaut est**faux** . Lorsque les performances sont**au** , La valeur par défaut est**vrai** . De même, lorsque Performance est**au** , un rapport de sous-éléments peut réinitialiser le rapport de point sur la valeur AutoRowFit. Lorsque la valeur du paramètre IsSetStyle est définie sur**faux** , la valeur de Performance n'est pas valide.

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
