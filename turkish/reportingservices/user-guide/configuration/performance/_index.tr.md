---
title: Verim
type: docs
weight: 30
url: /tr/reportingservices/performance/
---
 Performansı artırmak için Performans parametresini şu şekilde ayarlayın:**ÜZERİNDE**.

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

Çeşitli performans parametreleri aşağıdaki gibidir:

- **LimitCellsNumberForMerged** : birleştirilebilecek maksimum hücre sayısı. Varsayılan değer 1.000.000. Parametre değeri kullanıcı tarafından ayarlanır ve performans parametre anahtarından etkilenmez.

{{< highlight "java" >}}

 <Performance value="ON" IsAutoRowFit ="True" IsMerged="True" LimitCellsNumberForMerged="10000" IsSetStyle="True" IsConditionalFormatting ="True">

{{< /highlight >}}




- **AutoRowFit mi** : Performance değeri şu olduğunda**kapalı** , IsAutoRowFit'in değeri:**YANLIŞ** varsayılan olarak. Performans parametresinin değeri**üzerinde** , değer**doğru** varsayılan olarak. Performance'ın değeri şu olduğunda**üzerinde** , bir alt öğe raporu, nokta raporunu AutoRowFit değerine sıfırlayabilir.

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




- **Birleştirilmiş** : Performance değeri şu olduğunda**kapalı** , IsMerged varsayılan değeri:**YANLIŞ** . Performance'ın değeri şu olduğunda**üzerinde** , varsayılan değer**doğru** . Değer Performans parametresi olduğunda**üzerinde** , bir alt öğe raporu, nokta raporunu AutoRowFit değerine sıfırlayabilir.

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




- **SetStyle** : Performance değeri şu olduğunda**kapalı** , varsayılan değer**YANLIŞ** . Performans ne zaman**üzerinde** , varsayılan değer**doğru** . Ayrıca, Performans**üzerinde** , bir alt öğe raporu, nokta raporunu AutoRowFit değerine sıfırlayabilir.

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




- **Koşullu Biçimlendirme** : Performans**kapalı** , varsayılan değer**YANLIŞ** . Performans ne zaman**üzerinde** , varsayılan değer**doğru** . Ayrıca, Performans**üzerinde** , bir alt öğe raporu, nokta raporunu AutoRowFit değerine sıfırlayabilir. IsSetStyle parametre değeri olarak ayarlandığında**YANLIŞ** , Performans değeri geçersiz.

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
