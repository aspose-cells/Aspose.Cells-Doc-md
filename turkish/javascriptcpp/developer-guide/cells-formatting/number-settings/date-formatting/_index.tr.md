---
title: Sayısı Nasıl Tarih Olarak Biçimlendirilir
type: docs
weight: 10
url: /tr/javascript-cpp/format-number-to-date/
description: Bu makale, Aspose.Cells for JavaScript C++ API kullanarak sayıların tarih biçimlendirilmesini nasıl yapacağınızı tanıtacaktır.
keywords: numarayı tarih olarak biçimlendirme, hücre sayı ayarları, sayıyı tarihe biçimlendirme, tarih ayarları, tarih formatı.
---

## **Olası Kullanım Senaryoları**
Excel'de (ve herhangi bir elektronik tablo yazılımında) sayıları tarihe biçimlendirmek birkaç nedenle önemlidir, özellikle zaman veya takvim bilgisi içeren verilerle çalışırken. İşte neden sayıları tarihe formatlamanın faydalı olduğu:

1. Tarih Değerlerinin Doğru Yorumlanması: Excel'de tarihleri serisel sayılar olarak saklar (örneğin, 1 Ocak 1900 için 1 ve 6 Eylül 2021 için 44210). Bu sayılar uygun şekilde biçimlendirilmediğinde, kullanıcılar anlamsız sayılar görebilir, hatalı görüntüleyebilir. Doğru biçimlendirmeler, Excel'in bunları gerçek tarihler olarak görüntülemesine olanak tanır (örneğin, 09/06/2021 yerine 44210).
1. Zamanla İlgili Hesaplamaları Basitleştirir: Excel, iki tarih arasındaki gün sayısını hesaplama, gün ekleme veya çıkarma veya haftanın gününü belirleme gibi birçok hesaplama yapabilir. Sayılar tarih formatında değilse, Excel bu işlemleri etkili şekilde yapamaz. Örneğin, 09/01/2023 ve 10/01/2023 arasındaki gün sayısını öğrenmek istiyorsanız, sayılar tarih biçimindeyse, Excel kolayca hesaplayabilir.
1. Tutarlılığı Sağlar: Tüm tarih ile ilgili değerler doğru biçimlendirilmişse, tüm tarihler uyumlu, okunabilir bir tarzda görünür. Bu tutarlılık, işletme raporları, proje takvimleri ve veritabanlarında tarih tutarlılığının kritik olduğu durumlarda önemlidir.
Farklı bölgeler farklı tarih biçimleri kullanır (örneğin, ABD'de MM/Ay/GG, diğer birçok ülkede GG/Ay/MM), bu nedenle biçimlendirme, tarihlerinin doğru yorumlanmasını sağlar.
1. Okunabilirliği Artırır: Standart formatta sunulan tarihler (örneğin, 01/01/2024) ham seri numaralarına göre (örneğin 45000) daha kolay okunur. Doğru tarih biçimlendirmesi, elektronik tablonuzu daha kullanıcı dostu yapar ve karışıklığı önler. Bu, takvim, zaman çizelgeleri, etkinlik planlaması veya tarihsel veriler gibi durumlarda özellikle önemlidir.
1. Sıralama ve Filtreleme İşlevlerini Kolaylaştırır: Tarihler doğru biçimlendirildiğinde, Excel bunları gerçek tarihler olarak tanır ve bu da veriyi kronolojik olarak sıralamayı veya filtrelemeyi kolaylaştırır. Örneğin, bir olay listesini tarihe göre sıralayabilir veya belirli iki tarih arasında kayıtlar gösterecek şekilde filtre uygulayabilirsiniz. Uygun tarih biçimi olmadan, sıralama ham sayı değerine göre yapılabilir.
1. Tarih Fonksiyonlarının Kullanımını Etkinleştirir: Excel, şunlar gibi güçlü tarih fonksiyonları sağlar: BUGÜN(), DATEDIF(), İŞGÜNÜ(), YIL(), AY(), GÜN(). Bu fonksiyonların doğru hesaplamalar yapabilmesi için tarihlerin doğru biçimde ayarlanması gerekir.
1. Görselleştirmeyi Destekler (Grafikler/Zaman Çizelgeleri): Doğru biçimlendirilmiş tarihler, zamanın ana eksen olduğu grafik ve çizelgeler oluşturmak için kullanılabilir. Örneğin, bir zaman çizelgesi grafiğinde, Excel'in olayları doğru şekilde gösterebilmesi için tarihler tanınan biçimde olmalıdır. Yanlış biçimlendirilmiş veya biçimlendirilmemiş sayılar, anlamlı olmayan veya yanlış bilgiler içeren grafiklere yol açabilir.
1. Yanlış Yorumlamayı Önler: Ham sayılar kolaylıkla yanlış yorumlanabilir. Örneğin, 44210 genelleme sayısal bir değer olarak görülebilir, ancak tarih biçiminde olduğunda, 6 Eylül 2021'i temsil ettiği açıktır. Doğru biçimlendirilmiş tarihler, verilerin yanlış yorumlanmasını önler.
1. Veri Girişini Kolaylaştırır: Hücreler tarih biçiminde biçimlendirildiğinde, kullanıcılar geçerli bir tarih formatında veri girmeye teşvik edilir, bu da veri giriş hatalarını önler ve tarih değerlerinin doğru şekilde kaydedilmesini sağlar.
1. Programlamada ve Takipte Kritik: Herhangi bir durumda zamanlama, takip veya son teslim tarihleriyle ilgili (proje yönetimi, finansal tahmin veya zaman hassas raporlar gibi), sayıların tarih formatında olması doğruluk ve anlaşılabilirlik için çok önemlidir. Bu, daha iyi planlama ve yürütme sağlar.


## **Excel'de Sayıyı Tarehe Formatlama Kılavuzu**
Excel'de bir sayıyı tarihe dönüştürmek için şu adımları izleyin:

### **Şeridi Kullanarak (Giriş Sekmesi)**
1. Tarih olarak biçimlendirmek istediğiniz sayıların bulunduğu hücreleri seçin.
1. Şerideki Giriş sekmesine gidin.
1. Sayı Grubunda, Sayı Biçimi kutusundaki açılır oka tıklayın (varsayılan olarak "Genel" veya "Sayı" gösterilebilir).
1. Açılır menüden Kısa Tarih veya Uzun Tarih seçin. Kısa Tarih: tarihi kısaca gösterir, ör. AA/GG/YYYY (ABD formatı) veya GG/AA/YYYY (uluslararasıFormat). Uzun Tarih: tarihi daha açıklayıcı biçimde gösterir, ör. Pazartesi, 1 Ocak 2024.
<br>
<img src="1.png" width=60% />

### **Hücreleri Biçimlendir Diyalog Kutusunu Kullanarak**
1. Biçimlendirmek istediğiniz hücreleri seçin.
1. Seçili hücrelere sağ tıklayın ve Biçim Hücreleri’ni seçin veya Ctrl + 1 (Windows) veya Cmd + 1 (Mac) tuşlarına basın.
1. Biçim Hücreleri iletişim kutusundaki Sayı sekmesine gidin.
1. Sol taraftaki listeden Tarih seçeneğini seçin.
1. Sağdaki listeden istenen tarih formatını seçin (ör., AA/GG/YYYY, GG/AA/YYYY veya özel biçimler).
<br>
<img src="2.png" width=60% />
1. Tamam’a tıklayarak tarih formatını uygulayın.

## **Aspose.Cells ile Sayıyı Tarihe Formatlama Yöntemi**

Excel dosyasıyla çalışmak için Aspose.Cells for JavaScript C++ kütüphanesinde sayıların tarih olarak biçimlendirilmesi, hücrelere programatik olarak tarih biçimi uygulayarak yapılabilir. İşte bunu yapmanın yolu Aspose.Cells for JavaScript C++ kullanımıyla.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Date & Custom Format Example</h1>
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
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
            a1.value = 44210;

            // Create a style object to apply the date format
            const a1Style = a1.style;

            // "14" represents a standard date format in Excel (MM/DD/YYYY)
            a1Style.number = 14;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 44210;

            // Create a style object to apply the date format
            const a2Style = a2.style;
            // Custom format for YYYY-MM-DD
            a2Style.custom = "YYYY-MM-DD";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'DateFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and formatted successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
