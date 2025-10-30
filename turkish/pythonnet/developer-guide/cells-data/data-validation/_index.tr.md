---
title: Veri Doğrulama
type: docs
weight: 90
url: /tr/python-net/data-validation/
description: Aspose.Cells için Python via .NET API si aracılığıyla veri doğrulama nasıl eklenir öğrenin.
keywords: Python Excel Kütüphanesi, Python Veri Doğrulama Ekle, Python Doğrulama Değerini Al, Python Tamsayı Veri Doğrulama Ekle, Python Liste Veri Doğrulama Ekle, Python Tarih Veri Doğrulama Ekle, Python Zaman Veri Doğrulama Ekle, Python Metin Uzunluğu Veri Doğrulama Ekle, Varolan Doğrulamaya Python Hücre Alanı Ekle, Hücrede doğrulamanın açılır menü olduğunu nasıl kontrol edebilirsiniz?, Özel Doğrulama Ekle  
---

{{% alert color="primary" %}}

Microsoft Excel, çalışsayadaki verileri otomatik olarak filtreleme veya doğrulama özellikleri sağlar. Aspose.Cells için Python via .NET, Microsoft Excel'in veri doğrulama ve Otomatik Filtre özelliklerini tamamen destekler. Bu makale, Microsoft Excel'deki özellikleri nasıl kullanacağınızı ve bunları Aspose.Cells için Python via .NET kullanarak nasıl kodlayacağınızı açıklar.

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

### **Python Excel Kütüphanesi Aspose.Cells ile Veri Doğrulaması**

Veri doğrulaması, çalışma tablolarına girilen bilgileri doğrulamak için güçlü bir özelliktir. Veri doğrulaması ile geliştiriciler, kullanıcılara bir liste seçeneği sunabilir, veri girişlerini belirli bir tür veya boyuta sınırlayabilir, vb.
Python via .NET için Aspose.Cells'te her [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfının bir [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) özelliği vardır, bu özellik bir [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) nesneler koleksiyonunu temsil eder. Doğrulama ayarlamak için şu şekilde bazı [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) sınıfın özelliklerini ayarlayın:

- tip - doğrulama tipini temsil eder, bu, [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) numaralandırmasındaki önceden tanımlanmış değerlerden birini kullanarak belirtilebilir.
- Operatör - doğrulamada kullanılacak operatörü temsil eder, bu, [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype) numaralandırmasındaki önceden tanımlanmış değerlerden birini kullanarak belirtilebilir.
- formül1 - veri doğrulamasının ilk kısmı ile ilişkilendirilen değeri veya ifadeyi temsil eder.
- formül2 - veri doğrulamasının ikinci kısmı ile ilişkilendirilen değeri veya ifadeyi temsil eder.

[**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) nesnesinin özellikleri yapılandırıldığında, geliştiriciler oluşturulan doğrulamayı kullanarak doğrulanacak hücre aralığı hakkında bilgileri depolamak için [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) yapısını kullanabilir.

#### **Veri Doğrulama Türleri**

[**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) numaralandırmasının aşağıdaki üyeleri bulunmaktadır:

|**Üye Adı**|**Açıklama**|
| :- | :- |
|ANY_VALUE| Herhangi bir türden bir değeri belirtir.
|WHOLE_NUMBER| Tamsayılar için doğrulama tipini belirtir.
|ONDALIK|Ondalık sayılar için doğrulama tipini belirtir.
|LİSTE|Açılır kutu listesi için doğrulama tipini belirtir.
|DATE| Tarihler için doğrulama tipini belirtir.
|ZAMAN|Zaman için doğrulama tipini belirtir.
|TEXT_LENGTH| Metnin uzunluğu için doğrulama tipini belirtir.
|ÖZEL|Özel doğrulama tipini belirtir.

##### **Tamsayı Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralık içinde yalnızca tamsayılar girebilir. Aşağıdaki kod örnekleri, Tamsayı doğrulama tipini uygulamanın nasıl yapıldığını göstermektedir. Örnek, Microsoft Excel üzerinde oluşturduğumuz aynı veri doğrulamasını Aspose.Cells for Python via .NET kullanarak oluşturur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **Liste Veri Doğrulaması**

Bu tür doğrulama, kullanıcının bir açılır kutu listesinden değerler girmesine izin verir. Bu, veri içeren bir dizi satırın bir listesini sağlar. Örnekte, listedeki kaynağı tutmak için ikinci bir çalışma tablosu eklenir. Kullanıcılar yalnızca listeden değer seçebilir. Doğrulama alanı, birinci çalışma tablosundaki A1:A5 hücre aralığıdır.

Burada önemli olan nokta, [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) özelliğini **true** olarak ayarlamanızdır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **Tarih Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan tarih değerlerini doğrulanmış hücrelere girerler. Örnekte, kullanıcının 1970 ila 1999 arasında tarih girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **Zaman Veri Doğrulaması**

Bu tür doğrulama ile, kullanıcılar belirli bir aralıkta veya belirli kriterlere uyan saatleri doğrulanmış hücrelere girebilirler. Örnekte, kullanıcının 09:00 ile 11:30 arasında zaman girmesi kısıtlanmıştır. Burada doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **Metin Uzunluğu Veri Doğrulaması**

Bu tür doğrulama ile kullanıcılar, doğrulanan hücrelere belirli bir uzunluktaki metin değerlerini girebilirler. Örnekte, kullanıcıya en fazla 5 karakter içeren dize değerlerini girmesi engellenir. Doğrulama alanı B1 hücresidir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **Veri Doğrulama Kuralları**

Veri doğrulamaları uygulandığında, doğrulamanın farklı değerlerle kontrol edilebilir olması sağlanır. [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) doğrulama sonucunu almak için kullanılabilir. Aşağıdaki örnek, farklı değerlerle bu özelliği göstermektedir. Test için örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **Hücrede doğrulamanın açılır menü olup olmadığını kontrol et**

Gördüğümüz gibi bir hücre içinde uygulanabilecek birçok doğrulama türü bulunmaktadır. Doğrulamanın açılır menü olup olmadığını kontrol etmek istiyorsanız, [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) özelliği bunu test etmek için kullanılabilir. Aşağıdaki örnek kod, bu özelliğin kullanımını göstermektedir. Test için örnek bir dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **Mevcut Doğrulama Alanına Hücre Alanı Ekle**

Mevcut [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)'e [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) eklemek isteyebileceğiniz durumlar olabilir. Yeni alanı eklerken [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea) kullanarak [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) eklerseniz, Aspose.Cells, yeni alanın zaten var olup olmadığını kontrol etmek için tüm mevcut alanları kontrol eder. Dosyada çok sayıda doğrulama varsa, bu performansı olumsuz etkiler. Bunu aşmak için API, [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) yöntemini sağlar. *checkIntersection* parametresi, verilen alanın mevcut doğrulama alanlarıyla kesişimini kontrol edip etmeyeceğini belirtir. **false** ayarlamak diğer alanların kontrolünü devre dışı bırakır. *checkEdge* parametresi, uygulanan alanların kontrol edilip edilmeyeceğini belirtir. Yeni alanın sol üst alan olması durumunda iç ayarlar yeniden oluşturulur. Yeni alanın sol üst alan olmadığından eminseniz, bu parametreyi **false** olarak ayarlayabilirsiniz.

Aşağıdaki kod örneği, mevcut [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation)'e yeni [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) eklemek için [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) yönteminin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

Kaynak ve çıktı excel dosyaları referans için ekte sunulmuştur.

[Kaynak Dosyası](96928093.xlsx)

[Çıkış Dosyası](96928220.xlsx)


## **Gelişmiş Konular**
- [ODS Dosyalarında Hücre Doğrulamasını Al](/cells/tr/python-net/get-cell-validation-in-ods-files/)
- [Bir Hücreye Uygulanan Doğrulamayı Al](/cells/tr/python-net/get-validation-applied-on-a-cell/)
- [Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulama](/cells/tr/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="python-net" >}}
