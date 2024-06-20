---
title: Ошибка выполнения 429
type: docs
weight: 60
url: /ru/reportingservices/runtime-error-429/
---

##### **Описание**
Ошибка выполнения: '429' 
Компонент ActiveX не может создать объект 
Линия, вызывающая ошибку: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Решение**
{{% alert color="primary" %}} 

Перерегистрируйте **Aspose.Cells.ReportingServices.Client.dll** с помощью утилиты **Regasm.exe**: 

1. Запустите cmd.exe с правами администратора.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. Выполните **regasm.exe**, чтобы зарегистрировать **Aspose.Cells.ReportingServices.Client.dll** вручную. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Пожалуйста, проверьте рабочую среду для вашей системы. Например: 

- Если ваш Microsoft Office x64, выполните команду 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Если ваш Microsoft Office x86, выполните команду 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Пожалуйста, обратитесь к следующему примеру/команде:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
