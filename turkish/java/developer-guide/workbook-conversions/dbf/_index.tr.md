---
title: DBF Dosyalarını Okuma ve Yazma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Java kütüphanesidir ve dBASE III ve IV (DBF) dosyalarını okuma ve yazma desteği sunar. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve bu dosyalara veri dışa aktarma işlemlerini, dosya formatı ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklamaktadır.
keywords: Aspose.Cells, Java kütüphanesi, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya formatı, .dbf
type: docs
weight: 200
url: /tr/java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma için tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, Aspose.Cells'in zengin API'sini kullanarak verileri işleyebilir ve çalışma kitabını eski veritabanı uygulamalarında kullanılmak üzere DBF formatında geri kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File), başlangıçta 1980'lerin başında dBASE tarafından tanıtılan eski bir veritabanı dosya formatıdır. Formatın yaşına rağmen, DBF dosyaları özellikle muhasebe, CBS ve diğer özel uygulamalar olmak üzere yapılandırılmış verileri depolamak için birçok sektörde hâlâ yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern Java elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenize olanak tanır.

Kütüphane hem DBF dosyalarını okuma hem de yazma desteği sunar ve size şu yetenekleri sağlar:

- Mevcut DBF dosyalarından verileri Aspose.Cells Workbook nesnelerine içe aktararak daha fazla işleme veya diğer formatlara dönüştürme.
- Sıfırdan veya diğer elektronik tablo formatlarındaki verileri dönüştürerek yeni DBF dosyaları oluşturma.
- DBF formatına giren ve çıkan verilerde alan tanımlarını, veri türlerini ve kayıt yapılarını koruma.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir, bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü haline getirir.

## **Desteklenen DBF Sürümleri ve Özellikleri**

Aspose.Cells aşağıdaki DBF formatı sürümlerini destekler:

- **dBASE III** — DBF formatının orijinal ve en yaygın desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane, aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtlar ve alan tanımları korunarak DBF verilerinin bir Workbook nesnesine okunması.
- Çalışma kitabı verilerinin dBASE uyumlu uygulamalara dışa aktarım için DBF formatına geri yazılması.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerinin işlenmesi.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarının korunması.

### Sınırlamalar ve Dikkat Edilmesi Gerekenler**

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları aklınızda bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayt**tır.
- Alan adları en fazla **10 karakter** ile sınırlıdır, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYAAGG` formatında saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, bir DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi oldukça kolay hale getirir. Kütüphane, kaynak formatı belirtmek için `LoadOptions` sınıfını kullanır ve verilerin yükleme işlemi sırasında doğru şekilde yorumlanmasını sağlar.

### Aspose.Cells ile DBF Dosyası Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `LoadFormat` özelliğini `LoadFormat.Dbf` olarak ayarlamanız ve onu dosya yolu ile birlikte `Workbook` yapıcısına iletmeniz gerekir. Yüklendikten sonra, verilere `getWorksheets()` koleksiyonu aracılığıyla erişilebilir; burada hücreler arasında yineleme yapabilir, değerleri çıkarabilir veya verileri gerektiği gibi işleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını göstermektedir.

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();

LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

StringBuilder sb = new StringBuilder();

int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}

System.out.println(sb.toString());

String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);

System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

DBF dosyalarını doğrudan Microsoft Excel'de, Dosya Aç iletişim kutusunda dosyayı seçerek açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo olarak değerlendirecek ve kayıtlarını tablo biçiminde görüntüleyecektir. Bu, Aspose.Cells ile okuma veya yazma işleminden sonra verileri hızlı bir şekilde doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

Bir DBF dosyasına veri yazma, Aspose.Cells ile herhangi bir elektronik tablo formatını kaydetmeye benzer bir örüntü izler. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef format olarak `SaveFormat.Dbf` belirterek `save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için şu adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `getWorksheets()` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.Dbf` parametrelerini geçirerek `Workbook.save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını göstermektedir. DBF formatına dışa aktarım sırasında alan türlerinin nasıl işlendiğini göstermek için farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle bir çalışma sayfası doldurur.

```java
import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;

String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();

if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();

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
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());

// Veri satırı 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());

// Veri satırı 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());

// Veri satırı 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());

// Veri satırı 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());

// Daha iyi okunabilirlik için sütun genişliklerini ayarla
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, SaveFormat.DBF);
```

{{% alert color="primary" %}}

Bir DBF dosyasına veri yazarken, verilerinizin formatın sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYAAGG formatında temsil edilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilecek Hususlar**

Aspose.Cells ile DBF formatı arasında veri aktarımı sırasında, veri bütünlüğünü sağlamak için veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydetme sırasında otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler** karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tamsayılar ve ondalıklar) sayısal (N) alanlarına eşlenir.
- **Tarih değerleri** `YYYYAAGG` formatında tarih (D) alanlarına eşlenir.
- **Boole değerleri** mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler, ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum 10 karakter uzunluğunda.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakter içeremez.
- Girişte kullanılan büyük/küçük harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktının Doğrulanması

Bir DBF dosyası yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, alan adlarının sütun başlıkları olduğu ve kayıtların sağladığınız verilere göre doldurulduğu tablo biçiminde görünmelidir.

## **DBF ve Diğer Formatlar Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okuma ve yazmanın en pratik kullanım alanlarından biri, verileri DBF formatı ile XLSX, XLS veya CSV gibi modern elektronik tablo formatları arasında dönüştürmektir. Aspose.Cells geniş bir format yelpazesini desteklediğinden, bir DBF dosyasını kolayca yükleyebilir ve desteklenen herhangi bir formatta yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtım için sonucu bir XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasındaki verileri alıp eski sistemlerle entegrasyon için DBF formatına dışa aktarabilirsiniz.



{{< app/cells/assistant language="java" >}}