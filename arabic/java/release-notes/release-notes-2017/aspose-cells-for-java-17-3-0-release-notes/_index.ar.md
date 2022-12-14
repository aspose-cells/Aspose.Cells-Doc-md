---
title: Aspose.Cells for Java 17.3.0 ملاحظات الإصدار
type: docs
weight: 100
url: /ar/java/aspose-cells-for-java-17-3-0-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.3.0/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42205|يؤدي إعداد الصيغة بسلسلة حرفية طويلة إلى تلف ملف Excel|التعزيز|
|CELLSJAVA-42204|لم يتم عرض الحدود المنقطة من جدول البيانات إلى HTML|حشرة|
|CELLSJAVA-42198|حساب الصيغة خاطئ مع Aspose.Cells إنشاء ملف Excel|حشرة|
|CELLSJAVA-42156|تختفي الحدود العلوية والسفلية للخلايا أثناء التحويل إلى HTML|حشرة|
|CELLSJAVA-42208|يتم قطع التعليقات (في النهاية) رأسياً عند إنشاء ملف PDF عبر Aspose.Cells|حشرة|
|CELLSJAVA-42206|لا يتم تقديم خطوط شرطة المتسلسلة للمخططات بشكل صحيح في ملف PDF الناتج|حشرة|
|CELLSJAVA-42167 |يتم عرض تسميات محور الفئة في سطرين بعد تحويل المخطط إلى صورة|حشرة|
|CELLSJAVA-42199|مخطط الشلال ، الخط من الشريط الإجمالي والشريط قبل فقده مباشرةً|حشرة|
|CELLSJAVA-42201|المهمة الفرعية - تُعرض تسميات محور الفئة في سطرين بعد تحويل المخطط إلى صورة|حشرة|
|CELLSJAVA-42155|يحتوي المخطط الذي تم تصديره على تسميات محور س مختلفة عن تلك الموجودة في Excel|حشرة|
|CELLSJAVA-42128|المخطط خاطئ عند فتح ملف Excel المصدر وحفظه|حشرة|
|CELLSJAVA-42203|تم تغيير الخط بعد تحميل وإعادة حفظ XLSM|حشرة|
|CELLSJAVA-42196|تم إفساد تنسيق الملف الناتج في الملف المعاد حفظه|حشرة|
|CELLSJAVA-42195|مخطط الشلال ، إجمالي السلسلة يبدو خاطئًا|حشرة|
|CELLSJAVA-42181|عرض محمي بعد إعادة حفظ ملف XLS|حشرة|
|CELLSJAVA-42045|لم يتم إنشاء صورة مخطط نسيجي|حشرة|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **تخصيص إعدادات العولمة لجدول محوري**
باستخدام الإصدار الأخير 17.3.0 أو إصدار أحدث ، يمكن للمطورين تخصيص إعدادات العولمة للجدول المحوري في ملف Excel. يمكنهم تغيير الإجمالي المحوري ، والإجمالي الفرعي ، والإجمالي الكلي ، وجميع العناصر ، والعناصر المتعددة ، وتسميات الأعمدة ، وتسميات الصفوف ، ونص القيم الفارغة وفقًا للمتطلبات. يمكن للمطورين دمج هذه الميزة في تطبيقاتهم .NET ، بغض النظر عن لغة نص Excel. قد تكون عربية ، وهندية ، وبولندية ، وما إلى ذلك. جميع الطرق الجديدة المدعومة مذكورة أدناه:

1. **يضيف طريقة GlobalizationSettings.getPivotTotalName ()** - تحصل على اسم تسمية "الإجمالي" في PivotTable. يمكن للمطورين تجاوز هذه الطريقة عندما يحتوي PivotTable على اثنين أو أكثر من حقول PivotFields في منطقة البيانات.
1. **يضيف طريقة GlobalizationSettings.getPivotGrandTotalName ()** - تحصل على اسم علامة "الإجمالي الكلي" في PivotTable.
1. **يضيف طريقة GlobalizationSettings.getMultipleItemsName ()** - تحصل على اسم تسمية "(عناصر متعددة)" في PivotTable.
1. **يضيف طريقة GlobalizationSettings.getAllName ()** - تحصل على اسم التسمية "(الكل)" في PivotTable.
1. **يضيف GlobalizationSettings.getColumnLablesName ()** الطريقة - تحصل على اسم تسمية "عناوين الأعمدة" في PivotTable.
1. **يضيف طريقة GlobalizationSettings.getRowLablesName ()** - تحصل على اسم تسمية "Row Labels" في PivotTable.
1. **يضيف طريقة GlobalizationSettings.getEmptyDataName ()** - يحصل على اسم التسمية "(فارغ)" في PivotTable.
1. **إضافة أسلوب GlobalizationSettings.getSubTotalName (PivotFieldSubtotalType subTotalType)** - يحصل على اسم النوع "PivotFieldSubtotalType" في PivotTable.

يوضح مثال التعليمات البرمجية هذا كيفية تخصيص إعدادات العولمة لجدول محوري. يقوم بإنشاء فئة CustomPivotTableGlobalizationSettings المشتقة من فئة أساسية GlobalizationSettings ويتجاوز جميع الأساليب الضرورية. تُرجع هذه الأساليب النص المخصص للإجمالي المحوري والإجمالي الفرعي والإجمالي الكلي وكل العناصر والعناصر المتعددة وتسميات الأعمدة وتسميات الصفوف والقيم الفارغة. ثم يقوم بتعيين كائن هذه الفئة إلى خاصية Workbook.GlobalizationSettings. يقوم الكود بتحميل ملف Excel المصدر الذي يحتوي على الجدول المحوري ، ويقوم بتحديث بياناته وحسابها وحفظها كملف إخراج PDF. يمكن للمطورين أيضًا حفظ المصنف بأي تنسيق مدعوم.

**Java**

{{< highlight "java" >}}

 //Load your excel file

Workbook wb = new Workbook(dirPath + "samplePivotTableGlobalizationSettings.xlsx");



//Setting Custom Pivot Table Globalization Settings

wb.getSettings().setGlobalizationSettings(new CustomPivotTableGlobalizationSettings());



//Hide first worksheet that contains the data of the pivot table

wb.getWorksheets().get(0).setVisible(false);



//Access second worksheet

Worksheet ws = wb.getWorksheets().get(1);



//Access the pivot table, refresh and calculate its data

PivotTable pt = ws.getPivotTables().get(0);

pt.setRefreshDataFlag(true);

pt.refreshData();

pt.calculateData();

pt.setRefreshDataFlag(false);



//Pdf save options - save entire worksheet on a single pdf page

PdfSaveOptions options = new PdfSaveOptions();

options.setOnePagePerSheet(true);



//Save the output pdf 

wb.save(dirPath + "outputPivotTableGlobalizationSettings.pdf", options);



// it derives a new class, called CustomPivotTableGlobalizationSettings, from the GlobalizationSettings class, as follows:

class CustomPivotTableGlobalizationSettings extends GlobalizationSettings

{   

    //Gets the name of "Total" label in the PivotTable.

    //You need to override this method when the PivotTable contains two or more PivotFields in the data area.

    public String getPivotTotalName()

    {

        System.out.println("---------GetPivotTotalName-------------");

        return "AsposeGetPivotTotalName";

    }



    //Gets the name of "Grand Total" label in the PivotTable.

    public String getPivotGrandTotalName()

    {

        System.out.println("---------GetPivotGrandTotalName-------------");

        return "AsposeGetPivotGrandTotalName";

    }



    //Gets the name of "(Multiple Items)" label in the PivotTable.

    public String getMultipleItemsName()

    {

        System.out.println("---------GetMultipleItemsName-------------");

        return "AsposeGetMultipleItemsName";

    }



    //Gets the name of "(All)" label in the PivotTable.

    public String getAllName()

    {

        System.out.println("---------GetAllName-------------");

        return "AsposeGetAllName";

    }



    //Gets the name of "Column Labels" label in the PivotTable.

    public String getColumnLablesName()

    {

        System.out.println("---------GetColumnLablesName-------------");

        return "AsposeGetColumnLablesName";

    }



    //Gets the name of "Row Labels" label in the PivotTable.

    public String getRowLablesName()

    {

        System.out.println("---------GetRowLablesName-------------");

        return "AsposeGetRowLablesName";

    }



    //Gets the name of "(blank)" label in the PivotTable.

    public String getEmptyDataName()

    {

        System.out.println("---------GetEmptyDataName-------------");

        return "(blank)AsposeGetEmptyDataName";

    }



    //Gets the name of PivotFieldSubtotalType type in the PivotTable.

    public String getSubTotalName(int subTotalType)

    {

        System.out.println("---------GetSubTotalName-------------");



        switch (subTotalType)

        {

            case PivotFieldSubtotalType.SUM:

                return "AsposeSum";//polish



            case PivotFieldSubtotalType.COUNT:

                return "AsposeCount";



            case PivotFieldSubtotalType.AVERAGE:

                return "AsposeAverage";



            case PivotFieldSubtotalType.MAX:

                return "AsposeMax";



            case PivotFieldSubtotalType.MIN:

                return "AsposeMin";



            case PivotFieldSubtotalType.PRODUCT:

                return "AsposeProduct";



            case PivotFieldSubtotalType.COUNT_NUMS:

                return "AsposeCount";



            case PivotFieldSubtotalType.STDEV:

                return "AsposeStdDev";



            case PivotFieldSubtotalType.STDEVP:

                return "AsposeStdDevp";



            case PivotFieldSubtotalType.VAR:

                return "AsposeVar";

            case PivotFieldSubtotalType.VARP:

                return "AsposeVarp";

        }

        return "AsposeSubTotalName";

    }

}//End CustomPivotTableGlobalizationSettings

{{< /highlight >}}
### **قم بتنفيذ البرنامج النصي من جانب العميل في حدث تغيير الصفحة للتحكم في GridWeb**
باستخدام خاصية OnPageChangeClientFunction للتحكم في GridWeb ، يمكن للمطورين تنفيذ برنامج نصي من جانب العميل في حدث تغيير الصفحة لأن عنصر التحكم GridWeb يمكنه الاحتفاظ بالبيانات في صفحات متعددة. قد يحتاجون إلى عرض فهرس الصفحة الحالية في تطبيقات الويب الخاصة بهم.

1. **يضيف خاصية OnPageChangeClientFunction في GridWeb Control** - تحصل على وظيفة البرنامج النصي من جانب العميل أو تعينها ليتم استدعاؤها عند تغيير فهرس الصفحة. يصبح ساري المفعول فقط عندما يكون EnablePaging صحيحًا.

يوضح مثال التعليمات البرمجية هذا استخدام خاصية OnPageChangeClientFunction. يقوم بتعيين الخاصية مع وظيفة جانب العميل المسماة MyOnPageChange. الآن ، عندما يقوم المستخدم بتغيير صفحة GridWeb ، فإنه سوف يستدعي وظيفة جانب العميل MyOnPageChange التي تطبع**فهرس الصفحة الحالية**على ال**وحدة التحكم**:

**Java**

{{< highlight "java" >}}

 // It is the client side function MyOnPageChange that will be executed because of setting OnPageChangeClientFunction ="MyOnPageChange"property in GridWeb.

function MyOnPageChange(index) {

    console.log("current page is:" + (index+1));

}



// The following code explains how to enable paging and set the OnPageChangeClientFunction property.

GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
### **تحقق من صحة ورقة عمل Excel بأكملها**
بشكل افتراضي ، يتحقق GridWeb من صحة الخلايا المحدثة فقط ولا يتحقق من صحة ورقة عمل Excel بأكملها. ومع ذلك ، إذا طلب المطورون التحقق من صحة ورقة عمل Excel بالكامل على جانب العميل قبل طلب نشر GridWeb إلى الخادم ، فيجب عليك تعيين متغير needValidateall داخل acwmain.js إلى true.
### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

1. [تخصيص إعدادات العولمة للجدول المحوري](/cells/ar/java/customize-globalization-settings-for-pivot-table/)
1. [تنفيذ وظيفة جانب العميل عند تغيير صفحة GridWeb](/cells/ar/java/execute-client-side-function-on-gridweb-page-change/)
1. [تحقق من صحة ورقة العمل بأكملها بدلاً من الخلايا المحدثة فقط](/cells/ar/java/validate-entire-worksheet-instead-of-only-the-updated-cells/)
