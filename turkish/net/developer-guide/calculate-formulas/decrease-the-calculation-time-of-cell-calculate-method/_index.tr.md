---
title: Cell'in Hesaplama Süresini azaltın. Hesaplama yöntemi
type: docs
weight: 100
url: /tr/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **Olası Kullanım Senaryoları**

Normalde, kullanıcıların aramasını öneririz.[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)yöntemini bir kez kullanın ve ardından tek tek hücrelerin hesaplanan değerlerini alın. Ancak bazen kullanıcılar tüm çalışma kitabını hesaplamak istemezler. Sadece tek bir hücreyi hesaplamak istiyorlar. Aspose.Cells sağlar[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) ayarlayabileceğiniz özellik**yanlış** ve bireysel hücrenin hesaplama süresini önemli ölçüde azaltacaktır. Çünkü özyinelemeli özellik olarak ayarlandığında**doğru** , ardından hücrelerin tüm bağımlıları her aramada yeniden hesaplanır. Ancak özyinelemeli özellik olduğunda**yanlış**, ardından bağımlı hücreler yalnızca bir kez hesaplanır ve sonraki çağrılarda tekrar hesaplanmaz.

## **Cell.Calculate() yönteminin Hesaplama Süresini azaltın**

 Aşağıdaki örnek kod, kullanımını göstermektedir[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) Emlak. Lütfen bu kodu verilenlerle yürütün[örnek excel dosyası](5113710.xlsx) ve konsol çıktısını kontrol edin. Özyinelemeli özelliğin şu şekilde ayarlandığını göreceksiniz:**yanlış**hesaplama süresini önemli ölçüde azaltmıştır. Lütfen bu mülkü daha iyi anlamak için yorumları da okuyun.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Konsol Çıkışı**

 Bu, verilen ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısıdır.[örnek excel dosyası](5113710.xlsx) makinemizde. Lütfen unutmayın, çıktınız farklı olabilir, ancak özyinelemeli özelliği şu şekilde ayarladıktan sonra geçen süre:**yanlış** ayarlamaktan her zaman daha az olacaktır.**doğru**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
