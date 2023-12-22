---
title: Cell'in Hesaplama Süresini azaltın. Hesaplama yöntemi
description: Bu makalede Aspose.Cells Excel'de hücre hesaplama yöntemlerinin hesaplama süresini azaltmak için Aspose.Cells kitaplığının nasıl kullanılacağı anlatılmaktadır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir dosya oluşturarak hücre hesaplama yöntemini optimize etmek ve performansını artırmak için Aspose.Cells tarafından sağlanan yöntemleri kullanabiliriz. Son olarak değiştirdiğimiz Excel dosyasını diske kaydediyoruz.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /tr/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **Olası Kullanım Senaryoları**

Normalde kullanıcıların aramasını öneririz.[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)yöntemini bir kez kullanın ve ardından tek tek hücrelerin hesaplanan değerlerini alın. Ancak bazen kullanıcılar çalışma kitabının tamamını hesaplamak istemezler. Sadece tek bir hücreyi hesaplamak istiyorlar. Aspose.Cells sağlar[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) ayarlayabileceğiniz özellik**YANLIŞ**ve bireysel hücrenin hesaplama süresini önemli ölçüde azaltacaktır. Çünkü özyinelemeli özellik *true** olarak ayarlandığında hücrelerin tüm bağımlıları her çağrıda yeniden hesaplanır. Ancak özyinelemeli özellik *yanlış** olduğunda, bağımlı hücreler yalnızca bir kez hesaplanır ve sonraki çağrılarda yeniden hesaplanmaz.

##  **Cell.Calculate() yönteminin Hesaplama Süresini Azaltın**

 Aşağıdaki örnek kod kullanımını göstermektedir:[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) mülk. Lütfen bu kodu verilenlerle yürütün[örnek excel dosyası](5113710.xlsx) ve konsol çıkışını kontrol edin. Özyinelemeli özelliğin şu şekilde ayarlandığını göreceksiniz:**YANLIŞ**hesaplama süresini önemli ölçüde azalttı. Bu özelliği daha iyi anlamak için lütfen yorumları da okuyun.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **Konsol Çıkışı**

 Bu, verilen kodla çalıştırıldığında yukarıdaki örnek kodun konsol çıktısıdır.[örnek excel dosyası](5113710.xlsx) bizim makinemizde. Lütfen çıktınızın farklı olabileceğini ancak özyinelemeli özelliği şu şekilde ayarladıktan sonra geçen sürenin farklı olabileceğini unutmayın:**YANLIŞ**her zaman *true** olarak ayarlamaktan daha az olacaktır.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
