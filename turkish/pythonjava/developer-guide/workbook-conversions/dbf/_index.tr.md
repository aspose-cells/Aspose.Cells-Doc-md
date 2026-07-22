---
title: DBF Dosyalarını Okuma ve Yazma
linktitle: DBF Dosyalarını Okuma ve
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için Python via Java kütüphanesidir ve dBASE III ve IV (DBF) dosyalarını okuma ve yazma desteği sunar. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve DBF dosyalarına veri dışa aktarma işlemlerini, dosya formatı ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklar.
keywords: Aspose.Cells, Python via Java kütüphanesi, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya formatı, .dbf
type: docs
weight: 200
url: /tr/python-java/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma için tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, zengin Aspose.Cells API'sini kullanarak verileri düzenleyebilir ve çalışma kitabını eski veritabanı uygulamalarıyla kullanılmak üzere tekrar DBF formatında kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File), başlangıçta 1980'lerin başında dBASE tarafından tanıtılan eski bir veritabanı dosya formatıdır. Formatın eskiliğine rağmen, DBF dosyaları birçok sektörde, özellikle muhasebe, CBS ve diğer özel uygulamalarda yapılandırılmış verileri depolamak için hala yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern Python via Java elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenizi sağlar.

Kütüphane hem DBF dosyalarını okuma hem de yazma desteği sunar ve size şu yetenekleri sağlar:

- Mevcut DBF dosyalarındaki verileri, daha fazla işleme veya diğer formatlara dönüştürme için Aspose.Cells Workbook nesnelerine içe aktarın.
- Sıfırdan veya diğer elektronik tablo formatlarındaki verileri dönüştürerek yeni DBF dosyaları oluşturun.
- Verileri DBF formatına girerken ve çıkarken alan tanımlarını, veri türlerini ve kayıt yapılarını koruyun.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir, bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü yapar.

## **Desteklenen DBF Sürümleri ve Özellikler**

Aspose.Cells aşağıdaki DBF format sürümlerini destekler:

- **dBASE III** — DBF formatının orijinal ve en yaygın desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane, aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtlar ve alan tanımları korunarak DBF verilerinin bir Workbook nesnesine okunması.
- dBASE uyumlu uygulamalara dışa aktarma için çalışma kitabı verilerinin tekrar DBF formatına yazılması.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerinin işlenmesi.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarının korunması.

### Sınırlamalar ve Dikkat Edilmesi Gerekenler

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları aklınızda bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayttır**.
- Alan adları **10 karakterle** sınırlıdır, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYAAGG` formatında saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, bir DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi oldukça kolay hale getirir. Kütüphane, kaynak formatı belirtmek için `LoadOptions` sınıfını kullanır ve yükleme işlemi sırasında verilerin doğru şekilde yorumlanmasını sağlar.

### Aspose.Cells ile DBF Dosyası Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `LoadFormat` özelliğini `LoadFormat.Dbf` olarak ayarlamanız ve dosya yoluyla birlikte `Workbook` yapıcısına iletmeniz gerekir. Yüklendikten sonra, verilere `Worksheets` koleksiyonu üzerinden erişilebilir; burada hücreler arasında yineleme yapabilir, değerleri çıkarabilir veya verileri gerektiği gibi düzenleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını gösterir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat

dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")

loadOptions = LoadOptions(LoadFormat.Dbf)

workbook = Workbook(filePath, loadOptions)

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

sb = []

maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()

for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")

print("".join(sb))

outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.Xlsx)

print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

DBF dosyalarını doğrudan Microsoft Excel'de, Dosya Aç iletişim kutusunda dosyayı seçerek açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo olarak değerlendirerek kayıtlarını tablo düzeninde görüntüleyecektir. Bu, Aspose.Cells ile okuma veya yazma işleminden sonra verileri hızlıca doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

DBF dosyasına veri yazmak, Aspose.Cells ile herhangi bir elektronik tablo formatını kaydetmeye benzer bir model izler. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef format olarak `SaveFormat.Dbf` belirterek `Save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için şu adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `Worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.Dbf` parametre olarak ileterek `Workbook.save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını gösterir. DBF formatına dışa aktarırken alan türlerinin nasıl işlendiğini göstermek için farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle bir çalışma sayfası doldurur.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju

outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Sütun başlıkları
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")

# Veri satırı 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))

# Veri satırı 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))

# Veri satırı 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))

# Veri satırı 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))

# Veri satırı 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))

# Daha iyi okunabilirlik için sütun genişliklerini ayarla
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)

workbook.save(filePath, SaveFormat.DBf)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

DBF dosyasına veri yazarken, verilerinizin formatın sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYAAGG formatında gösterilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilmesi Gerekenler**

Verileri Aspose.Cells ile DBF formatı arasında aktarırken, veri bütünlüğünü sağlamak için veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydederken otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler** karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tamsayılar ve ondalık sayılar) sayısal (N) alanlarına eşlenir.
- **Tarih değerleri** `YYYYAAGG` formatında tarih (D) alanlarına eşlenir.
- **Boole değerleri** mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler, ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum uzunluk 10 karakter.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakterler içeremez.
- Girişte kullanılan büyük/küçük harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktının Doğrulanması

Bir DBF dosyasını yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, sütun başlıkları olarak alan adları ve sağladığınız verilere göre doldurulmuş kayıtlarla birlikte tablo düzeninde görünmelidir.

## **DBF ve Diğer Formatlar Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okuma ve yazmanın en pratik kullanım alanlarından biri, verileri DBF formatı ile XLSX, XLS veya CSV gibi modern elektronik tablo formatları arasında dönüştürmektir. Aspose.Cells geniş bir format yelpazesini desteklediğinden, bir DBF dosyasını kolayca yükleyebilir ve desteklenen herhangi bir başka formatta yeniden kaydedebilirsiniz veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından sonucu modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtmak için bir XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasındaki verileri alabilir ve eski sistemlerle entegrasyon için DBF formatına dışa aktarabilirsiniz.



{{< app/cells/assistant language="python" >}}