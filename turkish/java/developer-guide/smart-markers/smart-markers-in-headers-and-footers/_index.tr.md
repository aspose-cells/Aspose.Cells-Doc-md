---
title: Üstbilgi ve Altbilgi İçin Akıllı İşaretçiler | Aspose.Cells for Java
linktitle: Üstbilgi ve Altbilgi Akıllı İşaretçiler | Aspose.Cells
description: Çift açı işareti sözdizimi ve WorkbookDesigner.setEnableHeaderFooterMarkers seçeneği kullanarak sayfa üstbilgi ve altbilgi bölümlerine Smart Marker yer tutucularını getter-bean listeleri veya JSON veri kaynaklarıyla yerleştirin ve veri URI'ları aracılığıyla resimleri bağlayın, Aspose.Cells for Java’da.
keywords: Aspose.Cells for Java, Akıllı İşaretçiler, üstbilgiler, altbilgiler, üstbilgi altbilgi işaretçileri, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, getter bean, JSON veri kaynağı, veri bağlama, resim, veri URI, Java
type: docs
weight: 196
url: /tr/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Sayfa üstbilgileri ve altbilgileri genellikle rapor başlığı, raporlama dönemi, yazar ve departman gibi rapor meta verilerini içerir. Bu bilgiler zaten çalışma kitabını doldurmak için kullanılan veri kaynağında mevcutsa, bunları manuel olarak tekrar etmek gereksiz çoğaltmaya neden olur.  
Klasik Smart Marker sözdizimi, `&=Source.Field`, çalışma sayfası gövde hücrelerinde işlenir. `PageSetup.setHeader` veya `PageSetup.setFooter` aracılığıyla bir klasik işaretçiyi üstbilgi ya da altbilgiye yerleştirirseniz, bu metin olduğu gibi kalır çünkü üstbilgi ve altbilgi dizesi, `WorkbookDesigner.process()` tarafından taranan çalışma sayfası hücre ızgarasının bir parçası değildir.  
**Aspose.Cells for Java 26.11** ile birlikte, `WorkbookDesigner` üstbilgi/altbilgi işaretçi seçeneği varsayılan olarak `false` değerindedir. `designer.process()` çağrısından önce `designer.setEnableHeaderFooterMarkers(true)` çağırarak `<<Source.Field>>` biçiminde yazılmış yer tutucuların üstbilgi ve altbilgi bölüm dizelerinde çözülmesini sağlayabilirsiniz. Üstbilgi ve altbilgi yer tutucuları, gövde işaretçileriyle aynı veri kaynağını kullanır.  
Her üstbilgi ve altbilgi üç adreslenebilir bölüm içerir:
- Bölüm `0` sol bölümdür.
- Bölüm `1` orta bölümdür.
- Bölüm `2` sağ bölümdür.
Bu bölümleri yazmak için `PageSetup.setHeader(int section, String value)` ve `PageSetup.setFooter(int section, String value)` metodlarını kullanın. İşlemden sonra tamamlanmış metni almak için `PageSetup.getHeader(int section)` ve `PageSetup.getFooter(int section)` metodlarını kullanın.

{{% alert color="primary" %}}
`<<Source.Field>>` gibi bir yer tutucu, alan değerini metin olarak bölüm dizesine ekler. Resimler `(picture)` ek eki ve bir veri-URI değeriyle bağlanır.
{{% /alert %}}

## **Getter-Bean Listesi ile Üstbilgi/Altbilgi İşaretçilerini Etkinleştirme**
**Aspose.Cells for Java 26.11** içinde üstbilgi ve altbilgi yer tutucularını bir getter-bean listesiyle çözmek için aşağıdaki adımları izleyin:
1. Bir `Workbook` oluşturun ve örneğin `workbook.getWorksheets().get(0)` ifadesiyle indeks `0`’daki ilk `Worksheet` nesnesini elde edin.
2. `PageSetup.setHeader` ve `PageSetup.setFooter` metodlarıyla istenen üstbilgi ve altbilgi bölümlerine `<<Source.Field>>` yer tutucularını yazın.
3. Her yer tutucu alanı için bir getter (örneğin `getName()`) içeren küçük bir **PUBLIC** bean sınıfı tanımlayın ve yer tutucuların kullandığı kaynak önekine uygun bir kaynak adı seçin. Örneğin, `node` adlı bir kaynak, `<<node.Name>>` gibi yer tutucuları besler. Bu platformda iki bağlama kuralı doğrulanır: public **FIELDS** içeren bir bean hiçbir şey bağlamaz (motor getter’ları okur, alanları değil) ve **PACKAGE-PRIVATE** sınıf da bağlamaz — introspection yalnızca public sınıfları görür ve public olmayan bir bean `process()` sırasında `NullPointerException` hatası verir.
4. Çalışma kitabı için bir `WorkbookDesigner` oluşturun.
5. İşleme başlamadan önce `designer.setEnableHeaderFooterMarkers(true)` çağırın.
6. Listeyi ve kaynak adını `designer.setDataSource("node", table)` ile ekleyin.
7. `designer.process()` metodunu çağırın.
8. İşlemden sonra yer tutucular artık üstbilgi veya altbilgi metninde bulunmaz. Tamamlanmış bölüm dizelerini almak için `PageSetup.getHeader` ve `PageSetup.getFooter` metodlarını kullanın.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        private final String author;
        public Node(String name, String author) {
            this.name = name;
            this.author = author;
        }
        public String getName() {
            return name;
        }
        public String getAuthor() {
            return author;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Center header and center footer carry <<Source.Field>> placeholders
        worksheet.getPageSetup().setHeader(1, "Quarterly Report - <<node.Name>>");
        worksheet.getPageSetup().setFooter(1, "Prepared by <<node.Author>>");
        List<Node> table = Arrays.asList(new Node("Q4 2026", "Aspose.Cells"));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", table);
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        System.out.println("Footer: " + worksheet.getPageSetup().getFooter(1));
        // This prints:
        // Header: Quarterly Report - Q4 2026
        // Footer: Prepared by Aspose.Cells
        workbook.save("HeaderFooterSmartMarkers.xlsx");
    }
}
```

## **JSON Veri Kaynağı Kullanma**
Rapor verileri zaten JSON biçiminde mevcutsa getter-bean listesi yerine JSON kullanabilirsiniz. Kaynağı eklemek için `WorkbookDesigner.setJsonDataSource(String name, String json)` metodunu çağırın.  
`name` argümanı, yer tutucular tarafından kullanılan kaynak adıdır. Örneğin, `node` adı `<<node.Company>>` ve `<<node.Title>>` gibi yer tutucuları besler.  
`setJsonDataSource` metoduna satır verisini doğrudan aktarın:
- Bir satır dizisi, bir veya daha fazla satır nesnesi içeren bir JSON dizisi desteklenir.
- Tek satır nesnesi de doğrudan aktarılabilir.
- Satırları `{"rows":[...]}` gibi adlandırılmış bir üst düzey anahtar altında sarmalamayın. Bu sarıcı, bu iş akışı için beklenen satır-odaklı girdi biçimi değildir.
Tek bir JSON kaynağı, aynı `designer.process()` çağrısı sırasında iki işaretçi stilini de besleyebilir. Klasik `&=` işaretçisini bir çalışma sayfası gövde hücresinde ve çift açı işareti `<<>>` yer tutucularını üstbilgi ve altbilgi bölümlerinde çözebilir. Üstbilgi ve altbilgi yer tutucularının çözülmesi için yine `EnableHeaderFooterMarkers` seçeneğini etkinleştirmeniz gerekir.

```java
import com.aspose.cells.*;
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // Left header, right header, and a classic body marker — one JSON source feeds all three
        worksheet.getPageSetup().setHeader(0, "<<node.Company>>");
        worksheet.getPageSetup().setHeader(2, "Page <<node.Title>>");
        worksheet.getCells().get("A1").putValue("&=node.Company");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setJsonDataSource("node", "[{\"Company\":\"Aspose Pty Ltd\",\"Title\":\"Half-Year Report\"}]");
        designer.process();
        System.out.println("Left: " + worksheet.getPageSetup().getHeader(0));
        System.out.println("Right: " + worksheet.getPageSetup().getHeader(2));
        System.out.println("Body: " + worksheet.getCells().get("A1").getStringValue());
        // This prints:
        // Left: Aspose Pty Ltd
        // Right: Page Half-Year Report
        // Body: Aspose Pty Ltd
        workbook.save("HeaderFooterJsonMarkers.xlsx");
    }
}
```

## **Anahtar ve Çok Satırlı Kaynak Anlamı**
`EnableHeaderFooterMarkers` ayarı varsayılan olarak `false` olup, bu anahtar yalnızca üstbilgi ve altbilgi `<<Source.Field>>` yer tutucularını kontrol eder. Anahtar kapalıyken `designer.process()` klasik `&=` gövde işaretçilerini yine çözer, ancak bir üstbilgi ya da altbilgi içinde `<<Source.Field>>` yer tutucusu hâlâ düz metin olarak kalır.  
Bir üstbilgi veya altbilgi bölümü tek bir dizedir, tekrarlayan bir bant değildir. Veri kaynağı birden fazla satır içeriyorsa, ilk satır üstbilgi ve altbilgi değerlerini sağlar. Çözüldükten sonra değerler normal üstbilgi ya da altbilgi metni haline gelir. `workbook.save(...)` çağrısından sonra çalışma kitabında kalır ve kaydedilen çalışma kitabı tekrar yüklendiğinde de bulunur.  
Aşağıdaki örnek, aynı çok-satırlı bean listesini iki çalışma kitabına uygulayarak devre dışı ve etkin davranışı karşılaştırır. `plainDesigner` yer tutucuyu değiştirmeden bırakırken, `enabledDesigner` ilk satırı kullanarak çözer.

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String name;
        public Node(String name) {
            this.name = name;
        }
        public String getName() {
            return name;
        }
    }
    public static void main(String[] args) throws Exception {
        List<Node> table = Arrays.asList(
                new Node("First Row"),
                new Node("Second Row")
        );
        // Without the switch the placeholder stays literal text
        Workbook plainWorkbook = new Workbook();
        Worksheet plainSheet = plainWorkbook.getWorksheets().get(0);
        plainSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner plainDesigner = new WorkbookDesigner(plainWorkbook);
        plainDesigner.setDataSource("node", table);
        plainDesigner.process();
        // With the switch on, the FIRST row of a multi-row source wins
        Workbook enabledWorkbook = new Workbook();
        Worksheet enabledSheet = enabledWorkbook.getWorksheets().get(0);
        enabledSheet.getPageSetup().setHeader(1, "<<node.Name>>");
        WorkbookDesigner enabledDesigner = new WorkbookDesigner(enabledWorkbook);
        enabledDesigner.setEnableHeaderFooterMarkers(true);
        enabledDesigner.setDataSource("node", table);
        enabledDesigner.process();
        System.out.println("Without switch: " + plainSheet.getPageSetup().getHeader(1));
        System.out.println("With switch: " + enabledSheet.getPageSetup().getHeader(1));
        // This prints:
        // Without switch: <<node.Name>>
        // With switch: First Row
        enabledWorkbook.save("HeaderFooterMarkersEnabled.xlsx");
    }
}
```

## **Üstbilgi veya Altbilgiye Resim Bağlama**
`(picture)` eki, bir resmin üstbilgi veya altbilgi bölümüne bağlanmasını sağlar. Görüntünün görünmesi gereken yere `<<node.logo(picture)>>` yazın ve alan değerini bir veri URI olarak sağlayın — `data:image/png;base64,` öneki ardından görüntü baytlarının Base64 metni gelmelidir. `data:` öneki olmayan çıplak Base64 dizesi bir resim yerleştirmez.  
`designer.process()` sonrası:
1. Yer tutucu `&G` ile değiştirilir; bu, standart üstbilgi ve altbilgi resim kodudur. İşaretçi, bölüm dizesi içinde bir kod haline geldiği için `Logo: <<node.logo(picture)>>` gibi daha uzun bir metnin içinde yer alabilir.
2. Görüntü baytları, o çalışma sayfasının üstbilgi/altbilgi çizim katmanına eklenen bir medya parçası olarak çalışma kitabına gömülür, bu yüzden resim üstbilgi ya da altbilgiyle birlikte basılır.

```java
import com.aspose.cells.*;
import java.nio.file.*;
import java.util.*;
public class CodeRunner {
    public static class Node {
        private final String logo;
        public Node(String logo) {
            this.logo = logo;
        }
        public String getLogo() {
            return logo;
        }
    }
    public static void main(String[] args) throws Exception {
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        // The (picture) suffix binds the image named by the data-URI field into the header
        worksheet.getPageSetup().setHeader(1, "Logo: <<node.logo(picture)>>");
        String logoDataUri = "data:image/png;base64," + Base64.getEncoder().encodeToString(Files.readAllBytes(Paths.get("logo.png")));
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setEnableHeaderFooterMarkers(true);
        designer.setDataSource("node", Arrays.asList(new Node(logoDataUri)));
        designer.process();
        System.out.println("Header: " + worksheet.getPageSetup().getHeader(1));
        // This prints:
        // Header: Logo: &G
        workbook.save("HeaderFooterPicture.xlsx");
    }
}
```

Yazdırılan `&G` kodu, Excel’in üstbilgiyi işlerken yorumladığı resim kodudur — `logo.png` baytları artık `HeaderFooterPicture.xlsx` içinde bulunur ve resim kodun yerini alarak basılır.  
Üstbilgi ve altbilgi Smart Marker’larını kullanmak için `PageSetup.setHeader` ve `PageSetup.setFooter` metodlarıyla sol, orta ve sağ üstbilgi veya altbilgi bölümlerine `<<Source.Field>>` yer tutucularını yazın. `WorkbookDesigner` üzerinde `designer.setEnableHeaderFooterMarkers(true)` çağırdıktan sonra `designer.process()` metodunu çalıştırın ve değerleri `designer.setDataSource(name, list)` ile getter-bean listesi ya da `designer.setJsonDataSource(name, json)` ile sağlayın. Tamamlanmış bölümleri `PageSetup.getHeader` ve `PageSetup.getFooter` metodlarıyla okuyun. Aynı veri kaynağı, bir işlemde gövde işaretçilerini ve üstbilgi/altbilgi yer tutucularını besleyebilir. Bir bölüme resmi bağlamak için `(picture)` ekini veri-URI değeriyle ekleyin.

## **İlgili Makaleler**
- [SmartMarker Tek Hücre Dizi İşleme](/cells/tr/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}