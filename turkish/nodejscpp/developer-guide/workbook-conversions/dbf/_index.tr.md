---
title: DBF Dosyalarını Okuma ve Yazma
description: Aspose.Cells for Node.js via C++, elektronik tablo dosyalarıyla çalışmak için kullanılan ve dBASE III ve IV (DBF) dosyalarını okuma ve yazmayı destekleyen bir kütüphanedir. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve dışa aktarma işlemlerini, dosya biçimi ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklamaktadır.
keywords: Aspose.Cells, Node.js via C++, DBF, dBASE, DBF oku, DBF yaz, DBF içe aktar, DBF dışa aktar, dosya biçimi, .dbf
type: docs
weight: 200
url: /tr/nodejs-cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma için tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, zengin Aspose.Cells API'sini kullanarak verileri düzenleyebilir ve çalışma kitabını eski veritabanı uygulamalarıyla kullanılmak üzere tekrar DBF biçiminde kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File), başlangıçta 1980'lerin başında dBASE tarafından kullanıma sunulmuş eski bir veritabanı dosya biçimidir. Biçimin eski olmasına rağmen, DBF dosyaları özellikle muhasebe, CBS ve diğer özel uygulamalar olmak üzere yapılandırılmış verileri depolamak için birçok sektörde hâlâ yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern Node.js via C++ elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenize olanak tanır.

Kütüphane, hem DBF dosyalarını okuma hem de yazma desteği sunarak size aşağıdaki olanakları sağlar:

- DBF dosyalarından verileri, daha fazla işleme veya diğer biçimlere dönüştürme amacıyla Aspose.Cells Workbook nesnelerine içe aktarın.
- Sıfırdan veya diğer elektronik tablo biçimlerinden veri dönüştürerek yeni DBF dosyaları oluşturun.
- DBF biçiminden veri aktarırken ve bu biçime veri aktarırken alan tanımlarını, veri türlerini ve kayıt yapılarını koruyun.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir; bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü haline getirir.

## **Desteklenen DBF Sürümleri ve Özellikleri**

Aspose.Cells aşağıdaki DBF biçim sürümlerini destekler:

- **dBASE III** — DBF biçiminin orijinal ve en yaygın desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane, aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtlar ve alan tanımları korunarak DBF verilerinin bir Workbook nesnesine okunması.
- dBASE uyumlu uygulamalara dışa aktarmak için çalışma kitabı verilerinin tekrar DBF biçiminde yazılması.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerinin işlenmesi.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarının korunması.

### Sınırlamalar ve Dikkat Edilmesi Gerekenler

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları aklınızda bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayttır**.
- Alan adları **10 karakterle** sınırlıdır, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYAAGG` biçiminde saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, bir DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi oldukça kolay hale getirir. Kütüphane, kaynak biçimi belirtmek için `LoadOptions` sınıfını kullanır ve yükleme işlemi sırasında verilerin doğru yorumlanmasını sağlar.

### Aspose.Cells ile DBF Dosyası Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `LoadFormat` özelliğini `LoadFormat.Dbf` olarak ayarlamanız ve dosya yoluyla birlikte `Workbook` yapıcısına geçirmeniz gerekir. Yüklendikten sonra, verilere `Worksheets` koleksiyonu aracılığıyla erişilebilir; burada hücreler arasında yineleme yapabilir, değerleri çıkarabilir veya gerektiğinde verileri düzenleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını göstermektedir.

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
    sb += "|" + "\n";
}

console.log(sb);

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

DBF dosyalarını, Open (Aç) iletişim kutusunda dosyayı seçerek doğrudan Microsoft Excel'de açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo gibi değerlendirerek kayıtlarını tablo düzeninde görüntüleyecektir. Bu, Aspose.Cells ile okuduktan veya yazdıktan sonra verileri hızlı bir şekilde doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

DBF dosyasına veri yazma işlemi, Aspose.Cells ile herhangi bir elektronik tablo biçimini kaydetmeye benzer bir kalıp izler. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef biçim olarak `SaveFormat.Dbf` belirterek `save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için şu adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `Worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.Dbf` parametrelerini geçirerek `workbook.save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını göstermektedir. DBF biçimine dışa aktarırken alan türlerinin nasıl işlendiğini göstermek için farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle bir çalışma sayfasını doldurur.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");
const fs = require("fs");

const outputDir = "C:\\Output\\";
const filePath = path.join(outputDir, "output.dbf");

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

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

DBF dosyasına veri yazarken, verilerinizin biçimin sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYAAGG biçiminde temsil edilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilecek Hususlar**

Aspose.Cells ile DBF biçimi arasında veri aktarırken, veri bütünlüğünü sağlamak için veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydederken otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler** karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tamsayılar ve ondalık sayılar) sayısal (N) alanlarına eşlenir.
- **Tarih değerleri** `YYYYAAGG` biçiminde tarih (D) alanlarına eşlenir.
- **Boole değerleri** mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler, ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum uzunluk 10 karakterdir.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakter içeremez.
- Girişte kullanılan büyük/küçük harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktının Doğrulanması

Bir DBF dosyası yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, alan adlarının sütun başlıkları olduğu ve sağladığınız verilere göre kayıtların doldurulduğu tablo düzeninde görünmelidir.

## **DBF ve Diğer Biçimler Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okumanın ve yazmanın en pratik kullanım alanlarından biri, verileri DBF biçimi ile XLSX, XLS veya CSV gibi modern elektronik tablo biçimleri arasında dönüştürmektir. Aspose.Cells çok çeşitli biçimleri desteklediğinden, bir DBF dosyasını kolayca yükleyebilir ve desteklenen herhangi bir başka biçimde yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtmak üzere sonucu bir XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasından veri alabilir ve eski sistemlerle entegrasyon için bunu DBF biçiminde dışa aktarabilirsiniz.



{{< app/cells/assistant language="javascript" >}}