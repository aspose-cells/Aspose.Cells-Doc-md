---
title: DBF Dosyalarını Okuma ve Yazma
linktitle: DBF Dosyalarını Okuma ve Yazma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için JavaScript via C++ kitaplığıdır ve dBASE III ve IV (DBF) dosyalarını okuma ve yazmayı destekler. Bu makale, dosya biçimi ayrıntıları, desteklenen özellikler ve adım adım örnekler dâhil olmak üzere Aspose.Cells kullanarak DBF dosyalarından veri içe aktarma ve bu dosyalara veri dışa aktarma işleminin nasıl gerçekleştirileceğini açıklar.
keywords: Aspose.Cells, JavaScript via C++ kitaplığı, DBF, dBASE, DBF okuma, DBF yazma, DBF içe aktarma, DBF dışa aktarma, dosya biçimi, .dbf
type: docs
weight: 200
url: /tr/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, DBF (dBASE) dosyalarının okunmasını ve yazılmasını tam olarak destekler. Mevcut dBASE III ve dBASE IV dosyalarını bir Workbook nesnesine yükleyebilir, zengin Aspose.Cells API'sini kullanarak veriler üzerinde işlem yapabilir ve çalışma kitabını DBF biçiminde kaydederek daha sonra eski veritabanı uygulamalarında kullanabilirsiniz.
{{% /alert %}}

## **Giriş**
DBF (Veritabanı Dosyası), dBASE tarafından 1980'lerin başında tanıtılan eski bir veritabanı dosya biçimidir. Bu biçim eski olsa da DBF dosyaları, özellikle muhasebe, GIS ve diğer özel uygulama alanlarında olmak üzere birçok sektörde yapılandırılmış verileri depolamak için hâlâ yaygın olarak kullanılmaktadır. Aspose.Cells, bu eski dosyaları modern elektronik tablo iş akışlarına sorunsuz bir şekilde entegre etmenizi sağlar.
Kitaplık, DBF dosyalarını okuma ve yazma desteğiyle aşağıdaki işlemleri gerçekleştirmenizi sağlar:
- Mevcut DBF dosyalarındaki verileri Aspose.Cells Workbook nesnelerine içe aktararak daha fazla işlem yapabilir veya diğer biçimlere dönüştürebilirsiniz.
- Sıfırdan veya diğer elektronik tablo biçimlerinden dönüştürülen verilerden yeni DBF dosyaları oluşturun.
- DBF biçimiyle veri alışverişi sırasında alan tanımlarını, veri türlerini ve kayıt yapılarını koruyun.
DBF dosyaları Microsoft Excel ve diğer elektronik tablo uygulamalarında doğrudan açılabilir. Bu nedenle eski sistemler ile modern elektronik tablo araçları arasında kullanışlı bir köprü oluşturur.

## **Desteklenen DBF Sürümleri ve Özellikleri**
Aspose.Cells, DBF biçiminin aşağıdaki sürümlerini destekler:
- **dBASE III** — DBF biçiminin özgün ve en yaygın olarak desteklenen çeşidi.
- **dBASE IV** — Ek veri türlerini ve daha büyük alan boyutlarını destekleyen genişletilmiş sürüm.

### Desteklenen Özellikler
Kitaplık, aşağıdaki işlemler için kapsamlı destek sağlar:
- DBF verisini, tüm kayıtlar ve alan tanımları korunarak bir Workbook nesnesine okuma.
- Çalışma kitabı verisini DBF biçiminde geri yazarak dBASE uyumlu uygulamalara dışa aktarma.
- Karakter, sayısal, tarih ve mantıksal alanlar dâhil olmak üzere DBF dosyalarında kullanılan yaygın veri türlerini işleme.
- Alan adı, tür ve uzunluk gibi alan tanımlarını okuma/yazma işlemleri sırasında koruma.

### Sınırlamalar ve Dikkat Edilmesi Gerekenler
DBF dosyalarıyla çalışırken aşağıdaki kısıtları göz önünde bulundurun:
- Dosya başına en fazla **128** alan bulunabilir.
- En fazla kayıt boyutu **4000 bayttır**.
- Alan adları en fazla **10 karakter** uzunluğunda olmalı, büyük harfle yazılmalı ve boşluk içermemelidir.
- DBF dosyalarındaki tarih değerleri `YYYYMMDD` biçiminde saklanır.
- Karakter kodlaması, kaynak uygulamaya bağlı olarak değişebilir; genellikle Windows-1252 veya OEM kod sayfaları kullanılır.

## **DBF Dosyasını Okuma**
Aspose.Cells, DBF dosyasındaki verileri bir Workbook nesnesine yüklemenizi kolaylaştırır. Kitaplık, verilerin yükleme sırasında doğru yorumlanmasını sağlamak amacıyla kaynak biçimini belirleyen `LoadOptions` sınıfını kullanır.

### Aspose.Cells ile DBF Dosyasını Okuma
Bir DBF dosyasını okumak için bir `LoadOptions` örneği oluşturmanız, `loadFormat` özelliğini `LoadFormat.Dbf` olarak ayarlamanız ve bunu dosya yoluyla birlikte `Workbook` yapıcısına geçirmeniz gerekir. Yüklendikten sonra verilere `Worksheets` koleksiyonu üzerinden erişebilir; hücreler üzerinde yineleyebilir, değerleri çıkarabilir veya verileri gerektiğiniz şekilde düzenleyebilirsiniz.
Aşağıdaki örnek, mevcut bir DBF dosyasının Aspose.Cells ile nasıl yüklendiğini, ilk çalışma sayfasına nasıl erişildiğini ve hücre değerlerinin nasıl okunduğunu gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
DBF dosyalarını Microsoft Excel'de doğrudan açabilirsiniz; bunun için Aç iletişim kutusunda dosyayı seçmeniz yeterlidir. Excel, DBF dosyasını bir elektronik tablo olarak ele alır ve kayıtlarını tablo düzeninde görüntüler. Bu, Aspose.Cells ile okuma veya yazma işlemlerinden sonra verileri hızla doğrulamak için kullanışlıdır.
{{% /alert %}}

## **DBF Dosyasını Yazma**
DBF dosyasına veri yazma, Aspose.Cells ile diğer herhangi bir elektronik tablo biçimini kaydetmeye benzer bir süreci izler. Bir Workbook oluşturur veya yüklersiniz, çalışma sayfasını verilerle doldurursunuz ve ardından hedef biçim olarak `SaveFormat.Dbf` belirterek `save` yöntemini çağırırsınız.

### Aspose.Cells ile DBF Dosyasını Yazma
Bir DBF dosyası oluşturmak için şu adımları izleyin:
1. Yeni bir `Workbook` örneği oluşturun.
2. `Worksheets` koleksiyonundan ilk çalışma sayfasına erişin.
3. Çalışma sayfasını verilerinizle doldurun; ilk satıra başlıkları, sonraki satırlara ise kayıtları ekleyin.
4. Dosya yolunu ve `SaveFormat.Dbf` değerini parametre olarak geçirerek `Workbook.save` yöntemini çağırın.
Aşağıdaki örnek, sıfırdan yeni bir DBF dosyasının nasıl oluşturulacağını gösterir. Bu örnekte çalışma sayfası, DBF biçimine dışa aktarırken alan türlerinin nasıl işlendiğini göstermek amacıyla farklı veri türleri (dizeler, sayılar ve tarihler) içeren örnek verilerle doldurulur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Sütun başlıkları
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Veri satırı 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Veri satırı 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Veri satırı 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Veri satırı 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Veri satırı 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Daha iyi okunabilirlik için sütun genişliklerini ayarla
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
DBF dosyasına veri yazarken verilerinizin biçimin kısıtlamalarına uygun olduğundan emin olun. Alan adları en fazla 10 karakter uzunluğunda olmalı ve boşluk içermemelidir. Toplam boyutu 4000 baytı aşan kayıtlar doğru şekilde kaydedilmez. Tarihler, YYYYMMDD biçiminde temsil edilebilen geçerli tarih değerleri olmalıdır.
{{% /alert %}}

## **Veri Türü ve Biçimlendirme Hususları**
Aspose.Cells ile DBF biçimi arasında veri aktarırken veri türlerinin nasıl eşlendiğini anlamak, veri bütünlüğünün korunması açısından önemlidir.

### Hücre Türlerinden DBF Alan Türlerine
Aspose.Cells hücre değerleri, kaydedildiğinde otomatik olarak uygun DBF alan türlerine dönüştürülür:
- **Dizeler**, karakter (C) alanlarına eşlenir.
- **Sayısal değerler** (tam sayılar ve ondalıklar), sayısal (N) alanlarına eşlenir.
- **Tarih değerleri**, `YYYYMMDD` biçiminde tarih (D) alanlarına eşlenir.
- **Mantıksal değerler**, mantıksal (L) alanlarına eşlenir.

### Kodlama
DBF dosyaları, bunları oluşturan uygulamaya bağlı olarak farklı karakter kodlamaları kullanabilir. Aspose.Cells çoğu durumda kodlamayı şeffaf biçimde işler; ancak karakterlerin görüntülenmesiyle ilgili sorunlar yaşarsanız kaynak dosyanın kodlamasını doğrulamanız gerekebilir.

### Alan Adı Kuralları
DBF alan adları aşağıdaki kurallara uymalıdır:
- En fazla 10 karakter uzunluğunda olmalıdır.
- Bir harfle başlamalıdır.
- Boşluk veya özel karakter içeremez.
- Girdi değerindeki büyük/küçük harf kullanımından bağımsız olarak büyük harfle saklanır.

### Çıktının Doğrulanması
DBF dosyası yazıldıktan sonra sonucu Microsoft Excel veya dBASE uyumlu herhangi bir uygulamada açarak doğrulayabilirsiniz. Veriler, alan adlarının sütun başlığı olarak kullanıldığı bir tablo düzeninde görünmeli; kayıtlar ise sağladığınız verilere göre doldurulmalıdır.

## **DBF ile Diğer Biçimler Arasında Dönüştürme**
Aspose.Cells ile DBF dosyalarını okuma ve yazmanın en pratik kullanım senaryolarından biri, verileri DBF biçimiyle XLSX, XLS veya CSV gibi modern elektronik tablo biçimleri arasında dönüştürmektir. Aspose.Cells geniş bir biçim desteği sunduğundan, bir DBF dosyasını kolayca yükleyip desteklenen diğer herhangi bir biçimde yeniden kaydedebilir veya bunun tersini yapabilirsiniz.

{{< app/cells/assistant language="javascript-cpp" >}}