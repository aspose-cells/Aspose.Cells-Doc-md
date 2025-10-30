---  
title: Büyük Veri Setleri ile Çalışırken Bellek Kullanımını Optimize Etmek Node.js ve C++ kullanılarak  
linktitle: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme  
type: docs  
weight: 180  
url: /tr/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

Büyük veri setleri içeren veya büyük bir Microsoft Excel dosyasını okuyan çalışma kitabı oluştururken, toplam RAM miktarı her zaman bir endişedir. Bu zorlukla başa çıkmak için uyarlanabilecek önlemler vardır. Aspose.Cells for Node.js via C++, bellek kullanımını azaltmak, düşürmek ve optimize etmek için bazı ilgili seçenekler ve API çağrılarını sağlar. Ayrıca, işlemin daha verimli çalışmasına ve daha hızlı yürütülmesine yardımcı olabilir.  

Hücre verisi için bellek kullanımını optimize etmek ve genel bellek maliyetini azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) seçeneğini kullanın. Büyük veri setleri için hücreler oluştururken, varsayılan ayar ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)) kullanmaktan belirli bir miktarda bellek tasarrufu sağlayabilir.  

{{% /alert %}}  

## **Bellek Kullanımını Optimize Etme**  

### **Büyük Excel Dosyaları Okuma**  

Aşağıdaki örnek, optimize edilmiş modda büyük bir Microsoft Excel dosyasını nasıl okuyacağınızı göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Büyük Excel Dosyaları Yazma**  

Aşağıdaki örnek, optimize edilmiş bir modda bir çalışma sayfasına büyük bir veri seti yazmanın nasıl yapılacağını gösterir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Dikkat**  

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) tüm sürümler için uygulanır. Bazı durumlarda, özellikle hücreler için büyük veri setleri ile çalışma kitabı oluşturulurken, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) seçeneği bellek kullanımını optimize edebilir ve uygulamanın bellek maliyetini azaltabilir. Ancak, bu seçenek bazı özel durumlarda performansı azaltabilir, örneğin aşağıdaki gibi.  

1. **Hücrelere Rastgele ve Tekrarlı Erişim**: Hücre koleksiyonuna en etkili erişim sırası, satır satır hücreye erişmek ve sonra satır satır ilerlemektir. Özellikle, eğer satır/ Hücreleri [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) ve [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) tarafından edinilen Yorumlayıcı ile erişirseniz, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) ile maksimize edilir.  
2. **Hücreler ve Satırların Eklenmesi ve Silinmesi**: Lütfen dikkat edin ki, hücreler/satırlar üzerinde çok sayıda ekleme/silme işlemi varsa, performans düşüşü *MemoryPreference* modunda, *Normal* moduna göre belirgin olacaktır.  
3. **Farklı Hücre Tipleri Üzerinde İşlem Yapma**: Çoğu hücre string değeri veya formül içeriyorsa, bellek maliyeti *Normal* mod ile aynıdır, ancak birçok boş hücre veya hücre değeri sayısal, bool gibi ise, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) seçeneği daha iyi performans sağlayacaktır.  

{{< app/cells/assistant language="nodejs-cpp" >}}
