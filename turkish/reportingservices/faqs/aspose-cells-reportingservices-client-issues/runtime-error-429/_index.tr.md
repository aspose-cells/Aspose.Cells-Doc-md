---
title: Çalışma Zamanı Hatası 429
type: docs
weight: 60
url: /tr/reportingservices/runtime-error-429/
---
##### **Açıklama**
 Çalışma zamanı hatası: '429'
 ActiveX bileşeni nesne oluşturamıyor
 Hataya neden olan satır:
 AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient") olarak ayarlayın.
##### **Çözüm**
{{% alert color="primary" %}} 

 yeniden kaydol**Aspose.Cells.ReportingServices.Client.dll** kullanmak**regasm.exe** Yarar:

1. Cmd.exe'yi yönetici olarak çalıştırın.
1. cd $(Aspose.Cells for Reporting Services yükleme klasörü).
1.  Uygulamak**regasm.exe** Kayıt olmak**Aspose.Cells.ReportingServices.Client.dll** manuel olarak.

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

 Lütfen sisteminiz için çalışan ortamı kontrol edin. Örneğin:

-  Microsoft Office'iniz x64 ise, komutu çalıştırın

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

-  Microsoft Office'iniz x86 ise, komutu çalıştırın

{{< highlight "java" >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Lütfen aşağıdaki örneğe/komuta bakın:

{{< highlight "java" >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
