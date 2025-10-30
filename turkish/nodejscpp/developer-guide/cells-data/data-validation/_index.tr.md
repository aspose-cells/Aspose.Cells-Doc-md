---  
title: Veri Doğrulama
type: docs  
weight: 90  
url: /tr/nodejs-cpp/data-validation/  
description: Veri doğrulama eklemeyi öğrenin, Aspose.Cells for Node.js via C++ API sini kullanarak.  
keywords: Düğüm ile Veri Doğrulama Ekle Node.js ve C++ kullanımı, Doğrulama Değeri Alma Node.js ve C++ kullanımı, Bütün Sayı Veri Doğrulaması Ekle Node.js ve C++ kullanımı, Liste Veri Doğrulaması Ekle Node.js ve C++ kullanımı, Tarih Veri Doğrulaması Ekle Node.js ve C++ kullanımı, Zaman Veri Doğrulaması Ekle Node.js ve C++ kullanımı, Metin Uzunluğu Veri Doğrulaması Ekle Node.js ve C++ kullanımı, Varolan Doğrulama için Hücre Alanı Ekle Node.js ve C++, Hücredeki Doğrulamanın Dropdown olup olmadığını Kontrol Et Node.js, Özelleştirilmiş Doğrulama Ekle Node.js ve C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel, çalışma sayfası verilerini otomatik filtreleme veya doğrulama için bazı iyi özellikler sunar. Aspose.Cells, Microsoft Excel'in Veri Doğrulama ve Otomatik Filtreleme özelliklerini tam destekler. Bu makale, bu özelliklerin Excel'de nasıl kullanılacağı ve Aspose.Cells for Node.js via C++ kullanılarak nasıl kodlanacağı açıklamaktadır.  
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

### **Aspose.Cells for Node.js via C++ ile Veri Doğrulama**  

Veri doğrulaması, çalışma tablolarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulaması ile geliştiriciler, kullanıcılara bir liste seçeneği sunabilir, veri girişlerini belirli bir tür veya boyuta sınırlayabilir, vb.  
Aspose.Cells for Node.js via C++'te, her [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının, [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) nesne koleksiyonunu temsil eden [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) yöntemi vardır. Doğrulama kurmak için, [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) sınıfının bazı özellikleri aşağıdaki gibi ayarlanır:  

- Tip – doğrulama tipini temsil eder ve [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) enumundaki önceden tanımlanmış değerlerden biri kullanılarak belirtilebilir.  
- Operatör – doğrulamada kullanılacak operatörü temsil eder ve [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype) enumundaki önceden tanımlanmış değerlerden biri kullanılarak belirtilebilir.  
- Formül1 - Doğrulamanın ilk parçasıyla ilişkilendirilen değeri veya ifadeyi temsil eder.  
- Formül2 - Doğrulamanın ikinci parçası ile ilişkilendirilen değeri veya ifadeyi temsil eder.  

[**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) nesnesinin özellikleri yapılandırıldıktan sonra, geliştiriciler, oluşturulan doğrulama kullanılarak doğrulanacak hücre aralığı hakkında bilgi saklamak için [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) yapısını kullanabilirler.  

#### **Veri Doğrulama Türleri**  

[**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) sayımı aşağıdaki üyeleri içerir:  

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

Bu doğrulama türüyle, kullanıcılar doğrulanan hücrelere belirli bir aralıkta yalnızca tam sayılar girebilir. Aşağıdaki kod örnekleri, tüm sayısal doğrulama türünü nasıl uygularız gösterir. Bu örnek, yukarıda Microsoft Excel kullanarak oluşturduğumuzla aynı Veri Doğrulama'yu Aspose.Cells for Node.js via C++ kullanarak oluşturur.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **Liste Veri Doğrulaması**  

Bu tür doğrulama, kullanıcının bir açılır kutu listesinden değerler girmesine izin verir. Bu, veri içeren bir dizi satırın bir listesini sağlar. Örnekte, listedeki kaynağı tutmak için ikinci bir çalışma tablosu eklenir. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, birinci çalışma tablosundaki A1:A5 hücre aralığıdır.  

Burada önemli olan, [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) özelliğini **true** olarak ayarlamaktır.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **Tarih Veri Doğrulaması**  

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan tarih değerlerini doğrulanmış hücrelere girerler. Örnekte, kullanıcının 1970 ila 1999 arasında tarih girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **Zaman Veri Doğrulaması**  

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan saatleri doğrulanmış hücrelere girebilirler. Örnekte, kullanıcının 09:00 ile 11:30 arasında zaman girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **Metin Uzunluğu Veri Doğrulaması**  

Bu tür doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcıya en fazla 5 karakter içeren dize değerlerini girmesi engellenir. Doğrulama alanı B1 hücresidir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **Veri Doğrulama Kuralları**  

Veri doğrulamaları uygulandığında, hücrelerde farklı değerler atayarak doğrulama kontrol edilebilir. [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) doğrulama sonucunu almak için kullanılabilir. Aşağıdaki örnek, bu özelliğin farklı değerlerle gösterimini sağlar. Test etmek için örnek dosya aşağıdaki bağlantıdan indirilebilir:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **Hücrede doğrulamanın açılır menü olup olmadığını kontrol et**  

Görüldüğü gibi, bir hücre içerisinde uygulanabilecek birçok doğrulama tipi vardır. Eğer doğrulamanın açılır menü olup olmadığını kontrol etmek istiyorsanız, [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) yöntemi kullanılabilir. Aşağıdaki örnek bu özelliğin kullanımını gösterir. Test amaçlı bir dosya aşağıdaki bağlantıdan indirilebilir:  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **Mevcut Doğrulama Alanına Hücre Alanı Ekle**  

Mevcut [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)'ye [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) eklemek isteyebileceğiniz durumlar olabilir. [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-) kullanılarak [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) eklediğinizde, Aspose.Cells tüm mevcut alanları kontrol eder ve yeni alan zaten varsa tespit eder. Eğer dosyada çok sayıda doğrulama varsa, bu performansı olumsuz etkileyebilir. Bunu aşmak için API [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) metodunu sağlar. *checkIntersection* parametresi, verilen alan ile mevcut doğrulama alanlarının kesişip kesişmeyeceğini gösterir. Bunu **false** yaparsanız, diğer alanların kontrolü devre dışı kalır. *checkEdge* parametresi, ilgili alanların kontrollerini belirtir. Eğer yeni alan en üstsol alan ise, iç ayarlar yeniden oluşturulur. Eğer yeni alanın en üstsol alan olmadığına eminseniz, bu parametreyi **false** olarak ayarlayabilirsiniz.  

Aşağıdaki kod parçacığı, [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) metodunun mevcut [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation)'ye yeni [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) eklemesinde kullanımını gösterir.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

Kaynak ve çıktı excel dosyaları referans için ekte sunulmuştur.  

[Kaynak Dosyası](96928093.xlsx)  

[Çıkış Dosyası](96928220.xlsx)  

## **Gelişmiş Konular**  
- [ODS Dosyalarında Hücre Doğrulamasını Al](/cells/tr/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Bir Hücreye Uygulanan Doğrulamayı Al](/cells/tr/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulama](/cells/tr/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
