---
title: المؤشرات الذكية في رؤوس وتذييلات الصفحات | Aspose.Cells for Java
linktitle: علامات ذكية في الرأس والتذييل | Aspose.Cells
description: ضع نواقل المؤشرات الذكية في رؤوس وتذييلات الصفحات باستخدام بناء جملة الأقواس المزدوجة ومعامل WorkbookDesigner.setEnableHeaderFooterMarkers مع قوائم getter-bean أو مصادر بيانات JSON، واربط الصور عبر عناوين URI للبيانات، في Aspose.Cells for Java.
keywords: Aspose.Cells for Java, المؤشرات الذكية, رؤوس, تذييلات, مؤشرات الرأس والتذييل, setEnableHeaderFooterMarkers, WorkbookDesigner, PageSetup, setHeader, setFooter, setJsonDataSource, setDataSource, getter bean, مصدر بيانات JSON, ربط البيانات, صورة, data URI, Java
type: docs
weight: 196
url: /ar/java/smart-markers-in-headers-and-footers/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
غالبًا ما تحتوي رؤوس وتذييلات الصفحات على بيانات تعريف التقرير مثل عنوان التقرير، فترة التقرير، المؤلف، والقسم. عندما تكون هذه المعلومات موجودة بالفعل في مصدر البيانات المستخدم لملء المصنف، فإن تكرارها يدويًا يخلق ازدواجية غير ضرورية.  
تُعالج صيغة المؤشر الذكي الكلاسيكية، `&=Source.Field`، في خلايا جسم ورقة العمل. إذا وضعت علامة كلاسيكية في رأس أو تذييل عبر `PageSetup.setHeader` أو `PageSetup.setFooter`، فستظل نصًا حرفيًا لأن سلاسل الرأس والتذييل ليست جزءًا من شبكة خلايا ورقة العمل التي يفحصها `WorkbookDesigner.process()`.
بدءًا من **Aspose.Cells for Java 26.11**، يكون خيار العلامات في الرأس/التذييل في `WorkbookDesigner` مضبطًا على `false` بشكل افتراضي. استدعِ `designer.setEnableHeaderFooterMarkers(true)` قبل استدعاء `designer.process()` لإجراء استبدال النواقل المكتوبة على شكل `<<Source.Field>>` في سلاسل أقسام الرأس والتذييل. تستخدم نواقل الرأس والتذييل نفس مصدر البيانات مثل نواقل الجسم.
كل رأس وتذييل يحتوي على ثلاث أقسام يمكن عنونتها:
- القسم `0` هو القسم الأيسر.
- القسم `1` هو القسم المركزي.
- القسم `2` هو القسم الأيمن.
استخدم `PageSetup.setHeader(int section, String value)` و `PageSetup.setFooter(int section, String value)` لكتابة هذه الأقسام. بعد المعالجة، استخدم `PageSetup.getHeader(int section)` و `PageSetup.getFooter(int section)` لاسترجاع النص المكتمل.

{{% alert color="primary" %}}
نقطة وضع مثل `<<Source.Field>>` تُدرج قيمة الحقل كنص في سلسلة القسم. تُربط الصور باللاحقة `(picture)` وقيمة data-URI.
{{% /alert %}}

## **تمكين علامات الرأس/التذييل مع قائمة Getter-Bean**
استخدم التسلسل التالي لإجراء استبدال نواقل الرأس والتذييل باستخدام قائمة getter-bean في **Aspose.Cells for Java 26.11**:
1. أنشئ كائن `Workbook` واحصل على أول `Worksheet` في الفهرس `0`، على سبيل المثال باستخدام `workbook.getWorksheets().get(0)`.
2. اكتب نواقل `<<Source.Field>>` في أقسام الرأس والتذييل المطلوبة باستخدام `PageSetup.setHeader` و `PageSetup.setFooter`.
3. عرّف فئة bean عامة (PUBLIC) تحتوي على getter (مثال، `getName()`) لكل حقل من المؤشرات، واختر اسم مصدر يتطابق مع بادئة المصدر المستخدمة في النواقل. على سبيل المثال، المصدر المسمى `node` يدعم نواقل مثل `<<node.Name>>`. يتم التحقق من قاعدتين للربط على هذه المنصة: bean يحتوي على حقول عامة لا يربط أي شيء (المحرك يقرأ getters فقط)، وفئة ذات وصول PACKAGE-PRIVATE لا يربط أي شيء أيضًا — عملية الاستعراض لا ترى إلا الفئات العامة، وفئة غير عامة ستفشل `process()` باستثناء NullPointerException.
4. أنشئ كائن `WorkbookDesigner` للمصنف.
5. استدعِ `designer.setEnableHeaderFooterMarkers(true)` قبل المعالجة.
6. أرفق القائمة واسم مصدرها باستخدام `designer.setDataSource("node", table)`.
7. استدعِ `designer.process()`.
8. بعد المعالجة، لن تكون النواقل موجودة في نص الرأس أو التذييل. استخدم `PageSetup.getHeader` و `PageSetup.getFooter` لاسترجاع سلاسل الأقسام المكتملة.

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

## **استخدام مصدر بيانات JSON**
يمكنك استعمال JSON بدلاً من قائمة getter-bean عندما تكون بيانات التقرير متوفرة بالفعل بصيغة JSON. استدعِ `WorkbookDesigner.setJsonDataSource(String name, String json)` لإرفاق المصدر.  
معامل `name` هو اسم المصدر المستخدم في النواقل. على سبيل المثال، الاسم `node` يدعم نواقل مثل `<<node.Company>>` و `<<node.Title>>`.  
مرّر بيانات الصف مباشرة إلى `setJsonDataSource`:
- مصفوفة صفوف، مثل مصفوفة JSON تحتوي على كائن أو أكثر من كائنات الصف، مدعومة.
- يمكن أيضًا تمرير كائن صف واحد مباشرة.
- لا تقم بلف الصفوف تحت مفتاح أعلى مستوى مسمى مثل `{"rows":[...]}`. هذا الغلاف ليس الشكل المتوقع لإدخال صفوف موجهة لهذا التدفق.
يمكن لمصدر JSON واحد ملء كلا نمطي العلامة أثناء نفس استدعاء `designer.process()`. يمكنه استبدال علامة `&=` الكلاسيكية في خلية جسم ورقة العمل ونواقل الأقواس المزدوجة `<<>>` في أقسام الرأس والتذييل. لا يزال من الضروري تمكين `EnableHeaderFooterMarkers` لكي يتم استبدال نواقل الرأس والتذييل.

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

## **الإعدادات المتعددة للصفوف وسلامة التبديل**
إعداد `EnableHeaderFooterMarkers` يكون `false` بشكل افتراضي، ويُتحكم في نواقل الرأس/التذييل `<<Source.Field>>` فقط. عندما يكون المفتاح غير مفعَّل، فإن `designer.process()` لا يزال يحل نواقل الجسم الكلاسيكية `&=`، لكن نقطة وضع `<<Source.Field>>` في رأس أو تذييل تظل نصًا حرفيًا.  
القسم في الرأس أو التذييل هو سلسلة واحدة، وليس شريطًا متكررًا. إذا كان مصدر البيانات يحتوي على عدة صفوف، فإن الصف الأول يزوّد قيم الرأس والتذييل. بمجرد الاستبدال، تصبح القيم نصًا عاديًا في الرأس أو التذييل. تبقى هذه القيم في المصنف بعد استدعاء `workbook.save(...)` وتظهر عند تحميل المصنف المحفوظ مرة أخرى.  
المثال التالي ينشئ مصنفين باستخدام نفس قائمة bean متعددة الصفوف لتوضيح السلوك عند إيقاف وتمكين الخيار. يترك `plainDesigner` النواقل دون استبدال، بينما يحل `enabledDesigner` النواقل باستخدام الصف الأول.

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

## **ربط صورة في رأس أو تذييل**
اللاحقة `(picture)` تربط صورة في قسم الرأس أو التذييل. اكتب `<<node.logo(picture)>>` حيث تريد ظهور الصورة، وزوّد قيمة الحقل كعنوان URI للبيانات — البادئة `data:image/png;base64,` متبوعة بنص Base64 لبايتات الصورة. سلسلة Base64 بدون البادئة `data:` لا تُدرج صورة.  
بعد `designer.process()`:
1. يتم استبدال النقطة بـ `&G`، وهو رمز الصورة القياسي في الرأس والتذييل. بما أن العلامة تصبح كودًا داخل سلسلة القسم، يمكنها الوجود داخل نص أطول مثل `Logo: <<node.logo(picture)>>`.
2. تُدمج بايتات الصورة في المصنف كجزء وسائط مرفق بطبقة رسم الرأس/التذييل لتلك الورقة، لذا تُطبع الصورة مع الرأس أو التذييل.

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

يُطبع Excel الرمز `&G` ككود الصورة عند عرض الرأس — الآن بايتات `logo.png` موجودة داخل `HeaderFooterPicture.xlsx`، وتُطبع الصورة في موضع الكود.  
لاستخدام نواقل الرأس والتذييل الذكية، اكتب نواقل `<<Source.Field>>` في الأقسام اليسرى، الوسطى، واليمنى للرأس أو التذييل باستخدام `PageSetup.setHeader` و `PageSetup.setFooter`. استدعِ `designer.setEnableHeaderFooterMarkers(true)` على كائن `WorkbookDesigner` قبل استدعاء `designer.process()`، وزوّد القيم عبر `designer.setDataSource(name, list)` باستخدام قائمة getter-bean أو `designer.setJsonDataSource(name, json)`. اقرأ الأقسام المكتملة باستخدام `PageSetup.getHeader` و `PageSetup.getFooter`. يمكن لنفس مصدر البيانات ملء نواقل الجسم والنواقل في الرأس أو التذييل في تمريرة معالجة واحدة. أضف اللاحقة `(picture)` مع قيمة data-URI لربط صورة في القسم.

## **مقالات ذات صلة**
- [العرض الذكي لمصفوفة خلية واحدة](/cells/ar/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)

{{< app/cells/assistant language="java" >}}