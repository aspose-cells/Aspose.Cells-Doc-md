---
title: Excel Dosyalarını Çoklu Dosyalara Bölme
linktitle: Excel Dosyalarını Çoklu Dosyalara Bölme
description: Aspose.Cells for JavaScript via C++ bir JavaScript via C++ kütüphanesidir ve elektronik tablo dosyalarıyla çalışmayı sağlar; tek bir Excel dosyasını çoklu dosyalara bölmeyi destekler. Bu makale, Excel dosyalarını her çalışma sayfasını ayrı bir çalışma kitabına kopyalayarak ve belirli hücre aralıklarını diğer çalışma kitaplarına kopyalayarak nasıl bölüneceğini tanıtacaktır.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, elektronik tablo, Excel dosyasını böl, çalışma sayfasını kopyala, aralığı kopyala, birden fazla çalışma kitabı, ayrı dosyalar olarak kaydet
type: docs
weight: 195
url: /tr/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ tek bir Excel dosyasını çoklu dosyalara bölmeyi destekler. Bunu yapmanın iki temel yolu vardır: (1) kaynak çalışma kitabındaki her çalışma sayfasını yeni bir çalışma kitabına kopyalayıp ayrı bir dosya olarak kaydetmek ve (2) bir çalışma sayfasındaki belirli bir hücre aralığını yeni bir çalışma kitabına kopyalamak. Her iki yaklaşım da, veri alt kümelerini dağıtmanız, farklı alıcılar için daha küçük raporlar oluşturmanız veya bireysel işleme için verileri izole etmeniz gerektiğinde kullanışlıdır.
{{% /alert %}}

## **Giriş**
Bir geliştiricinin tek bir Excel dosyasını birkaç daha küçük dosyaya bölmesi gereken birçok gerçek dünya senaryosu vardır. Örneğin, bir çalışma kitabı her bölüm için bir çalışma sayfası içerebilir ve her bölüm yöneticisinin yalnızca kendi sayfasını alması gerekebilir. Diğer durumlarda, bir çalışma sayfasındaki belirli bir tabloyu veya veri bloğunu ayırıp e-posta ile bağımsız bir dosya olarak göndermek isteyebilirsiniz; böylece çalışma kitabının geri kalanını ortaya çıkarmamış olursunuz. Büyük birleşik çalışma kitapları da daha kolay işlenebilmesi, daha hızlı yüklenebilmesi veya diğer sistemler tarafından daha sonraki işlem için daha küçük parçalara bölünmesi gerekebilir.  
Aspose.Cells for JavaScript via C++ bu görev için iki esnek yaklaşım sunar. İlk yaklaşım, kaynak çalışma kitabındaki her çalışma sayfasını dolaşır ve içeriğini yepyeni bir `Workbook` örneğine kopyalar; her birini ayrı bir dosya olarak kaydeder. İkinci yaklaşım, bir çalışma sayfasındaki belirli bir hücre aralığına odaklanır ve yalnızca o aralığı yeni bir çalışma kitabına kopyalar. Her iki durumda da genel akış aynı olur: `Workbook` sınıfını kullanarak kaynak çalışma kitabını yükleyin, ilgili veriye `Worksheet` ve `Cells` nesneleri aracılığıyla erişin, içeriği hedef `Workbook` nesnesine aktarın ve ardından hedefi diske kaydedin.

## **Her Çalışma Sayfasını Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşım Genel Bakışı**
Bu yaklaşımda, kaynak çalışma kitabı bir kez açılır ve `Worksheets` koleksiyonundaki her `Worksheet` için yeni bir hedef `Workbook` oluşturulur. Kaynak çalışma sayfasının içeriği, hedef çalışma kitabının ilk çalışma sayfasına kopyalanır ve hedef çalışma kitabı, kaynak çalışma sayfasının adından türetilen bir adla dosyaya kaydedilir. Sonuç, her çalışma sayfası için bir çıktı dosyasıdır; her dosya tek bir kaynak sayfasının verilerini içerir.  
Bu yöntem, kaynak çalışma kitabındaki her çalışma sayfasının mantıksal olarak bağımsız bir bilgi birimini (örneğin bir departman, bölge, ay veya ürün hattı) temsil ettiği ve bu birimleri ayrı ayrı teslim veya işlemek istediğiniz durumlar için uygundur.

### **Adımlar**
Aşağıdaki adımlar, her çalışma sayfasını yeni bir çalışma kitabına kopyalayarak bir Excel dosyasını nasıl böleceğinizi açıklar:
1. `Workbook` nesnesini örnekleyerek ve dosya yolunu yapıcıya geçirerek kaynak Excel dosyasını açın.  
2. `Workbook.Worksheets` koleksiyonunu bir `for` veya `for...of` döngüsüyle dolaşarak kaynak dosyadaki her `Worksheet` işlenir.  
3. Döngü içinde, geçerli çalışma sayfası için yeni bir hedef `Workbook` örneği (boş bir çalışma kitabı) oluşturun.  
5. Kaynak çalışma sayfasının içeriğini hedef çalışma sayfasına kopyalayın. Bu, kaynak çalışma sayfasının `Cells` koleksiyonundaki hücreleri döngüyle gezerek değerleri karşılık gelen hedef hücrelere yazmak ya da `Cells.Copy` yöntemini kullanarak tüm bir aralığı tek seferde aktarmak suretiyle yapılabilir.  
6. Kaynak çalışma sayfasının adını içeren bir çıktı dosya yolu oluşturun (örneğin `dataDir + worksheet.Name + ".xls"`), böylece her oluşturulan dosyanın benzersiz bir adı olur.  
7. Hedef `Workbook.Save` yöntemini çağırarak dosyayı diske yazın.  
8. Tüm çalışma sayfaları işlenene kadar 3‑7. adımları tekrarlayın.

### **Kod Örneği**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

Beklenen çıktı, veri dizininde kaynak çalışma kitabındaki her çalışma sayfası için bir dosya olacak şekilde yeni dosyalar kümesidir. Her dosya, ilgili kaynak sayfasının adını taşır ve dosya, tek bir sayfanın verilerini (ve isteğe bağlı olarak biçimlendirmesini) içerir.

## **Bir Aralığı Yeni Bir Çalışma Kitabına Kopyalayarak Excel Dosyasını Bölme**

### **Yaklaşım Genel Bakışı**
Bazen bölmeniz gereken veri, bütün bir çalışma sayfası yerine bir çalışma sayfasının belirli bir dikdörtgen bölgesi, örneğin `A1:D10` gibi bir hücre aralığı ya da belirli bir tabloyu temsil eden adlandırılmış bir aralık olabilir. Bu durumlarda tüm çalışma sayfalarını kopyalamak gereksizdir ve daha hassas bir yaklaşım gerekir: kaynak aralığı belirleyin, yalnızca bu aralığı yeni bir çalışma kitabına kopyalayın ve yeni dosyayı kaydedin.  
Bu yaklaşım, büyük bir çalışma sayfasından tek bir tablo, rapor bloğu veya veri alanı çıkarmak ve ilişkili olmayan tüm içeriği göz ardı etmek istediğinizde idealdir. Aynı zamanda, kullanıcı tarafından seçilen bir sayfa bölgesini bağımsız dosyalar olarak dışa aktarmak için de kullanışlıdır.

### **Adımlar**
Aşağıdaki adımlar, belirli bir aralığı yeni bir çalışma kitabına kopyalayarak bir Excel dosyasını nasıl böleceğinizi açıklar:
1. Dosya yolunu vererek bir `Workbook` nesnesi oluşturup kaynak Excel dosyasını açın.  
2. Kopyalamak istediğiniz aralığı içeren hedef `Worksheet`'i, indeks (örneğin ilk sayfa) ya da `Worksheets` koleksiyonundan ad ile alın.  
3. Kopyalanacak aralığı tanımlayın. Bu, `A1:C10` gibi sabit bir hücre aralığı, `Worksheet.Cells` koleksiyonundan alınan adlandırılmış bir aralık ya da `Worksheet.Cells.CreateRange` ile oluşturulan bir aralık olabilir.  
4. Yeni bir hedef `Workbook` örneği oluşturun.  
5. Hedef çalışma kitabının ilk `Worksheet`'ine (varsayılan sayfa) erişin.  
6. Kaynak aralığı, genellikle `A1` hücresinden başlayarak hedef çalışma sayfasına kopyalayın. Hedef `Cells` koleksiyonundaki `Cells.Copy` yöntemi tüm bir aralığı kopyalamak için kullanılabilir; alternatif olarak, kaynak aralığın hücreleri döngüyle gezilip `PutValue` ile hedef hücrelere yazılabilir. İsteğe bağlı olarak `CopyOptions` sağlanarak neyin aktarılacağı (yalnızca değerler, değerler ve stiller, formüller vb.) kontrol edilebilir.  
7. `Workbook.Save` yöntemiyle hedef çalışma kitabını yeni bir dosya yolunda diske kaydedin.

### **Kod Örneği**
Beklenen çıktı, veri dizininde yalnızca belirtilen aralıktaki değerleri (ve isteğe bağlı biçimlendirmeyi) içeren tek bir yeni dosyadır. Hedef dosya, kaynak dosyanın diğer verileriyle hiçbir ilişkiye sahip değildir; sadece `A1` hücresinden başlayan çıkarılan aralığı içerir.

## Related Articles
- [Aspose.Cells for JavaScript via C++ içinde Pivot Tablosuna Filtre Alanları Ekle](/cells/tr/javascript-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for JavaScript via C++ içinde Pivot Tablolarına Stil Uygula](/cells/tr/javascript-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştir](/cells/tr/javascript-cpp/change-page-field-layout/)
- [Aspose.Cells for JavaScript via C++ içinde Sparkline'ı Görüntü ve HTML'ye Dönüştür](/cells/tr/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Excel'i OFD Formatına Dönüştürme](/cells/tr/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}