---  
title: Excel İş Sayfasının Dondurma Panellerini Node.js ile C++ kullanarak kilitleyin  
linktitle: Pano Dondur  
type: docs  
weight: 190  
url: /tr/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: Bu makalede, Aspose.Cells for Node.js via C++ kullanarak Excel Çalışma Sayfalarının bölmelerini programlı olarak nasıl donduracağınızı öğrenin.  
keywords: Panelleri dondur, Pencereyi dondur.  
---  

## **Giriş**  

Bu makalede, Panelleri Dondurmayı Öğreneceğiz. Bir anlamlı başlık altındaki büyük veri kümesine sahipseniz ve kaydırırken başlığı göremiyorsanız, veya her kayıtta birçok veri varsa, panelleri dondurabilir ve kaydırılan diğer verilerle birlikte donmuş bölümü görebilirsiniz. Üst satırlarda veya ilk sütunlarda başlıkları kolayca görebilirsiniz. Panelleri dondurma veya çözme, verilerin görünümünü değiştirir, veriyi değil.  

## **Excel'de**  

**![Excel'de Panoları Dondur](Freeze-panes.png)**  

1. Panelleri dondurmak, satır ve sütunları dondurmak istiyorsanız, önce bir hücre seçin (örneğin B2).  
2. Görünüm > Panoları Dondur'a tıklayın.  
3. Açılır menüden Panoları Dondur'a tıklayın.  
4. Kaydırdığınızda veya sağa kaydırdığınızda, ilk satır ve sütun donmuş kalır.  

**![Donmuş Paneller](Frozen-Panes.png)**  

Gördüğünüz gibi, 1. Satır ve sütun A dondurulmuştur, ikinci satır 32 ve ikinci görünür sütun D'dir.  

Panelleri dondurmak ile büyük verilerinizi satır veya sütun etiketlerini takip etmeye gerek kalmadan görüntüleyebilirsiniz.  

## **Aspose.Cells for Node.js via C++ ile Pencereleri Dondur**  
Aspose.Cells for Node.js via C++ ile pencereleri dondurmak basittir. Lütfen seçilen Hücrede pencereleri dondurmak için [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) yöntemini kullanın.  
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.  
2. Worksheet.freezePanes() yöntemi ile Pencereleri Dondur.  
3. Dosyayı kaydedin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).  

