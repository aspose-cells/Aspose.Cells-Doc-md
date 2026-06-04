---
title: DBF Dosyalarını Okuma ve Yazma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kütüphanesidir ve dBASE III ve IV (DBF) dosyalarını okuma ve yazma desteği sunar. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve bu dosyalara veri dışa aktarma işlemlerini, dosya biçimi ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklamaktadır.
keywords: Aspose.Cells, C++ kütüphanesi, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya biçimi, .dbf
type: docs
weight: 200
url: /tr/cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma konusunda tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, Aspose.Cells'in zengin API'sini kullanarak verileri düzenleyebilir ve çalışma kitabını eski veritabanı uygulamalarıyla kullanılmak üzere DBF biçiminde geri kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File - Veritabanı Dosyası), 1980'lerin başında dBASE tarafından tanıtılan eski bir veritabanı dosya biçimidir. Biçimin eskiliğine rağmen, DBF dosyaları yapılandırılmış verileri depolamak için muhasebe, CBS ve diğer özel uygulamalar başta olmak üzere birçok sektörde hâlâ yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern C++ elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenizi sağlar.

Kütüphane, hem DBF dosyalarını okuma hem de yazma desteği sunarak size şu yetenekleri sağlar:

- Daha fazla işleme veya diğer biçimlere dönüştürme amacıyla mevcut DBF dosyalarındaki verileri Aspose.Cells Workbook nesnelerine aktarma.
- Sıfırdan veya diğer elektronik tablo biçimlerinden veri dönüştürerek yeni DBF dosyaları oluşturma.
- Verileri DBF biçimine girerken ve çıkarken alan tanımlarını, veri türlerini ve kayıt yapılarını koruma.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir; bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü haline getirir.

## **Desteklenen DBF Sürümleri ve Özellikler**

Aspose.Cells aşağıdaki DBF biçim sürümlerini destekler:

- **dBASE III** — DBF biçiminin orijinal ve en yaygın desteklenen varyantı.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane, aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtların ve alan tanımlarının korunduğu DBF verilerini bir Workbook nesnesine okuma.
- dBASE uyumlu uygulamalara dışa aktarmak için çalışma kitabı verilerini DBF biçimine geri yazma.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerini işleme.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarını koruma.

### **Sınırlamalar ve Dikkat Edilmesi Gerekenler**

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları göz önünde bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayttır**.
- Alan adları en fazla **10 karakter** ile sınırlıdır, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYMMDD` biçiminde saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, bir DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi kolaylaştırır. Kütüphane, kaynak biçimi belirtmek için `LoadOptions` sınıfını kullanır ve verilerin yükleme işlemi sırasında doğru yorumlanmasını sağlar.

### Aspose.Cells ile DBF Dosyası Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `LoadFormat` özelliğini `LoadFormat.Dbf` olarak ayarlamanız ve dosya yoluyla birlikte `Workbook` yapıcısına iletmeniz gerekir. Yüklendikten sonra, verilere `Worksheets` koleksiyonu aracılığıyla erişilebilir; burada hücreleri yineleyebilir, değerleri çıkarabilir veya gerektiğinde verileri düzenleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını göstermektedir.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

DBF dosyalarını doğrudan Microsoft Excel'de, Dosya Aç iletişim kutusunda dosyayı seçerek açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo olarak değerlendirecek ve kayıtlarını tablo biçiminde görüntüleyecektir. Bu, Aspose.Cells ile okuma veya yazma işleminden sonra verileri hızlıca doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

DBF dosyasına veri yazma işlemi, Aspose.Cells ile herhangi bir elektronik tablo biçimini kaydetmeye benzer bir örüntü izler. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef biçim olarak `SaveFormat.Dbf` belirterek `Save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için aşağıdaki adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `Worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.Dbf` parametre olarak geçirerek `Workbook.Save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını göstermektedir. DBF biçimine dışa aktarırken alan türlerinin nasıl işlendiğini göstermek için farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle bir çalışma sayfası doldurur.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Sütun başlıkları
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // Veri satırı 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // Veri satırı 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // Veri satırı 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // Veri satırı 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // Veri satırı 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // Daha iyi okunabilirlik için sütun genişliklerini ayarla
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

DBF dosyasına veri yazarken, verilerinizin biçimin sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYMMDD biçiminde gösterilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilecek Hususlar**

Aspose.Cells ile DBF biçimi arasında veri aktarırken, veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak, veri bütünlüğünü sağlamak için önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydederken otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler**, karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tamsayılar ve ondalık sayılar), sayısal (N) alanlarına eşlenir.
- **Tarih değerleri**, `YYYYMMDD` biçiminde tarih (D) alanlarına eşlenir.
- **Boole değerleri**, mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler; ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum uzunluk 10 karakterdir.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakterler içeremez.
- Girişte kullanılan büyük/küçük harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktıyı Doğrulama

Bir DBF dosyasını yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, alan adlarının sütun başlıkları olarak yer aldığı ve sağladığınız verilere göre kayıtların doldurulduğu tablo biçiminde görünmelidir.

## **DBF ve Diğer Biçimler Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okumanın ve yazmanın en pratik kullanım alanlarından biri, verileri DBF biçimi ile XLSX, XLS veya CSV gibi modern elektronik tablo biçimleri arasında dönüştürmektir. Aspose.Cells çok çeşitli biçimleri desteklediğinden, bir DBF dosyasını kolayca yükleyebilir ve desteklenen herhangi bir biçimde yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtmak için sonucu XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasındaki verileri alıp eski sistemlerle entegrasyon için DBF biçiminde dışa aktarabilirsiniz.



{{< app/cells/assistant language="cpp" >}}