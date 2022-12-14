---
title: Cell'in Hesaplama Süresini azaltın. Hesaplama yöntemi
type: docs
weight: 860
url: /tr/java/decrease-the-calculation-time-of-cell-calculate-method/
---
Olası Kullanım Senaryoları

 Normalde, kullanıcıların aramasını öneririz.[Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\) ) yöntemini bir kez kullanın ve ardından tek tek hücrelerin hesaplanan değerlerini alın. Ancak bazen kullanıcılar tüm çalışma kitabını hesaplamak istemezler. Sadece tek bir hücreyi hesaplamak istiyorlar. Aspose.Cells sağlar[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) ayarlayabileceğiniz özellik**yanlış**ve bireysel hücrenin hesaplama süresini önemli ölçüde azaltacaktır. Çünkü özyinelemeli özellik olarak ayarlandığında**doğru**, ardından hücrelerin tüm bağımlıları her aramada yeniden hesaplanır. Ancak özyinelemeli özellik olarak ayarlandığında**yanlış**, ardından bağımlı hücreler yalnızca bir kez hesaplanır ve sonraki çağrılarda tekrar hesaplanmaz.
## **Cell.Calculate() yönteminin Hesaplama Süresini azaltın**
 Aşağıdaki örnek kod, kullanımını göstermektedir[CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) Emlak. Lütfen bu kodu verilenlerle yürütün[örnek excel dosyası](5472288.xlsx) ve konsol çıktısını kontrol edin. Özyinelemeli özelliğin şu şekilde ayarlandığını göreceksiniz:**yanlış**hesaplama süresini önemli ölçüde azaltmıştır. Lütfen bu mülkü daha iyi anlamak için yorumları da okuyun.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsol Çıkışı**
 Bu, verilen ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısıdır.[örnek excel dosyası](5472288.xlsx) makinemizde. Lütfen unutmayın, çıktınız farklı olabilir, ancak özyinelemeli özelliği şu şekilde ayarladıktan sonra geçen süre:**yanlış** ayarlamaktan her zaman daha az olacaktır.**doğru**.



{{< highlight "java" >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
