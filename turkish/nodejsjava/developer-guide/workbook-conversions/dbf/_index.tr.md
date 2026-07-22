---
title: DBF Dosyalarını Okuma ve Yazma
linktitle: DBF Dosyalarını Okuma ve
description: Aspose.Cells for Node.js via Java, elektronik tablo dosyalarıyla çalışmak için bir kütüphanedir ve dBASE III ve IV (DBF) dosyalarını okuma ve yazma desteği sunar. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve DBF dosyalarına veri dışa aktarma işlemlerini, dosya biçimi ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklar.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya biçimi, .dbf
type: docs
weight: 200
url: /tr/nodejs-java/reading-and-writing-dbf-files/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma konusunda tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, zengin Aspose.Cells API'sini kullanarak verileri düzenleyebilir ve çalışma kitabını eski veritabanı uygulamalarıyla kullanılmak üzere tekrar DBF biçiminde kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File), başlangıçta 1980'lerin başında dBASE tarafından sunulan eski bir veritabanı dosya biçimidir. Biçimin yaşına rağmen, DBF dosyaları özellikle muhasebe, CBS ve diğer özel uygulamalar olmak üzere yapılandırılmış verileri depolamak için birçok sektörde hâlâ yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern Node.js elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenize olanak tanır.

Kütüphane hem DBF dosyalarını okuma hem de yazma desteği sunarak size şu yetenekleri sağlar:

- Mevcut DBF dosyalarındaki verileri, daha fazla işleme veya diğer biçimlere dönüştürme için Aspose.Cells Workbook nesnelerine içe aktarın.
- Sıfırdan veya diğer elektronik tablo biçimlerinden veri dönüştürerek yeni DBF dosyaları oluşturun.
- DBF biçimine giriş ve çıkış veri aktarımı sırasında alan tanımlarını, veri türlerini ve kayıt yapılarını koruyun.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir; bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü haline getirir.

## **Desteklenen DBF Sürümleri ve Özellikler**

Aspose.Cells aşağıdaki DBF biçim sürümlerini destekler:

- **dBASE III** — DBF biçiminin özgün ve en yaygın desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtlar ve alan tanımları korunarak DBF verilerinin bir Workbook nesnesine okunması.
- dBASE uyumlu uygulamalara dışa aktarma için çalışma kitabı verilerinin tekrar DBF biçiminde yazılması.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerinin işlenmesi.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarının korunması.

### Sınırlamalar ve Dikkat Edilmesi Gerekenler

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları aklınızda bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayt**tır.
- Alan adları **10 karakter** ile sınırlıdır, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYMMDD` biçiminde saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, bir DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi kolaylaştırır. Kütüphane, kaynak biçimi belirtmek için `LoadOptions` sınıfını kullanarak verilerin yükleme işlemi sırasında doğru şekilde yorumlanmasını sağlar.

### Aspose.Cells ile DBF Dosyası Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `LoadFormat` özelliğini `LoadFormat.DBF` olarak ayarlamanız ve dosya yoluyla birlikte `Workbook` yapıcısına iletmeniz gerekir. Yüklendikten sonra, verilere `Worksheets` koleksiyonu aracılığıyla erişilebilir; burada hücreler arasında yineleme yapabilir, değerleri çıkarabilir veya verileri gerektiği gibi düzenleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını gösterir.

```javascript
let sb = "";

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb += "|" + value;
    }
    sb += "|\n";
}

console.log(sb);

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

DBF dosyalarını doğrudan Microsoft Excel'de, Dosya Aç iletişim kutusunda dosyayı seçerek açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo olarak değerlendirecek ve kayıtlarını tablo düzeninde görüntüleyecektir. Bu, Aspose.Cells ile okuma veya yazma sonrasında verileri hızlıca doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

Bir DBF dosyasına veri yazmak, Aspose.Cells ile herhangi bir elektronik tablo biçimini kaydetmeye benzer bir model izler. Bir Workbook oluşturur veya yükler, çalışma sayfasını verilerle doldurur ve ardından hedef biçim olarak `SaveFormat.DBF` belirterek `save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için şu adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `Worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.DBF` parametre olarak geçirerek `Workbook.save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını gösterir. DBF biçimine dışa aktarırken alan türlerinin nasıl işlendiğini göstermek için çalışma sayfasını farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle doldurur.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Sütun başlıkları
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Veri satırı 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// Veri satırı 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// Veri satırı 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// Veri satırı 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// Veri satırı 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// Daha iyi okunabilirlik için sütun genişliklerini ayarla
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Bir DBF dosyasına veri yazarken, verilerinizin biçimin sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYMMDD biçiminde temsil edilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilecek Noktaları**

Aspose.Cells ile DBF biçimi arasında veri aktarımı yaparken, veri bütünlüğünü sağlamak için veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydederken otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler**, karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tamsayılar ve ondalıklar), sayısal (N) alanlarına eşlenir.
- **Tarih değerleri**, `YYYYMMDD` biçiminde tarih (D) alanlarına eşlenir.
- **Boole değerleri**, mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler, ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum 10 karakter uzunluğunda.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakter içeremez.
- Girişte kullanılan büyük/küçük harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktının Doğrulanması

Bir DBF dosyasını yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, sütun başlıkları olarak alan adları ve sağladığınız verilere göre doldurulmuş kayıtlarla tablo düzeninde görünmelidir.

## **DBF ve Diğer Biçimler Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okuma ve yazmanın en pratik kullanım örneklerinden biri, verileri DBF biçimi ile XLSX, XLS veya CSV gibi modern elektronik tablo biçimleri arasında dönüştürmektir. Aspose.Cells çok çeşitli biçimleri desteklediğinden, bir DBF dosyasını kolayca yükleyebilir ve desteklenen herhangi bir başka biçimde yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtmak için sonucu bir XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasından veri alabilir ve eski sistemlerle entegrasyon için DBF biçiminde dışa aktarabilirsiniz.



{{< app/cells/assistant language="javascript" >}}