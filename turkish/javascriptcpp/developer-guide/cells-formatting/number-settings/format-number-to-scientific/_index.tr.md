---
title: Bilimsel Sayıya Biçimlendirme Nasıl Yapılır
type: docs
weight: 10
url: /tr/javascript-cpp/how-to-format-number-to-scientific/
description: Bu makale, Aspose.Cells for JavaScript i C++ API kullanarak Sayı Formatını Bilimsel dönüştürmeyi tanıtacaktır.
keywords: Bir sayıyı bilimsel gösterim biçimine dönüştürün, Bir sayıyı bilimsel gösterim formatına çevirin, Bir sayıyı bilimsel gösterim biçiminde ifade edin, Bir sayısal değeri eşdeğer bilimsel gösterime biçimlendirin, Bir miktarı bilimsel gösterim formatında görüntülemeye uyarlayın, Sayıyı Bilimsel Sayıya Biçimlendir
---

## **Olası Kullanım Senaryoları**
Excel'de sayıları bilimsel gösterime biçimlendirmek birkaç nedenle faydalıdır, özellikle çok büyük veya çok küçük sayılarla çalışırken. Bilimsel gösterim, bu sayıları daha kompakt, standart bir biçimde ifade etmesine olanak tanır, böylece onları okumak, karşılaştırmak ve anlamak daha kolay olur. İşte Excel'de sayıları bilimsel gösterime biçimlendirme nedenleri:

1. **Alan Tasarrufu**: Bilimsel gösterim, büyük sayıların görüntülenmesinde gereken alanı azaltır. Bu özellikle, hücre büyüklüğünün sınırlı olduğu ve okunabilirliğin önemli olduğu tablolar için faydalıdır.

2. **Gelişmiş Okunabilirlik**: Çok büyük veya çok küçük sayılar için, bilimsel gösterim değerin ölçeğini hızla kavramayı sağlar. Sayıları sunma şeklini standart hale getirerek, sıfırları saymaya gerek kalmadan büyüklüğü anlayabilirsiniz.

3. **Karşılaştırma Kolaylığı**: Sayılar bilimsel gösterimle gösterildiğinde, büyüklüklerinin karşılaştırması daha kolay olur. Çünkü gösterimdeki üs kısmı, sayının ölçeğini doğrudan gösterir.

4. **Doğruluk ve Kesinlik**: Bilimsel ve mühendislik bağlamlarında, yüksek kesinlik gerektiren sayılar üzerinde çalışmak sıklıkla gereken bir durumdur. Bilimsel gösterim, önemli basamakların kesin temsilini sağlar ve ölçümde anlamlı olan rakamları netleştirir.

5. **Standartlaştırma**: Bilimsel gösterim, sayıları temsil etmek için evrensel olarak tanınan bir formattır; bu da bu şekilde biçimlendirilmiş verilerin, bilim insanları, mühendisler ve matematikçiler dahil olmak üzere küresel bir kitle tarafından kolayca anlaşılmasını sağlar.

6. **Veri Analizi ve Sunumu**: Çok büyük veya çok küçük sayılar içeren veri setlerini analiz ederken, bu sayıları bilimsel gösterime dönüştürmek, analiz sürecini daha düzgün hale getirebilir. Ayrıca, verilerin raporlar, makaleler veya sunumlar içinde daha etkili sunulmasına yardımcı olur.

7. **Excel'in Sınırlamalarından Kaçınma**: Excel, bir hücrede gösterebileceği rakam sayısında bir sınırlamaya sahiptir. Bu sınırın üzerinde olan sayılar, Excel tarafından otomatik olarak bilimsel gösterime çevrilir, böylece hassasiyet kaybı önlenir. Bilimsel gösterimi anlayıp kullanarak, bu sınırlamalar içinde daha etkin çalışabilirsiniz.

Özetle, Excel'de sayıları bilimsel gösterime biçimlendirmek, çok büyük veya çok küçük değerler içeren verileri işlemek, sunmak ve analiz etmek için pratik bir yaklaşımdır. Bu, açıklığı artırır, hassasiyeti sağlar ve nicel bilgilerin iletimini kolaylaştırır.

## **Excel'de Sayı Nasıl Bilimsel Formata Getirilir**
Excel'de sayıları bilimsel gösterime biçimlendirmek için yerleşik biçimlendirme seçeneklerini kullanabilirsiniz. Bilimsel gösterim, çok büyük veya çok küçük olan sayıları rahatlıkla ifade etmenin bir yoludur. Bu, bilim insanları, matematikçiler ve mühendisler tarafından yaygın şekilde kullanılır. Excel'de, özellikle çok büyük veya çok küçük sayıları verinizde ele almak için bu fonksiyon oldukça faydalıdır.

İşte Excel'de sayıları bilimsel gösterime biçimlendirme yöntemleri:

### Şeridi Kullanarak

1. **Hücreleri Seçin**: Öncelikle biçimlendirmek istediğiniz hücreleri seçin. Birden fazla hücreyi seçmek için tıklayıp sürükleyebilir veya Ctrl+Tıklayarak ardışık olmayan hücreleri seçebilirsiniz.

2. **Hücreleri Biçimlendir Penceresini Açın**: Seçilen hücrelere sağ tıklayın ve açılan menüden `Hücreleri Biçimlendir`i seçin. Alternatif olarak, Şeritteki Giriş sekmesine gidin, Sayı grubundaki küçük oka tıklayarak `Hücreleri Biçimlendir` penceresini açabilirsiniz.

3. **Bilimsel Formatı Seçin**: Hücreleri Biçimlendir penceresinde, zaten seçilmediyse `Sayı` sekmesine tıklayın. Kategori listesinden `Bilimsel`i seçin.

4. **Ondalık Basamak Sayısını Belirleyin**: Kaç basamak göstermek istediğinizi belirtebilirsiniz. Örneğin, 2 seçerseniz, 1230 sayısı 1.23E+03 formatında gösterilir.

5. **Tamam'a Tıklayın**: Ondalık basamak sayısını belirledikten sonra, `Tamam` butonuna tıklayarak seçili hücrelere bilimsel gösterim formatını uygulayın.

### Şeridi Kısayolu Kullanarak

Daha hızlı bir yöntem için, şerit kısayolunu da kullanabilirsiniz:

1. **Hücreleri Seçin**: Biçimlendirmek istediğiniz hücreleri seçin.

2. **Giriş Sekmesine Gidin**: Giriş sekmesinde, Sayı grubunda, sayı biçimleri için açılır menüyü bulacaksınız.

3. **Daha Fazla Sayı Biçimi Seçin**: Açılır menüye tıklayın ve en alttan `Daha Fazla Sayı Biçimi...` seçeneğini seçin. Bu, doğrudan Sayı sekmesine sahip Hücreleri Biçimlendir penceresini açacaktır.

4. **Bilimsel'yi Seçin ve Ayarlayın**: Yukarıdaki aynı adımları takip ederek Bilimsel seçeneğini seçin ve gerekirse ondalık basamağı sayısını ayarlayın.

### Klavye Kısayolu

Daha da hızlı bir yöntem için, bir klavye kısayolu kullanabilirsiniz:

1. **Hücreleri Seçin**: Biçimlendirmek istediğiniz hücreleri vurgulayın.

2. **Hücreleri Biçimlendir Penceresini Açın**: `Ctrl` + `1` tuşlarına basın ve Hücreleri Biçimlendir penceresini açın.

3. **Bilimsel Formatı Seçin**: Daha sonra yukarıdaki adımları takip ederek bilimsel gösterimi uygulayın.

### Sonuç

Excel'de sayıları bilimsel gösterime biçimlendirmek basittir ve Hücreleri Biçimlendir penceresi aracılığıyla hızla yapılabilir. Bu özellik, çok büyük veya çok küçük sayılar içeren veri setleriyle çalışırken özellikle kullanışlıdır, böylece okumak ve yorumlamak daha kolay hale gelir.

## **Aspose.Cells for JavaScript'te Sayı Büyüklüğünü Bilimsel yapma**
Aspose.Cells for JavaScript'te sayıları bilimsel gösterime dönüştürmek için, hücrenin `Style.custom` özelliğini kullanabilirsiniz. Aspose.Cells, çalışma sayfalarınızdaki veriler için özel biçimlendirmeyi tanımlamanıza olanak tanır, bunlar arasında bilimsel gösterim de bulunur.

İşte adım adım nasıl yapacağınız hakkında yönlendirme:

### Adım 1: Aspose.Cells Kurulumu

İlk olarak, projenizde Aspose.Cells for JavaScript'i C++ kullanarak referans verdiğinizden emin olun. Bunu Aspose web sitesinden edinebilirsiniz.

### Adım 2: Yeni Çalışma Kitabı Oluştur veya Var Olanı Aç

Yeni bir çalışma kitabı oluşturabilir veya var olanı açabilirsiniz. 

### Adım 3: İstenen Çalışma Sayfasına Erişin

Sayısal verileri bilimsel gösterime biçimlendirmek istediğiniz çalışma sayfasına erişmeniz gerekir. Eğer yeni bir çalışma kitabı ile çalışıyorsanız, muhtemelen ilk çalışma sayfası ile çalışıyor olacaksınız.

### Adım 4: Hücreyi Bilimsel Gösterim Formatına Getirin

Bir hücrenin sayısını bilimsel gösterimde görüntülemek için, özel formatını ayarlamanız gerekir.

### Adım 5: Çalışma Kitabını Kaydet

Hücreleri ihtiyaçlarınıza göre biçimlendirdikten sonra, çalışma kitabınızı kaydetmeyi unutmayın. Bu, hücreler bilimsel gösterimde biçimlendirilmiş çalışma kitabınızı kaydedecektir.

### Örnek Kod

İşte bu adımları gösteren kod parçası:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Format Cell as Scientific Notation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const cell = worksheet.cells.get("A1");

            // Set the value of the cell as a number
            cell.value = 12345.6789;

            // Get the cell's style
            const style = cell.style;

            // Set the custom format of the cell to scientific notation
            style.custom = "0.00E+00";

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and formatted successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### Sonuç

Bu adımları izleyerek, Aspose.Cells for JavaScript'i C++ kullanarak sayıları bilimsel gösterime biçimlendirebilirsiniz. Format dizgesini (`"0.00E+00"`) ihtiyaçlara göre özelleştirebilir, ondalık basamak sayısını veya diğer bilimsel gösterim özelliklerini ayarlayabilirsiniz.
