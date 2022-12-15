---
title: Configuración de rendimiento
type: docs
weight: 20
url: /es/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

Los usuarios pueden optimizar el rendimiento hasta cierto punto. Puede configurar algunos atributos y parámetros en el**Aspose.Cells.ReportingServices.xml** archivo como se describe a continuación.

{{% /alert %}} 
### **Sección de rendimiento**
Esto muestra la sección Rendimiento tal como está de forma predeterminada.

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
### **Parámetros de rendimiento**
-  LimitCellsNumberForMerged: el valor predeterminado del parámetro es 1000000. El valor del parámetro lo establece el cliente y no se ve afectado por el cambio del parámetro de rendimiento. Consulte la siguiente configuración.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit: puede ser verdadero o falso:
 - Cuando el parámetro Rendimiento se establece en 'apagado', el valor predeterminado es falso.
 - Cuando el parámetro Rendimiento se establece en 'activado', el valor predeterminado es verdadero.
 - Cuando el parámetro Rendimiento se establece en 'activado', un informe de subelemento puede restablecer el parámetro AutoRowFile del informe.
 Consulte la siguiente configuración.

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

-  IsMerged: puede ser verdadero o falso:
 - Cuando el parámetro Rendimiento se establece en 'apagado', el valor predeterminado es falso.
 - Cuando el parámetro Rendimiento se establece en 'activado', el valor predeterminado es verdadero.
 - Cuando el parámetro Rendimiento se establece en 'activado', un informe de subelemento puede restablecer el parámetro AutoRowFile del informe.
 Consulte la siguiente configuración.

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

-  IsSetStyle: puede ser verdadero o falso:
 - Cuando el parámetro Rendimiento se establece en 'apagado', el valor predeterminado es falso.
 - Cuando el parámetro Rendimiento se establece en 'activado', el valor predeterminado es verdadero.
 - Cuando el parámetro Rendimiento se establece en 'activado', un informe de subelemento puede restablecer el parámetro AutoRowFile del informe.
 Consulte la siguiente configuración.

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

- IsConditionalFormatting: puede ser verdadero o falso:
 - Cuando el parámetro Rendimiento se establece en 'apagado', el valor predeterminado es falso.
 - Cuando el parámetro Rendimiento se establece en 'activado', el valor predeterminado es verdadero.
 - Cuando el parámetro Rendimiento se establece en 'activado', el informe de subelementos puede restablecer el parámetro AutoRowFile del informe de puntos.
 - Cuando el parámetro IsSetStyle se establece en false, el valor del parámetro Performance no es válido.
 Consulte la siguiente configuración.

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
