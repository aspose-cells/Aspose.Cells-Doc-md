---
title: Veri doğrulama
type: docs
weight: 90
url: /tr/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerini otomatik olarak filtrelemek veya doğrulamak için bazı iyi özellikler sağlar. Aspose.Cells, Microsoft Excel'in veri doğrulama ve Otomatik Filtre özelliklerini tam olarak destekler. Bu makalede, Microsoft Excel'deki özelliklerin nasıl kullanılacağı ve bunların Aspose.Cells kullanılarak nasıl kodlanacağı açıklanmaktadır.

{{% /alert %}}

## **Veri Doğrulama Türleri ve Yürütme**

Veri doğrulama, bir çalışma sayfasına girilen verilerle ilgili kuralları belirleme yeteneğidir. Örneğin, TARİH etiketli bir sütunun yalnızca tarihleri veya başka bir sütunun yalnızca sayıları içerdiğinden emin olmak için doğrulamayı kullanın. TARİH etiketli bir sütunun yalnızca belirli bir aralıktaki tarihleri içermesini bile sağlayabilirsiniz. Veri doğrulama ile çalışma sayfasındaki hücrelere nelerin girildiğini kontrol edebilirsiniz.

Microsoft Excel, bir dizi farklı veri doğrulama türünü destekler. Her tür, bir hücreye veya hücre aralığına ne tür verilerin girildiğini kontrol etmek için kullanılır. Aşağıda, kod parçacıkları şunun nasıl doğrulanacağını göstermektedir:

- Numbers tamdır, yani ondalık kısmı yoktur.
- Ondalık sayılar doğru yapıyı takip eder. Kod örneği, bir hücre aralığının iki ondalık boşluğa sahip olması gerektiğini tanımlar.
- Değerler, bir değerler listesiyle sınırlıdır. Liste doğrulama, bir hücreye veya hücre aralığına uygulanabilen ayrı bir değer listesi tanımlar.
- Tarihler belirli bir aralığa giriyor.
- Bir zaman belirli bir aralıktadır.
- Bir metin belirli bir karakter uzunluğundadır.

### **Microsoft Excel ile Veri Doğrulama**

Microsoft Excel'i kullanarak doğrulama oluşturmak için:

1. Bir çalışma sayfasında doğrulama uygulamak istediğiniz hücreleri seçin.
1.  itibaren**Veri** menü, seç**Doğrulama**. Doğrulama iletişim kutusu görüntülenecektir.
1.  Tıkla**Ayarlar** sekmesine gidin ve ayarlara girin.

### **Aspose.Cells ile Veri Doğrulama**

Veri doğrulama, çalışma sayfalarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulama ile geliştiriciler, kullanıcılara bir seçenek listesi sağlayabilir, veri girişlerini belirli bir tür veya boyutla kısıtlayabilir, vb.
 Aspose.Cells'de, her biri[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfın bir[**Doğrulamalar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)koleksiyonunu temsil eden özellik[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation) nesneler. Doğrulamayı ayarlamak için bazılarını ayarlayın.[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation)sınıfın özellikleri aşağıdaki gibidir:

- Tür – önceden tanımlanmış değerlerden biri kullanılarak belirtilebilen doğrulama türünü temsil eder.[**Doğrulama Türü**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)numaralandırma.
-  Operatör – doğrulamada kullanılacak olan ve önceden tanımlanmış değerlerden biri kullanılarak belirtilebilen operatörü temsil eder.[**OperatörTürü**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)numaralandırma.
- Formül1 – veri doğrulamanın ilk kısmıyla ilişkili değeri veya ifadeyi temsil eder.
- Formül2 – veri doğrulamanın ikinci kısmıyla ilişkili değeri veya ifadeyi temsil eder.

 Ne zaman[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation) nesnenin özellikleri yapılandırıldı, geliştiriciler[**hücre alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)oluşturulan doğrulama kullanılarak doğrulanacak hücre aralığı hakkında bilgi depolamak için yapı.

#### **Veri Doğrulama Türleri**

 bu[**Doğrulama Türü**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)numaralandırma aşağıdaki üyelere sahiptir:

|**Üye adı**|**Açıklama**|
|:- |:- |
|Herhangi bir değer|Herhangi bir türden bir değeri belirtir.|
|Bütün sayı|Tam sayılar için doğrulama türünü belirtir.|
|Ondalık|Ondalık sayılar için doğrulama türünü belirtir.|
|Liste|Açılır liste için doğrulama türünü belirtir.|
|Tarih|Tarihler için doğrulama türünü belirtir.|
|Zaman|Zaman için doğrulama türünü belirtir.|
|Metin Uzunluğu|Metnin uzunluğu için doğrulama türünü belirtir.|
|Gelenek|Özel doğrulama türünü belirtir.|

##### **Tam Sayı Veri Doğrulaması**

Bu doğrulama türünde, kullanıcılar doğrulanmış hücrelere yalnızca belirli bir aralıktaki tam sayıları girebilir. Aşağıdaki kod örnekleri, WholeNumber doğrulama türünün nasıl uygulanacağını gösterir. Örnek, yukarıda Microsoft Excel kullanarak oluşturduğumuz aynı veri doğrulamasını Aspose.Cells kullanarak oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Liste Veri Doğrulaması**

Bu doğrulama türü, kullanıcının bir açılır listeden değerler girmesine izin verir. Bir liste sağlar: veri içeren bir dizi satır. Örnekte, liste kaynağını tutmak için ikinci bir çalışma sayfası eklenmiştir. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, ilk çalışma sayfasındaki A1:A5 hücre aralığıdır.

 ayarını yapmanız burada önemlidir.[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) mülkiyet**doğru**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Tarih Veri Doğrulaması**

Bu tür bir doğrulama ile kullanıcılar, doğrulanmış hücrelere belirli bir aralıktaki veya belirli ölçütleri karşılayan tarih değerlerini girer. Örnekte, kullanıcı 1970 ile 1999 yılları arasında tarih girmekle sınırlandırılmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Zaman Verisi Doğrulama**

Bu tür bir doğrulama ile kullanıcılar, doğrulanmış hücrelere belirli bir aralıktaki veya bazı ölçütleri karşılayan zamanlar girebilir. Örnekte, kullanıcı 09:00 ile 11:30 AM arasındaki saatleri girmekle sınırlandırılmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Metin Uzunluğu Veri Doğrulaması**

Bu tür bir doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcının en fazla 5 karakter içeren dize değerleri girmesi kısıtlanmıştır. Doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Veri Doğrulama Kuralları**

Veri doğrulamaları uygulandığında, hücrelere farklı değerler atanarak doğrulama kontrol edilebilir.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) doğrulama sonucunu almak için kullanılabilir. Aşağıdaki örnek, bu özelliği farklı değerlerle göstermektedir. Örnek dosya, test için aşağıdaki bağlantıdan indirilebilir:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Hücredeki doğrulamanın açılır olup olmadığını kontrol edin**

 Gördüğümüz gibi, bir hücre içinde uygulanabilecek birçok doğrulama türü vardır. Doğrulamanın açılır olup olmadığını kontrol etmek istiyorsanız,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) özelliği bunu test etmek için kullanılabilir. Aşağıdaki örnek kod, bu özelliğin kullanımını gösterir. Test için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **CellArea'yı mevcut Doğrulamaya ekleyin**

 Eklemek isteyebileceğiniz durumlar olabilir.[**hücre alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)mevcut[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation). eklediğinizde[**hücre alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) kullanarak[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells, yeni alanın zaten var olup olmadığını görmek için tüm mevcut alanları kontrol eder. Dosyada çok sayıda doğrulama varsa, bu bir performans isabeti alır. Bunun üstesinden gelmek için API,[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) yöntem. bu*checkKavşak* parametresi, belirli bir alanın mevcut doğrulama alanlarıyla kesişiminin kontrol edilip edilmeyeceğini belirtir. ayarlanıyor**YANLIŞ** diğer alanların kontrolünü devre dışı bırakacaktır. bu*checkEdge* parametre uygulanan alanların kontrol edilip edilmeyeceğini belirtir. Yeni alan sol üst alan olursa dahili ayarlar yeniden oluşturulur. Yeni alanın sol üst alan olmadığından eminseniz bu parametreyi şu şekilde ayarlayabilirsiniz:**YANLIŞ**.

Aşağıdaki kod parçacığı,[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) yeni ekleme yöntemi[**hücre alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)mevcut[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Kaynak ve çıktı excel dosyaları referans için eklenmiştir.

[Kaynak dosyası](96928093.xlsx)

[Çıktı dosyası](96928220.xlsx)


## **ileri konular**
- [ODS Dosyalarında Cell Doğrulaması Alın](/cells/tr/net/get-cell-validation-in-ods-files/)
- [Cell'de Doğrulama Uygulayın](/cells/tr/net/get-validation-applied-on-a-cell/)
- [Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın](/cells/tr/net/verify-that-cell-value-satisfies-data-validation-rules/)
