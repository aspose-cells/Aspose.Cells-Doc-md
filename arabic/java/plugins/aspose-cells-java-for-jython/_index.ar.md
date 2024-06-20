---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /ar/java/aspose-cells-java-for-jython/
---

## **مقدمة**

### **ما هو Jython؟**

Jython هو تنفيذ للغة Python بلغة Java يجمع بين القوة التعبيرية والوضوح. يتوفر Jython بحرية للاستخدام التجاري وغير التجاري ويُوزع مع الشفرة المصدرية. تكمل Jython Java وتكون مناسبة بشكل خاص للمهام التالية:

- **البرمجة النصية المضمنة** - يمكن لمبرمجي Java إضافة مكتبات Jython إلى نظامهم للسماح للمستخدمين النهائيين بكتابة نصوص بسيطة أو مُعقَّدة تضيف وظائف إلى التطبيق.
- **التجربة التفاعلية** - يوفر Jython مُفسّرًا تفاعليًا يمكن استخدامه للتفاعل مع حزم Java أو مع تطبيقات Java قيد التشغيل. يسمح هذا للمبرمجين بالتجربة وتصحيح أي نظام Java باستخدام Jython.
- **تطوير التطبيقات السريع** - تكون برامج Python عادةً أقصر بمقدار 2-10 مرات من البرنامج المعادل في Java. يترجم ذلك مباشرة إلى زيادة في إنتاجية المبرمج. يتيح التفاعل المتماسك بين Python و Java للمطورين مزج اللغتين بحرية سواء أثناء التطوير أو عند شحن المنتجات.

### **Aspose.Cells for Java**

Aspose.Cells for Java هو مكتبة فئة متقدمة للغة Java تتيح لك إجراء مجموعة كبيرة من مهام معالجة المستندات مباشرة داخل برنامج Java الخاص بك
تطبيقات.

Aspose.Cells for Java يدعم معالجة الخلايا (DOC، DOCX، OOXML، RTF) HTML، OpenDocument، PDF، EPUB، XPS، SWF وجميع تنسيقات الصور. باستخدام Aspose.Cells يمكنك
توليد، تعديل، وتحويل المستندات دون استخدام Microsoft Cells.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java for Jython هو مشروع يوضح / يقدم أمثلة على استخدام واجهة برمجة التطبيقات Aspose.Cells for Java في Jython.

## **متطلبات النظام والمنصات المدعومة**

### **متطلبات النظام**

**فيما يلي متطلبات النظام لاستخدام Aspose.Cells Java for Jython:**

- يجب تثبيت Java 1.5 أو أحدث
- تم تنزيل مكون Aspose.Cells
- Jython 2.7.0

### **المنصات المدعومة**

**إليك المنصات المدعومة:**

- Aspose.Cells 15.4 وما بعدها.
- بيئة تطوير Java (Eclipse، NetBeans ...)

## **تنزيل التثبيت والاستخدام**

### **التحميل**

**تنزيل الأمثلة من مواقع التعاون الاجتماعي للترميز**

إصدارات تشغيل الأمثلة التي يمكن تنزيلها على جميع المواقع المذكورة أدناه على مواقع التعاون الاجتماعي:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**تحميل مكون Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **التثبيت**

- ضع ملف جرار Aspose.Cells for Java الذي تم تحميله في دليل "lib".
- استبدل "your-lib" باسم ملف الجرار المحمل في ملف _*init*_.py.

### **استخدام**

يمكنك إنشاء مستند HelloWorld باستخدام الكود المثال التالي:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **الدعم، التوسيع والمساهمة**

### **الدعم**

منذ الأيام الأولى لـ Aspose ، كنا نعلم أن مجرد منح عملائنا منتجات جيدة لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن أنفسنا مطورين ونفهم مدى إزعاج القضايا التقنية أو العيوب في البرمجيات التي توقفك عن القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل ، وليس لخلقها.

هذا هو السبب في أننا نقدم الدعم المجاني. يستحق أي شخص يستخدم منتجاتنا ، سواء اشتروها أو كانوا يستخدمون تقييمًا ، كامل انتباهنا واحترامنا.

يمكنك تسجيل أي مشاكل أو اقتراحات متعلقة بـ Aspose.Cells Java for Jython باستخدام أي من البيئات التالية:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **تمديد والمساهمة**

Aspose.Cells Java for Jython هو مفتوح المصدر ويتوفر رمز مصدره على مواقع الترميز الاجتماعي الرئيسية المدرجة أدناه. يُشجع المطورون على تحميل رمز المصدر والمساهمة من خلال اقتراح أو إضافة ميزات جديدة أو تحسين القائمة، بحيث يمكن للآخرين أيضًا الاستفادة من ذلك.

### **رمز المصدر**

يمكنك الحصول على آخر رمز مصدري من أحد المواقع التالية

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
