---
title: Настройка производительности
type: docs
weight: 20
url: /ru/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Пользователи могут оптимизировать производительность в определенной степени. Вы можете настроить некоторые атрибуты и параметры в файле **Aspose.Cells.ReportingServices.xml**, как описано ниже.

{{% /alert %}} 
### **Раздел производительности**
Это показывает раздел производительности по умолчанию.

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
### **Параметры производительности**
- LimitCellsNumberForMerged – Значение по умолчанию параметра - 1000000. Значение параметра устанавливается клиентом и не зависит от переключателя параметров производительности. Пожалуйста, обратитесь к следующей конфигурации. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – Может быть либо true, либо false: 
  - Когда параметр Performance установлен в 'off', значение по умолчанию - false.
  - Когда параметр Performance установлен в 'on', значение по умолчанию - true.
  - Когда параметр Performance установлен в 'on', подэлемент отчета может переопределить параметр AutoRowFile отчета.
    Пожалуйста, обратитесь к следующей конфигурации. 

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

- IsMerged - Может быть либо true, либо false: 
  - Когда параметр Performance установлен в 'off', значение по умолчанию - false.
  - Когда параметр Performance установлен в 'on', значение по умолчанию - true.
  - Когда параметр Performance установлен в 'on', подэлемент отчета может переопределить параметр AutoRowFile отчета.
    Пожалуйста, обратитесь к следующей конфигурации. 

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

- IsSetStyle - Может быть либо true, либо false: 
  - Когда параметр Performance установлен в 'off', значение по умолчанию - false.
  - Когда параметр Performance установлен в 'on', значение по умолчанию - true.
  - Когда параметр Performance установлен в 'on', подэлемент отчета может переопределить параметр AutoRowFile отчета.
    Пожалуйста, обратитесь к следующей конфигурации. 

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

- IsConditionalFormatting - Может быть либо true, либо false: 
  - Когда параметр Performance установлен в 'off', значение по умолчанию - false.
  - Когда параметр Performance установлен в 'on', значение по умолчанию - true.
  - Когда параметр Performance установлен в 'on', подэлемент отчета может переопределить параметр AutoRowFile отчета.
  - Когда параметр IsSetStyle установлен в false, значение параметра Performance недопустимо.
    Пожалуйста, обратитесь к следующей конфигурации. 

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
