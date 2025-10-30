---
title: Node.js kullanarak C++ ile Bağımlılar ve Bağımlı Hücreler
linktitle: Önceden Gelir ve Bağımlılar
type: docs
weight: 230
url: /tr/nodejs-cpp/precedents-and-dependents/
description: Karmaşık finansal hesap çizelgelerinde bağlı hücreleri tanımlamanın yollarını anlamak ve bağımlı hücreleri ve bağımlı olmayan hücreleri izlemek için Aspose.Cells for Node.js via C++ ü kullanmayı öğrenin.
---

{{% alert color="primary" %}} 

Özellikle ortak geliştirilen karmaşık finansal çalışma tabloları, en utanç verici hataları saklayabilir. Formüllerin doğruluğunu kontrol etmek ve bir hatanın kaynağını bulmak, öncü hücreler ve bağımlı hücreleri kullanan formülün olduğu durumlarda zor olabilir.

{{% /alert %}} 
## **Giriş**
- **Öncül hücreler**, başka bir Hücredeki bir formül tarafından başvurulan hücrelerdir. Örneğin, eğer D10 hücresi =B5 formülünü içeriyorsa, B5 hücresi D10 hücresinin öncül hücresidir.
- **Bağımlı hücreler**, diğer hücrelere referans veren formüller içerir. Örneğin, D10 hücresinde =B5 formülü varsa, D10 hücresi B5 hücresine bağımlıdır.

Elektronik tabloyu okunabilir hale getirmek için belki de bir formülde kullanılan hangi hücreleri açıkça göstermek istersiniz. Benzer şekilde, diğer hücrelerin bağımlı hücrelerini çıkarmak isteyebilirsiniz.

Aspose.Cells, hücreleri izlemenize ve hangi hücrelerin bağlı olduğunu bulmanıza olanak tanır.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Microsoft Excel**
Formüller, müşteri tarafından yapılan değişikliklere bağlı olarak değişebilirler. Örneğin, C3 ve C4 hücrelerinde bir formül içeren ve C1'in C3 ve C4'e bağımlı olduğu durumu düşünelim (bu durumda formül geçersiz kılınmış olur), diğer hücrelerin iş kurallarına göre tabloyu dengelemek için değişmesi gerekebilir.

Benzer şekilde, C1 hücresi '=(B1*22)/(M2*N32)' formülünü içeriyorsa, C1'in bağımlı olduğu hücreleri, yani precedent hücreleri (B1, M2 ve N32), bulmak istiyorum.

Belirli bir hücrenin bağımlılığını başka hücrelere izlemek isteyebilirsiniz. İş kuralları formüllerde gömülüyse, bağımlılığı bulmak ve buna göre bazı kuralları uygulamak isteriz. Benzer şekilde, belirli bir hücrenin değeri değiştirilirse, çalışma sayfasındaki hangi hücrelerin bu değişimden etkilendiğini bilmek isteriz.

Microsoft Excel, öncekileri ve bağımlıları izlemek için kullanıcılara olanak sağlar.

1. **Görünüm Araç Çubuğu**'nda **Formül Denetimi**'ni seçin. Formül Denetimi iletişim kutusu görüntülenecektir.
1. Önceden Gelenleri İzleme:
   1. Önceden gelen hücreleri bulmak istediğiniz formül içeren hücreyi seçin.
   1. Doğrudan veri sağlayan her hücreye izleyici okunu göstermek için **Formül Denetimi** araç çubuğunda **Önceden Gelenleri İzle**'yi tıklatın.
1. Belirli bir hücreyi referans olarak alan formülleri izle (bağımlılar)
   1. Bağımlı hücreleri belirlemek istediğiniz hücreyi seçin.
   1. Aktif hücreye bağımlı olan her hücreye izleyici okunu göstermek için Formül Denetimi araç çubuğunda **Trace Dependents**'a tıklayın.
## **Öncekileri ve Bağımlı Hücreleri İzleme: Aspose.Cells**
### **Öncüleri İzleme**
Aspose.Cells, precedent hücreleri almayı kolaylaştırır. Basit formül precedentlerine veri sağlayan hücreleri almanın yanı sıra adlandırılmış aralıklara göre karmaşık formül precedentlerine veri sağlayan hücreleri de bulabilir.

Aşağıdaki örnekte, bir şablon excel dosyası olan Book1.xls kullanılmıştır. Elektronik tabloda veri ve formüller bulunmaktadır.

Aspose.Cells, bir hücrenin öncülerini izlemek için kullanılan [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [Cell.getPrecedents()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedents--) metodunu sağlar. Bu, çağrılan alanların bir koleksiyonunu döndürür. Yukarıda görebileceğiniz gibi, Book1.xls dosyasında, B7 hücresinde "=SUM(A1:A3)" formülü vardır. Bu nedenle, A1:A3 hücreleri B7 hücresinin öncüleri olarak kabul edilir. Aşağıdaki örnek, Book1.xls şablon dosyasını kullanarak öncüleri izleme özelliğini gösterir.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B4");
// Check if the cell object is not null before proceeding
if (cell) 
{
const ret = cell.getPrecedents();
if (!ret.isNull() && ret.getCount() > 0)
{
const area = ret.get(0);
console.log(area.getSheetName());
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));
console.log(AsposeCells.CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));
}
else
{
console.error("No precedents found for the cell.");
}
} 
else 
{
console.error("Cell B4 is null.");
}
```
### **Bağımlıları İzleme**
Aspose.Cells, çalışma sayfalarındaki bağlı hücreleri almanıza olanak tanır. Sadece basit bir formüle ilişkin verileri sağlayan hücreleri değil, aynı zamanda isimli alanlar içeren karmaşık formüllerin bağımlılarını sağlayan hücreleri de bulabilir.

Aspose.Cells, [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [Cell.getDependents(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependents-boolean-) metodunu sağlar; bu, bir hücrenin bağımlılarını izlemek için kullanılır. Örneğin, Book1.xlsx dosyasında B2 ve C2 hücrelerinde sırasıyla "=A1+20" ve "=A1+30" formülleri bulunur. Bu örnek, A1 hücresinin bağımlılarını nasıl izleyebileceğinizi gösterir.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
const cell = cells.get("B2");
// Ensure dependents is an array
const dependents = cell.getDependents(true);

if (Array.isArray(dependents)) 
{
for (const c of dependents) 
{
console.log(c.getName());
}
} 
else 
{
console.error("Dependents is not an array");
}
```
### **Hesaplama zincirine göre precedent ve bağımlı hücreleri izleme**
Yukarıdaki bağımlı ve öncüleri izleme API'leri, formül ifadesine göre sırasıyla düzenlenmiştir. Kullanıcıların birkaç formül arasındaki karşılıklı bağımlılıkları izlemek için kolay bir yol sağlarlar. Eğer çalışma kitabında çok sayıda formül varsa ve kullanıcı her hücre için öncüleri ve bağımlıları izlemek istiyorsa, performansı düşük olur. Bu durumda, kullanıcı [Cell.getPrecedentsInCalculation()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getPrecedentsInCalculation--) ve [Cell.getDependentsInCalculation(boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#getDependentsInCalculation-boolean-) metodlarını kullanmayı düşünmelidir. Bu iki yöntem, bağımlılıkları hesaplama zinciri doğrultusunda izler. Bu yüzden, bunları kullanmadan önce [FormulaSettings.getEnableCalculationChain()](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--) ile hesaplama zincirini etkinleştirmeniz gerekir. Sonrasında, [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kullanarak çalışma kitabını tamamen hesaplayın ve ardından, ihtiyaç duyduğunuz tüm hücreler için öncüleri veya bağımlıları izleyebilirsiniz.

Bazı formüller için, getPrecedents ve getPrecedentsInCalculation sonuçları farklı olabilir ve getDependents ile getDependentsInCalculation sonuçları da farklı olabilir. Örneğin, A1 hücresinin formülü "=IF(TRUE,B2,C3)" ise, getPrecedents A1 için B2 ve C3'ü sağlar. Buna göre, B2 ve C3'ün bağımlısı A1'dir. Ancak, bu formül hesaplandığında, sadece B2'nin sonucu etkileyebileceği açıktır. Bu nedenle, getPrecedentsInCalculation C3'ü A1 için sağalmaz ve getDependentsInCalculation A1'i C3 için sağlayamaz. Bazen kullanıcılar, sadece şu anki verilerle formüllerin hesaplanan sonucunu gerçekten etkileyen iç bağımlılıkları izleme gereksinimi duyarlar; bu durumda, getDependentsInCalculation/getPrecedentsInCalculation kullanmak daha uygun olur.

Aşağıdaki örnek, hücreler için hesaplama zincirine göre öncüleri ve bağımlıları nasıl izleyebileceğinizi gösterir:


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const cells = workbook.getWorksheets().get(0).getCells();
cells.get("A1").setFormula("=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
cells.get("A2").setFormula("=IF(TRUE,B2,B1)");
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);
workbook.calculateFormula();

let en = cells.get("B1").getDependentsInCalculation(false);
console.log("B1's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}


en = cells.get("B2").getDependentsInCalculation(false);
console.log("B2's calculation dependents:");
for (var cell of en) {
console.log(cell.getName());
}

en = cells.get("A1").getPrecedentsInCalculation();
console.log("A1's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}


en = cells.get("A2").getPrecedentsInCalculation();
console.log("A2's calculation precedents:");
for (var area of en) {
console.log(area.toString());
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
