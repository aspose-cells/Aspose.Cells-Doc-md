---
title: Performans Yapılandırması
type: docs
weight: 20
url: /tr/reportingservices/performance-configuration/
---
{{% alert color="primary" %}} 

 Kullanıcılar performansı bir dereceye kadar optimize edebilir. Bazı nitelikleri ve parametreleri yapılandırabilirsiniz.**Aspose.Cells.ReportingServices.xml** aşağıda açıklandığı gibi dosya.

{{% /alert %}} 
### **Performans Bölümü**
Bu, Performans bölümünü varsayılan olarak olduğu gibi gösterir.

**xml**

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
### **Performans parametreleri**
-  LimitCellsNumberForMerged – Parametrenin varsayılan değeri 1000000'dir. Parametre değeri istemci tarafından ayarlanır ve performans parametresinin anahtarından etkilenmez. Lütfen aşağıdaki yapılandırmaya bakın.

**xml**

{{< highlight "csharp" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000"  IsSetStyle="True" IsConditionalFormatting ="True">



{{< /highlight >}}

-  IsAutoRowFit – Doğru veya yanlış olabilir:
 - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer yanlıştır.
 - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer doğrudur.
 - Performans parametresi "açık" olarak ayarlandığında, bir alt öğe raporu, raporun AutoRowFile parametresini sıfırlayabilir.
Lütfen aşağıdaki yapılandırmaya bakın.

**xml**

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

-  IsMerged – Doğru veya yanlış olabilir:
 - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer yanlıştır.
 - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer doğrudur.
 - Performans parametresi "açık" olarak ayarlandığında, bir alt öğe raporu, raporun AutoRowFile parametresini sıfırlayabilir.
Lütfen aşağıdaki yapılandırmaya bakın.

**xml**

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

-  IsSetStyle – Doğru veya yanlış olabilir:
 - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer yanlıştır.
 - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer doğrudur.
 - Performans parametresi "açık" olarak ayarlandığında, bir alt öğe raporu, raporun AutoRowFile parametresini sıfırlayabilir.
Lütfen aşağıdaki yapılandırmaya bakın.

**xml**

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

-  IsConditionalFormatting – Doğru veya yanlış olabilir:
 - Performans parametresi 'kapalı' olarak ayarlandığında, varsayılan değer yanlıştır.
 - Performans parametresi 'açık' olarak ayarlandığında, varsayılan değer doğrudur.
 - Performans parametresi 'on' olarak ayarlandığında, alt öğe raporu, nokta raporunun AutoRowFile parametresini sıfırlayabilir.
 - IsSetStyle parametresi false olarak ayarlandığında, Performans parametresinin değeri geçersizdir.
Lütfen aşağıdaki yapılandırmaya bakın.

**xml**

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
