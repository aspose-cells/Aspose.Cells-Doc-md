---
title: Hücre.Calculate yönteminin Hesaplama Zamanını Düşürme
type: docs
weight: 860
url: /tr/java/decrease-the-calculation-time-of-cell-calculate-method/
---


Olası Kullanım Senaryoları

Normalde, kullanıcılara [Workbook.CalculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) methodunu bir kez çağrıp ardından individüel hücrelerin hesaplanmış değerlerini almayı öneririz. Ancak bazen, kullanıcılar tüm çalışma kitabını hesaplamak istemezler. Sadece tek bir hücreyi hesaplamak isterler. Aspose.Cells, [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) özelliği sağlar ve bu özelliği **false** olarak ayarlarsanız, individüel hücrelerin hesaplanma süresi önemli ölçüde azalacaktır. Çünkü recursive özelliği **true** olarak ayarlandığında, her çağrıda hücrelerin bağımlıları tekrar hesaplanır. Ancak recursive özelliği **false** olarak ayarlandığında, bağımlı hücreler sadece bir kez hesaplanır ve ardışık çağrılarda tekrar hesaplanmazlar.
## **Hücre.Calculate() Yönteminin Hesaplama Zamanını Azaltma**
Aşağıdaki örnek kod, [CalculationOptions.Recursive](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#Recursive) özelliğinin kullanımını göstermektedir. Lütfen bu kodu verilen [örnek excel dosyası](5472288.xlsx) ile çalıştırın ve konsol çıktısını kontrol edin. **false** olarak recursive özelliğini ayarladıktan sonra hesaplama süresinin önemli ölçüde azaldığını göreceksiniz. Lütfen bu özelliğin daha iyi anlaşılması için yorumları da okuyun.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DecreaseCalculationTime-DecreaseCalculationTime.java" >}}
## **Konsol Çıktısı**
Yukarıdaki örnek kodun verilen [örnek excel dosyası](5472288.xlsx) ile çalıştırıldığında konsol çıktısı budur. Lütfen dikkat edin, kendi çıktınız farklı olabilir ancak recursive özelliğini **false** olarak ayarladıktan sonra geçen süre her zaman **true** olarak ayarlamaktan daha az olacaktır.



{{< highlight java >}}

 Recursive true: 51 seconds

Recursive false: 16 seconds

{{< /highlight >}}
