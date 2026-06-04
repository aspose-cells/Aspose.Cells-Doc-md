---
title: DBF Dosyalarını Okuma ve Yazma
description: Aspose.Cells, Python via .NET aracılığıyla elektronik tablo dosyalarıyla çalışmak için kullanılan ve dBASE III ve IV (DBF) dosyalarını okumayı ve yazmayı destekleyen bir kütüphanedir. Bu makale, Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve bu dosyalara veri dışa aktarma işlemlerini, dosya biçimi ayrıntılarını, desteklenen özellikleri ve adım adım örnekleri açıklamaktadır.
keywords: Aspose.Cells, Python via .NET kütüphanesi, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya biçimi, .dbf
type: docs
weight: 200
url: /tr/python-net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells, DBF (dBASE) dosyalarını okuma ve yazma için tam destek sağlar. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, Aspose.Cells'in zengin API'sini kullanarak verileri düzenleyebilir ve çalışma kitabını eski veritabanı uygulamalarıyla kullanılmak üzere tekrar DBF biçiminde kaydedebilirsiniz.

{{% /alert %}}

## **Giriş**

DBF (DataBase File), 1980'lerin başında dBASE tarafından tanıtılan eski bir veritabanı dosya biçimidir. Biçimin eskiliğine rağmen, DBF dosyaları yapılandırılmış verileri depolamak için özellikle muhasebe, CBS ve diğer özel uygulamalar olmak üzere birçok endüstride hala yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern Python via .NET elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenize olanak tanır.

Kütüphane, hem DBF dosyalarını okumayı hem de yazmayı destekleyerek size şu yetenekleri sağlar:

- Mevcut DBF dosyalarından verileri, daha fazla işleme veya diğer biçimlere dönüştürme için Aspose.Cells Workbook nesnelerine içe aktarın.
- Sıfırdan veya diğer elektronik tablo biçimlerinden veri dönüştürerek yeni DBF dosyaları oluşturun.
- Verileri DBF biçimine aktarırken ve bu biçimden dışa aktarırken alan tanımlarını, veri türlerini ve kayıt yapılarını koruyun.

DBF dosyaları doğrudan Microsoft Excel ve diğer elektronik tablo uygulamalarında da açılabilir, bu da onları eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü haline getirir.

## **Desteklenen DBF Sürümleri ve Özellikleri**

Aspose.Cells aşağıdaki DBF biçim sürümlerini destekler:

- **dBASE III** — DBF biçiminin orijinal ve en yaygın desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş bir sürüm.

### Desteklenen Özellikler

Kütüphane, aşağıdaki işlemler için kapsamlı destek sağlar:

- Tüm kayıtlar ve alan tanımları korunarak DBF verilerinin bir Workbook nesnesine okunması.
- Çalışma kitabı verilerinin dBASE uyumlu uygulamalara dışa aktarım için tekrar DBF biçimine yazılması.
- Karakter, sayısal, tarih ve mantıksal alanlar dahil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerinin işlenmesi.
- Okuma/yazma işlemleri sırasında alan adı, türü ve uzunluğu gibi alan tanımlarının korunması.

### Sınırlamalar ve Dikkat Edilmesi Gerekenler

DBF dosyalarıyla çalışırken aşağıdaki kısıtlamaları göz önünde bulundurun:

- Dosya başına maksimum alan sayısı **128**'dir.
- Maksimum kayıt boyutu **4000 bayttır**.
- Alan adları **10 karakter** ile sınırlıdır, büyük harf olmalıdır ve boşluk içeremez.
- DBF dosyalarındaki tarih değerleri `YYYYMMDD` biçiminde saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir (genellikle Windows-1252 veya OEM kod sayfaları).

## **DBF Dosyası Okuma**

Aspose.Cells, DBF dosyasındaki verileri bir Workbook nesnesine yüklemeyi kolaylaştırır. Kütüphane, kaynak biçimini belirtmek için `LoadOptions` sınıfını kullanır ve yükleme işlemi sırasında verilerin doğru şekilde yorumlanmasını sağlar.

### Aspose.Cells ile Bir DBF Dosyasını Okuma

Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `load_format` özelliğini `LoadFormat.DBF` olarak ayarlamanız ve dosya yolu ile birlikte `Workbook` yapıcısına iletmeniz gerekir. Yüklendikten sonra, verilere `worksheets` koleksiyonu aracılığıyla erişilebilir; burada hücreler arasında yineleme yapabilir, değerleri çıkarabilir veya verileri gerektiği gibi düzenleyebilirsiniz.

Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells'e nasıl yükleneceğini, ilk çalışma sayfasına nasıl erişileceğini ve hücre değerlerinin nasıl okunacağını göstermektedir.

```python
import os
import aspose.cells as ac

data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")

load_options = ac.LoadOptions(ac.LoadFormat.DBF)

workbook = ac.Workbook(file_path, load_options)

worksheet = workbook.worksheets[0]

cells = worksheet.cells

lines = []

max_row = cells.max_data_row
max_col = cells.max_data_column

for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells[i, j]
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))

result = "\n".join(lines) + ("\n" if lines else "")
print(result)

output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)

print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}

DBF dosyalarını doğrudan Microsoft Excel'de, Dosya Aç iletişim kutusunda dosyayı seçerek açabilirsiniz. Excel, DBF dosyasını bir elektronik tablo olarak değerlendirerek kayıtlarını tablo düzeninde görüntüleyecektir. Bu, Aspose.Cells ile okuduktan veya yazdıktan sonra verileri hızlı bir şekilde doğrulamak için kullanışlıdır.

{{% /alert %}}

## **DBF Dosyası Yazma**

Bir DBF dosyasına veri yazmak, Aspose.Cells ile başka herhangi bir elektronik tablo biçimini kaydetmeye benzer bir kalıba uyar. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef biçim olarak `SaveFormat.DBF` belirterek `save` yöntemini çağırırsınız.

### Aspose.Cells ile Bir DBF Dosyası Yazma

Bir DBF dosyası oluşturmak için şu adımları izleyin:

1. Yeni bir `Workbook` örneği oluşturun.
2. `worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları ve sonraki satırlara kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.DBF` parametre olarak ileterek `Workbook.save` yöntemini çağırın.

Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını göstermektedir. DBF biçimine dışa aktarırken alan türlerinin nasıl işlendiğini göstermek için farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle bir çalışma sayfası doldurur.

```python
from datetime import datetime

outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Sütun başlıkları
cells[0, 0].put_value("ID")
cells[0, 1].put_value("Name")
cells[0, 2].put_value("Department")
cells[0, 3].put_value("Salary")
cells[0, 4].put_value("HireDate")

# Veri satırı 1
cells[1, 0].put_value(101)
cells[1, 1].put_value("John Smith")
cells[1, 2].put_value("Engineering")
cells[1, 3].put_value(75000.50)
cells[1, 4].put_value(datetime(2020, 3, 15))

# Veri satırı 2
cells[2, 0].put_value(102)
cells[2, 1].put_value("Jane Doe")
cells[2, 2].put_value("Marketing")
cells[2, 3].put_value(68000.75)
cells[2, 4].put_value(datetime(2019, 7, 22))

# Veri satırı 3
cells[3, 0].put_value(103)
cells[3, 1].put_value("Bob Johnson")
cells[3, 2].put_value("Finance")
cells[3, 3].put_value(82000.00)
cells[3, 4].put_value(datetime(2021, 1, 10))

# Veri satırı 4
cells[4, 0].put_value(104)
cells[4, 1].put_value("Alice Brown")
cells[4, 2].put_value("Human Resources")
cells[4, 3].put_value(71000.25)
cells[4, 4].put_value(datetime(2018, 11, 5))

# Veri satırı 5
cells[5, 0].put_value(105)
cells[5, 1].put_value("Charlie Wilson")
cells[5, 2].put_value("Operations")
cells[5, 3].put_value(79500.80)
cells[5, 4].put_value(datetime(2022, 5, 30))

# Daha iyi okunabilirlik için sütun genişliklerini ayarla
worksheet.cells.set_column_width(0, 8)
worksheet.cells.set_column_width(1, 20)
worksheet.cells.set_column_width(2, 20)
worksheet.cells.set_column_width(3, 12)
worksheet.cells.set_column_width(4, 14)

workbook.save(filePath, ac.SaveFormat.Dbf)
```

{{% alert color="primary" %}}

Bir DBF dosyasına veri yazarken, verilerinizin biçimin sınırlamalarına uygun olduğundan emin olun. Alan adları 10 karakterden uzun olmamalı ve boşluk içermemelidir. Toplamda 4000 baytı aşan kayıtlar doğru şekilde kaydedilmeyecektir. Tarihler, YYYYMMDD biçiminde temsil edilebilen geçerli tarih değerleri olmalıdır.

{{% /alert %}}

## **Veri Türü ve Biçimlendirme Dikkat Edilecek Hususlar**

Aspose.Cells ile DBF biçimi arasında veri aktarırken, veri türlerinin iki sistem arasında nasıl eşlendiğini anlamak, veri bütünlüğünü sağlamak için önemlidir.

### Hücre Türlerinden DBF Alan Türlerine

Aspose.Cells hücre değerleri, kaydederken otomatik olarak uygun DBF alan türlerine dönüştürülür:

- **Dizeler** karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tamsayılar ve ondalık sayılar) sayısal (N) alanlarına eşlenir.
- **Tarih değerleri** `YYYYMMDD` biçiminde tarih (D) alanlarına eşlenir.
- **Boolean değerler** mantıksal (L) alanlarına eşlenir.

### Kodlama

DBF dosyaları, onları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf bir şekilde işler, ancak karakter görüntüleme sorunlarıyla karşılaşırsanız, kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları

DBF alan adları aşağıdaki kurallara uymalıdır:

- Maksimum uzunluk 10 karakter.
- Bir harf ile başlamalıdır.
- Boşluk veya özel karakterler içeremez.
- Girişte kullanılan harf durumundan bağımsız olarak büyük harf olarak saklanır.

### Çıktının Doğrulanması

Bir DBF dosyasını yazdıktan sonra, sonucu Microsoft Excel'de veya herhangi bir dBASE uyumlu uygulamada açarak doğrulayabilirsiniz. Veriler, alan adlarının sütun başlıkları olarak göründüğü ve sağladığınız verilere göre kayıtların doldurulduğu tablo düzeninde görünmelidir.

## **DBF ve Diğer Biçimler Arasında Dönüştürme**

Aspose.Cells ile DBF dosyalarını okumanın ve yazmanın en pratik kullanım durumlarından biri, verileri DBF biçimi ile XLSX, XLS veya CSV gibi modern elektronik tablo biçimleri arasında dönüştürmektir. Aspose.Cells çok çeşitli biçimleri desteklediğinden, bir DBF dosyasını kolayca yükleyebilir ve desteklenen başka herhangi bir biçimde yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

Örneğin, bir DBF dosyasını okuyabilir, Aspose.Cells API'sini kullanarak biçimlendirme veya hesaplamalar uygulayabilir ve ardından modern elektronik tablo uygulamalarıyla çalışan kullanıcılara dağıtmak için sonucu bir XLSX dosyası olarak kaydedebilirsiniz. Tersine, bir XLSX veya CSV dosyasındaki verileri alabilir ve eski sistemlerle entegrasyon için DBF biçiminde dışa aktarabilirsiniz.



{{< app/cells/assistant language="python" >}}