---
title: Hücre.Calculate yönteminin Hesaplama Zamanını Düşürme
type: docs
weight: 860
url: /tr/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Olası Kullanım Senaryoları

Genellikle, kullanıcıların [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) yöntemini bir kez çağırmalarını ve ardından bireysel hücrelerin hesaplanan değerlerini almalarını öneririz. Ancak bazen kullanıcılar tüm çalışma kitabını değil, sadece bir hücreyi hesaplamak isteyebilir. Aspose.Cells, [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) özelliğini sağlar ve bunu **false** olarak ayarlayabilirsiniz, bu da bireysel hücrenin hesaplama süresini önemli ölçüde azaltır. Çünkü recursive özellik **true** olarak ayarlandığında, tüm bağımlı hücreler her çağrıda yeniden hesaplanır. Ancak recursive **false** olarak ayarlandığında, bağımlı hücreler yalnızca bir kez hesaplanır ve sonraki çağrılarda yeniden hesaplanmaz.
## **Hücre.Calculate() Yönteminin Hesaplama Zamanını Azaltma**
Aşağıdaki örnek kod, [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) özelliğinin kullanımını göstermektedir. Lütfen bu kodu verilen [örnek excel dosyası](5472288.xlsx) ile çalıştırın ve konsol çıktısını kontrol edin. **false** olarak recursive özelliğini ayarladıktan sonra hesaplama süresinin önemli ölçüde azaldığını göreceksiniz. Lütfen bu özelliğin daha iyi anlaşılması için yorumları da okuyun.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun verilen [örnek excel dosyası](5472288.xlsx) ile çalıştırıldığında konsol çıktısı budur. Lütfen dikkat edin, kendi çıktınız farklı olabilir ancak recursive özelliğini **false** olarak ayarladıktan sonra geçen süre her zaman **true** olarak ayarlamaktan daha az olacaktır.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
