---
title: Actuación
type: docs
weight: 30
url: /es/reportingservices/performance/
---
 Para mejorar el rendimiento, establezca el parámetro Rendimiento en**EN**.

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

Los diversos parámetros de rendimiento son los siguientes:

- **LimitCellsNumberForMerged** : el número máximo de celdas que se pueden combinar. El valor predeterminado 1.000.000. El usuario establece el valor del parámetro y no se ve afectado por el interruptor del parámetro de rendimiento.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : Cuando el valor de Rendimiento es**apagado** , el valor de IsAutoRowFit es**falso**por defecto. Cuando el valor del parámetro de rendimiento es**en** , el valor es**verdadero** por defecto. Cuando el valor de Performance es**en** , un informe de subelemento puede restablecer el informe de puntos al valor AutoRowFit.

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




- **Está fusionado** : Cuando el valor de Rendimiento es**apagado** , el valor predeterminado de IsMerged es**falso** . Cuando el valor de Performance es**en** , El valor predeterminado es**verdadero** . Cuando el valor del parámetro Performance es**en** , un informe de subelemento puede restablecer el informe de puntos al valor AutoRowFit.

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




- **IsSetStyle** : Cuando el valor de Rendimiento es**apagado** , El valor predeterminado es**falso** . Cuando el rendimiento es**en** , El valor predeterminado es**verdadero** . Además, cuando el rendimiento es**en** , un informe de subelemento puede restablecer el informe de puntos al valor AutoRowFit.

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




- **EsFormatoCondicional** : cuando el rendimiento es**apagado** , El valor predeterminado es**falso** . Cuando el rendimiento es**en** , El valor predeterminado es**verdadero** . Además, cuando el rendimiento es**en** , un informe de subelemento puede restablecer el informe de puntos al valor AutoRowFit. Cuando el valor del parámetro IsSetStyle se establece en**falso** , el valor de Rendimiento no es válido.

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
