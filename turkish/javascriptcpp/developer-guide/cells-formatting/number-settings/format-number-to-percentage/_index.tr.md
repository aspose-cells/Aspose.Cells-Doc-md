---
title: Sayı Formatını Yüzdeye Çevirme Nasıl Yapılır
type: docs
weight: 10
url: /tr/javascript-cpp/how-to-format-number-to-percentage/
description: Bu makale, Aspose.Cells for JavaScript i C++ API kullanarak Sayı Formatını Yüzdeye dönüştürmeyi tanıtacaktır.
keywords: Bir sayıyı yüzde biçimine dönüştürün, Sayısal değerleri yüzdeye dönüştürün, Sayıları yüzde olarak gösterilecek şekilde değiştirin, Sayıları yüzde biçiminde biçimlendirin, Sayısal rakamları yüzde temsiline ayarlayın, Sayı Formatını Yüzdeye Çevir
---

## **Olası Kullanım Senaryoları**
Excel'de sayıları yüzdeye biçimlendirmek, çeşitli nedenlerden dolayı yaygın bir uygulamadır; her biri verilerin netliği, doğruluğu ve anlaşılabilirliğini artırır. İşte Excel'de sayıların yüzdelik olarak biçimlendirilmesinin bazı temel nedenleri:

1. **Netlik ve Okunabilirlik**: Yüzdeler, evrensel olarak anlaşılan bir biçimdir ve verilerin okunmasını ve yorumlanmasını kolaylaştırır. Ondalık veya kesirli bir değeri yüzdeye dönüştürerek, hemen anlaşılır hale getirirsiniz; bu, çoğu kullanıcı için bütünün bir parçası olduğunun daha sezgisel olmasını sağlar.

2. **Tutarlılık**: Karşılaştırmalar içeren raporlar veya veri analizlerinde, sayıların yüzdeye biçimlendirilmesi tutarlılığı sağlar. Bu, farklı veri setlerinden oran veya oranları karşılaştırırken özellikle önemlidir. Veri sunumundaki tutarlılık, daha doğru karşılaştırmalar ve sonuçlar elde edilmesine yardımcı olur.

3. **Basitleştirme**: Yüzdeler karmaşık bilgileri basitleştirir. Örneğin, "%50" demek, "0.5" veya "1/2" demekten daha doğrudur ve çoğu kişi tarafından daha kolay anlaşılır. Bu sadeleştirme, teknik bir arka plana sahip olmayan izleyiciye veri iletiminde kritiktir.

4. **Görselleştirme**: Grafik veya çizelge oluştururken, yüzdeler veri görselleştirmesini daha etkili hale getirebilir. Örneğin, pasta çizelgeleri, bütünün parçalarını temsil ettiği için ve veriler yüzde olarak biçimlendirildiğinde daha sezgiseldir.

5. **Analiz ve Karar Verme**: İş ve finans alanında, yüzdeler genellikle büyüme, kâr marjları ve diğer anahtar performans göstergelerini (KPI'lar) temsil etmek için kullanılır. Bu sayıları yüzdeye biçimlendirmek, analizleri kolaylaştırır ve net, anlaşılır metriklere dayalı kararlar alınmasını sağlar.

6. **Alan Tasarrufu**: Bazı durumlarda, sayıları yüzdeye biçimlendirmek, belge veya elektronik tablo alanını koruyarak daha temiz ve düzenli görünmesini sağlar. Bu özellikle, alanın kıt olduğu tablolar veya pano görünümleri için faydalıdır.

7. **Eğitsel ve Öğretici Amaçlar**: Eğitim ortamlarında, sayıları yüzdeye biçimlendirmek, öğrencilerin kesirleri, oranları ve oranları daha iyi anlamalarına yardımcı olabilir. Bu, matematiksel kavramların pratik bir uygulamasıdır.

Excel'de bir sayıyı yüzde olarak biçimlendirmek için, verilerin bulunduğu hücreleri seçip "Yüzde" biçim seçeneğini tercih edin; bu, Ribbon'daki Giriş sekmesi veya sağ tıklayarak "Hücreleri Biçimlendir" menüsü üzerinden yapılabilir. Excel daha sonra sayıları yüzde olarak gösterecek, orijinal ondalık değerleri 100 ile çarpacak ve yüzde işareti ekleyecektir. Bu otomatik dönüşüm, yukarıda bahsedilen nedenleri kolaylaştırır ve veri yönetimi ile sunumu hem verimli hem de etkili hale getirir.

## **Excel'de Sayı Formatını Yüzdeye Çevirme Nasıl Yapılır**
Excel'de sayıları yüzdeye biçimlendirmek, birkaç adımda gerçekleştirilebilen basit bir işlemdir. İşte nasıl yapılır:

### Şeridi Kullanarak

1. **Hücreleri Seçin**: Öncelikle, yüzde biçiminde biçimlendirmek istediğiniz hücre veya hücre aralığını seçin.
2. **Ribbon’a Git**: Excel’in üst kısmındaki şeride bakın. "Giriş" adlı bir sekme göreceksiniz.
3. **Yüzde Biçim Düğmesi**: "Giriş" sekmesinde, "Sayı" grubunda, "%" simgeli bir düğme göreceksiniz. Bu, "Yüzde Biçimi" düğmesidir.
4. **Yüzde Formatını Uygula**: "%" düğmesine tıklayın. Excel, seçilen hücreleri otomatik olarak yüzde biçiminde biçimlendirecek, hücre değerini 100 ile çarpacak ve yüzde işareti ekleyecektir. Örneğin, hücreye "0.1" yazarsanız ve yüzde biçim uygularsanız, "10%" olarak gösterilecektir.

### Hücreleri Biçimlendirme Diyaloğunu Kullanarak

1. **Hücreleri Seçin**: Biçimlendirmek istediğiniz hücreleri vurgulayın.
2. **Hücreleri Biçimlendir Diyaloğunu Açın**: Seçili hücrelerden birine sağ tıklayın ve "Hücreleri Biçimlendir" seçeneğini seçin; alternatif olarak, `Ctrl + 1` tuşlarına basarak Diyalog kutusunu açabilirsiniz.
3. **Yüzdeyi Seçin**: Hücreleri Biçimlendir penceresinde, "Sayı" sekmesine tıklayın ve listesinden "Yüzde"yi seçin.
4. **Ondalıkların Sayısını Ayarlayın**: Görüntülemek istediğiniz ondalık basamak sayısını ayarlayabilirsiniz. Örneğin, iki ondalık gösterimini istiyorsanız, "Ondalık basamak" kutusuna "2" yazın.
5. **Uygula**: "Tamam" düğmesine tıklayın ve yüzde biçimini uygulayın. Seçili hücreler artık yüzde değerlerini gösterecektir.

### Formül Kullanarak

Bir formül kullanıyorsanız veya var olan bir sayıyı yüzdeye dönüştürmek istiyorsanız, sayıyı 100 ile çarpıp yüzde simgesini format olarak ekleyebilirsiniz.

Örneğin, A1 hücresinde bir değeriniz varsa ve B1 hücresinde yüzde olarak göstermek istiyorsanız, aşağıdaki formülü kullanabilirsiniz:

```excel
=A1*100 & "%"
```

Ancak, bu yöntem sonucu metin olarak kabul eder ve sayı değil, bu da diğer hesaplamaları etkileyebilir.

### Klavye Kısayolu

Mouse kullanmadan hızlı biçim değiştirme için:
- Biçimlendirmek istediğiniz hücreleri seçin.
- `Ctrl + Shift + %` tuşlarına basın. Bu, seçilen hücrelere yüzde biçimini uygular.

Unutmayın, bir sayıyı yüzde olarak biçimlendirirken, Excel esasen hücre değerini 100 ile çarpar. Yani, yüzde olarak görüntülemek istediğiniz veriyi girerken, onu ondalık olarak girin (örn., 10% için "0.1" girin).

## **Aspose.Cells for JavaScript'i C++ kullanarak sayıları yüzdeye dönüştürmenin yolu nedir?**
Aspose.Cells for JavaScript'i C++ kullanarak sayıları yüzdeye biçimlendirmek oldukça basit bir işlemdir. Aspose.Cells, Excel dosyalarını oluşturmanıza, düzenlemenize ve dönüştürmenize imkan tanıyan güçlü bir kütüphanedir; bu, özellikle JavaScript uygulamalarında Microsoft Excel'in yüklü olmasına gerek kalmadan kullanılabilir. İşte Aspose.Cells for JavaScript'i C++ kullanarak sayıları yüzdeye biçimlendirme adımları:

### Adım 1: Aspose.Cells for JavaScript'i C++ üzerinden yükleyin

İlk olarak, projenizde Aspose.Cells for JavaScript'i C++ kullanarak referans verdiğinizden emin olun. Bunu Aspose web sitesinden edinebilirsiniz.

### Adım 2: Yeni Çalışma Kitabı Oluştur veya Var Olanı Aç

Yeni bir çalışma kitabı oluşturabilir veya var olanı açabilirsiniz. 


### Adım 3: Çalışma Sayfasına Erişim

Yüzde biçimlendirmek istediğiniz hücrelerin bulunduğu çalışma sayfasına erişmeniz gerekir. Yeni bir çalışma kitabı ile çalışıyorsanız, muhtemelen ilk çalışma sayfasıyla ilgileneceksiniz.

### Adım 4: Yüzde Biçimlendirmeyi Uygula

Bir hücreyi veya hücre aralığını yüzde olarak görüntüleyecek şekilde biçimlendirmek için, hücrenin veya aralığın stil sayı biçimini yüzde biçimine ayarlamanız gerekir. Bir hücre aralığı için, aralık boyunca döngü yapıp her hücreye ayrı ayrı stili uygulayabilirsiniz.

### Adım 5: Çalışma Kitabını Kaydet

Son olarak, çalışma kitabını bir dosyaya veya akışa kaydedin.

### Örnek Kod

İşte bu adımları gösteren kod parçası:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Format Cell as Percentage Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const cell = worksheet.cells.get("A1");

            // Set the cell value
            cell.value = 0.25;

            // Get the cell's style
            const style = cell.style;

            // Set the number format to percentage
            style.number = 9; // Number 9 corresponds to the percentage format

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### Sonuç

Bu adımları izleyerek, Aspose.Cells for JavaScript'i C++ üzerinde kullanarak sayıları yüzdeye kolayca biçimlendirebilirsiniz. Aspose.Cells, hücreleri biçimlendirme, formüllerle çalışma ve daha fazlasını içeren Excel dosyalarını manipüle etmek için geniş özellikler sunar, bu da onları Excel verileriyle çalışan JavaScript geliştiricileri için güçlü bir araç haline getirir.
