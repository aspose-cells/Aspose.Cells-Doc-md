---
title: Конфигурация производительности
type: docs
weight: 20
url: /ru/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

Пользователи могут оптимизировать производительность в определенной степени. Вы можете настроить некоторые атрибуты и параметры в**Aspose.Cells.ReportingServices.xml** файл, как описано ниже.

{{% /alert %}} 
### **Раздел производительности**
Это показывает раздел «Производительность», как он есть по умолчанию.

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
### **Параметры производительности**
-  LimitCellsNumberForMerged — значение параметра по умолчанию — 1000000. Значение параметра задается клиентом, и на него не влияет переключатель параметра производительности. Пожалуйста, обратитесь к следующей конфигурации.

**XML**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit — может быть как истинным, так и ложным:
 - Когда для параметра «Производительность» установлено значение «Выкл», значение по умолчанию — «ложь».
 - Когда для параметра «Производительность» установлено значение «включено», значение по умолчанию равно true.
 - Когда для параметра «Производительность» установлено значение «включено», отчет о подэлементах может переустанавливать параметр AutoRowFile отчета.
 Пожалуйста, обратитесь к следующей конфигурации.

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

-  IsMerged — может быть как истинным, так и ложным:
 - Когда для параметра «Производительность» установлено значение «Выкл», значение по умолчанию — «ложь».
 - Когда для параметра «Производительность» установлено значение «включено», значение по умолчанию равно true.
 - Когда для параметра «Производительность» установлено значение «включено», отчет о подэлементах может переустанавливать параметр AutoRowFile отчета.
 Пожалуйста, обратитесь к следующей конфигурации.

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

-  IsSetStyle — может принимать значение true или false:
 - Когда для параметра «Производительность» установлено значение «Выкл», значение по умолчанию — «ложь».
 - Когда для параметра «Производительность» установлено значение «включено», значение по умолчанию равно true.
 - Когда для параметра «Производительность» установлено значение «включено», отчет о подэлементах может переустанавливать параметр AutoRowFile отчета.
 Пожалуйста, обратитесь к следующей конфигурации.

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

- IsConditionalFormatting — может принимать значение true или false:
 - Когда для параметра «Производительность» установлено значение «Выкл», значение по умолчанию — «ложь».
 - Когда для параметра «Производительность» установлено значение «включено», значение по умолчанию равно true.
 - Когда для параметра «Производительность» установлено значение «включено», отчет о подэлементах может переустанавливать параметр AutoRowFile отчета о точках.
 - Если для параметра IsSetStyle задано значение false, значение параметра Performance является недопустимым.
 Пожалуйста, обратитесь к следующей конфигурации.

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
