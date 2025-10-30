---
title: Golang ile C++ üzerinden Veri Doğrulama
linktitle: Veri Doğrulama
type: docs
weight: 90
url: /tr/go-cpp/data-validation/
description: Aspose.Cells for C++ API kullanarak veri doğrulama nasıl eklenir öğrenin.
keywords: Veri Doğrulama Ekle, Doğrulama Değerini Alma, Tamsayı Veri Doğrulama Ekle, Liste Veri Doğrulama Ekle, Tarih Veri Doğrulama Ekle, Zaman Veri Doğrulama Ekle, Metin Uzunluğu Veri Doğrulama Ekle, Varolan Doğrulamaya Hücre Alanı Ekle, Hücredeki doğrulama açılır menü mü, Özel Doğrulama Ekle  
---

{{% alert color="primary" %}}

Microsoft Excel, çalışma sayfası verilerini otomatik filtreleme veya doğrulama için iyi özellikler sağlar. Aspose.Cells, Microsoft Excel'in veri doğrulama ve Otomatik Filtre özelliklerini tam olarak destekler. Bu makalede, bu özelliklerin Microsoft Excel'de nasıl kullanılacağı ve Aspose.Cells kullanılarak nasıl kodlanacağı anlatılmaktadır.

{{% /alert %}}

## **Veri Doğrulama Türleri ve Uygulama**

Veri doğrulama, çalışsayadaki girilen verilere ilişkin kuralların ayarlanabilme yeteneğidir. Örneğin, bir sütunun TARIH olarak etiketlendiğinden emin olmak için doğrulamayı kullanın ve yalnızca tarihlerin bulunduğu veya başka bir sütunda yalnızca sayıların bulunduğundan emin olun. Aynı zamanda BELİRLİ bir tarih aralığında yalnızca tarihlerin bulunduğundan emin olabilirsiniz. Veri doğrulama ile çalışarak, çalışsayadaki hücrelere neyin girileceğini kontrol edebilirsiniz.

Microsoft Excel, çeşitli farklı veri doğrulama türlerini desteklemektedir. Her tür, bir hücre veya hücre aralığına hangi veri türünün girileceğini kontrol etmek için kullanılır. Aşağıda, aşağıdaki durumların doğrulanma şeklini gösteren kod örnekleri bulunmaktadır:

- Sayıların tam olduğunu, yani onların ondalık kısmının olmadığını doğrulama.
- Ondalık sayıların doğru yapısı takip edildiğini doğrulama. Kod örneği, bir hücre aralığının iki ondalık alanı olması gerektiğini tanımlar.
- Değerlerin belirli bir değer listesine sınırlı olduğunu doğrulama. Liste doğrulama, bir hücre veya hücre aralığına uygulanabilen ayrı bir değer listesi tanımlar.
- Tarihlerin belirli bir aralıkta olmasını sağlama.
- Zamanın belirli bir aralıkta olup olmadığını kontrol etme.
- Bir metnin belirli bir karakter uzunluğunda olup olmadığını kontrol etme.

### **Microsoft Excel ile Veri Doğrulama**

Microsoft Excel kullanarak doğrulamalar oluşturmak için:

1. Bir çalışsayfada, doğrulama uygulamak istediğiniz hücreleri seçin.
1. **Data** menüsünden **Doğrulama** seçeneğini seçin. Doğrulama iletişim kutusu görüntülenecektir.
1. **Ayarlar** sekmesine tıklayın ve ayarları girin.

### **Aspose.Cells ile Veri Doğrulama**

Veri doğrulaması, çalışma tablolarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulaması ile geliştiriciler, kullanıcılara bir liste seçeneği sunabilir, veri girişlerini belirli bir tür veya boyuta sınırlayabilir, vb.
Aspose.Cells'de, her [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfının bir [**GetValidations()**](https://reference.aspose.com/cells/go-cpp/worksheet/getvalidations/) özelliği vardır. Bu özellik, bir [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) koleksiyonunu temsil eder. Doğrulamayı kurmak için, [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) sınıfının bazı özelliklerini aşağıdaki gibi ayarlayın:

- Tip - [**ValidationType**](https://reference.aspose.com/cells/go-cpp/validationtype/) numaralı sayısal değerlerden birini kullanarak belirtilebilen doğrulama tipini temsil eder.
- Operatör - doğrulamada kullanılacak operatörü temsil eder, bu, [**OperatorType**](https://reference.aspose.com/cells/go-cpp/operatortype/) numaralandırmasındaki önceden tanımlanmış değerlerden birini kullanarak belirtilebilir.
- Formül1 - Doğrulamanın ilk parçasıyla ilişkilendirilen değeri veya ifadeyi temsil eder.
- Formül2 - Doğrulamanın ikinci parçası ile ilişkilendirilen değeri veya ifadeyi temsil eder.

[**Validation**](https://reference.aspose.com/cells/go-cpp/validation/) nesnesinin özellikleri yapılandırıldığında, geliştiriciler oluşturulan doğrulamayı kullanarak doğrulanacak hücre aralığı hakkında bilgileri depolamak için [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) yapısını kullanabilir.

#### **Veri Doğrulama Türleri**

[**ValidationType**](https://reference.aspose.com/cells/go-cpp/validationtype/) numaralandırmasının aşağıdaki üyeleri bulunmaktadır:

|**Üye Adı**|**Açıklama**|
| :- | :- |
|AnyValue|Herhangi bir türün bir değeri olarak belirtilir.
|WholeNumber|Tamsayılar için doğrulama türünü belirtir.
|Decimal|Ondalık sayılar için doğrulama türünü belirtir.
|List|Açılır kutu listesi için doğrulama türünü belirtir.
|Date|Tarihler için doğrulama türünü belirtir.
|Time|Zamanlar için doğrulama türünü belirtir.
|TextLength|Metnin uzunluğu için doğrulama türünü belirtir.
|Custom|Özel doğrulama türünü belirtir.

##### **Tamsayı Veri Doğrulaması**

Bu tür doğrulama ile kullanıcılar doğrulanmış hücrelere yalnızca belirli bir aralık içinde tam sayılar girebilirler. Aşağıdaki örnek kodlar, WholeNumber doğrulama türünü uygulamanın nasıl yapılacağını göstermektedir. Örnek, Aspose.Cells kullanılarak Microsoft Excel ile yukarıda oluşturduğumuz aynı veri doğrulamasını oluşturur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation.go" >}}
##### **Liste Veri Doğrulaması**

Bu tür doğrulama, kullanıcının bir açılır kutu listesinden değerler girmesine izin verir. Bu, veri içeren bir dizi satırın bir listesini sağlar. Örnekte, listedeki kaynağı tutmak için ikinci bir çalışma tablosu eklenir. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, birinci çalışma tablosundaki A1:A5 hücre aralığıdır.

Burada önemli olan nokta, [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/go-cpp/validation/getincelldropdown/) özelliğini **true** olarak ayarlamanızdır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-1.go" >}}
##### **Tarih Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan tarih değerlerini doğrulanmış hücrelere girerler. Örnekte, kullanıcının 1970 ila 1999 arasında tarih girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-2.go" >}}
##### **Zaman Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan saatleri doğrulanmış hücrelere girebilirler. Örnekte, kullanıcının 09:00 ile 11:30 arasında zaman girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-3.go" >}}
##### **Metin Uzunluğu Veri Doğrulaması**

Bu tür doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcıya en fazla 5 karakter içeren dize değerlerini girmesi engellenir. Doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-4.go" >}}
### **Veri Doğrulama Kuralları**

Veri doğrulamaları uygulandığında, doğrulamanın farklı hücrelere farklı değerler atayarak kontrol edilebilir. Doğrulama sonucunu almak için [**Cell.GetValidationValue**](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) kullanılabilir. Aşağıdaki örnek bu özelliği farklı değerlerle göstermektedir. Test için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-5.go" >}}
## **Hücrede doğrulamanın açılır menü olup olmadığını kontrol et**

Gördüğümüz gibi bir hücre içinde uygulanabilecek birçok doğrulama türü bulunmaktadır. Doğrulamanın açılır menü olup olmadığını kontrol etmek istiyorsanız, [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/go-cpp/validation/getincelldropdown/) özelliği bunu test etmek için kullanılabilir. Aşağıdaki örnek kod, bu özelliğin kullanımını göstermektedir. Test için örnek bir dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-6.go" >}}
## **Mevcut Doğrulama Alanına Hücre Alanı Ekle**

Mevcut [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)'e [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/) eklemek isteyebileceğiniz durumlar olabilir. Yeni alanı eklerken [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) kullanarak [**CellArea**](https://reference.aspose.com/cells/go-cpp/cellarea/) eklerseniz, Aspose.Cells, yeni alanın zaten var olup olmadığını kontrol etmek için tüm mevcut alanları kontrol eder. Dosyada çok sayıda doğrulama varsa, bu performansı olumsuz etkiler. Bunu aşmak için API, [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/) yöntemini sağlar. *checkIntersection* parametresi, verilen alanın mevcut doğrulama alanlarıyla kesişimini kontrol edip etmeyeceğini belirtir. **false** ayarlamak diğer alanların kontrolünü devre dışı bırakır. *checkEdge* parametresi, uygulanan alanların kontrol edilip edilmeyeceğini belirtir. Yeni alanın sol üst alan olması durumunda iç ayarlar yeniden oluşturulur. Yeni alanın sol üst alan olmadığından eminseniz, bu parametreyi **false** olarak ayarlayabilirsiniz.

Aşağıdaki kod örneği, mevcut [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)'e yeni [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) eklemek için [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/go-cpp/validation/addarea_cellarea/) yönteminin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataValidation-7.go" >}}
Kaynak ve çıktı excel dosyaları referans için ekte sunulmuştur.

[Kaynak Dosyası](96928093.xlsx)

[Çıkış Dosyası](96928220.xlsx)

## **Gelişmiş Konular**
- [ODS Dosyalarında Hücre Doğrulamasını Al](/cells/tr/cpp/get-cell-validation-in-ods-files/)
- [Bir Hücreye Uygulanan Doğrulamayı Al](/cells/tr/cpp/get-validation-applied-on-a-cell/)
- [Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulama](/cells/tr/cpp/verify-that-cell-value-satisfies-data-validation-rules/)
