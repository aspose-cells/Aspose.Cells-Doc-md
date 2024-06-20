---
title: Çalışma Zamanı Hatası 429
type: docs
weight: 60
url: /tr/reportingservices/runtime-error-429/
---

##### **Açıklama**
Çalışma zamanı hatası: '429' 
ActiveX bileşeni nesne oluşturamaz 
Hatanın neden olduğu satır: 
Set AsposeClientTools = CreateObject("Aspose.Cells.ReportingServices.Client.AsposeClient"). 
##### **Çözüm**
{{% alert color="primary" %}} 

Aspose.Cells.ReportingServices.Client.dll'yi **Regasm.exe** yardımcı programını kullanarak yeniden kaydettirin: 

1. cmd.exe'yi yönetici olarak çalıştırın.
1. cd $(Aspose.Cells for Reporting Services installation folder).
1. **regasm.exe**'yi manuel olarak **Aspose.Cells.ReportingServices.Client.dll**'yi kaydetmek için çalıştırın. 

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm  Aspose.Cells.ReportingServices.Client.dll  /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase

{{< /highlight >}}

Sisteminiz için çalışma ortamını kontrol edin. Örneğin: 

- Microsoft Office'iniz x64 ise, komutu çalıştırın 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework64\v2.0.50727\regasm.exe

{{< /highlight >}}

- Microsoft Office'iniz x86 ise, komutu çalıştırın 

{{< highlight java >}}

 @: ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm.exe

{{< /highlight >}}

Lütfen aşağıdaki örnek/komuta bakın:

{{< highlight java >}}

 ...%WINDIR%\Microsoft.NET\Framework\v2.0.50727\regasm "C:\Program Files (x86)\Aspose\Aspose.Cells for Reporting Services\Bin\Aspose.Cells.ReportingServices.Client.dll" /tlb Aspose.Cells.ReportingServices.Client.tlb /codebase 

{{< /highlight >}}

{{% /alert %}}
