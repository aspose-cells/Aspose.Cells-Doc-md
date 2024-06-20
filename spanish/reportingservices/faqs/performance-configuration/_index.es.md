---
title: Configuración de rendimiento
type: docs
weight: 20
url: /es/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Los usuarios pueden optimizar el rendimiento hasta cierto punto. Se pueden configurar algunos atributos y parámetros en el archivo **Aspose.Cells.ReportingServices.xml** como se describe a continuación.

{{% /alert %}} 
### **Sección de Rendimiento**
Esto muestra la sección de Rendimiento tal como está por defecto.

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
### **Parámetros de Rendimiento**
- LimitCellsNumberForMerged – El valor por defecto del parámetro es 1000000. El valor del parámetro es establecido por el cliente y no se ve afectado por el interruptor de parámetros de rendimiento. Por favor refiérase a la siguiente configuración. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – Puede ser verdadero o falso: 
  - Cuando el parámetro de rendimiento está configurado en 'off', el valor predeterminado es falso.
  - Cuando el parámetro de rendimiento está configurado en 'on', el valor predeterminado es verdadero.
  - Cuando el parámetro de rendimiento está configurado en 'on', un subelemento del informe puede restablecer el parámetro AutoRowFile del informe.
    Consulte la siguiente configuración. 

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

- IsMerged – Puede ser verdadero o falso: 
  - Cuando el parámetro de rendimiento está configurado en 'off', el valor predeterminado es falso.
  - Cuando el parámetro de rendimiento está configurado en 'on', el valor predeterminado es verdadero.
  - Cuando el parámetro de rendimiento está configurado en 'on', un subelemento del informe puede restablecer el parámetro AutoRowFile del informe.
    Consulte la siguiente configuración. 

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

- IsSetStyle – Puede ser verdadero o falso: 
  - Cuando el parámetro de rendimiento está configurado en 'off', el valor predeterminado es falso.
  - Cuando el parámetro de rendimiento está configurado en 'on', el valor predeterminado es verdadero.
  - Cuando el parámetro de rendimiento está configurado en 'on', un subelemento del informe puede restablecer el parámetro AutoRowFile del informe.
    Consulte la siguiente configuración. 

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

- IsConditionalFormatting: Puede ser verdadero o falso: 
  - Cuando el parámetro de rendimiento está configurado en 'off', el valor predeterminado es falso.
  - Cuando el parámetro de rendimiento está configurado en 'on', el valor predeterminado es verdadero.
  - Cuando el parámetro de rendimiento está configurado en 'on', el subelemento del informe puede restablecer el parámetro AutoRowFile del informe de puntos.
  - Cuando el parámetro IsSetStyle está configurado en falso, el valor del parámetro de rendimiento es inválido.
    Consulte la siguiente configuración. 

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
