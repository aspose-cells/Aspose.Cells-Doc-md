---  
title: Grid çizgileri ve Satır Sütun Başlıklarını Göster ve Gizle ile Node.js kullanarak C++  
linktitle: Izgara Çizgileri ve Satır Sütun Başlıklarını Gösterme ve Gizleme  
type: docs  
weight: 30  
url: /tr/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/  
description: Bu makale, Node.js API sini C++ aracılığıyla kullanarak bir Excel çalışma sayfasının ızgara çizgileri, satır ve sütun başlıklarını programatik olarak gizleme veya gösterme için örnek kod sağlar.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, varsayılan olarak görünür olan çalışma taşraflarının izgara çizgilerini gizleme ve göstermeyi destekler. Aynı zamanda çalışma taşraflarının Satır Sütun Başlıklarının görünürlüğünü kontrol etmeyi sağlar.  
{{% /alert %}}  

## **Izgara Çizgilerini Gösterme ve Gizleme**  

Tüm Excel çalışma taşraları varsayılan olarak izgara çizgilerine sahiptir. Onlar, belirli hücrelere veri girmeyi kolaylaştırdığı için hücreleri çevreler. Izgara çizgileri, bir çalışma taşrasını hücre koleksiyonu olarak görüntülememizi sağlar, burada her hücre kolayca tanımlanabilir.  

### **Izgaraların Görünürlüğünü Kontrol Etme**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş özellikler ve yöntemler sunar. Izgara çizgilerinin görünürlüğünü kontrol etmek için [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) özelliğini kullanın. [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabileceği anlamına gelir.  

#### **Izgaraları Görünür Yapma**  

Izgara çizgilerini görünür hale getirmek için [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) özelliğini **true** olarak ayarlayın.  

#### **Izgaraları Gizleme**  

Izgara çizgilerini gizlemek için [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) özelliğini **false** olarak ayarlayın.  

Aşağıda, bir excel dosyasını (book1.xls) açarak ilk çalışma sayfasındaki ızgara çizgilerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden [**Worksheet.isGridlinesVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isGridlinesVisible--) özelliğinin kullanımı gösterilmektedir.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileData = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file data
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the grid lines of the first worksheet of the Excel file
worksheet.setIsGridlinesVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Satır Sütun Başlıklarını Göster ve Gizle**  

Bir Excel dosyasındaki tüm çalışma sayfaları, satırlar ve sütunlarda düzenlenmiş hücrelerden oluşur. Tüm satırlar ve sütunlar benzersiz değerlere sahiptir ve bunları tanımlamak ve bireysel hücreleri tanımlamak için kullanılır. Örneğin, satırlar numaralandırılır - 1, 2, 3, 4, vb. - ve sütunlar alfabetik sıraya göre düzenlenir - A, B, C, D, vb. Satır ve sütun değerleri başlıklarda görüntülenir. Aspose.Cells kullanılarak, geliştiriciler bu satır ve sütun başlıklarının görünürlüğünü kontrol edebilir.  

### **Çalışma sayfalarının görünürlüğünü kontrol etmek**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş özellikler ve yöntemler sunar. Satır ve sütun başlıklarının görünürlüğünü kontrol etmek için [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğini kullanın. [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabileceği anlamına gelir.  

#### **Satır/Sütun Başlıklarını Görünür Yapma**  

Satır ve sütun başlıklarını görünür yapmak için [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğini **true** olarak ayarlayın.  

#### **Satır/Sütun Başlıklarını Gizleme**  

Satır ve sütun başlıklarını gizlemek için [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğini **false** olarak ayarlayın.  

Aşağıda, bir excel dosyasını (book1.xls) açarak ilk çalışma sayfasındaki satır ve sütun başlıklarını gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden [**Worksheet.isRowColumnHeadersVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isRowColumnHeadersVisible--) özelliğinin kullanımı gösterilmektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file path
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the headers of rows and columns
worksheet.setIsRowColumnHeadersVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Ayrıca, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) sınıfının [**Cells.unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) ve [**Cells.unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) metodlarını kullanarak birden fazla satır ve sütunu görünür hale getirmek de mümkündür.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
