---
title: DBF Dosyalarını Okuma ve Yazma
linktitle: DBF Dosyalarını Okuma ve
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kütüphanesidir ve dBASE III ve IV (DBF) dosyalarını okuma ve yazma desteği sunar. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve DBF dosyalarına veri dışa aktarma işlemlerini, dosya formatı ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklar.
keywords: Aspose.Cells, .NET kütüphanesi, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya formatı, .dbf
type: docs
weight: 200
url: /tr/net/reading-and-writing-dbf-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma için tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, Aspose.Cells'in zengin API'sini kullanarak verileri düzenleyebilir ve çalışma kitabını eski veritabanı uygulamalarıyla kullanılmak üzere tekrar DBF formatında kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File), 1980'lerin başında dBASE tarafından kullanıma sunulan eski bir veritabanı dosya formatıdır. Formatın eskiliğine rağmen, DBF dosyaları birçok sektörde yapılandırılmış verileri depolamak için yaygın olarak kullanılmaya devam etmektedir; özellikle muhasebe, CBS ve diğer özel uygulamalarda. Aspose.Cells, bu eski dosyaları modern .NET elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenize olanak tanır.

Kütüphane, hem DBF dosyalarını okuma hem de yazma desteği sunar ve size şu yetenekleri sağlar:

- Mevcut DBF dosyalarındaki verileri, daha fazla işleme veya diğer formatlara dönüştürme için Aspose.Cells Workbook nesnelerine içe aktarma.
- Sıfırdan veya diğer elektronik tablo formatlarından veri dönüştürerek yeni DBF dosyaları oluşturma.
- Verileri DBF formatına içe ve dışa aktarırken alan tanımlarını, veri türlerini ve kayıt yapılarını koruma.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir, bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü haline getirir.

## **Desteklenen DBF Sürümleri ve Özellikler**

Aspose.Cells aşağıdaki DBF formatı sürümlerini destekler:

- **dBASE III** — DBF formatının orijinal ve en yaygın desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane, aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtlar ve alan tanımları korunarak DBF verilerinin bir Workbook nesnesine okunması.
- Çalışma kitabı verilerinin dBASE uyumlu uygulamalara dışa aktarım için tekrar DBF formatına yazılması.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerinin işlenmesi.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarının korunması.

### Sınırlamalar ve Dikkat Edilecek Hususlar

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları aklınızda bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayt**'tır.
- Alan adları en fazla **10 karakter** uzunluğunda olabilir, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYAAGG` formatında saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, bir DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi kolaylaştırır. Kütüphane, kaynak formatı belirtmek için `LoadOptions` sınıfını kullanır ve verilerin yükleme işlemi sırasında doğru şekilde yorumlanmasını sağlar.

### Aspose.Cells ile DBF Dosyası Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `LoadFormat` özelliğini `LoadFormat.Dbf` olarak ayarlamanız ve dosya yolu ile birlikte `Workbook` yapıcısına iletmeniz gerekir. Yüklendikten sonra, verilere `Worksheets` koleksiyonu üzerinden erişilebilir; burada hücreler arasında yineleme yapabilir, değerleri çıkarabilir veya verileri gerektiği gibi işleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını gösterir.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

DBF dosyalarını doğrudan Microsoft Excel'de, Dosya Aç iletişim kutusunda dosyayı seçerek açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo olarak değerlendirecek ve kayıtlarını tablo şeklinde bir düzende görüntüleyecektir. Bu, Aspose.Cells ile okuma veya yazma işleminden sonra verileri hızlıca doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

DBF dosyasına veri yazmak, Aspose.Cells ile başka herhangi bir elektronik tablo formatını kaydetmeye benzer bir kalıp izler. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef format olarak `SaveFormat.Dbf` belirterek `Save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için şu adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `Worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.Dbf` parametre olarak ileterek `Workbook.Save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını gösterir. DBF formatına dışa aktarırken alan türlerinin nasıl işlendiğini göstermek için çalışma sayfasını farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle doldurur.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// Sütun başlıkları
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// Veri satırı 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// Veri satırı 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// Veri satırı 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// Veri satırı 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// Veri satırı 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// Daha iyi okunabilirlik için sütun genişliklerini ayarla
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Bir DBF dosyasına veri yazarken, verilerinizin formatın sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYAAGG formatında temsil edilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilecek Hususlar**

Verileri Aspose.Cells ile DBF formatı arasında aktarırken, veri bütünlüğünü sağlamak için veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydetme sırasında otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler** karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tam sayılar ve ondalık sayılar) sayısal (N) alanlarına eşlenir.
- **Tarih değerleri** `YYYYAAGG` formatında tarih (D) alanlarına eşlenir.
- **Mantıksal değerler** mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler; ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum uzunluk 10 karakterdir.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakter içeremez.
- Girişte kullanılan büyük/küçük harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktının Doğrulanması

Bir DBF dosyasını yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, sütun başlıkları olarak alan adları ve sağladığınız verilere göre doldurulmuş kayıtlarla tablo şeklinde bir düzende görünmelidir.

## **DBF ve Diğer Formatlar Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okuma ve yazmanın en pratik kullanım senaryolarından biri, verileri DBF formatı ile XLSX, XLS veya CSV gibi modern elektronik tablo formatları arasında dönüştürmektir. Aspose.Cells geniş bir format yelpazesini desteklediğinden, bir DBF dosyasını kolayca yükleyip desteklenen herhangi bir başka formatta yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından sonucu modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtım için bir XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasındaki verileri alıp eski sistemlerle entegrasyon için DBF formatına dışa aktarabilirsiniz.



{{< app/cells/assistant language="csharp" >}}