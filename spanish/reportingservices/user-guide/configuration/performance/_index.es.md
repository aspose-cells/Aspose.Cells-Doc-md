---
title: Rendimiento
type: docs
weight: 30
url: /es/reportingservices/performance/
---

Para mejorar el rendimiento, establezca el parámetro de Rendimiento en **ON**.

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

Los diversos parámetros de rendimiento son los siguientes:

- **LimitCellsNumberForMerged**: el número máximo de celdas que se pueden fusionar. El valor predeterminado es 1,000,000. El valor del parámetro lo define el usuario y no se ve afectado por el interruptor del parámetro de rendimiento. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit**: Cuando el valor de Rendimiento es **off**, el valor de IsAutoRowFit es **falso** de forma predeterminada. Cuando el valor del parámetro de rendimiento es **on**, el valor es **verdadero** de forma predeterminada. Cuando el valor de Rendimiento es **on**, un subelemento de informe puede restablecer el punto de informe al valor AutoRowFit. 

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




- **IsMerged**: Cuando el valor de Rendimiento es **off**, el valor predeterminado de IsMerged es **falso**. Cuando el valor de Rendimiento es **on**, el valor predeterminado es **verdadero**. Cuando el valor del parámetro de rendimiento es **on**, un subelemento de informe puede restablecer el punto de informe al valor AutoRowFit. 

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




- **IsSetStyle**: Cuando el valor de Rendimiento es **off**, el valor predeterminado es **falso**. Cuando Rendimiento es **on**, el valor predeterminado es **verdadero**. Además, cuando Rendimiento es **on**, un subelemento de informe puede restablecer el punto de informe al valor AutoRowFit. 

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




- **IsConditionalFormatting**: Cuando el Rendimiento está **apagado**, el valor predeterminado es **false**. Cuando el Rendimiento está **encendido**, el valor predeterminado es **true**. Además, cuando el rendimiento está **encendido**, un subinforme puede restablecer el informe de puntos al valor AutoRowFit. Cuando el valor del parámetro IsSetStyle se establece en **false**, el valor de Rendimiento no es válido. 

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
