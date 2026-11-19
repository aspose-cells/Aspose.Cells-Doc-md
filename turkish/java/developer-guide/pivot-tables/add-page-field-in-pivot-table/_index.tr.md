---
title: Aspose.Cells for Java'te PivotTable'a filtre alanları ekleme
description: Java için Aspose.Cells kullanarak pivot tablolara filtre alanları eklemeyi ve yapılandırmayı öğrenin; filtre alanları ekleme, tekli seçim filtrelemesi ve çoklu seçim filtrelemesi dahil.
linktitle: Filtre Alanları Ekleme
keywords: Aspose.Cells, Java, pivot tablo, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, pivot tablolardaki filtre alanlarının tüm yaşam döngüsünü destekler. Yüksek düzeyli bir kolaylık API'si veya daha düşük düzeyli `PageFields` koleksiyonu aracılığıyla bir filtre alanı ekleyebilir, filtreni tekli seçim modunda yönetebilir, filtreyi temizleyerek her sayfa öğesini gösterebilir ya da Excel'deki onay kutusu kullanıcı arayüzü üzerinden kullanıcıların aynı anda birden fazla sayfa öğesi seçebilmesi için alanı çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**
filtre alanı, kaynak verilerin *hangi alt kümesinin* pivot gövdesinde görüntüleneceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de oluşturulan pivot'un üst kısmında bir açılır liste olarak görür ve mevcut sayfa öğelerinden birini seçmek, pivot gövdesini yalnızca o sayfa öğesine ait kayıtların özetlenmesi için yeniden oluşturur. Bir pivot alanı, `PivotFieldType.Row`, `PivotFieldType.Column` veya `PivotFieldType.Data` yerine `PivotFieldType.Page` olarak kaydedildiğinde filtre alanı haline gelir.
filtre alanı iki davranışta çalışabilir. Varsayılan **tekli seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür, dolayısıyla pivot gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve pivot gövdesi işaretlenen tüm sayfa öğelerinin birleşimini özetler. Aynı kaynak alan, tek bir özelliğin açılıp kapatılmasıyla bu davranışlar arasında ileri geri taşınabilir.
Aspose.Cells for Java, bir filtre alanı kaydetmek için iki eşdeğer yol sunar. Yüksek düzeyli API, kaynak-sütun adını alan ve alanı tek bir çağrıyla ekleyen `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` yöntemidir. Daha düşük düzeyli API ise, zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini filtre alanına eklemek istediğinizde kullanılan `PivotTable.PageFields.add(PivotField)` yöntemidir. Her iki API de aynı `PageFields` koleksiyonunu doldurur ve bu makalenin devamında bunlar arasında nasıl seçim yapılacağı ve her filtreleme modunun nasıl yönetileceği gösterilmektedir.

## **filtre alanı Ekleme**
Bir pivot alanını filtre alanına kaydetmenin iki yolu vardır. Yüksek düzeyli çağrı, kaynak-sütun adını bir dize olarak alır ve en yaygın yoldur. Daha düşük düzeyli çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden fazla pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `PivotTable.PageFields` koleksiyonuna yerleştirir; ardından oluşturulan pivot'un üst kısmında sayfa açılır listesi olarak görünür.

### addFieldToArea ile filtre alanı Ekleme
Aşağıdaki örnek, küçük bir Fruit / Year / Amount veri kümesi oluşturur, E3 hücresine bir pivot tablo yerleştirir (satır alanında `Fruit`, veri alanında `Amount` ve filtre alanında `Year`), pivot'u yeniler ve çalışma kitabını kaydeder.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Refresh and calculate the pivot table data
pivotTable.calculateData();
// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### PageFields.add ile filtre alanı Ekleme
Zaten bir `PivotField` örneğiyle çalışıyorsanız, onu doğrudan `PivotTable.PageFields.add` yöntemine geçebilirsiniz. Pivot tablo ve filtre alanı, önceki senaryodakiyle tam olarak aynı şekilde oluşturulur; yalnızca son sayfa-alanı kaydı daha düşük düzeyli API çağrısıyla değiştirilir.

```java
import com.aspose.cells.*;
// - The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit->Row,
//   Amount->Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add - the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Tekli Seçim Filtrelemesi (Tek Bir Sayfa Öğesini Gösterme)**
Varsayılan tekli seçim davranışında, filtre alanı tek bir açılır liste olarak işlenir ve `PivotField.CurrentPageItem` tamsayısı, pivot gövdesini hangi sayfa öğesinin yönlendireceğini seçer. Belirli bir indeks atamak o tek öğeyi seçer; özel bekçi değeri `0x7FFD` (ondalık 32765) atamak ise filtreyi temizler, böylece tüm sayfa öğeleri aynı anda özetlenir. Tekli seçim varsayılandır; bunu açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme
`CurrentPageItem` öğesini sihirli değer olan `0x7FFD` olarak ayarlamak, filtreni temizlemekle eşdeğerdir: pivot gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Create pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivot = pivotTables.add("=A1:C7", 2, 4);
// Configure pivot fields: Fruit to Row, Amount to Data, Year to Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items",
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Belirli Bir Öğeyi Gösterme
`CurrentPageItem` öğesini gerçek bir indekse ayarlamak yalnızca o sayfa öğesini seçer. İndeks, öğenin filtre alanının sıralanmış öğe listesindeki konumudur; dolayısıyla örneğin `1` değeri, sıralamadan sonraki ikinci öğeyi seçer.

```java
import com.aspose.cells.*;
// Create workbook
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Add pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivotTable = pivotTables.add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Çoklu Seçim Filtrelemesi**
Çoklu seçim filtrelemesi, sayfa açılır listesini bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birden fazla sayfa öğesi seçmesine olanak tanır. Aspose.Cells, birlikte çalışan iki özellik sunar. Çoklu seçim kullanıcı arayüzünün hiçbir şekilde geçerli olması için `PivotField.IsMultipleItemSelectionAllowed` öğesinin önce `true` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.IsHidden` öğesi onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir ya da yalnızca belirli öğeleri beyaz listeye alabilirsiniz.
Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Year filtre alanında çoklu seçimi etkinleştirir ve ardından iki örüntü gösterir: Bölüm A, her girdi için `IsHidden` öğesini `false` olarak bırakarak her sayfa öğesini gösterir; Bölüm B ise yalnızca seçtiğiniz kaynak değerlerini beyaz listeye alır ve `switch (pivotItems[i].getStringValue())` bloğu aracılığıyla diğer her şeyi gizler.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
PivotTable pivotTable = pivots.add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Part A -- select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Part B -- select only specific items by source value
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Not:** `PivotItem.IsHidden` aracılığıyla çoklu seçim filtrelemesi kullanırken, **en az bir `PivotItem` görünür kalmalıdır** (`IsHidden == false`). Her öğe gizlenirse, Excel dosyayı açarken ya çöker ya da boş bir pivot oluşturur. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API ve Hangi Mod Kullanılmalı?**
Aşağıdaki tablo, her senaryoyu ayrıntılı olarak okumak zorunda kalmadan doğru kombinasyonu seçebilmeniz için her API'nin ve modun ne zaman kullanılacağını özetler.
| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| Kaynak-sütun adına göre filtre alanı ekleme (en yaygın) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | yok | Yüksek düzeyli, tek satır. Bir `PivotField` referansına ihtiyacınız olmadığı sürece bunu kullanın. |
| Zaten bir `PivotField` nesneniz varken filtre alanı ekleme | `PivotTable.PageFields.add(PivotField)` | yok | Alan nesnesi başka yerden elde edildiğinde veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.CurrentPageItem` | belirli bir indekse ayarlanır | Örneğin, `1` sıralı listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreni temizleme | `PivotField.CurrentPageItem` | `0x7FFD` olarak ayarlanır | Sihirli değer olan `0x7FFD` (ondalık 32765), "tüm öğeler" için bekçi değerdir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.IsMultipleItemSelectionAllowed` | `true` olarak ayarlanır | Herhangi bir `IsHidden` çağrısının geçerli olmasından önce gereklidir. |
| Çoklu seçim listesinde tek tek öğeleri gizleme / gösterme | `PivotItem.IsHidden` | öğeye göre ayarlanır | En az bir öğe görünür kalmalıdır (`IsHidden == false`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemesini yapılandırırken görünürlük kısıtlamasını her zaman hatırlayın. Çoklu seçim filtre alanındaki her `PivotItem` gizlenirse, Excel dosyayı açarken çöker veya boş bir pivot oluşturur. Beyaz listenizi kaynak verilerinize göre oluşturun, böylece en az bir öğe görünür kalsın; kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılır.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}