---
title: Спектакль
type: docs
weight: 30
url: /ru/reportingservices/performance/
---
 Чтобы повысить производительность, установите для параметра Производительность значение**НА**.

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

Различные параметры производительности следующие:

- **Лимитселснумберформержед** : максимальное количество ячеек, которые можно объединить. Значение по умолчанию 1 000 000. Значение параметра задается пользователем и не зависит от переключателя параметров производительности.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **IsAutoRowFit** : Когда значение производительности равно**выключенный** , значение IsAutoRowFit равно**ЛОЖЬ** по умолчанию. Когда значение параметра производительности равно**на** , значение**истинный** по умолчанию. Когда значение производительности равно**на** , отчет о подэлементах может сбросить отчет о точках до значения AutoRowFit.

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




- **Объединён** : Когда значение производительности равно**выключенный** , значение по умолчанию IsMerged равно**ЛОЖЬ** . Когда значение производительности равно**на** , значение по умолчанию**истинный** . Когда параметр производительности имеет значение**на** , отчет о подэлементах может сбросить отчет о точках до значения AutoRowFit.

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




- **Иссетстиле** : Когда значение производительности равно**выключенный** , значение по умолчанию**ЛОЖЬ** . Когда производительность**на** , значение по умолчанию**истинный** . Кроме того, когда производительность**на** , отчет о подэлементах может сбросить отчет о точках до значения AutoRowFit.

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




- **IsConditionalFormatting** : Когда производительность**выключенный** , значение по умолчанию**ЛОЖЬ** . Когда производительность**на** , значение по умолчанию**истинный** . Кроме того, когда производительность**на** , отчет о подэлементах может сбросить отчет о точках до значения AutoRowFit. Если для параметра IsSetStyle задано значение**ЛОЖЬ** , значение Performance недопустимо.

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
