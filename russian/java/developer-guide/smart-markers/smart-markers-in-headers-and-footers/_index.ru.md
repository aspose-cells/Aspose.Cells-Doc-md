---
title: Smart Markers в заголовках и нижних колонтитулах | Aspose.Cells for Java
linktitle: Smart Markers в колонтитулах | Aspose.Cells
description: Размещайте заполнители Smart Markers в заголовках и нижних колонтитулах страниц с помощью синтаксиса двойных угловых скобок и переключателя WorkbookDesigner.setEnableHeaderFooterMarkers, используя списки bean-геттеров или JSON-источники данных, а также привязывайте изображения через data-URI в Aspose.Cells for Java.
keywords: Aspose.Cells for Java, Smart Markers, заголовки, нижние колонтитулы, маркер заголовка и нижнего колонтитула, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, bean-геттер, JSON-источник данных, привязка данных, изображение, data URI, Java
type: docs
weight: 196
url: /ru/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Возможные сценарии использования**
Заголовки и нижние колонтитулы страниц обычно содержат метаданные отчёта, такие как название отчёта, период отчётности, автор и отдел. Когда эта информация уже присутствует в источнике данных, используемом для заполнения рабочей книги, её ручное дублирование создаёт ненужную избыточность.  
Классический синтаксис Smart Marker, `&=Source.Field`, обрабатывается в ячейках тела рабочего листа. Если разместить классический маркер в заголовке или нижнем колонтитуле с помощью `PageSetup.setHeader` или `PageSetup.setFooter`, он останется буквальным текстом, поскольку строки заголовка и нижнего колонтитула не являются частью сетки ячеек листа, сканируемой `WorkbookDesigner.process()`.  
Начиная с **Aspose.Cells for Java 26.11**, опция маркеров заголовка/нижнего колонтитула в `WorkbookDesigner` имеет значение `false` по умолчанию. Вызовите `designer.setEnableHeaderFooterMarkers(true)` перед вызовом `designer.process()`, чтобы разрешить заполнители, записанные как `<<Source.Field>>` в строках разделов заголовка и нижнего колонтитула. Заполнители заголовков и нижних колонтитулов используют тот же источник данных, что и маркеры тела.  
Каждый заголовок и нижний колонтитул содержит три адресуемых раздела:
- Раздел `0` — левый раздел.  
- Раздел `1` — центральный раздел.  
- Раздел `2` — правый раздел.  

Для записи этих разделов используйте `PageSetup.setHeader(int section, String value)` и `PageSetup.setFooter(int section, String value)`. После обработки получите завершённый текст с помощью `PageSetup.getHeader(int section)` и `PageSetup.getFooter(int section)`.

{{% alert color="primary" %}}
Заполнитель вида `<<Source.Field>>` вставляет значение поля как текст в строку раздела. Изображения привязываются с помощью суффикса `(picture)` и значения data-URI.  
{{% /alert %}}

## **Включить маркеры заголовка/нижнего колонтитула с помощью списка bean-геттеров**
Используйте следующую последовательность для разрешения заполнителей заголовка и нижнего колонтитула с помощью списка bean-геттеров в **Aspose.Cells for Java 26.11**:

1. Создайте объект `Workbook` и получите его первый `Worksheet` (рабочий лист) с индексом `0`, например, с помощью `workbook.getWorksheets().get(0)`.  
2. Запишите заполнители `<<Source.Field>>` в нужные разделы заголовка и нижнего колонтитула с помощью `PageSetup.setHeader` и `PageSetup.setFooter`.  
3. Определите небольшой публичный bean-класс с геттером (например, `getName()`) для каждого поля заполнителя и выберите имя источника, совпадающее с префиксом, используемым в заполнителях. Например, источник с именем `node` поддерживает заполнители вида `<<node.Name>>`. На этой платформе проверяются два правила привязки: bean с публичными полями ничего не привязывает (движок читает только геттеры), а класс с пакетным уровнем доступа также ничего не привязывает — интроспекция видит только публичные классы, а непубличный bean приводит к `process()` с `NullPointerException`.  
4. Создайте `WorkbookDesigner` для рабочей книги.  
5. Вызовите `designer.setEnableHeaderFooterMarkers(true)` перед обработкой.  
6. Присоедините список и его имя источника с помощью `designer.setDataSource("node", table)`.  
7. Вызовите `designer.process()`.  
8. После обработки заполнители более не присутствуют в тексте заголовка или нижнего колонтитула. Используйте `PageSetup.getHeader` и `PageSetup.getFooter` для получения завершённых строк разделов.

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

## **Использовать JSON-источник данных**
Вы можете использовать JSON вместо списка bean-геттеров, когда данные отчёта уже доступны в формате JSON. Вызовите `WorkbookDesigner.setJsonDataSource(String name, String json)`, чтобы присоединить источник.  

Аргумент `name` — это имя источника, используемое заполнителями. Например, имя `node` поддерживает заполнители `<<node.Company>>` и `<<node.Title>>`.  

Передайте данные строк непосредственно в `setJsonDataSource`:
- Поддерживается массив строк, например JSON-массив, содержащий одну или несколько объектов строк.  
- Можно также передать один объект строки напрямую.  
- Не оборачивайте строки в именованный верхний ключ, такой как `{"rows":[...]}`. Этот оболочный объект не соответствует ожидаемой форме ввода, ориентированной на строки, для данного рабочего процесса.  

Один JSON-источник может заполнять оба стиля маркеров во время одного вызова `designer.process()`. Он может разрешить классический маркер `&=` в ячейке тела листа и заполнители двойных угловых скобок `<<>>` в разделах заголовка и нижнего колонтитула. По-прежнему необходимо включить `EnableHeaderFooterMarkers` для разрешения заполнителей заголовка и нижнего колонтитула.

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

## **Переключение и семантика источника с несколькими строками**
Настройка `EnableHeaderFooterMarkers` по умолчанию имеет значение `false`, и переключатель управляет только заполнителями `<<Source.Field>>` в заголовке и нижнем колонтитуле. Когда переключатель выключен, `designer.process()` по-прежнему разрешает классические маркеры `&=` в теле листа, но заполнитель `<<Source.Field>>` в заголовке или нижнем колонтитуле остаётся буквальным текстом.  

Раздел заголовка или нижнего колонтитула представляет собой одну строку, а не повторяющийся блок. Если источник данных содержит несколько строк, первая строка поставляет значения заголовка и нижнего колонтитула. После разрешения значения становятся обычным текстом заголовка или нижнего колонтитула. Они сохраняются в рабочей книге после вызова `workbook.save(...)` и присутствуют при повторной загрузке сохранённой книги.  

В следующем примере создаются две рабочие книги на основе одного и того же списка bean-геттеров с несколькими строками, чтобы продемонстрировать различия между отключённым и включённым поведением. `plainDesigner` оставляет заполнитель без изменений, тогда как `enabledDesigner` разрешает его, используя первую строку.

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

## **Привязать изображение к заголовку или нижнему колонтитулу**
Суффикс `(picture)` привязывает изображение к разделу заголовка или нижнего колонтитула. Запишите `<<node.logo(picture)>>` там, где должно появиться изображение, и передайте значение поля как data-URI — префикс `data:image/png;base64,`, за которым следует Base64-текст байтов изображения. Обычная строка Base64 без префикса `data:` не встраивает изображение.  

После `designer.process()`:
1. Заполнитель заменяется на `&G`, стандартный код изображения для заголовка и нижнего колонтитула. Поскольку маркер становится кодом внутри строки раздела, он может находиться внутри более длинного текста, например `Logo: <<node.logo(picture)>>`.  
2. Байты изображения встраиваются в рабочую книгу как часть медиа, привязанная к слою рисунков заголовка/нижнего колонтитула данного листа, поэтому изображение печатается вместе с заголовком или нижним колонтитулом.

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

Печатный `&G` — это код изображения, который Excel интерпретирует при рендеринге заголовка; байты `logo.png` теперь находятся внутри файла `HeaderFooterPicture.xlsx`, и изображение печатается вместо кода. Чтобы использовать Smart Markers в заголовках и нижних колонтитулах, запишите заполнители `<<Source.Field>>` в левый, центральный и правый разделы с помощью `PageSetup.setHeader` и `PageSetup.setFooter`. Вызовите `designer.setEnableHeaderFooterMarkers(true)` у `WorkbookDesigner` перед `designer.process()` и предоставьте значения через `designer.setDataSource(name, list)` с помощью списка bean-геттеров или `designer.setJsonDataSource(name, json)`. Прочитайте готовые разделы с помощью `PageSetup.getHeader` и `PageSetup.getFooter`. Один и тот же источник данных может заполнять маркеры тела и заполнители заголовка или нижнего колонтитула за один проход обработки. Добавьте суффикс `(picture)` с значением data-URI, чтобы привязать изображение к разделу.

## Сопутствующие статьи
- [Отображение массива в отдельной ячейке SmartMarker](/cells/ru/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}