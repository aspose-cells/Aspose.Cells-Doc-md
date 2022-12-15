---
title: Aspose.Cells Java لـ Jython
type: docs
weight: 70
url: /ar/java/aspose-cells-java-for-jython/
---
## **مقدمة**

### **ما هو جايثون؟**

Jython هو تطبيق Java لـ Python يجمع بين القوة التعبيرية والوضوح. Jython متاح مجانًا للاستخدام التجاري وغير التجاري ويتم توزيعه مع شفرة المصدر. Jython مكمل لـ Java وهو مناسب بشكل خاص للمهام التالية:

- **البرمجة النصية المضمنة** - Java يمكن للمبرمجين إضافة مكتبات Jython إلى نظامهم للسماح للمستخدمين النهائيين بكتابة نصوص بسيطة أو معقدة تضيف وظائف للتطبيق.
- **التجريب التفاعلي** - يوفر Jython مترجمًا تفاعليًا يمكن استخدامه للتفاعل مع حزم Java أو مع تشغيل تطبيقات Java. هذا يسمح للمبرمجين بتجربة وتصحيح أي نظام Java باستخدام جايثون.
- **التطوير السريع للتطبيق** برامج Python عادة ما تكون أقصر بمقدار 2-10 مرة من البرامج المكافئة Java. هذا يترجم مباشرة إلى زيادة إنتاجية المبرمج. يتيح التفاعل السلس بين Python و Java للمطورين خلط اللغتين بحرية أثناء التطوير وفي منتجات الشحن.

### **Aspose.Cells for Java**

Aspose.Cells for Java هي مكتبة صفية متقدمة for Java تمكنك من أداء مجموعة كبيرة من مهام معالجة المستندات مباشرة داخل Java
التطبيقات.

Aspose.Cells for Java يدعم معالجة Cells (DOC و DOCX و OOXML و RTF) HTML و OpenDocument و PDF و EPUB و XPS و SWF وجميع تنسيقات الصور. مع Aspose.Cells يمكنك ذلك
إنشاء وتعديل وتحويل المستندات دون استخدام Microsoft Cells.

### **Aspose.Cells Java لـ Jython**

Aspose.Cells Java لـ Jython هو مشروع يوضح / يقدم Aspose.Cells for Java API في جايثون.

## **متطلبات النظام والأنظمة الأساسية المدعومة**

### **متطلبات النظام**

**فيما يلي متطلبات النظام لاستخدام Aspose.Cells Java لـ Jython:**

- Java 1.5 أو أعلى مثبتة
- تم تحميل Aspose.Cells المكون
- جايثون 2.7.0

### **المنصات المدعومة**

**فيما يلي المنصات المدعومة:**

- Aspose.Cells 15.4 وما فوق.
- Java IDE (Eclipse، NetBeans ...)

## **تنزيل التثبيت والاستخدام**

### **جارى التحميل**

**تنزيل أمثلة من مواقع الترميز الاجتماعي**

الإصدارات التالية من الأمثلة قيد التشغيل متاحة للتنزيل على جميع مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**تنزيل Aspose.Cells for Java المكون**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **التثبيت**

- ضع ملف جرة Aspose.Cells for Java الذي تم تنزيله في دليل "lib".
- استبدل "your-lib" باسم ملف jar الذي تم تنزيله في ملف _ * init * _. py.

### **استخدام**

يمكنك إنشاء مستند HelloWorld باستخدام رمز المثال التالي:

{{< highlight "java" >}}

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

## **الدعم والتوسيع والمساهمة**

### **الدعم**

منذ الأيام الأولى من Aspose ، علمنا أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن مطورون بأنفسنا ونفهم مدى الإحباط عندما تمنعك مشكلة فنية أو غرابة في البرنامج من القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل وليس خلقها.

هذا هو السبب في أننا نقدم الدعم المجاني. أي شخص يستخدم منتجاتنا ، سواء اشتراها أو استخدم تقييمًا ، يستحق كامل اهتمامنا واحترامنا.

يمكنك تسجيل أي مشكلات أو اقتراحات تتعلق بـ Aspose.Cells Java لـ Jython باستخدام أي من الأنظمة الأساسية التالية:

- [جيثب](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **تمديد والمساهمة**

Aspose.Cells Java لـ Jython مفتوح المصدر وكود المصدر الخاص به متاح على مواقع الترميز الاجتماعي الرئيسية المدرجة أدناه. يتم تشجيع المطورين على تنزيل الكود المصدري والمساهمة من خلال اقتراح أو إضافة ميزة جديدة أو تحسين الميزات الموجودة ، بحيث يمكن للآخرين الاستفادة منها أيضًا.

### **مصدر الرمز**

يمكنك الحصول على أحدث كود مصدر من أحد المواقع التالية

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
