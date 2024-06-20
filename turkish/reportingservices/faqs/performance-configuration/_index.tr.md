---
title: Performans Yapılandırması
type: docs
weight: 20
url: /tr/reportingservices/performance-configuration/
---

{{% alert color="primary" %}} 

Kullanıcılar performansı belirli bir ölçüde optimize edebilir. Aşağıda **Aspose.Cells.ReportingServices.xml** dosyasında bazı öznitelikler ve parametreler yapılandırılabilir.

{{% /alert %}} 
### **Performans Bölümü**
Bu, Performans bölümünü varsayılan olarak gösterir.

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
### **Performans Parametreleri**
- LimitCellsNumberForMerged – Parametrenin varsayılan değeri 1000000'dir. Parametre değeri istemci tarafından ayarlanır ve performans parametresinin anahtarı tarafından etkilenmez. Lütfen aşağıdaki yapılandırmaya bakınız. 

**XML**

{{< highlight csharp >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

- IsAutoRowFit – True veya false olabilir: 
  - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer false'dır.
  - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer true'dur.
  - Performans parametresi "açık" olarak ayarlandığında, alt öğe rapor, raporun AutoRowFile parametresini yeniden ayarlayabilir.
    Lütfen aşağıdaki yapılandırmaya bakınız. 

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

- IsMerged – True veya false olabilir: 
  - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer false'dır.
  - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer true'dur.
  - Performans parametresi "açık" olarak ayarlandığında, alt öğe rapor, raporun AutoRowFile parametresini yeniden ayarlayabilir.
    Lütfen aşağıdaki yapılandırmaya bakınız. 

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

- IsSetStyle – True veya false olabilir: 
  - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer false'dır.
  - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer true'dur.
  - Performans parametresi "açık" olarak ayarlandığında, alt öğe rapor, raporun AutoRowFile parametresini yeniden ayarlayabilir.
    Lütfen aşağıdaki yapılandırmaya bakınız. 

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

- IsConditionalFormatting – True veya false olabilir: 
  - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer false'dır.
  - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer true'dur.
  - Performans parametresi 'açık' olarak ayarlandığında, alt öğe raporu otomatik satır dosyası parametresini yeniden ayarlayabilir.
  - IsSetStyle parametresi false olarak ayarlandığında, Performans parametresinin değeri geçersizdir.
    Lütfen aşağıdaki yapılandırmaya bakınız. 

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
