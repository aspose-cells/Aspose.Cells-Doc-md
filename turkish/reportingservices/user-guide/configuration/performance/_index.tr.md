---
title: Performans
type: docs
weight: 30
url: /tr/reportingservices/performance/
---

Performansı artırmak için Performans parametresini **AÇIK** olarak ayarlayın.

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="False">

    <Report name="">

    <AutoRowFit value="True"/>

    <SetStyle value="True"/>

    <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}

Çeşitli performans parametreleri aşağıdaki gibidir:

- **MergeEdilecekHücreSayısıSınırı**: Birleştirilebilecek maksimum hücre sayısı. Varsayılan değer 1.000.000. Parametre değeri kullanıcı tarafından belirlenir ve performans parametresi anahtarı tarafından etkilenmez. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **OtomatikSatırUygunluğu**: Performans değeri **kapalı** olduğunda, OtomatikSatırUygunluğu değeri varsayılan olarak **false** olur. Performans parametresi değeri **açık** olduğunda, değer varsayılan olarak **true** olur. Performans parametresi **açık** olduğunda, bir alt eleman raporu OtomatikSatırUygunluğu değerine sıfırlayabilir.Puan raporunu OtomatikSatırUygunluğu değerine sıfırlayabilir. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="Test">

      <AutoRowFit value="False"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **BirleştirildiMi**: Performans değeri **kapalı** olduğunda, BirleştirildiMi varsayılan değeri **false** olur. Performans değeri **açık** olduğunda, varsayılan değer **true** olur. Performans parametresi **açık** olduğunda, bir alt eleman raporu OtomatikSatırUygunluğu değerine sıfırlayabilir. 

{{< highlight java >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="False"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **StilAyarlandıMı**: Performans değeri **kapalı** olduğunda, varsayılan değer **false** olur. Performans **açık** olduğunda, varsayılan değer **true** olur. Ayrıca, Performans **açık** olduğunda, bir alt eleman raporu OtomatikSatırUygunluğu değerine sıfırlayabilir. 

{{< highlight java >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="False"/>

      <Merged value="True"/>

      <ConditionalFormatting value="True"/>

      </Report>

   </Performance>

{{< /highlight >}}




- **KoşulluBiçimlendirmeMı**: Performans değeri **kapalı** olduğunda, varsayılan değer **false** olur. Performans **açık** olduğunda, varsayılan değer **true** olur. Ayrıca, Performans **açık** olduğunda, bir alt eleman raporu OtomatikSatırUygunluğu değerine sıfırlayabilir. StilAyarlandıMı parametre değeri **false** olarak ayarlandığında, Performans değeri geçersizdir. 

{{< highlight java >}}

   <Performance value="ON" IsAutoRowFit ="True" IsMerged="True"  IsSetStyle="True" IsConditionalFormatting ="True">

    <Report name="">

      <AutoRowFit value="True"/>

      <SetStyle value="True"/>

      <Merged value="True"/>

      <ConditionalFormatting value="False"/>

      </Report>

   </Performance>

{{< /highlight >}}
