---
title: Ошибка выполнения 429
type: docs
weight: 60
url: /ru/reportingservices/runtime-error-429/
---
##### **Описание**
 Ошибка выполнения: "429"
 Компонент ActiveX не может создать объект
 Строка, вызывающая ошибку:
 Установите AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient").
##### **Решение**
{{% alert color="primary" %}} 

 Перерегистрировать**Aspose.Cells.ReportingServices.Client.dll** с использованием**Regasm.exe** полезность:

1. Запустите cmd.exe от имени администратора.
1. cd $(Aspose.Cells для папки установки служб Reporting Services).
1.  Выполнять**regasm.exe** зарегистрироваться**Aspose.Cells.ReportingServices.Client.dll** вручную.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 Пожалуйста, проверьте рабочую среду для вашей системы. Например:

-  Если ваш офис Microsoft — x64, выполните команду

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  Если ваш офис Microsoft — x86, выполните команду

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Пожалуйста, обратитесь к следующему примеру/команде:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
