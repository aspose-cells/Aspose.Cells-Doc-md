---
title: Veri Doğrulama
type: docs
weight: 70
url: /tr/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel, elektronik tablo verilerini otomatik filtreleme veya doğrulama konularında bazı iyi özellikler sunar.

[Veri doğrulama](/cells/tr/java/data-validation/), çalışma sayfasına girilen verilere ilişkin kurallar belirleme yeteneğidir.

{{% /alert %}} 
## **Veri Doğrulama Türleri ve Uygulama**
Microsoft Excel, çeşitli farklı veri doğrulama türlerini desteklemektedir. Her tür, bir hücre veya hücre aralığına hangi veri türünün girileceğini kontrol etmek için kullanılır. Aşağıda, aşağıdaki durumların doğrulanma şeklini gösteren kod örnekleri bulunmaktadır:

- [Sayıların tam olduğunu](/cells/tr/java/data-validation/) yani ondalık kısmın olmadığını doğrulayın.
- [Ondalık sayıların doğru yapısını](/cells/tr/java/data-validation/) takip ettiğini doğrulayın. Kod örneği, belirli bir aralıkta hücrelerin iki ondalık basamağa sahip olması gerektiğini tanımlar.
- [Değerlerin belirli bir değerler listesine sınırlı](/cells/tr/java/data-validation/) olduğunu doğrulayın.
- [Tarihlerin belirli bir aralıkta olmasını](/cells/tr/java/data-validation/) doğrulayın.
- [Zamanın belirli bir aralıkta olduğunu](/cells/tr/java/data-validation/) doğrulayın.
- [Bir metnin belirli bir karakter uzunluğunda olduğunu](/cells/tr/java/data-validation/) doğrulayın.
### **Microsoft Excel ile Veri Doğrulama**
Microsoft Excel kullanarak doğrulamalar oluşturmak için:

1. Bir çalışsayfada, doğrulama uygulamak istediğiniz hücreleri seçin.
1. **Veri** menüsünden, **Doğrulama**'yı seçin.
   Doğrulama iletişim kutusu görüntülenir.
1. **Ayarlar** sekmesini tıklayın ve aşağıda gösterildiği gibi ayarları girin. 

   **Veri doğrulama ayarları** 

![todo:image_alt_text](data-validation_1.png)
### **Aspose.Cells ile Veri Doğrulama**
Veri doğrulaması, çalışma tablolarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulaması ile geliştiriciler, kullanıcılara bir liste seçeneği sunabilir, veri girişlerini belirli bir tür veya boyuta sınırlayabilir, vb.
 Aspose.Cells'de her [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, bir [Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations) öğesine sahiptir, bu da bir [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) nesneler koleksiyonunu temsil eder. Doğrulama ayarını yapmak için [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) nesnesinin bazı özelliklerini ayarlayın:

- [Type](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): Doğrulama türünü temsil eder, bu da [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) numaralandırmasındaki önceden tanımlanmış değerlerden biri kullanılarak belirtilebilir.
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): doğrulamada kullanılacak olan operatörü temsil eder. Bu, önceden tanımlanmış değerlerden birini kullanarak [OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType) numaralandırmasında belirtilebilir.
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): veri doğrulamanın ilk kısmıyla ilişkili değeri veya ifadeyi temsil eder.
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): veri doğrulamanın ikinci kısmıyla ilişkili değeri veya ifadeyi temsil eder.

[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) nesnesinin özellikleri yapılandırıldığında, geliştiriciler oluşturulan doğrulamayı kullanarak doğrulanacak hücre aralığı hakkında bilgi depolamak için [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) yapısını kullanabilirler.
#### **Veri Doğrulama Türleri**
Veri doğrulama, her hücreye işletme kurallarını yerleştirmenize olanak tanır, böylece yanlış girişler hata mesajlarına neden olur. İş kuralları, bir işletmenin nasıl çalıştığını belirleyen politika ve prosedürlerdir. Aspose.Cells, tüm önemli veri doğrulama türlerini destekler.

[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) numaralandırmasının aşağıdaki üyeleri bulunmaktadır:

|**Üye Adı**|**Açıklama**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Herhangi bir türden bir değeri belirtir.|
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Tamsayılar için doğrulama türünü belirtir.|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Ondalık sayılar için doğrulama türünü belirtir.|
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Açılır liste için doğrulama türünü belirtir.|
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Tarihler için doğrulama türünü belirtir.|
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Saatler için doğrulama türünü belirtir.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Metnin uzunluğu için doğrulama türünü belirtir.|
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Özel doğrulama türünü belirtir.|
#### **Programlama Örneği: Tamsayı Veri Doğrulaması**
Bu tür doğrulama ile kullanıcılar, doğrulanmış hücrelere yalnızca belirtilen aralıkta tamsayı girebilirler. Aşağıdaki kod örnekleri, [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER) doğrulama türünü uygulamanın nasıl gerçekleştirileceğini gösterir. Örnek, yukarıda Microsoft Excel kullanarak oluşturduğumuz doğrulamayı Aspose.Cells kullanarak oluşturur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Programlama Örneği: Ondalık Sayı Veri Doğrulaması**
Bu tür doğrulama ile kullanıcı, ondalık sayıları doğrulanmış hücrelere girebilir. Örnekte, kullanıcı yalnızca ondalık değer girmesi için kısıtlanmıştır ve doğrulama alanı A1:A10'dur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Programlama Örneği: Liste Veri Doğrulaması**
Bu tür doğrulama, kullanıcının bir açılır listeden değer girmesine olanak tanır. Bir liste sağlar: veri içeren bir dizi satır. Kullanıcılar yalnızca listeden değer seçebilir. İlk çalışma sayfasındaki doğrulama alanı A1:A5 hücre aralığıdır.

Burada önemli olan nokta, [Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) özelliğini **true** olarak ayarlamanızdır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Programlama Örneği: Tarih Veri Doğrulaması**
Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan tarih değerlerini doğrulanmış hücrelere girerler. Örnekte, kullanıcının 1970 ila 1999 arasında tarih girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Programlama Örnekleri: Zaman Veri Doğrulaması**
Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan saatleri doğrulanmış hücrelere girebilirler. Örnekte, kullanıcının 09:00 ile 11:30 arasında zaman girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Programlama Örnekleri: Metin Uzunluğu Veri Doğrulaması**
Bu tür doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcıya en fazla 5 karakter içeren dize değerlerini girmesi engellenir. Doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Veri Doğrulama Kuralları**
Veri doğrulamaları uygulandığında, doğrulama farklı değerler atayarak kontrol edilebilir. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) doğrulama sonucunu almak için kullanılabilir. Aşağıdaki örnek, bu özelliği farklı değerlerle göstermektedir. Deneme dosyasını test etmek için aşağıdaki bağlantıdan indirebilirsiniz:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Bir hücredeki doğrulamanın açılır kutu olup olmadığını kontrol et**
Gördüğümüz gibi hücre içinde uygulanabilir birçok doğrulama türü bulunmaktadır. Bir doğrulamanın açılır kutu olup olmadığını kontrol etmek istiyorsanız, [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) özelliği buna test etmek için kullanılabilir. Aşağıdaki örnek kod bu özelliğin kullanımını göstermektedir. Test için deneme dosyasını aşağıdaki bağlantıdan indirebilirsiniz:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Mevcut Doğrulama Alanına Hücre Alanı Ekle**
Bir hücrede mevcut [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)'ya eklenecek durumlar olabilir. [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)) kullanarak [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)'nın eklenmesi durumunda, Aspose.Cells yeni bölgenin zaten mevcut olup olmadığını kontrol eder. Dosyada çok sayıda doğrulama bulunuyorsa bu performansı etkiler. Bunu aşmak için API, [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) metodunu sağlar. *checkIntersection* parametresi, belirtilen alanın mevcut doğrulama alanlarıyla kesişimini kontrol edip etmeyeceğini belirtir. Bu parametreyi **false** olarak ayarlamak, diğer alanların kontrolünü devre dışı bırakır. *checkEdge* parametresi, uygulanan alanları kontrol edip etmeyeceğini belirtir. Yeni alanın sol üst alan olmadığından eminseniz, bu parametreyi **false** olarak ayarlayabilirsiniz.

Aşağıdaki kod örneği, [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) metodu kullanılarak mevcut [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)'nın içine yeni [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) eklemeyi göstermektedir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Kaynak ve çıktı excel dosyaları referans için ekte sunulmuştur.

[Kaynak Dosyası](PivotTableHideAndSortSample.xlsx)

[Çıktı Dosyası](ValidationsSample_out.xlsx)


## **Gelişmiş Konular**
- [ODS Dosyalarında Hücre Doğrulamasını Al](/cells/tr/java/get-cell-validation-in-ods-files/)
- [Bir Hücreye Uygulanan Doğrulamayı Al](/cells/tr/java/get-validation-applied-on-a-cell/)
- [Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulama](/cells/tr/java/verify-that-cell-value-satisfies-data-validation-rules/)
