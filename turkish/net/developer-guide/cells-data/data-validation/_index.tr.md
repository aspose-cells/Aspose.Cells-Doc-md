---
title: Veri doğrulama
type: docs
weight: 90
url: /tr/net/data-validation/
description: Aspose.Cells for .NET API numaralı telefondan veri doğrulamayı nasıl ekleyeceğinizi öğrenin.
keywords: Add Data Validation, Get Validation Value, Add Whole Number Data Validation, Add List Data Validation, Add Date Data Validation, Add Time Data Validation, Add Text Length Data Validation, Add CellArea to existing Validation, Check if validation in cell is dropdown, Add Custom Valication  
---
{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerini otomatik olarak filtrelemek veya doğrulamak için bazı iyi özellikler sağlar.Aspose.Cells, Microsoft Excel'in veri doğrulama ve Otomatik Filtreleme özelliklerini tam olarak destekler. Bu makalede, Microsoft Excel'deki özelliklerin nasıl kullanılacağı ve bunların Aspose.Cells kullanılarak nasıl kodlanacağı açıklanmaktadır.

{{% /alert %}}

##  **Veri Doğrulama Türleri ve Yürütülmesi**

Veri doğrulama, bir çalışma sayfasına girilen verilere ilişkin kuralları belirleme yeteneğidir. Örneğin, DATE etiketli bir sütunun yalnızca tarihleri içerdiğinden veya başka bir sütunun yalnızca sayılar içerdiğinden emin olmak için doğrulamayı kullanın. Hatta DATE etiketli bir sütunun yalnızca belirli bir aralıktaki tarihleri içerdiğinden bile emin olabilirsiniz. Veri doğrulama ile çalışma sayfasındaki hücrelere nelerin girildiğini kontrol edebilirsiniz.

Microsoft Excel bir dizi farklı veri doğrulama türünü destekler. Her tür, bir hücreye veya hücre aralığına ne tür verinin girildiğini kontrol etmek için kullanılır. Aşağıda kod parçacıkları bunun nasıl doğrulanacağını göstermektedir:

- Numbers tamdır, yani ondalık kısmı yoktur.
- Ondalık sayılar doğru yapıyı takip eder. Kod örneği, bir hücre aralığının iki ondalık boşluğa sahip olması gerektiğini tanımlar.
- Değerler bir değerler listesiyle sınırlıdır. Liste doğrulama, bir hücreye veya hücre aralığına uygulanabilecek değerlerin ayrı bir listesini tanımlar.
- Tarihler belirli bir aralıkta yer almaktadır.
- Bir zaman belirli bir aralıktadır.
- Bir metin belirli bir karakter uzunluğundadır.

###  **Microsoft Excel ile Veri Doğrulama**

Microsoft Excel'i kullanarak doğrulamalar oluşturmak için:

1. Çalışma sayfasında doğrulama uygulamak istediğiniz hücreleri seçin.
1.  itibaren**Veri** menüsünde *Doğrulama**'yı seçin. Doğrulama iletişim kutusu görüntülenecektir.
1.  Tıkla**Ayarlar** sekmesine tıklayın ve ayarları girin.

###  **Aspose.Cells ile Veri Doğrulama**

Veri doğrulama, çalışma sayfalarına girilen bilgilerin doğrulanması için güçlü bir özelliktir. Veri doğrulamayla geliştiriciler kullanıcılara bir seçenek listesi sunabilir, veri girişlerini belirli bir tür veya boyutla sınırlandırabilir vb.
 Aspose.Cells'de her biri[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf var[**Doğrulamalar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) koleksiyonunu temsil eden mülk[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation) nesneler. Doğrulamayı ayarlamak için bazı ayarları yapın.[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation)class'ın özellikleri aşağıdaki gibidir:

- Tür – önceden tanımlanmış değerlerden biri kullanılarak belirtilebilen doğrulama türünü temsil eder.[**Doğrulama Türü**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)numaralandırma.
-  Operatör – doğrulamada kullanılacak operatörü temsil eder ve bu operatör, önceden tanımlanmış değerlerden biri kullanılarak belirtilebilir.[**Operatör Türü**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)numaralandırma.
- Formül1 – veri doğrulamanın ilk bölümüyle ilişkili değeri veya ifadeyi temsil eder.
- Formül2 – veri doğrulamanın ikinci kısmıyla ilişkili değeri veya ifadeyi temsil eder.

 Ne zaman[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation) nesnenin özellikleri yapılandırıldığında, geliştiriciler[**Hücre Alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)Oluşturulan doğrulama kullanılarak doğrulanacak hücre aralığı hakkındaki bilgileri depolayan yapı.

####  **Veri Doğrulama Türleri**

[**Doğrulama Türü**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)numaralandırma aşağıdaki üyelere sahiptir:

|**Üye adı**|**Tanım**|
| :- | :- |
|Herhangi bir değer|Herhangi bir türden bir değeri belirtir.|
|Bütün sayı|Tam sayılar için doğrulama türünü belirtir.|
|Ondalık|Ondalık sayılar için doğrulama türünü belirtir.|
|Liste|Açılır liste için doğrulama türünü belirtir.|
|Tarih|Tarihler için doğrulama türünü belirtir.|
|Zaman|Zaman için doğrulama türünü belirtir.|
|Metin Uzunluğu|Metnin uzunluğu için doğrulama türünü belirtir.|
|Gelenek|Özel doğrulama türünü belirtir.|

#####  **Tam Sayı Veri Doğrulaması**

Bu doğrulama türüyle kullanıcılar, doğrulanan hücrelere yalnızca belirli bir aralıktaki tam sayıları girebilir. Aşağıdaki kod örnekleri WholeNumber doğrulama türünün nasıl uygulanacağını gösterir. Örnek, yukarıda Microsoft Excel'i kullanarak oluşturduğumuz Aspose.Cells'i kullanarak aynı veri doğrulamayı oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

#####  **Veri Doğrulamasını Listeleme**

Bu tür doğrulama, kullanıcının açılır listeden değer girmesine olanak tanır. Bir liste sağlar: veri içeren bir dizi satır. Örnekte liste kaynağını tutmak için ikinci bir çalışma sayfası eklenmiştir. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, ilk çalışma sayfasındaki A1:A5 hücre aralığıdır.

 Burada ayarlamanız önemlidir.[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)özelliği *true** olarak değiştirin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

#####  **Tarih Veri Doğrulaması**

Bu tür doğrulamayla kullanıcılar, doğrulanan hücrelere belirli bir aralıktaki veya belirli kriterleri karşılayan tarih değerlerini girer. Örnekte, kullanıcının 1970 ila 1999 arasındaki tarihleri girmesi sınırlandırılmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

#####  **Zaman Veri Doğrulaması**

Bu doğrulama türüyle kullanıcılar, doğrulanan hücrelere belirli bir aralıktaki veya bazı kriterleri karşılayan süreleri girebilir. Örnekte, kullanıcının 09:00 ile 11:30 arası saatleri girmesi sınırlandırılmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

#####  **Metin Uzunluğu Veri Doğrulaması**

Bu doğrulama türüyle kullanıcılar, doğrulanan hücrelere belirli uzunluktaki metin değerlerini girebilir. Örnekte, kullanıcının en fazla 5 karakter içeren dize değerleri girmesi sınırlandırılmıştır. Doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

###  **Veri Doğrulama Kuralları**

 Veri doğrulamaları uygulandığında, hücrelere farklı değerler atanarak doğrulama kontrol edilebilir.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) doğrulama sonucunu almak için kullanılabilir. Aşağıdaki örnekte bu özellik farklı değerlerle gösterilmektedir. Örnek dosya test için aşağıdaki bağlantıdan indirilebilir:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

##  **Hücredeki doğrulamanın açılır olup olmadığını kontrol edin**

 Gördüğümüz gibi bir hücre içinde uygulanabilecek birçok doğrulama türü vardır. Doğrulamanın açılır olup olmadığını kontrol etmek istiyorsanız,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)özelliği bunu test etmek için kullanılabilir. Aşağıdaki örnek kod, bu özelliğin kullanımını gösterir. Test için örnek bir dosya aşağıdaki bağlantıdan indirilebilir:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

##  **Mevcut Doğrulamaya CellArea'yı ekle**

 Eklemek isteyebileceğiniz durumlar olabilir[**Hücre Alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)mevcut olana[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation). Eklediğinizde[**Hücre Alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) kullanarak[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells, yeni alanın zaten mevcut olup olmadığını görmek için mevcut tüm alanları kontrol eder. Dosyada çok sayıda doğrulama varsa bu durum performansta bir düşüşe neden olur. Bunun üstesinden gelmek için API şunları sağlar:[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) yöntem.*kontrolKavşak* parametresi belirli bir alanın mevcut doğrulama alanlarıyla kesişmesinin kontrol edilip edilmeyeceğini gösterir. Bunu ayarlamak**YANLIŞ** diğer alanların kontrolünü devre dışı bırakacaktır.*checkEdge*parametresi uygulanan alanların kontrol edilip edilmeyeceğini gösterir. Yeni alan sol üst alan haline gelirse dahili ayarlar yeniden oluşturulur. Yeni alanın sol üst alan olmadığından eminseniz bu parametreyi *false** olarak ayarlayabilirsiniz.

Aşağıdaki kod parçacığı kullanımını göstermektedir[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) yeni ekleme yöntemi[**Hücre Alanı**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)mevcut olana[**Doğrulama**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Kaynak ve çıktı excel dosyaları referans amacıyla eklenmiştir.

[Kaynak dosyası](96928093.xlsx)

[Çıktı dosyası](96928220.xlsx)


##  **İleri konular**
- [ODS Dosyalarında Cell Doğrulamasını Alın](/cells/tr/net/get-cell-validation-in-ods-files/)
- [Doğrulamayı Cell numarasına uygulayın](/cells/tr/net/get-validation-applied-on-a-cell/)
- [Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın](/cells/tr/net/verify-that-cell-value-satisfies-data-validation-rules/)
