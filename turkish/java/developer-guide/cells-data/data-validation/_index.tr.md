---
title: Veri doğrulama
type: docs
weight: 70
url: /tr/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel, çalışma sayfası verilerini otomatik olarak filtrelemek veya doğrulamak için bazı iyi özellikler sağlar.

[Veri doğrulama](/cells/tr/java/data-validation/) bir çalışma sayfasına girilen verilerle ilgili kuralları belirleme yeteneğidir. Örneğin, TARİH etiketli bir sütunun yalnızca tarihleri veya başka bir sütunun yalnızca sayıları içerdiğinden emin olmak için doğrulamayı kullanın. TARİH etiketli bir sütunun yalnızca belirli bir aralıktaki tarihleri içermesini bile sağlayabilirsiniz. Veri doğrulama ile çalışma sayfasındaki hücrelere nelerin girildiğini kontrol edebilirsiniz. Aspose.Cells, Microsoft Excel'in veri doğrulama ve otomatik filtreleme özelliklerini tam olarak destekler. Bu makalede, Microsoft Excel'deki özelliklerin nasıl kullanılacağı ve bunların Aspose.Cells kullanılarak nasıl kodlanacağı açıklanmaktadır.

{{% /alert %}} 
## **Veri Doğrulama Türleri ve Yürütme**
Microsoft Excel, bir dizi farklı veri doğrulama türünü destekler. Her tür, bir hücreye veya hücre aralığına ne tür verilerin girildiğini kontrol etmek için kullanılır. Aşağıda, kod parçacıkları şunun nasıl doğrulanacağını göstermektedir:

- [Numbers bütündür](/cells/tr/java/data-validation/)yani ondalık kısmı yoktur.
- [Ondalık sayılar doğru yapıyı takip eder](/cells/tr/java/data-validation/). Kod örneği, bir hücre aralığının iki ondalık boşluğa sahip olması gerektiğini tanımlar.
- [Değerler, bir değerler listesiyle sınırlıdır](/cells/tr/java/data-validation/). Liste doğrulama, bir hücreye veya hücre aralığına uygulanabilen ayrı bir değer listesi tanımlar.
- [Tarihler belirli bir aralığa giriyor](/cells/tr/java/data-validation/).
- [Zaman belirli bir aralıkta](/cells/tr/java/data-validation/).
- [Bir metin belirli bir karakter uzunluğundadır](/cells/tr/java/data-validation/).
### **Microsoft Excel ile Veri Doğrulama**
Microsoft Excel'i kullanarak doğrulama oluşturmak için:

1. Bir çalışma sayfasında doğrulama uygulamak istediğiniz hücreleri seçin.
1. itibaren**Veri**menü, seç**Doğrulama**.
 Doğrulama iletişim kutusu görüntülenir.
1. Tıkla**Ayarlar**sekmesine gidin ve aşağıda gösterildiği gibi ayarları girin.

   **Veri doğrulama ayarları** 

![yapılacaklar:resim_alternatif_metin](data-validation_1.png)
### **Aspose.Cells ile Veri Doğrulama**
Veri doğrulama, çalışma sayfalarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulama ile geliştiriciler, kullanıcılara bir seçenek listesi sağlayabilir, veri girişlerini belirli bir tür veya boyutla kısıtlayabilir, vb.
 Aspose.Cells'de, her biri[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)sınıfın bir[Doğrulamalar](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)koleksiyonunu temsil eden nesne[Doğrulama](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)nesneler. Doğrulamayı ayarlamak için bazılarını ayarlayın.[Doğrulama](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)sınıfın özellikleri:

- [Tip](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): içinde önceden tanımlanmış değerlerden biri kullanılarak belirtilebilen doğrulama tipini temsil eder.[Doğrulama Türü](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)numaralandırma.
- [Şebeke](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): doğrulamada kullanılacak operatörü temsil eder ve bu, ön tanımlı değerlerden biri kullanılarak belirtilebilir.[OperatörTürü](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)numaralandırma.
- [formül1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): veri doğrulamanın ilk kısmıyla ilişkili değeri veya ifadeyi temsil eder.
- [formül2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): veri doğrulamanın ikinci kısmıyla ilişkili değeri veya ifadeyi temsil eder.

Ne zaman[Doğrulama](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)nesnenin özellikleri yapılandırıldı, geliştiriciler[hücre alanı](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)oluşturulan doğrulama kullanılarak doğrulanacak hücre aralığı hakkında bilgi depolamak için yapı.
#### **Veri Doğrulama Türleri**
Veri doğrulama, yanlış girişlerin hata mesajlarına neden olması için her hücreye iş kuralları oluşturmanıza olanak tanır. İş kuralları, bir işletmenin nasıl çalıştığını yöneten politikalar ve prosedürlerdir. Aspose.Cells, tüm önemli veri doğrulama türlerini destekler.

bu[Doğrulama Türü](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)numaralandırma aşağıdaki üyelere sahiptir:

|**Üye adı**|**Açıklama**|
|:- |:- |
|[HERHANGİ BİR DEĞER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Herhangi bir türden bir değeri belirtir.|
|[BÜTÜN SAYI](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Tam sayılar için doğrulama türünü belirtir.|
|[ONDALIK](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Ondalık sayılar için doğrulama türünü belirtir.|
|[LİSTE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Açılır liste için doğrulama türünü belirtir.|
|[TARİH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Tarihler için doğrulama türünü belirtir.|
|[ZAMAN](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Zaman için doğrulama türünü belirtir.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Metnin uzunluğu için doğrulama türünü belirtir.|
|[GELENEK](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Özel doğrulama türünü belirtir.|
#### **Programlama Örneği: Tam Sayı Veri Doğrulaması**
Bu doğrulama türünde, kullanıcılar doğrulanmış hücrelere yalnızca belirli bir aralıktaki tam sayıları girebilir. Aşağıdaki kod örnekleri,[BÜTÜN SAYI](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)doğrulama türü. Örnek, yukarıda Microsoft Excel kullanarak oluşturduğumuz aynı veri doğrulamasını Aspose.Cells kullanarak oluşturur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Programlama Örneği: Ondalık Veri Doğrulama**
Bu tür bir doğrulama ile kullanıcı, doğrulanmış hücrelere ondalık sayılar girebilir. Örnekte, kullanıcı yalnızca ondalık değer girmekle sınırlandırılmıştır ve doğrulama alanı A1:A10'dur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Programlama Örneği: Liste Veri Doğrulaması**
Bu doğrulama türü, kullanıcının bir açılır listeden değerler girmesine izin verir. Bir liste sağlar: veri içeren bir dizi satır. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, ilk çalışma sayfasındaki A1:A5 hücre aralığıdır.

ayarını yapmanız burada önemlidir.[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Programlama Örneği: Tarih Veri Doğrulaması**
Bu tür bir doğrulama ile kullanıcılar, doğrulanmış hücrelere belirli bir aralıktaki veya belirli ölçütleri karşılayan tarih değerlerini girer. Örnekte, kullanıcı 1970 ile 1999 yılları arasında tarih girmekle sınırlandırılmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Programlama Örnekleri: Zaman Veri Doğrulaması**
Bu tür bir doğrulama ile kullanıcılar, doğrulanmış hücrelere belirli bir aralıktaki veya bazı ölçütleri karşılayan zamanlar girebilir. Örnekte, kullanıcı 09:00 ile 11:30 AM arasındaki saatleri girmekle sınırlandırılmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Programlama Örnekleri: Metin Uzunluğu Veri Doğrulaması**
Bu tür bir doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcının en fazla 5 karakter içeren dize değerleri girmesi kısıtlanmıştır. Doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Veri Doğrulama Kuralları**
Veri doğrulamaları uygulandığında, hücrelere farklı değerler atanarak doğrulama kontrol edilebilir.[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) doğrulama sonucunu almak için kullanılabilir. Aşağıdaki örnek, bu özelliği farklı değerlerle göstermektedir. Örnek dosya, test için aşağıdaki bağlantıdan indirilebilir:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Bir hücrede doğrulamanın açılır olup olmadığını kontrol edin**
 Gördüğümüz gibi, bir hücre içinde uygulanabilecek birçok doğrulama türü vardır. Doğrulamanın açılır olup olmadığını kontrol etmek istiyorsanız,[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) özelliği bunu test etmek için kullanılabilir. Aşağıdaki örnek kod, bu özelliğin kullanımını gösterir. Test için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **CellArea'yı mevcut Doğrulamaya ekleyin**
Eklemek isteyebileceğiniz durumlar olabilir.[hücre alanı](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)mevcut[Doğrulama](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). eklediğinizde[hücre alanı](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)kullanarak[Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells, yeni alanın zaten var olup olmadığını görmek için tüm mevcut alanları kontrol eder. Dosyada çok sayıda doğrulama varsa, bu bir performans isabeti alır. Bunun üstesinden gelmek için API,[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) yöntem. bu*checkKavşak*parametresi, belirli bir alanın mevcut doğrulama alanlarıyla kesişiminin kontrol edilip edilmeyeceğini belirtir. ayarlanıyor**YANLIŞ**diğer alanların kontrolünü devre dışı bırakacaktır. bu*checkEdge*parametre uygulanan alanların kontrol edilip edilmeyeceğini belirtir. Yeni alan sol üst alan olursa dahili ayarlar yeniden oluşturulur. Yeni alanın sol üst alan olmadığından eminseniz bu parametreyi şu şekilde ayarlayabilirsiniz:**YANLIŞ**.

Aşağıdaki kod parçacığı,[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) yeni ekleme yöntemi[hücre alanı](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)mevcut[Doğrulama](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Kaynak ve çıktı excel dosyaları referans için eklenmiştir.

[Kaynak dosyası](PivotTableHideAndSortSample.xlsx)

[Çıktı dosyası](ValidationsSample_out.xlsx)


## **ileri konular**
- [ODS Dosyalarında Cell Doğrulaması Alın](/cells/tr/java/get-cell-validation-in-ods-files/)
- [Cell'de Doğrulama Uygulayın](/cells/tr/java/get-validation-applied-on-a-cell/)
- [Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın](/cells/tr/java/verify-that-cell-value-satisfies-data-validation-rules/)
